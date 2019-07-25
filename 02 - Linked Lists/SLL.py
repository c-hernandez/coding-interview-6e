class SLL(object):

  class _Node(object):
    def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

  def __init__(self, head=None):
    self.head = self._Node(head)

  def __str__(self):
      pass

  def __eq__(self, other):
      pass

  def insert(self, data):
      pass
  
  def delete(self, data):
      pass