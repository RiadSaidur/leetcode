def findOwner(name: str):
  if len(set(name)) == 1 and '.' in set(name) and len(name) != 3:
    print("CAN'T TELL")
    return

  owners = ['Alice', 'Cindy', 'Bob']

  for owner in owners:
    belongsTo = owner

    for i in range(len(name)):
      if len(owner) <= i:
        break
      
      if name[i] != '.' and name[i] != owner[i]:
        belongsTo = ''

    if len(belongsTo) == len(name):
      print(belongsTo)
      return
  
  print("SOMETHING'S WRONG")

findOwner(str(input()))