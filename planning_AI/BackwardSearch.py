from State import State
from Action import Action


def can_undo_action(action, state):
    for effect in action.get_add_list():
        if state.get_positive_literals().__contains__(effect):
            return True

    for effect in action.get_delete_list():
        if state.get_negative_literals().__contains__(effect):
            return True


def undo_action(state, action):
    new_state = State()
    new_state.get_positive_literals().extend(state.get_positive_literals())
    new_state.get_negative_literals().extend(state.get_negative_literals())

    #removing from add list
    for unit in action.add_list:
        if new_state.get_positive_literals().__contains__(unit):
            new_state.positive_literals.remove(unit)

    #adding positive preconditional
    for unit in action.get_positive_preconditions():
        if not new_state.get_positive_literals().__contains__(unit):
            new_state.positive_literals.append(unit)

    #deleting from delete list literals
    for unit in action.get_delete_list():
        if new_state.get_negative_literals().__contains__(unit):
            new_state.negative_literals.remove(unit)

    for unit in action.get_negative_preconditions():
        if not new_state.get_negative_literals().__contains__(unit):
            new_state.negative_literals.append(unit)

    for unit in new_state.get_positive_literals():
        if new_state.get_negative_literals().__contains__(unit):
            new_state.positive_literals.remove(unit)

    for unit in new_state.get_negative_literals():
        if new_state.get_positive_literals().__contains__(unit):
            new_state.negative_literals.remove(unit)

    return new_state


class BackwardSearch:

    def __init__(self, init: State, final: State, actions):
        self.init = init
        self.final = final
        self.actions = actions

        self.currentStates = []
        self.exploredStates = []

    def search(self):
        self.currentStates.append(self.final)

        while len(self.currentStates) != 0:
            state = self.currentStates.pop(0)
            for action in self.actions:

                explored_state = False

                for unit in self.exploredStates:
                    if unit == state:
                        explored_state = True

                if not explored_state:
                    if can_undo_action(action, state):
                        new_state = undo_action(state, action)
                        new_state.action = action
                        new_state.parent = state
                        self.currentStates.append(new_state)

            self.exploredStates.append(state)
            if self.check_goal():
                return

    def check_goal(self):
        for state in self.currentStates:
            if state.final_state(self.init):
                action_results = []
                while state.parent is not None:
                    action_results.append(state.action)
                    state = state.parent

                while len(action_results) != 0:
                    result = action_results.pop(0)
                    print(result.action_name)
                return True

        return False

