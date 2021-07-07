
######### Breadth-First  Algorithm ###########
from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['tom'] = []
graph['jonny'] = []

def search(name):
  search_queue = deque() # this create a queue in python
  search_queue += graph[name] # we will add all of the neighbors to the queue
  searched = [] # to make sure we dont check a person twice
  while search_queue:
    person =  search_queue.popleft() # we grab the first element in the queue
    if not person in searched:
      if person_is_a_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False

def person_is_a_seller(name):
    return name[-1] == 'm'

search('you')