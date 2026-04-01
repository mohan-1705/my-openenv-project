from env import SimpleEnv

env = SimpleEnv()

tasks = env.get_tasks()

results = []

for task in tasks:
    state = env.reset()
    done = False

    while not done:
        output = env.step()
        state = output["state"]
        done = output["done"]

    final_state = state["state"]
    score = env.grade(final_state, task["goal"])

    results.append({
        "task": task["name"],
        "final_state": final_state,
        "score": score
    })

print({"results": results})
