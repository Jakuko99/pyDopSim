from game.api_package import REStation


class SignalFinder:
    def __init__(self, relief: REStation):
        self.relief = relief

    def find_signal_by_button(self, button_id: str) -> str:
        if "T_1" in button_id:
            if button_id == "T_1_S1" or button_id == "T_1_D1":
                return "S1"
            elif button_id == "T_1_S2" or button_id == "T_1_D2":
                return "L1"
            elif "T_1L" in button_id:
                if button_id == "T_1L_S":
                    return "Se1"
                return "1L"
            elif "T_2L" in button_id:
                if button_id == "T_2L_S":
                    return "Se2"
                return "2L"

        elif "T_2" in button_id:
            if button_id == "T_2_S1" or button_id == "T_2_D1":
                return "S2"
            elif button_id == "T_2_S2" or button_id == "T_2_D2":
                return "L2"
            elif "T_2L" in button_id:
                return "2L"

        elif "T_3" in button_id:
            if button_id == "T_3_S1" or button_id == "T_3_D1":
                return "S3"
            elif button_id == "T_3_S2" or button_id == "T_3_D2":
                return "L3"

        elif "T_4" in button_id:
            if button_id == "T_4_S1":
                return "Se3"
            elif button_id == "T_4_S2":
                return "Se4"
            elif button_id == "T_4a_S":
                return "Se5"

        elif "T_5" in button_id:
            if button_id == "T_5_S1" or button_id == "T_5_D1":
                return "S5"
            elif button_id == "T_5_S2" or button_id == "T_5_D2":
                return "L5"

        elif "T_S" in button_id:
            return "S"

        elif "T_1L" in button_id:
            return "1L"

        else:
            return None
