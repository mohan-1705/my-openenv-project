class SimpleEnv:
    def __init__(self):
        self.state_val = 0
        self.steps = 0

    def reset(self):
        self.state_val = 0
        self.steps = 0
        return {"state": self.state_val}

    def step(self, action):
        self.steps += 1

        if action == "increase":
            self.state_val += 1
            reward = 1
        elif action == "decrease":
            self.state_val -= 1
            reward = -1
        else:
            reward = 0

        done = self.steps >= 5

        return {"state": self.state_val}, reward, done, {}

    def state(self):
        return {"state": self.state_val}