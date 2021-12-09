class Solution(object):
  def restoreString(self, s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    characters = list(s)

    shuffledCharacters = ['']*len(s)

    for idx, indice in enumerate(indices):
      shuffledCharacters[indice] = characters[idx]

    return ''.join(list(character for character in shuffledCharacters))