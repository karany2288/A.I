import queue as Q 
from RMP import dict_gn 
start = "Arad" 
goal = "Bucharest" 
result = ""

def DLS(city,visitedstack,startlimit,endlimit): 
    global result 
    found = 0 
    result = result + city + " " 
    visitedstack.append(city) 
    if city == goal: 
        return 1 
    if startlimit == endlimit: 
        return 0 
    for eachcity in dict_gn[city].keys(): 
        if eachcity not in visitedstack: 
            found = DLS(eachcity,visitedstack,startlimit+1,endlimit) 
        if found: 
            return found 

def IDDFS(city,visitedstack,endlimit): 
    global result 
    for i in range(0,endlimit): 
        print("Seaching at Limit:", i) 
        found = DLS(city,visitedstack, 0 , i) 
        if found: 
            print("Found") 
            break 
        else: 
            print("Not Found!") 
            print(result) 
            print("______") 
            result="" 
            visitedstack = []

def main(): 
    visitedstack = [] 
    IDDFS(start,visitedstack,9) 
    print("IDDFS Traversal from ", start, " to ",goal," is:")
    print(result)
main()
