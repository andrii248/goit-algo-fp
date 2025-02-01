import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls=1000000):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sums_count[roll_sum] += 1

    probabilities = {s: (count / num_rolls) * 100 for s, count in sums_count.items()}
    return probabilities


def plot_probabilities(probabilities):
    theoretical_probs = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78,
    }

    sums = list(probabilities.keys())
    sim_values = list(probabilities.values())
    theo_values = [theoretical_probs[s] for s in sums]

    plt.figure(figsize=(10, 5))
    plt.bar(sums, sim_values, width=0.4, label="Simulated", color="blue", alpha=0.6)
    plt.bar(
        [s + 0.4 for s in sums],
        theo_values,
        width=0.4,
        label="Theoretical",
        color="red",
        alpha=0.6,
    )

    plt.xlabel("Sum of Dice")
    plt.ylabel("Probability (%)")
    plt.title("Simulated vs Theoretical Probabilities of Dice Sums")
    plt.xticks(sums)
    plt.legend()
    plt.show()


# Виконання симуляції
num_rolls = 1000000
simulated_probs = simulate_dice_rolls(num_rolls)
plot_probabilities(simulated_probs)
