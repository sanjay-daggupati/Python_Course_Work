user={"hi":["hello","world"],
      "hello":["hi","world"]}
words=0
for v in user.values():
    for i in v:
        words+=len(i.split())
print(words)
print(user.items())