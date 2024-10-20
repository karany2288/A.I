import queue as Q
from RMP import dict_gn  # Dictionary with distances between cities
from RMP import dict_hn  # Dictionary with heuristic values for cities

# Define start and goal cities
start = 'Arad'
goal = 'Bucharest'

result = ''  # To store the result path

# Function to calculate f(n) = g(n) + h(n)
def get_fn(citystr):
    cities = citystr.split(",")
    gn = 0
    hn = 0
    # Calculate g(n) (total distance) by summing distances between consecutive cities
    for ctr in range(len(cities) - 1):
        gn += dict_gn[cities[ctr]][cities[ctr + 1]]
    # Get h(n) (heuristic) for the last city
    hn = dict_hn[cities[-1]]
    return hn + gn

# Function to print the contents of the priority queue
def printout(cityq):
    print("Queue status:")
    for i in range(cityq.qsize()):
        print(cityq.queue[i])

# Expand the current node and add neighbors to the queue
def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get()
    result = citystr + "::" + str(tot)  # Update the result with the path
    if thiscity == goal:  # If we reach the goal, return
        return
    
    # Get the next best f(n) in the queue (second-best option)
    nexttot = 999
    if not cityq.empty():
        nexttot, nextcitystr, nextthiscity = cityq.queue[0]
    
    print("Expanded city:", thiscity)
    print("Second best f(n):", nexttot)
    
    # Temporary priority queue to hold the expanded nodes
    tempq = Q.PriorityQueue()
    
    # Explore neighbors of the current city
    for cty in dict_gn[thiscity]:
        tempq.put((get_fn(citystr + ',' + cty), citystr + ',' + cty, cty))
    
    # Process the best two options and decide which to expand
    for ctr in range(1, 3):
        ctrtot, ctrcitystr, ctrthiscity = tempq.get()
        if ctrtot < nexttot:  # If a better option is found
            cityq.put((ctrtot, ctrcitystr, ctrthiscity))  # Expand this city
        else:  # Otherwise, continue with the current city
            cityq.put((ctrtot, citystr, thiscity))
            break
    
    printout(cityq)  # Print the queue after expansion
    expand(cityq)  # Recursive call to expand further

# Main function to initiate the search
def main():
    cityq = Q.PriorityQueue()  # Initialize the priority queue
    thiscity = start
    cityq.put((999, "NA", "NA"))  # Dummy node to ensure queue is not empty initially
    cityq.put((get_fn(start), start, thiscity))  # Add the start city with its f(n)
    expand(cityq)  # Start expanding the cities
    print("Final path and cost:", result)  # Print the final result

# Run the main function
main()
