from Action import Action

class State:
    def __init__(self):
        self.positive_literals = []
        self.negative_literals = []
        self.action = None
        self.parent = None

    def get_positive_literals(self):
        return self.positive_literals

    def get_negative_literals(self):
        return self.negative_literals

    def add_literal(self, is_positive, literal):
        if is_positive:
            self.positive_literals.append(literal)
        else:
            self.negative_literals.append(literal)

    def satisfied_precondition(self, precondition):
        return self.positive_literals.__contains__(precondition) \
               and not self.negative_literals.__contains__(precondition)

    def satisfied_precondition_two(self, action: Action):
        for positive in action.get_positive_preconditions():
            if not self.positive_literals.__contains__(positive):
                return False

        for negative in action.get_negative_preconditions():
            if self.positive_literals.__contains__(negative):
                return False
            if not self.negative_literals.__contains__(negative):
                return False

        return True

    def do_action(self, action):
        state = State()
        state.positive_literals.append(self.positive_literals)
        state.negative_literals.append(self.negative_literals)

        for unit in action.get_add_list():
            if not state.positive_literals.__contains__(unit):
                state.positive_literals.append(unit)

        for unit in action.get_delete_list():
            if not state.negative_literals.__contains__(unit):
                state.negative_literals.append(unit)

        for index in range(0, len(state.positive_literals)):
            positive_literal = state.positive_literals[index]
            if state.negative_literals.__contains__(positive_literal):
                state.positive_literals.remove(index)

        for index in range(0, len(state.negative_literals)):
            negative_literal = state.negative_literals[index]
            if state.positive_literals.__contains__(negative_literal):
                state.negative_literals.remove(index)

        return state

    def final_state(self, final):
        positive_matched = True
        negative_matched = True

        for literal in final.get_positive_literals():
            if not self.get_positive_literals().__contains__(literal) \
                    or self.get_negative_literals().__contains__(literal):
                positive_matched = False
                break

        for literal in final.get_negative_literals():
            if not self.get_negative_literals().__contains__(literal) \
                    or self.get_positive_literals().__contains__(literal):
                negative_matched = False
                break

        return negative_matched and positive_matched

    def compare_states(self, state):
        return state.positive_literals == self.positive_literals \
               and state.negative_literals == self.negative_literals
