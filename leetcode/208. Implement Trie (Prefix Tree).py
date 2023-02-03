class TrieNode:
  def __init__(self):
    self.childrens = {}
    self.endOfWord = False

class Trie:

  def __init__(self):
    self.node = TrieNode()

  def insert(self, word: str) -> None:
    cur = self.node
    for char in word:
      if char not in cur.childrens:
        cur.childrens[char] = TrieNode()
      cur = cur.childrens[char]
    cur.endOfWord = True


  def search(self, word: str) -> bool:
    cur = self.node
    for char in word:
      if char not in cur.childrens:
        return False
      cur = cur.childrens[char]
    return cur.endOfWord
    

  def startsWith(self, prefix: str) -> bool:
    cur = self.node
    for char in prefix:
      if char not in cur.childrens:
        return False
      cur = cur.childrens[char]
    return True