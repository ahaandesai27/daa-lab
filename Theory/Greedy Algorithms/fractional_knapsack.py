def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0

    for weight, value in items:
        if capacity == 0:
            break
        take_weight = min(weight, capacity)
        ratio = value/weight
        total_value += take_weight * ratio
        capacity -= take_weight

    return total_value

# Example usage
items = [(10, 60), (20, 100), (30, 120)]        # (weight, value)
capacity = 50

max_value = fractional_knapsack(items, capacity)
print("Maximum value:", max_value)