class SimpleEnv:
    def __init__(self):
        self.state = 0
        self.max_state = 10

    def reset(self):
        self.state = 0
        return {"state": self.state}

    def step(self, action=None):
        # move forward
        self.state += 1

        done = self.state >= self.max_state

        #  Reward logic 
        reward = self.state / self.max_state  # progress-based reward

        return {
            "state": {"state": self.state},
            "reward": reward,
            "done": done
        }

    #  TASKS 
    def get_tasks(self):
        return [
            {"name": "easy", "goal": 3},
            {"name": "medium", "goal": 6},
            {"name": "hard", "goal": 10}
        ]

    #  GRADER 
    def grade(self, final_state, goal):
        if final_state >= goal:
            return 1.0
        else:
            return final_state / goal
