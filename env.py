class SimpleEnv:
    def __init__(self):
        self.state = 0

    def reset(self):
        self.state = 0
        return {"state": self.state}

    def step(self, action):
        self.state += 1
        reward = 1
        done = self.state >= 5

        return {
            "state": {"state": self.state},
            "reward": reward,
            "done": done
        }
