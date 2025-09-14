class random_policy:
    def __init__(self):
        pass
    def act(self, obs, action_space):
        return action_space.sample()
    def update(self, *arg):
        pass