user={"hi":["hello Sanjay","world"],
      "hello":["hi","world"]}
words=0
print(user.values())
for v in user.values():
    for i in v:
        words+=len(i.split())
print(words)
print(user.items())

scores = {'Alice': 90, 'Bob': 85, 'Charlie': 95}
winner = max(key=scores.get)
print(winner)  
key=scores.get
print(key)
