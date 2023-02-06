import collections
from typing import List


class Solution:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
      return 0

    stopBoard = collections.defaultdict(lambda: [])

    for bus,route_bus in enumerate(routes):
      for route in route_bus:
        stopBoard[route].append(bus)

    stack=collections.deque([source])

    busTaken=set()
    routeTaken=set()
    res=0

    while stack:
      res+=1
      lenStack=len(stack)
      
      for _ in range(lenStack):
        r=stack.popleft()
        routeTaken.add(r)

        for bus in stopBoard[r]:
          if bus not in busTaken:
            busTaken.add(bus)

            for route in routes[bus]:
              if route not in routeTaken:
                if route==target: 
                  return res
                else: 
                  stack.append(route)
              
    return -1