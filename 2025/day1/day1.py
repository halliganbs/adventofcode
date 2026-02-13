class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class CircularLinkedList:
    def __init__(self):   
        self.head = None
        self.target = None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.target = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            new_node.prev = current
            current.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
    
    def get_target(self):
        return self.target.data
    def right(self):
        self.target = self.target.next
    def left(self):
        self.target = self.target.prev

if __name__ == "__main__":
    dial = CircularLinkedList()
    for i in range(100):
        # print(i)
        dial.append(i)
    # print(dial.get_target())
    # for _ in range(5):
    #     dial.right()
    # print(dial.get_target())
    for _ in range(50):
        dial.left()
    print(dial.get_target())
    
    with open('input.txt') as f:
        the_numbers = [line.rstrip() for line in f]
    num_zeros = 0
    code = []
    for n in the_numbers:
        direction = n[0]
        amount = int(n[1:])
        # print(direction, amount)
        for j in range(amount):
            if direction == 'R':
                dial.right()
                value = dial.get_target()
                if value == 0:
                    num_zeros+=1
            elif direction == 'L':
                dial.left()
                value = dial.get_target()
                if value == 0:
                    num_zeros+=1

    print("Number of Zeros:", num_zeros)
    # print("Code:", code)