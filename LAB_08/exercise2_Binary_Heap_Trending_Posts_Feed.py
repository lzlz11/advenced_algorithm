import math
from typing import List, Optional, Tuple

class HeapEntry:
    def __init__(self, likes: int, post_id: str, timestamp: int):
        self.likes = likes
        self.post_id = post_id
        self.timestamp = timestamp

class TrendingHeap:
    def __init__(self):
        self.heap: List[HeapEntry] = []
        self.size: int = 0

def parent(i: int) -> int:
    return (i - 1) // 2

def left_child(i: int) -> int:
    return 2 * i + 1

def right_child(i: int) -> int:
    return 2 * i + 2

def swap(heap: List[HeapEntry], i: int, j: int) -> None:
    """Swap two elements in the heap list"""
    temp = heap[i]
    heap[i] = heap[j]
    heap[j] = temp

def heap_up(heap: List[HeapEntry], index: int) -> None:
    """When inserting a new element at the end, ensure heap property by likes"""
    while index > 0:
        p = parent(index)
        if heap[index].likes > heap[p].likes:
            swap(heap, index, p)
            index = p
        else:
            break

def heap_down(heap: List[HeapEntry], index: int, heap_size: int) -> None:
    """When deleting the root, re-heapify by likes"""
    largest = index
    left = left_child(index)
    right = right_child(index)
    
    # Compare with left child
    if left < heap_size and heap[left].likes > heap[largest].likes:
        largest = left
    
    # Compare with right child
    if right < heap_size and heap[right].likes > heap[largest].likes:
        largest = right
    
    # If largest is not the current index, swap and continue
    if largest != index:
        swap(heap, index, largest)
        heap_down(heap, largest, heap_size)

def find_index(heap: List[HeapEntry], post_id: str) -> int:
    """Find the index of a post by its post_id"""
    for i in range(len(heap)):
        if heap[i].post_id == post_id:
            return i
    return -1

def initialize(heap: TrendingHeap) -> None:
    """Initialize an empty TrendingHeap"""
    heap.heap = []
    heap.size = 0

def push(heap: TrendingHeap, post_id: str, likes: int, timestamp: int) -> None:
    """Insert a new post into the heap"""
    new_entry = HeapEntry(likes, post_id, timestamp)
    heap.heap.append(new_entry)
    heap.size += 1
    heap_up(heap.heap, heap.size - 1)

def pop_max(heap: TrendingHeap) -> Optional[HeapEntry]:
    """Remove and return the post with maximum likes"""
    if heap.size == 0:
        return None
    
    max_entry = heap.heap[0]
    heap.heap[0] = heap.heap[heap.size - 1]
    heap.heap.pop()  # Remove last element
    heap.size -= 1
    
    if heap.size > 0:
        heap_down(heap.heap, 0, heap.size)
    
    return max_entry

def peek_max(heap: TrendingHeap) -> Optional[HeapEntry]:
    """Return the post with maximum likes without removing it"""
    if heap.size == 0:
        return None
    return heap.heap[0]

def get_top_k(heap: TrendingHeap, k: int) -> List[HeapEntry]:
    """Return the top k posts with maximum likes"""
    # Create a copy of the heap list
    temp_heap = heap.heap.copy()
    result = []
    effective_k = min(k, heap.size)
    
    for i in range(effective_k):
        if len(temp_heap) == 0:
            break
        
        max_entry = temp_heap[0]
        temp_heap[0] = temp_heap[-1]
        temp_heap.pop()
        
        if len(temp_heap) > 0:
            heap_down(temp_heap, 0, len(temp_heap))
        
        result.append(max_entry)
    
    return result

def update_likes(heap: TrendingHeap, post_id: str, new_likes: int, new_timestamp: int) -> None:
    """Update the likes of a specific post"""
    index = find_index(heap.heap, post_id)
    if index == -1:
        return
    
    old_likes = heap.heap[index].likes
    
    # Update the post
    heap.heap[index].likes = new_likes
    heap.heap[index].timestamp = new_timestamp
    
    # Re-heapify based on whether likes increased or decreased
    if new_likes > old_likes:
        heap_up(heap.heap, index)
    else:
        heap_down(heap.heap, index, heap.size)

def size(heap: TrendingHeap) -> int:
    return heap.size

def is_valid_heap(heap: TrendingHeap) -> bool:
    """Check if the heap satisfies the max-heap property"""
    n = heap.size
    for i in range(n // 2):
        left = left_child(i)
        right = right_child(i)
        
        if left < n and heap.heap[i].likes < heap.heap[left].likes:
            return False
        
        if right < n and heap.heap[i].likes < heap.heap[right].likes:
            return False
    
    return True

def get_height(heap: TrendingHeap) -> int:
    """Return the height of the heap tree"""
    if heap.size == 0:
        return 0
    return math.floor(math.log2(heap.size)) + 1

def get_level_order(heap: TrendingHeap) -> List[List[HeapEntry]]:
    """Return the heap elements in level order traversal"""
    result = []
    level = 0
    start = 0
    elements_per_level = 1
    
    while start < heap.size:
        end = min(start + elements_per_level, heap.size)
        level_elements = heap.heap[start:end]
        result.append(level_elements)
        start = end
        elements_per_level *= 2
        level += 1
    
    return result