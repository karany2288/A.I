import queue as Q
from RMP import dict_gn, dict_hn
start = 'Arad' 
goal = "Bucharest" 
result='' 
def BFS(city,cityq,visitedq): 
    global result 
    if city==start: 
        result = result + "" + city 
    for eachcity in dict_gn[city].keys():
        if eachcity==goal: 
            result = result + " " + eachcity
            return 
        if eachcity not in cityq.queue and eachcity not in visitedq.queue:
            cityq.put(eachcity) 
            result = result + " " + eachcity
    visitedq.put(city) 
    BFS(cityq.get(),cityq,visitedq)
def main(): 
 cityq = Q.Queue() 
 visitedq = Q.Queue() 
 BFS(start,cityq,visitedq) 
 print("BFS Traversal From ", start," to " , goal, "is :")
 print(result) 
main() 