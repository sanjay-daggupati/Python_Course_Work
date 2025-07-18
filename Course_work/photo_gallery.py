Photo_Gallery=["Beach.png","mountain.png","party1.png","selfie.png","birthday.png","concert.png","sunset.png","trip1.png"]
for i in range(0,len(Photo_Gallery)):
    print(f"{i+1}. {Photo_Gallery[i]}")
selection_photos=set((map(int,input().split(","))))
print(selection_photos)
print("Sharing the following photos")
for i in selection_photos:
    print(f"{Photo_Gallery[i-1]}")
    