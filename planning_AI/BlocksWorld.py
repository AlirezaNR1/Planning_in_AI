from State import State
from Action import Action


class BlocksWorld:
    def __init__(self):
        self.initial = self.initial_state()
        self.final = self.final_state()
        self.Place = []
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
        state.add_literal(True, "On(A,Table)")
        state.add_literal(True, "On(B,Table)")
        state.add_literal(True, "On(C,A)")
        state.add_literal(True, "Clear(B)")
        state.add_literal(True, "Clear(C)")
        state.add_literal(True, "Clear(Table)")

        return state

    def final_state(self):
        state = State()
        state.add_literal(True, "On(A,B)")
        state.add_literal(True, "On(B,C)")

        return state

    def set_literals(self):
        self.Place.append("A")
        self.Place.append("B")
        self.Place.append("C")
        self.Place.append("Table")

    def set_actions(self):

        for b in self.Place:
            if b == "Table":
                continue

            for x in self.Place:
                for y in self.Place:
                    if not b == x and not b == y and not x == y:
                        if y != "Table":
                            self.set_normal_move(b, x, y)

                if not x == "Table" and not b == x:
                    self.set_move_to_table(b, x)

    def set_normal_move(self, b, x, y):
        action = Action("Move(" + b + "," + x + "," + y + ")")
        if b == "table" or y == "table":
            return

        action.add_precondition(True, "On(" + b + "," + x + ")")
        action.add_precondition(True, "Clear(" + b + ")")
        action.add_precondition(True, "Clear(" + y + ")")

        action.add_effect(False, "On(" + b + "," + x + ")")
        action.add_effect(True, "On(" + b + "," + y + ")")
        action.add_effect(True, "Clear(" + x + ")")
        action.add_effect(False, "Clear(" + y + ")")

        self.actions.append(action)

    def set_move_to_table(self, b, x):
        action = Action("MoveToTable(" + b + "," + x + ")")

        action.add_precondition(True, "On(" + b + "," + x + ")")
        action.add_precondition(True, "Clear(" + b + ")")

        action.add_effect(True, "On(" + b + ",Table)")
        action.add_effect(False, "On(" + b + "," + x + ")")
        action.add_effect(True, "Clear(" + x + ")")

        self.actions.append(action)
