#Exercise 3
import math

def compute_similarity(userA, userB):
    dot_product=0
    nomA=0
    nomB = 0

    for i in range(len(userA)-1):
        dot_product+= userA[i]*userB[i]
        nomA += userA[i] * userA[i]
        nomB += userB[i] * userB[i]

    if nomA == 0 or nomB == 0:
        return 0

    return dot_product/ (math.sqrt(nomA) * math.sqrt(nomB))

    def find_topK(target_user, k):
        similarity_list=[]

    for i in range(len(target_user)):
        if i != target_user:
            similarity=compute_similarity(userA[target_user], userB[i])
            similarity_list.append((i, similarity))

    similarity_list.sort(key=lambda x: x[1], reverse=True)

    return similarity_list
