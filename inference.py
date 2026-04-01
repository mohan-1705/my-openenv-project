from env import SimpleEnv

env = SimpleEnv()
state = env.reset()

for i in range(5):
    action = "increase"   # simple baseline
    state, reward, done, _ = env.step(action)
    print(f"Step {i}, State: {state}, Reward: {reward}")

    if done:
        break