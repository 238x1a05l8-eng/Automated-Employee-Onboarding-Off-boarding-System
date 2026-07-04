import matplotlib.pyplot as plt

# Roadmap tasks
tasks = [
    ("Requirement Analysis", 1, 2),
    ("Stakeholder Alignment", 2, 2),
    ("System Design", 4, 3),
    ("Development", 7, 5),
    ("Testing", 12, 3),
    ("Deployment", 15, 2),
    ("Training", 17, 2),
    ("Project Closure", 19, 1)
]

fig, ax = plt.subplots(figsize=(12, 6))

# Plot Gantt bars
for i, (task, start, duration) in enumerate(tasks):
    ax.barh(task, duration, left=start, color="steelblue", edgecolor="black")

# Formatting
ax.set_xlabel("Project Timeline (Weeks)")
ax.set_title("Execution Roadmap")
ax.set_xlim(0, 21)
ax.set_xticks(range(1, 21))
ax.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()