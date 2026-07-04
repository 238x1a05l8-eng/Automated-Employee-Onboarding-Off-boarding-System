import matplotlib.pyplot as plt

# Stakeholder data
stakeholders = {
    "CEO": (9, 9),
    "Project Manager": (8, 8),
    "Customer": (6, 9),
    "Development Team": (5, 7),
    "Suppliers": (4, 5),
    "Government": (9, 4),
    "Investors": (8, 6),
    "Media": (3, 7),
    "Local Community": (2, 5),
    "End Users": (4, 8)
}

# Create figure
plt.figure(figsize=(10, 8))

# Plot stakeholders
for name, (power, interest) in stakeholders.items():
    plt.scatter(power, interest, s=120, color="steelblue")
    plt.text(power + 0.1, interest + 0.1, name, fontsize=9)

# Draw quadrant lines
plt.axhline(y=5, color='gray', linestyle='--')
plt.axvline(x=5, color='gray', linestyle='--')

# Quadrant labels
plt.text(1, 9.5, "Keep Informed", fontsize=11, color="green")
plt.text(6.2, 9.5, "Manage Closely", fontsize=11, color="green")
plt.text(1, 1, "Monitor", fontsize=11, color="red")
plt.text(6.2, 1, "Keep Satisfied", fontsize=11, color="orange")

# Labels and title
plt.title("Stakeholder Mapping (Power vs Interest Matrix)", fontsize=14)
plt.xlabel("Power")
plt.ylabel("Interest")

# Set limits
plt.xlim(0, 10)
plt.ylim(0, 10)

# Grid
plt.grid(alpha=0.3)

plt.show()