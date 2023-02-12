def reverseWords(s: str) -> str:
  wordList = s.split(' ')

  for i in range(len(wordList)):
    wordList[i] = wordList[i][::-1]

  return ' '.join(wordList)

print(reverseWords(s = "Let's take LeetCode contest"))