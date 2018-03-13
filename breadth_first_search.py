#!/usr/bin/python3

# breadth_first_search.py - implementation of Breadth First Search
# In this example, I am looking for someone in my network of friends who speaks
# French. I will try to find the 'shortest path' to the person who speaks
# French. I will return the name of the closest French-speaking person, or None
# if nobody in my network speaks French.

# Creating the graph:
graph = {}
graph['Me'] = ['Derrick', 'Isiah', 'Aleah', 'Jenny']

# 1st Degree Connections
graph['Derrick'] = ['Aaron', 'Marissa', 'Suzy']
graph['Isiah'] = ['Patrick', 'Jack', 'Suzy']
graph['Jenny'] = ['Pierre', 'Raphael', 'Mike']
graph['Aleah'] = []

# 2nd Degree Connections
graph['Aaron'] = []
graph['Marissa'] = ['Peggy']
graph['Patrick'] = []
graph['Jack'] = []
graph['Suzy'] = ['Olivia']
graph['Pierre'] = []
graph['Raphael'] = []
graph['Mike'] = []

# 3rd Degree Connections
graph['Peggy'] = []
graph['Olivia'] = []

# Who speaks French?
french_speakers = ['Suzy', 'Pierre', 'Olivia']

def breadth_first_search(name):
    # Create a queue to ensure we are looking at our closes neighbors first
    from collections import deque
    people_to_check = deque()
    # Initiate the queue with `name`'s neighbors
    people_to_check += graph[name]
    # Create a list of people we've already checking someone twice
    already_checked = []
    # While the queue isn't empty...
    while people_to_check:
        # Pop off the first person and check if they speak French
        person = people_to_check.popleft()
        if person not in already_checked:
            if person in french_speakers:
                return person
            # If not, add their neighbors to the end of the queue
            else:
                people_to_check += graph[person]
                already_checked.append(person)

print(breadth_first_search('Me'))
