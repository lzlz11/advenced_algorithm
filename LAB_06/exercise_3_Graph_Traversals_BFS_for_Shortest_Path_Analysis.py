from collections import deque

class SocialNetwork:
    def __init__(self):
        self.adjacency_list = {}

    def add_user(self,user):
        if user not in self.adjacency_list:
            self.adjacency_list[user] = []
    
    def add_friendship(self,user1,user2):
        if user1 in self.adjacency_list and user2 in self.adjacency_list:
            if user2 not in self.adjacency_list[user1]:
                self.adjacency_list[user1].append(user2)
            if user1 not in self.adjacency_list[user2]:
                self.adjacency_list[user2].append(user1)

    def bfs(self,start_user):
        order = []
        visited = set()
        queue = deque()

        visited.add(start_user)
        queue.append(start_user)

        while queue:
            user = queue.popleft()
            order.append(user)
            for neighbor in self.adjacency_list[user]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            
        return order
    

    def bfs_with_distances(self,start_user):
        queue = deque()
        distances = {start_user:0}
        queue.append(start_user)

        while queue:
            user = queue.popleft()

            for neighbor in self.adjacency_list[user]:
                if neighbor not in distances:
                    distances[neighbor] = distances + 1
                    queue.append(neighbor)
        
        return distances
    

    def shortest_path(self,start_user,target_user):
        if start_user == target_user:
            return [start_user]
        
        parent = {start_user:None}
        queue = [start_user]

        while queue:
            user = queue.pop(0)
            for neighbor in self.adjacency_list[user]:
                if neighbor not in parent:
                    parent[neighbor] = user

                    if neighbor == target_user:
                        path = []
                        curr = target_user
                        while curr is not None:
                            path.append(curr)
                            curr = parent[curr]
                        path.reverse()
                        return path
                    queue.append(neighbor)
            
        return None
    
    def degrees_of_separation(self, start_user, target_user):
        distances = self.bfs_with_distances(start_user)
        return distances.get(target_user, -1)
    

    def friends_within_k_hops(self, start_user, k):
        distances = self.bfs_with_distances(start_user)
        result = set()
    
        for user, distance in distances.items():
            if 1 <= distance <= k:
                result.add(user)
        
        return result
    


    def compute_average_degrees_of_separation(self):
        total_distance = 0
        count = 0
        users = list(self.adjacency_list.keys())
        n = len(users)

        for i in range(n):
            user = users[i]
            distances = self.bfs_with_distances(user)

            for j in range(i+1,n):
                target = users[j]
                dist = distances.get(target,None)
                if dist is not None:
                    total_distance = total_distance + dist
                    count = count + 1
        if count == 0:
            return 0
        
        return total_distance / count
    

    
    def get_distance_distribution(self, start_user):
        distances = self.bfs_with_distances(start_user)
        distribution = {}
    
        for user, dist in distances.items():
            if user != start_user:
                distribution[dist] = distribution.get(dist, 0) + 1
    
        return distribution


    def recommend_friends(self, start_user, max_recommendations=5):
        distances = self.bfs_with_distances(start_user)
        current_friends = set(self.adjacency_list[start_user])
        candidates = {}
    
        for user, dist in distances.items():
            if dist == 2 and user not in current_friends and user != start_user:
                user_friends = set(self.adjacency_list[user])
                common_friends = user_friends.intersection(current_friends)
                count = len(common_friends)
                candidates[user] = count
    
        sorted_candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
    
        result = [user for user, count in sorted_candidates[:max_recommendations]]
    
        return result