def greedy_solver_1(items, capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken

def greedy_solver_2(items, capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order of most valuable until the knapsack is full
    sorted_items = sorted(items, key=lambda x: x.value, reverse=True)

    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in sorted_items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken

def greedy_solver_3(items, capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order of smallest until the knapsack is full
    sorted_items = sorted(items, key=lambda x: x.weight)

    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in sorted_items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken

def greedy_solver_4(items, capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order of value_density until the knapsack is full
    sorted_items = sorted(items, key=lambda x: x.value_density, reverse=True)

    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in sorted_items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken