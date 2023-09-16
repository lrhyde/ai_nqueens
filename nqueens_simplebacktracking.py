# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:48:08 2021

@author: 1531402
"""


def test_solution(state):
    for var in range(len(state)): 
        left = state[var]
        middle = state[var] 
        right = state[var]
        for compare in range(var + 1, len(state)): 
            left -= 1
            right += 1
            if state[compare] == middle: 
                #print(var, "middle", compare) 
                return False
            if left >= 0 and state[compare] == left: 
                #print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right: 
                #print(var, "right", compare)
                return False
    return True


def goal_test(state):
    return test_solution(state)
    #return is_possible(state)

def is_possible(state):
    for i in range(len(state)):
        if(not state[i] ==-1):
            for j in range(i):
                if(state[i]==state[j]): return False
        else: return False
    for i in range(len(state)):
        if(not state[i] ==-1):
            for j in range(i):
                if(not state[j]==-1): 
                    if(abs(i-j)==abs(state[i]-state[j])): return False
        else: return False
    return True

def csp_backtracking(state):
    if is_possible(state): return state
    var = get_next_unassigned_var(state)
    if(var==None): return None
    for val in get_sorted_values(state, var): 
        new_state = val
        result = csp_backtracking(new_state)
        if (not result ==None):
            return result
    return None


def get_next_unassigned_var(state):
    for i, num in enumerate(state):
        if(num==-1): return i
    return None


def get_sorted_values(state, var):
    #array = state
    #returner = []
    #for i in range(len(state)):
    #    copyA = array
    #    copyA[var] = i
    #    returner.append(copyA)
    #return returner    
    returner = []
    for i in range(len(state)):
        arr = state[:var] + [i] + state[var+1:]
        returner.append(arr)
    return returner 


def createBoard(size):
    array = []
    for i in range(size):
        array.append(-1)
    return array
print(csp_backtracking(createBoard(9)))
#get_next_unassigned_var just pick the first row where a 
#queen hasn’t been placed, and 
#get_sorted_values would simply produce, in ascending order, 
#a list of all available spaces in that row