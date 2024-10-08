'''
백준 5397번. 키로커

< : 화살표 왼쪽 키
> : 화살표 오른쪽 키
- : Backspace
'''
class Node(object):
    def __init__(self,value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Kiroker(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.cursor = self.tail

    def insert_bk(self, value):
        new_node = Node(value)
        cur_prev = self.cursor.prev
        
        new_node.next = self.cursor
        new_node.prev = cur_prev
        cur_prev.next = new_node
        self.cursor.prev = new_node

    def remove(self):
        if self.cursor.prev == self.head:
            return  # 더미 헤드 바로 뒤에 삭제할 노드가 없으면 그냥 리턴
        
        cur_prev = self.cursor.prev
        self.cursor.prev = cur_prev.prev
        cur_prev.prev.next = self.cursor
    
    def printResults(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.value,end="")
            else:
                print(p.value)
            p = p.next

n = int(input())
for _ in range(n):
    kiro = Kiroker()  
    k = list(input())
    for i in k:
        if i == '<': 
            if kiro.cursor.prev is not kiro.head:
                kiro.cursor = kiro.cursor.prev
            else:
                pass
        elif i == '>':
            if kiro.cursor.next is not None:
                kiro.cursor = kiro.cursor.next
            else:
                pass
        elif i == '-':
            kiro.remove()
        else:
            kiro.insert_bk(i)
    kiro.printResults()
            

        
