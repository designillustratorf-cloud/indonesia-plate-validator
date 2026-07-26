from flask import Flask, render_template, request, redirect, url_for, send_file

from dfa import DFAValidator
from regex_validator import regex_validate
from export import export

app = Flask(__name__)

dfa = DFAValidator()
history = []


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    regex_result = None
    dfa_result = None
    states = []
    transitions = []

    if request.method == "POST":

        plate = request.form.get("plate", "").strip().upper()

        regex_result = regex_validate(plate)

        dfa_data = dfa.validate(plate)

        dfa_result = dfa_data["valid"]
        states = dfa_data["history"]
        transitions = dfa_data["transitions"]

        result = "VALID" if (regex_result and dfa_result) else "TIDAK VALID"

        history.insert(
            0,
            {
                "plate": plate,
                "regex": regex_result,
                "dfa": dfa_result,
                "result": result,
            },
        )

    valid = sum(1 for item in history if item["result"] == "VALID")
    invalid = sum(1 for item in history if item["result"] == "TIDAK VALID")

    return render_template(
        "index.html",
        result=result,
        regex_result=regex_result,
        dfa_result=dfa_result,
        states=states,
        transitions=transitions,
        history=history,
        valid=valid,
        invalid=invalid,
    )


@app.route("/simulator")
def simulator():
    return render_template("simulator.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/reset")
def reset():
    history.clear()
    return redirect(url_for("home"))


@app.route("/export/csv")
def export_csv():

    if len(history) == 0:
        return redirect(url_for("home"))

    filename = export(history)

    return send_file(
        filename,
        as_attachment=True,
        download_name="history.csv",
        mimetype="text/csv"
    )


@app.route("/api/history")
def api_history():

    return {
        "total": len(history),
        "valid": sum(1 for item in history if item["result"] == "VALID"),
        "invalid": sum(1 for item in history if item["result"] == "TIDAK VALID"),
        "history": history,
    }


@app.route("/api/validate", methods=["POST"])
def api_validate():

    plate = request.form.get("plate", "").strip().upper()

    regex = regex_validate(plate)

    dfa_data = dfa.validate(plate)

    return {
        "plate": plate,
        "regex": regex,
        "dfa": dfa_data["valid"],
        "status": "VALID" if (regex and dfa_data["valid"]) else "TIDAK VALID",
        "states": dfa_data["history"],
        "transitions": dfa_data["transitions"],
        "final_state": dfa_data["final_state"],
    }


if __name__ == "__main__":
    app.run(debug=True)