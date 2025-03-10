class DisjointSet:
    def init(self):
        self.parent = self
        self.size = 1

    def findParent(self):
        if self.parent == self:
            return self
        else:
            return DisjointSet.findParent(self.parent)

    def union(self, otherFriendNetwork):
        friend1 = DisjointSet.findParent(self)
        friend2 = DisjointSet.findParent(otherFriendNetwork)
        if friend1 == friend2:
            return friend1.size

        elif friend1.size > friend2.size:
            friend2.parent = friend1
            friend1.size += friend2.size
            return friend1.size
        else:
            friend1.parent = friend2
            friend2.size += friend1.size
            return friend2.size

def main():
    cases = int(input())
    network = {}

    for i in range(cases):
        lines = int(input())

        for i in range(lines):
            friend1, friend2 = input().split()
            if friend1 not in network:
                network[friend1] = DisjointSet()
            if friend2 not in network:
                network[friend2] = DisjointSet()

            mutuals = network[friend1].union(network[friend2])
            print(mutuals)

        network = {}
main()