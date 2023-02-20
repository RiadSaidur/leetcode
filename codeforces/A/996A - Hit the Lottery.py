withdraw = int(input())

notes = [100, 20, 10, 5, 1]

noteCount = 0

for note in notes:
  noteCount += withdraw//note
  withdraw -= withdraw//note * note

print(noteCount)