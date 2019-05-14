import random
import queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        friendships = []
        # create all possible friend combinations
        for f1 in range(1, self.lastID + 1):
            for f2 in range(f1 + 1, self.lastID + 1):
                friendships.append((f1, f2))
        # randomize
        random.shuffle(friendships)
        # create friendships corresponding to:
        # avgFriendships * numUsers = numFriendships
        numFriendships = avgFriendships * self.lastID // 2
        for friendship in range(numFriendships):
            f = friendships[friendship]
            self.addFriendship(f[0], f[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # initialize visited with userID and path to self
        visited[userID] = [userID]
        # bfs to get shortest path from userID to userID's extended network
        q = queue.Queue()
        q.put(userID)
        while not q.empty():
            usr = q.get()
            for friend in self.friendships[usr]:
                # if friend has not been visited...
                if not friend in visited:
                    # add friends to queue
                    q.put(friend)
                    # update visited with path to each friend
                    tmp = visited[usr].copy()
                    tmp.append(friend)
                    visited[friend] = tmp

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(f"users: {sg.users}")
    print(f"friendships: {sg.friendships}")
    connections = sg.getAllSocialPaths(1)
    print(f"connections: {connections}")
