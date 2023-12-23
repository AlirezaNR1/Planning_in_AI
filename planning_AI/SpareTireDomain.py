from State import State
from Action import Action


class SpareTireDomain:
    def __init__(self):
        self.initial = self.initial_state()
        self.final = self.final_state()
        self.Tires = []
        self.locations = []
        self.actions = []
        self.current_states = []
        self.explored_states = []

        self.set_literals()
        self.set_actions()

    def get_initial(self):
        return self.initial

    def get_final(self):
        return self.final

    def get_actions(self):
        return self.actions

    def initial_state(self):
        state = State()
        state.add_literal(True, "At(Flat,Axle)")
        state.add_literal(True, "At(Spare,Trunk)")

        return state

    def final_state(self):
        state = State()
        state.add_literal(True, "At(Spare,Axle)")

        return state

    def set_literals(self):
        self.Tires.append("Flat")
        self.Tires.append("Spare")
        self.locations.append("Axle")
        self.locations.append("Trunk")
        self.locations.append("Ground")

    def set_actions(self):

        for obj in self.Tires:
            for location in self.locations:
                if location != "Ground":
                    action = Action("Remove" + obj + location)
                    action.add_precondition(True, "At(" + obj + "," + location + ")")
                    action.add_effect(False, "At(" + obj + "," + location + ")")
                    action.add_effect(True, "At(" + obj + ",Ground)")

                    self.actions.append(action)

        for obj in self.Tires:
            action = Action("PutOn" + obj + "Axle")
            action.add_precondition(True, "At(" + obj + ",Ground)")
            action.add_precondition(False, "At(Flat,Axle)")
            action.add_effect(False, "At(" + obj + ",Ground)")
            action.add_effect(True, "At(" + obj + ",Axle)")

            self.actions.append(action)

        action = Action("LeaveOverNight")
        action.add_effect(False, "At(Spare,Ground)")
        action.add_effect(False, "At(Spare,Axle)")
        action.add_effect(False, "At(Spare,Trunk)")
        action.add_effect(False, "At(Flat,Ground)")
        action.add_effect(False, "At(Flat,Axle)")
        action.add_effect(False, "At(Flat,Trunk)")

        self.actions.append(action)
