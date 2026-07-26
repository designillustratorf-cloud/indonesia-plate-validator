import csv
from datetime import datetime


def export(history):
    filename = f'history_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:

        writer = csv.writer(file)

        writer.writerow([
            "No",
            "Plat Nomor",
            "Regex",
            "DFA",
            "Status"
        ])

        for i, item in enumerate(history, start=1):

            writer.writerow([
                i,
                item["plate"],
                "VALID" if item["regex"] else "INVALID",
                "VALID" if item["dfa"] else "INVALID",
                item["result"]
            ])

    return filename