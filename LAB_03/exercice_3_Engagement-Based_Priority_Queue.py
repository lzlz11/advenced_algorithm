from datetime import datetime,timedelta
import math

class Post:
    def __init__(self,post_id:str,user_id:str,content:str,timestamp:datetime,likes:int=0,
                 comments:int = 0,shares:int = 0):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares

    def engagement_score(self) ->int:
        return (self.likes * 1) + (self.comments * 2) + (self.shares * 3)

#2 Define nodes
class QueueNode:
    def __init__(self,data:Post):
        self.val = data
        self.link = None

#3. Class PriorityQueue and operations
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.rear = None
        self.count = 0
    def is_empty(self) -> bool:
        return self.head is None
    def size(self) -> int:
        return self.count
    def peek_max(self) -> Post | None:
        if self.head is not None:
            return self.head.val
        else:
            return None

    def enqueue(self, post: Post):
        new_node = QueueNode(post)
        if self.head is None:
            self.head = new_node
            self.rear = new_node
        elif new_node.val.engagement_score() > self.head.val.engagement_score():
            new_node.link = self.head
            self.head = new_node
        else:
            current = self.head
            while current.link is not None and current.link.val.engagement_score() >= new_node.val.engagement_score():
                current = current.link
            new_node.link = current.link
            current.link = new_node
            if new_node.link is None:
                self.rear = new_node
        
        self.count += 1

    def dequeue_max(self) -> Post | None:
        if self.is_empty():
            print("error. Queue is empty")
            return None
        
        to_delete = self.head
        max_post = to_delete.val  
        
        if self.head.link is None:
            self.head = None
            self.rear = None
        else:
            self.head = self.head.link
        
        del to_delete
        self.count -= 1
        return max_post


# 4. Priority updates: 
    def update_score(self, post_id: str, new_likes: int, new_comments: int, new_shares: int):
        prev = None
        current = self.head
        target_node = None

        while current is not None:
            if current.val.post_id == post_id:
                target_node = current
                if prev is None:
                    self.head = current.link
                else:  
                    prev.link = current.link
                if current == self.rear:
                    self.rear = prev
                self.count -= 1
                break  
            prev = current
            current = current.link
        if target_node is not None:
            target_node.val.likes = new_likes
            target_node.val.comments = new_comments
            target_node.val.shares = new_shares
            self.enqueue(target_node.val)


    def refresh_all(self):
        temp_list = []
        current = self.head
        while current is not None:
            temp_list.append(current.val)
            current = current.link
        self.head = None
        self.rear = None
        self.count = 0
        for post in temp_list:
            self.enqueue(post)

#5.Trending window: 
    def get_top_k(self, k: int) -> list[Post]:
        result = []
        current = self.head
        count = 0
        while current is not None and count < k:
            result.append(current.val)
            current = current.link
            count += 1
        return result

    def decay_older_than(self, cutoff_time: datetime, decay_rate: float = 0.2):
        temp_list = []
        current = self.head
        while current is not None:
            post = current.val
            if post.timestamp < cutoff_time:
                original_score = post.engagement_score()
                decayed_score = math.floor(original_score * (1 - decay_rate))
                scale = decayed_score / original_score if original_score != 0 else 1.0
                post.likes = math.floor(post.likes * scale)
                post.comments = math.floor(post.comments * scale)
                post.shares = math.floor(post.shares * scale)
            temp_list.append(post)
            current = current.link
        self.head = None
        self.rear = None
        self.count = 0
        for post in temp_list:
            self.enqueue(post)




