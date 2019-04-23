"""APPROACH = 
1. Loop through txt file appending lines into a list
2. Sort the list by Room, Visitor, InOut
3. Aggregate mins on Room & Visitor
4. Iterate through new list values, summing mins per room and counting visitors per room
5. Calc avg time per visit using above 2 values and output to txt file
"""

from pprint import pprint

with open('traffic.txt', 'r') as file_object:
    traffic_rows = []

    for line in file_object:        
        line = line.rstrip('\n')
        x = line.split(" ")
        mins = int(x[3])
        if x[0] == "0" or x[0] == "5":
            """Make the In min value a negative as we're going to
               aggregrate with the Out min value."""
            if x[2] == "I":
                mins = mins *-1
            traffic_rows.append({int(x[0]), int(x[1]), x[2], mins})                  
       
    pprint(traffic_rows)

    #traffic_rows = sorted(traffic_rows)  
    #print(traffic_rows) 

