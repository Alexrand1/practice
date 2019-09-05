from collections import deque
from collections import Counter
import heapq

class Node(object):
    def __init__(self, value):
        self.value = value
        self.adjacentNodes = []
    def exists(self):
        if type(self) == Node:
            return True
        else:
            False


def breadthFirst(statringNode, soughtValue):
    visitedNodes = set()
    queue = deque([statringNode])
    count = -1
    while len(queue) > 0:
        node = queue.pop()
        if node in visitedNodes:
            continue
        visitedNodes.add(node)
        if node.value == soughtValue:
            return True, count
        for n in node.adjacentNodes:
            if n not in visitedNodes:
                queue.appendleft(n)
        count += 1
    return False


def build_tree(snode, wordList, endWord):
    for word in wordList:
        count = 0
        for c in word:
            if c in snode.value:
                count += 1
            if count == len(word) - 1:
                new_node = Node(word)
                snode.adjacentNodes.append(new_node)
                wordList.pop(wordList.index(word))
                break
    if not wordList:
        return snode.value
    elif new_node.value == 0:
        wordList.pop(wordList.index(word))
    elif new_node.value == endWord:
        return snode.value
    else:
        build_tree(new_node, wordList, endWord)
    for n in snode.adjacentNodes:
        print(n.value)



snode = Node('hot')
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]

temp = snode.value
ls = []
def sort_ls(lis, startword, ls):
    for word in lis:
        count = 0
        for c in word:
            if c in startword:
                count += 1
                if count == len(startword):
                    ls.append(lis.pop(lis.index(word)))
                    break
                elif count == len(startword)-1:
                    ls.append(lis.pop(lis.index(word)))
                    break
    if ls:
        temp = ls[len(ls)-1]
    elif not ls:
        temp = startword
    return sort_ls(lis, temp, ls)
    return ls
print(sort_ls(wordList, snode.value, ls))





snode.adjacentNodes = [Node(x) for x in sorted(wordList)]
print(breadthFirst(snode, 'dog'))
