def upper_bound_estimator(items, capacity):
    sorted_items = sorted(items, key=lambda x: x.value_density, reverse=True)

    value = 0
    weight = 0

    for ix in range(0, len(sorted_items)):
        if weight + sorted_items[ix].weight <= capacity:
            value += sorted_items[ix].value
            weight += sorted_items[ix].weight
        else:
            value += sorted_items[ix].value_density * (capacity - weight)
            break

    return value


def depth_search_recursion(take_next, items, capacity, best_possible, best_seen = 0):
    
    if not take_next and best_possible - items[0].value < best_seen:
        taken = None
        value = None
        valid_solution = False

        return taken, value, valid_solution
    # Termination of recursion
    elif len(items) == 1:
        
        if take_next and items[0].weight <= capacity:
            taken = [1]
            value = items[0].value
            valid_solution = True
            best_seen = value           
        elif take_next:
            taken = None
            value = None
            valid_solution = False
            best_seen = -1
        else:
            taken = [0]
            value = 0
            valid_solution = True
            best_seen = value

        return taken, value, valid_solution
    # Main part
    else:

        if items[0].index == 2:
            a=5

        if take_next and items[0].weight <= capacity:
            
            taken_left, value_left, valid_solution_left = depth_search_recursion(True, items[1:], capacity - items[0].weight, best_possible, best_seen)
            if value_left is not None and value_left > best_seen:
                best_seen = value_left
            
            taken_right, value_right, valid_solution_right = depth_search_recursion(False, items[1:], capacity - items[0].weight, best_possible - items[0].value, best_seen)
            if value_right is not None and value_right > best_seen:
                best_seen = value_right

            if (not valid_solution_left and not valid_solution_right):
                    taken = None
                    value = None
                    valid_solution = False
                    
            elif not valid_solution_right:
                    taken = [1] + taken_left
                    value = items[0].value + value_left
                    valid_solution = True   
                    
            elif not valid_solution_left:
                    taken = [1] + taken_right
                    value = items[0].value + value_right
                    valid_solution = True
                    
            else:
                if value_left > value_right:
                    taken = [1] + taken_left
                    value = items[0].value + value_left
                    valid_solution = True    
                else:
                    taken = [1] + taken_right
                    value = items[0].value + value_right
                    valid_solution = True 
            
        elif take_next:
            taken = None
            value = None
            valid_solution = False
            
            return taken, value, valid_solution
        else:
            taken_left, value_left, valid_solution_left = depth_search_recursion(True, items[1:], capacity, best_possible, best_seen)
            if value_left is not None and value_left > best_seen:
                best_seen = value_left

            taken_right, value_right, valid_solution_right = depth_search_recursion(False, items[1:], capacity, best_possible - items[0].value, best_seen)
            if value_right is not None and value_right > best_seen:
                best_seen = value_left

            if (not valid_solution_left and not valid_solution_right):
                    taken = None
                    value = None
                    valid_solution = False
                    
            elif not valid_solution_right:
                    taken = [0] + taken_left
                    value = value_left
                    valid_solution = True   
                    
            elif not valid_solution_left:
                    taken = [0] + taken_right
                    value = value_right
                    valid_solution = True
                    
            else:
                if value_left > value_right:
                    taken = [0] + taken_left
                    value = value_left
                    valid_solution = True
                else:
                    taken = [0] + taken_right
                    value = value_right
                    valid_solution = True 
                
                
        return taken, value, valid_solution
        
def depth_search(items, capacity, sort_version = True):

    if sort_version:
        sorted_items = sorted(items, key=lambda x: x.value, reverse=True)
    else:
        sorted_items = items

    optimistic_estimate = sum([x.value for x in sorted_items])
    print(optimistic_estimate)
    #optimistic_estimate = upper_bound_estimator(sorted_items, capacity)
    #print(optimistic_estimate)

    taken_left, value_left, valid_solution_left = depth_search_recursion(True, sorted_items, capacity, optimistic_estimate, -1)
    if valid_solution_left:
        taken_right, value_right, valid_solution_right = depth_search_recursion(False, sorted_items, capacity, optimistic_estimate, value_left)
    else:
        taken_right, value_right, valid_solution_right = depth_search_recursion(False, sorted_items, capacity, optimistic_estimate, -1)
    
    if (not valid_solution_left and not valid_solution_right):
            taken = None
            value = None
            valid_solution = False
            
    elif not valid_solution_right:
            taken = taken_left
            value = value_left
            valid_solution = True   
            
    elif not valid_solution_left:
            taken = taken_right
            value = value_right
            valid_solution = True
            
    else:
        if value_left > value_right:
            taken = taken_left
            value = value_left
            valid_solution = True    
        else:
            taken = taken_right
            value = value_right
            valid_solution = True

    if sort_version:
        taken_final = [0]*len(items)
        for item in range(0,len(items)):
            if taken[item] == 1:
                taken_final[sorted_items[item].index] = 1
    else:
        taken_final = taken

    return taken_final, value, valid_solution
