import datetime
import random
class CommentNone:

    def __init__(self, user_id, content, timestamp, likes):
        self.comment_id = random.randint(1, 1000)
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.replies = []

    def addReplies(self, comment):
        self.replies.append(comment)

    def getReplies(self):
        return self.replies

class thread:

    def __init__(self):
        self.comments = []

    def addComment(self, comment):
        self.comments.append(comment)


def getComments_rec(comment):
    comments = [comment.content]
    for replie in comment.getReplies():
        comments += getComments_rec(replie)
    return comments

def getComments_it(comment):
    comments = []
    stack = [comment]
    while stack != []:
        curr_comment = stack.pop()
        comments.append(curr_comment.content)
        for replie in curr_comment.getReplies():
            stack.append(replie)
    return comments

c1 = CommentNone(1, "c1", datetime.datetime.now(), 1)
c2 = CommentNone(2, "c2", datetime.datetime.now(), 2)
c3 = CommentNone(3, "c3", datetime.datetime.now(), 3)
c4 = CommentNone(4, "c4", datetime.datetime.now(), 4)
c5 = CommentNone(5, "c1_1", datetime.datetime.now(), 5)
c6 = CommentNone(6, "c2_1", datetime.datetime.now(), 6)
c7 = CommentNone(7, "c3_1", datetime.datetime.now(), 7)
c8 = CommentNone(8, "c1_1_1", datetime.datetime.now(), 8)
c9 = CommentNone(9, "c1_2", datetime.datetime.now(), 9)
c10 = CommentNone(10, "c1_2_1", datetime.datetime.now(), 10)
c11 = CommentNone(12, "c1_2_1_1", datetime.datetime.now(), 11)

c1.addReplies(c5)
c2.addReplies(c6)
c3.addReplies(c7)
c5.addReplies(c8)
c1.addReplies(c9)
c9.addReplies(c10)
c10.addReplies(c11)

print(getComments_rec(c1))
print(getComments_it(c1))