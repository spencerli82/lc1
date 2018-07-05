class Node(object):

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoubleList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    if current_node.next is not None:
                        current_node.next.prev = current_node.prev
                    else:
                        self.tail = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    #current_node.next.prev = None
                    self.head.prev = None

            current_node = current_node.next

    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            print current_node.next.data if hasattr(current_node.next, "data") else None

            current_node = current_node.next

class Solution(object):
    def isIsomorphic(self, s, t):
        sourceMap, targetMap = {}, {}
        for x in range(len(s)):
            source, target = sourceMap.get(t[x]), targetMap.get(s[x])
            # print source, target, s, t, sourceMap, targetMap
            if source is None and target is None:
                sourceMap[t[x]], targetMap[s[x]] = s[x], t[x]
            elif target != t[x] or source != s[x]:
                return False
        return True

    def isIsomorphic2(self, s, t):
        a = map(s.find, s)
        b = map(t.find, t)
        return map(s.find, s) == map(t.find, t)

d = Solution()
d.isIsomorphic2('egg', 'add')

d = DoubleList()

d.append(5)
d.append(6)
d.append(50)
d.append(30)

d.show()

d.remove(30)
d.remove(5)

d.show()
