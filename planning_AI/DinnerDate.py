from State import State
from Action import Action


class DinnerDate:
    def __init__(self):
        self.initial = self.initial_state()
        self.final = self.final_state()
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
        state.add_literal(True, "garbage")
        state.add_literal(True, "cleanHands")
        state.add_literal(True, "quiet")

        return state

    def final_state(self):
        state = State()
        state.add_literal(True, "dinner")
        state.add_literal(True, "present")
        state.add_literal(False, "garbage")

        return state

    def set_literals(self):
        return

    def set_actions(self):

        action1 = Action("cook")
        action1.add_precondition(True, "cleanHands")
        action1.add_effect(True, "dinner")
        self.actions.append(action1)

        action2 = Action("wrap")
        action2.add_precondition(True, "quiet")
        action2.add_effect(True, "present")
        self.actions.append(action2)

        action3 = Action("carry")
        action3.add_effect(False, "garbage")
        action3.add_effect(False, "cleanHands")
        self.actions.append(action3)

        action4 = Action("dolly")
        action4.add_effect(False, "garbage")
        action4.add_effect(False, "quiet")
        self.actions.append(action4)
