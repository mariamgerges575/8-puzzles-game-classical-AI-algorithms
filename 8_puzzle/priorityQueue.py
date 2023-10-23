import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def push(self, pair):
        heapq.heappush(self.elements, pair)

    def pop(self):
        return heapq.heappop(self.elements)
if __name__=='__main__':
# Usage example
    pq = PriorityQueue()

    # Push pairs of integers into the priority queue
    pq.push((5, 3))
    pq.push((2, 7))
    pq.push((8, 1))
    pq.push((4, 6))

    # Pop pairs in order of priority (sorted by the first element)
    while pq.elements:
        pair = pq.pop()
        print(pair)
