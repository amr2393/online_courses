import numpy as np

def build_cost_matrix(items, capacity):

    cost = np.zeros((capacity+1, len(items)+1))

    for item_ix in range(1, len(items)+1):
        for capacity_ix in range(1, capacity+1):

            if items[item_ix-1].weight <= capacity_ix:
                cost[capacity_ix, item_ix] = \
                  max(\
                    cost[capacity_ix, item_ix-1], \
                    items[item_ix-1].value + cost[capacity_ix-items[item_ix-1].weight, item_ix-1]\
                   )
            else:
                cost[capacity_ix, item_ix] = cost[capacity_ix, item_ix-1]


    return cost

def backtrack(cost, items):

    value = cost[-1, -1]
    taken = [0]*(len(items)+1)

    capacity_index = np.shape(cost)[0]-1
    for item_index in range(len(items), 0, -1):
        
        if cost[capacity_index, item_index-1] < cost[capacity_index, item_index]:
            taken[item_index] = 1
            capacity_index -= items[item_index-1].weight

    taken = taken[1:]

    return value, taken

def dp_optimizer(items, capacity):

    cost = build_cost_matrix(items, capacity)
    value, taken = backtrack(cost, items)

    return value, taken
