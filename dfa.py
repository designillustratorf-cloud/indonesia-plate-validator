class DFAValidator:

    def __init__(self):
        self.start_state = "q0"
        self.accept_state = "q4"

    def validate(self, plate):

        plate = plate.replace(" ", "").upper()

        state = self.start_state
        history = [state]
        transitions = []

        digit_count = 0
        suffix_count = 0

        for char in plate:

            previous = state

            if state == "q0":

                if char.isalpha():
                    state = "q1"
                else:
                    return self.reject(history, transitions)

            elif state == "q1":

                if char.isalpha():
                    state = "q2"

                elif char.isdigit():
                    state = "q3"
                    digit_count = 1

                else:
                    return self.reject(history, transitions)

            elif state == "q2":

                if char.isdigit():
                    state = "q3"
                    digit_count = 1

                else:
                    return self.reject(history, transitions)

            elif state == "q3":

                if char.isdigit():

                    digit_count += 1

                    if digit_count > 4:
                        return self.reject(history, transitions)

                elif char.isalpha():

                    state = "q4"
                    suffix_count = 1

                else:
                    return self.reject(history, transitions)

            elif state == "q4":

                if char.isalpha():

                    suffix_count += 1

                    if suffix_count > 3:
                        return self.reject(history, transitions)

                else:
                    return self.reject(history, transitions)

            transitions.append({
                "from_state": previous,
                "input": char,
                "to_state": state
            })

            history.append(state)

        valid = (
            state == self.accept_state
            and 1 <= digit_count <= 4
            and 1 <= suffix_count <= 3
        )

        return {
            "valid": valid,
            "history": history,
            "transitions": transitions,
            "final_state": state
        }

    def reject(self, history, transitions):

        return {
            "valid": False,
            "history": history,
            "transitions": transitions,
            "final_state": history[-1]
        }