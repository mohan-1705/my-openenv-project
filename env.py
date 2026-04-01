class MyEnv:
    def __init__(self):
        self.state = 0

    def reset(self):
        self.state = 0
        return {"state": self.state}

    def step(self):
        self.state += 1
        reward = 1
        done = self.state >= 5
        return {"state": self.state}, reward, done, {}
