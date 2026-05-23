items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    result = []

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            result.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return result, total_calories

def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]

            if w >= cost:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - cost] + calories)

    w = budget
    result = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            result.append(name)
            w -= items[name]["cost"]

    result.reverse()

    return result, dp[n][budget]

budget = int(input("Введіть суму бюджету: "))

print("Greedy:")
print(greedy_algorithm(items, budget))

print("\nDynamic Programming:")
print(dynamic_programming(items, budget))