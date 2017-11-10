# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:56:03 2017

@author: Ellabban Amr
"""

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight', 'value_density'])


with open("C:\\Users\\Ellabban Amr\\Documents\\GitHub\\online_courses\\01_Discrete_Optimization\\Week2\\knapsack\\data\\ks_4_0", 'r') as input_data_file:
            input_data = input_data_file.read()

            
lines = input_data.split('\n')

firstLine = lines[0].split()
item_count = int(firstLine[0])
capacity = int(firstLine[1])

items = []

for i in range(1, item_count+1):
    line = lines[i]
    parts = line.split()
    items.append(Item(i-1, int(parts[0]), int(parts[1]), float(parts[0]) / float(parts[1])))

taken = [0]*len(items)      

def depth_search_recursion(take_next, items, capacity):
    
    # Termination of recursion
    if len(items) == 1:
        
        if take_next and items[0].weight <= capacity:
            taken = [1]
            value = items[0].value
            valid_solution = True            
        elif take_next:
            taken = None
            value = None
            valid_solution = False
        else:
            taken = [0]
            value = 0
            valid_solution = True
    
        return taken, value, valid_solution
    # Main part
    else:
        
        if take_next and items[0].weight <= capacity:
            
            taken_left, value_left, valid_solution_left = depth_search_recursion(True, items[1:], capacity - items[0].weight)
            
            taken_right, value_right, valid_solution_right = depth_search_recursion(False, items[1:], capacity - items[0].weight)

            if (not valid_solution_left and not valid_solution_right):
                    taken = None
                    value = None
                    valid_solution = False
                    
            elif not valid_solution_right:
                    taken = [1] + taken_left
                    value = items[0].weight + value_left
                    valid_solution = True   
                    
            elif not valid_solution_left:
                    taken = [1] + taken_right
                    value = items[0].weight + value_right
                    valid_solution = True
                    
            else:
                if value_left > value_right:
                    taken = [1] + taken_left
                    value = items[0].weight + value_left
                    valid_solution = True    
                else:
                    taken = [1] + taken_right
                    value = items[0].weight + value_right
                    valid_solution = True 
            
        elif take_next:
            taken = None
            value = None
            valid_solution = False
            
            return taken, value, valid_solution
        else:
            taken_left, value_left, valid_solution_left = depth_search_recursion(True, items[1:], capacity)
            
            taken_right, value_right, valid_solution_right = depth_search_recursion(False, items[1:], capacity)
            

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
        
def depth_search(items, capacity):
    
    taken_left, value_left, valid_solution_left = depth_search_recursion(True, items, capacity - items[0].weight)
    taken_right, value_right, valid_solution_right = depth_search_recursion(False, items, capacity)
    
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
        
                
    return taken, value, valid_solution