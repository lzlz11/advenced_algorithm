from datetime import datetime
from typing import List
import math

class Post:
    def __init__(self, post_id: str, user_id: str, content_preview: str, 
                 timestamp: datetime, likes: int, comments: int, shares: int):
        self.post_id = post_id
        self.user_id = user_id
        self.content_preview = content_preview
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares
    
    def engagement_score(self) -> int:
        return (self.likes * 1) + (self.comments * 2) + (self.shares * 3)


# Part A: Maximum Engagement
def max_engagement(posts: List[Post], left: int, right: int) -> int:
    """
    Recursively find post with highest engagement score
    Returns the maximum engagement score
    """
    if left == right:
        return posts[left].engagement_score()
    
    mid = (left + right) // 2
    
    max_left = max_engagement(posts, left, mid)
    max_right = max_engagement(posts, mid + 1, right)
    
    # Return the larger engagement score
    if max_left > max_right:
        return max_left
    else:
        return max_right


# Part B: Total and Average
def sum_engagement(posts: List[Post], left: int, right: int) -> int:

    if left == right:
        return posts[left].engagement_score()
    
    mid = (left + right) // 2
    
    sum_left = sum_engagement(posts, left, mid)
    sum_right = sum_engagement(posts, mid + 1, right)
    
    return sum_left + sum_right


def average_engagement(posts: List[Post], left: int, right: int) -> float:
    """
    Compute average engagement score using sum_engagement
    """
    total = sum_engagement(posts, left, right)
    count = right - left + 1
    average_engagement = total / count
    return average_engagement


# Part C: Count by Threshold
def count_above_threshold(posts: List[Post], left: int, right: int, threshold: int) -> int:

    if left == right:
        if posts[left].engagement_score() > threshold:
            return 1
        else:
            return 0
    
    mid = (left + right) // 2
    
    count_left = count_above_threshold(posts, left, mid, threshold)
    count_right = count_above_threshold(posts, mid + 1, right, threshold)
    
    return count_left + count_right


# Part D: Merge Sort by Engagement
def merge_sort_by_engagement(posts: List[Post], left: int, right: int) -> None:

    if left >= right:
        return
    
    mid = (left + right) // 2
    
    merge_sort_by_engagement(posts, left, mid)
    merge_sort_by_engagement(posts, mid + 1, right)
    
    merge(posts, left, mid, right)


def merge(posts: List[Post], left: int, mid: int, right: int) -> None:
    """
    Merge two sorted halves of the posts array
    """
    # Calculate sizes of two subarrays
    n1 = mid - left + 1
    n2 = right - mid
    
    left_array = [None] * n1
    right_array = [None] * n2
    
    # Copy data to temporary arrays
    for i in range(n1):
        left_array[i] = posts[left + i]
    
    for j in range(n2):
        right_array[j] = posts[mid + 1 + j]
    
    # Initial indices
    i = 0 
    j = 0  
    k = left  
    
    # Merge the two arrays based on engagement score
    while i < n1 and j < n2:
        if left_array[i].engagement_score() <= right_array[j].engagement_score():
            posts[k] = left_array[i]
            i += 1
        else:
            posts[k] = right_array[j]
            j += 1
        k += 1
    
    # Copy remaining elements 
    while i < n1:
        posts[k] = left_array[i]
        i += 1
        k += 1
    
    while j < n2:
        posts[k] = right_array[j]
        j += 1
        k += 1


def find_peak_hour(likes: List[int], left: int, right: int) -> int:
    """
    Recursively find the peak hour (maximum likes) in a unimodal array
    Returns the index of the peak element
    """
    if right == left:
        return left
    
    mid = (left + right) // 2
    
    # If mid < mid+1, peak is to the right
    if likes[mid] < likes[mid + 1]:
        return find_peak_hour(likes, mid + 1, right)
    # Otherwise, peak is to the left
    else:
        return find_peak_hour(likes, left, mid)
    


