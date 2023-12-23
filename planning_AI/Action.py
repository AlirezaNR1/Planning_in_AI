class Action:
    def __init__(self, name):
        self.action_name = name
        self.positive_preconditions = []
        self.negative_preconditions = []
        self.effects = []
        self.add_list = []
        self.delete_list = []

    def get_name(self):
        return self.action_name

    def get_positive_preconditions(self):
        return self.positive_preconditions

    def get_negative_preconditions(self):
        return self.negative_preconditions

    def get_effects(self):
        return self.effects

    def get_add_list(self):
        return self.add_list

    def get_delete_list(self):
        return self.delete_list

    def add_precondition(self, positive, precondition):
        if positive:
            self.positive_preconditions.append(precondition)
        else:
            self.negative_preconditions.append(precondition)

    def add_effect(self, positive, effect):
        self.effects.append(effect)
        if positive:
            self.add_list.append(effect)
        else:
            self.delete_list.append(effect)

