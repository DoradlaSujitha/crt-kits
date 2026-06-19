#linear queue
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,values):
        self.queue.append(values)
        print(f"{values} is enqueue successfull")
    def dequeue(self):
        self.queue.pop()
    def front(self):
        return self.queue[0]
    def rear(self):
        return self.queue[-1]
    def display(self):
        return self.queue
    def isEmpty(self):
        if self.queue==0:
            print("Queue is empty")
        else:
            print("Queue is not empty")
    def clear(self):
        self.queue=[]
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.display())
print(q.isEmpty())
print(q.front())
print(q.rear())
q.dequeue()
print(q.display())
q.clear()
print(q.display())
    
#CircularQueue
class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def IsFull(self):
        return(self.rear+1)% self.size==self.front
    def isEmpty(self):
       return self.front==-1
    def enqueue(self, value):
        if(self.IsFull()):
            return "Queue Over Flow!"
        if self.isEmpty():self.front=0
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear+1]=value
        print(f"Enqueued {value} at index {self.rear}")
    def dequeue(self):
        if self.isEmpty():
            return "Queue Underflow!"
        val=self.queue[self.front]
        self.queue[self.front]=None
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return val
    def display(self):
        if self.isEmpty():print("Empty");return
        i,elems= self.front,[]
        while True:
            elems.append(self.queue[i])
            if i==self.rear:break
            i=(i+1)%self.size
        print("CQ:",elems)
d=CircularQueue(5)
d.enqueue(10)
d.enqueue(20)
d.enqueue(30)
print(d.display())
print(d.isEmpty())
d.dequeue()
print(d.display())

#deque
from collections import deque
class Deque:
    def __init__(self):
        self.dq = deque()
    def addFront(self,value):
        self.dq.appendleft(value)
        print(f"AddFront {value} -> {list(self.dq)}")
    def addRare(self, value):
        self.dq.append(value)
        print(f"AddRear {value} -> {list(self.dq)}")
    def removeFront(self):
        if self.isEmpty(): return "Empty!"
        val = self.dq.popleft()
        print(f"RemFront {val} -> {list(self.dq)}")
        return val
    def removeRare(self):
        if self.isEmpty(): return "Empty!"
        val = self.dq.pop()
        print(f"RemRare {val} -> {list(self.dq)}")
        return val
    def peekFront(self):
        return self.dq[0] if not self.isEmpty() else "Empty"
    def peekRare(self):
        return self.dq[-1] if not self.isEmpty() else "Empty"
    def isEmpty(self):
        return len(self.dq) == 0
dq = Deque()
dq.addFront(10)
dq.addRare(20)
dq.addFront(5)
dq.addRare(30)
dq.removeFront()
dq.removeRare()
print("Front:", dq.peekFront())
print("Rear:", dq.peekRare())
print("Empty?", dq.isEmpty())

#priority queue
import heapq
class PriorityQueue:
    def __init__(self):
        self.heap=[]
        self.counter=0
    def insert(self,item,priority):
        heapq.heappush(self.heap,(priority,self.counter,item))
        self.counter+=1
        print(f"Inserted '{item}'with priority {priority}")
    def extractMin(self):
        if self.isEmpty(): return "Queue is Empty"
        priority,_,item=heapq.heappop(self.heap)
        print(f"Extracted '{item}'with priority {priority}")
    def peek(self):
        return self.heap[0][2] if not self.isEmpty() else "Empty"
    def isEmpty(self):
        return len(self.heap)==0
    def size(self):
        return len(self.heap)
pq=PriorityQueue()
pq.insert("Low Task",5)
pq.insert("High Task",1)
pq.insert("Med Task",3)
print("Peek: ",pq.peek())
pq.extractMin()
pq.extractMin()
