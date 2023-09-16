# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:48:08 2021

@author: 1531402
"""
import time, random

def test_solution(state):
    if(state==None): return False
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
                if(abs(i-j)==abs(state[i]-state[j])): return False
        else: return False
    """
    for i in range(len(state)):
        if(not state[i] ==-1):
            for j in range(i):
                if(not state[j]==-1): 
                    if(abs(i-j)==abs(state[i]-state[j])): return False
        else: return False
        """
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

def csp_backtracking2(state, fullCols, fullDiags):
    if is_possible(state): return state
    var = get_next_unassigned_var(state)
    if(var==None): return None
    for val in get_sorted_values2(state, var, fullCols): 
        if(val not in fullCols):
            new_state = state[:var] + [val] + state[var+1:]
            fc2 = fullCols[0:len(fullCols)]
            fc2.append(val)
            fd2 = fullCols[0:len(fullCols)]
            fd2.append(val-var)
            result = csp_backtracking2(new_state, fc2, fd2)
            if (not result ==None):
                return result
    return None


def get_next_unassigned_var(state):
    """
    #for i, num in enumerate(state):
        #if(num==-1): return i
    for i in range(int(len(state)/2)):
        if(state[int(len(state)/2) + i]==-1): return int(len(state)/2) + i
        if(state[int(len(state)/2) - i]==-1): return int(len(state)/2) - i
    return None
    """
    if(-1 not in state): return None
    var = None
    while(var==None):
        i = random.randint(0, len(state)-1)
        if(state[i]==-1): return i

def get_sorted_values(state, var):
    return list(range(0, len(state)))

def get_sorted_values2(state, var, fullCols):
    arr = []
    while(len(arr)<len(state)-len(fullCols)):
        i = random.randint(0, len(state)-1)
        if(i not in fullCols and i not in arr): arr.append(i)
    return arr


def createBoard(size):
    array = []
    for i in range(size):
        array.append(-1)
    return array

def createFlawed(size):
    array = [-1]
    for i in range(size):
        potential = -1
        while(potential in array):
            potential = random.randint(0, size-1)
        array.append(potential)
    array.remove(-1)
    return array

def countC(state):
    collisions= 0
    past = []
    for i in range(len(state)):
        for j in range(i):
            if(state[i]==state[j] and (j, i) not in past): 
                collisions+=1
                past.append((i, j))
            elif(abs(i-j)==abs(state[i]-state[j]) and (j, i) not in past): 
                collisions+=1
                past.append((i, j))
    return collisions
def countCR(state, i):
    collisions= 0
    past = []
    for j in range(len(state)):
        if(state[i]==state[j] and (j, i) not in past): 
            collisions+=1
            past.append((i, j))
        elif(abs(i-j)==abs(state[i]-state[j]) and (j, i) not in past): 
            collisions+=1
            past.append((i, j))
    return collisions

def incRepair(state):
    collisions = countC(state)
    print(str(collisions))
    while(collisions>0):
        mostColl = []
        for i in range(len(state)):
            mostColl.append(countCR(state, i))
        va = [i for i, x in enumerate(mostColl) if x == max(mostColl)]
        var = random.choice(va)
        leastColl = []
        for i in range(len(state)):
            arr = state[:var] + [i] + state[var+1:]
            leastColl.append(countCR(arr, var))
        va = [i for i, x in enumerate(leastColl) if x == min(leastColl)]
        state[var] = random.choice(va)
        collisions = countC(state)
        print(state)
        print(str(collisions))
    return state
a = createFlawed(47)
print(a)
#print(str(countC(a)))
t = time.perf_counter()
array1 = incRepair(a)
t2 = time.perf_counter()
a = createFlawed(67)
print(a)
#print(str(countC(a)))
t3 = time.perf_counter()
array = incRepair(a)
t4 = time.perf_counter()
print(array1)
print(str(test_solution(array1)) + " in " +  str(t2-t))
print(array)
print(str(test_solution(array)) + " in " + str(t4-t3))
"""
size1 = 20
t1 = time.perf_counter()
solution1 = csp_backtracking2(createBoard(size1), [])
t2 = time.perf_counter()
print(str(solution1))
print(str(size1) + ": " + str(test_solution(solution1)) + " in " + str(t2-t1))
"""
"""
size2 = 8
t3 = time.perf_counter()
solution2 = csp_backtracking(createBoard(size1))
t4 = time.perf_counter()
print(str(solution2))
print(str(size2) + ": " + str(test_solution(solution2)) + " in " + str(t4-t3))
t5 = time.perf_counter()
print("total: " + str(t5-t1))
"""
