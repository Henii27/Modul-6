class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def print_list(self):
    temp = self.head
    while temp:
      print(temp.data, end=" ")
      temp = temp.next

if __name__ == "__main__":
  llist = LinkedList()
  llist.insert_at_beginning(10)
  llist.insert_at_beginning(20)
  llist.insert_at_beginning(30)
  llist.print_list()
  
