# ex of using a list as a queue
from collections import deque

queue=deque(["ra-men","sushi","natto"])
queue.append("happy")
queue.append("info")

print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

#additional operations for comparison
print(queue.pop())
print(queue)

