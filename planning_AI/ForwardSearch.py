from State import State
from Action import Action


class ForwardSearch:

    def __init__(self, init: State, final: State, actions):
        self.init = init
        self.final = final
        self.actions = actions

        self.currentStates = []
        self.exploredStates = []

    def search(self):
        self.currentStates.append(self.init)

        while len(self.currentStates) != 0:
            state = self.currentStates.pop(0)
            self.do_action_on_state(state)
            self.exploredStates.append(state)
            if self.check_goal():
                return

    def do_action_on_state(self, state: State):
        for action in self.actions:
            if self.contain(state):
                return
            if self.can_do_action(state, action):
                new_state = self.do_action(state, action)
                new_state.action = action
                new_state.parent = state
                self.currentStates.append(new_state)

    def do_action(self, state: State, action):
        new_state = State()
        for positive in state.get_positive_literals():
            new_state.positive_literals.append(positive)
        for negative in state.get_negative_literals():
            new_state.negative_literals.append(negative)

        for temp in action.get_add_list():
            if not new_state.positive_literals.__contains__(temp):
                new_state.positive_literals.append(temp)
            if new_state.negative_literals.__contains__(temp):
                new_state.negative_literals.remove(temp)

        for temp in action.get_delete_list():
            if not new_state.negative_literals.__contains__(temp):
                new_state.negative_literals.append(temp)
            if new_state.positive_literals.__contains__(temp):
                new_state.positive_literals.remove(temp)

        for i in range(0, len(new_state.positive_literals)):
            positive = new_state.positive_literals[i]
            if new_state.negative_literals.__contains__(positive):
                new_state.positive_literals.remove(positive)

        for i in range(0, len(new_state.negative_literals)):
            negative = new_state.negative_literals[i]
            if new_state.positive_literals.__contains__(new_state):
                new_state.negative_literals.remove(negative)

        return new_state

    def contain(self, state: State):
        for temp in self.exploredStates:
            equal = True

            string1 = "".join(temp.positive_literals)
            string2 = "".join(state.positive_literals)

            string3 = "".join(temp.negative_literals)
            string4 = "".join(state.negative_literals)

            if string1 == string2 and string3 == string4:
                return True

            # for positive in temp.positive_literals:
            #     if not state.positive_literals.__contains__(positive):
            #         equal = False
            # for negative in temp.negative_literals:
            #     if not state.negative_literals.__contains__(negative):
            #         equal = False

            # if equal:
            #     return True

        return False

    def can_do_action(self, state: State, action: Action):
        return state.satisfied_precondition_two(action)

    def check_goal(self):
        for current_state in self.currentStates:
            if current_state.final_state(self.final):
                self.print_actions(current_state)

                return True

        return False

    def print_actions(self, final_state: State):
        temp = State()
        temp = final_state

        action_list = []

        while temp.parent is not None:
            action_list.append(temp.action.action_name)
            temp = temp.parent

        while len(action_list) != 0:
            print(action_list.pop())
