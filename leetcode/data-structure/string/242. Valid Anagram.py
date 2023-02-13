import collections


def isAnagram(s: str, t: str) -> bool:
  return collections.Counter(s) == collections.Counter(t)