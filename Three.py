class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

root = Node("Akar")
root.left = Node("Anak Kiri")
root.right = Node("Anak Kanan")
def preorder(node):
  if node is None:
    return

  print(node.value)
  preorder(node.left)
  preorder(node.right)

preorder(root)

