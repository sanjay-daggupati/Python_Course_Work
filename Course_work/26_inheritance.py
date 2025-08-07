## Single Inheritanece
"""
class Status:
    def uploadImage(self,image_url):
        self.image=image_url
        print(f"'{self.image}' is uploaded to your status")

class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')

Sanjay=Status()
Sanjay.uploadImage('selfie.png')
Raghava=StatusV1()
Raghava.uploadImage("Good Morning.png")
Raghava.addCaption("Morning Friends!!!")

class StatusV2(Status):
    def like(self):
        print("You can Like status")
    """
### One-to-many->Inheritance
"""
class Status:
    def uploadImage(self,image_url):
        self.image=image_url
        print(f"'{self.image}' is uploaded to your status")

class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')

class StatusV2(Status):
    def like(self):
        print("You can Like status")

Sanjay=Status()
Sanjay.uploadImage('selfie.png')

Raghava=StatusV1()
Raghava.uploadImage("Good Morning.png")
Raghava.addCaption("Morning Friends!!!")

Venkat=StatusV2()
Venkat.uploadImage("Coffee.png")
Venkat.like()
"""
## Multiple Inheritance
"""
class Status:
    def uploadImage(self,image_url):
        self.image=image_url
        print(f"'{self.image}' is uploaded to your status")

class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')

class StatusV2(Status):
    def like(self):
        print("You can Like status")

class StatusV3(StatusV1,StatusV2):
    def addMusic(self,music):
        self.music=music
        print(f"{self.music}... is added to your status")

Sanjay=Status()
Sanjay.uploadImage('selfie.png')
print()
Raghava=StatusV1()
Raghava.uploadImage("Good Morning.png")
Raghava.addCaption("Morning Friends!!!")
print()
Venkat=StatusV2()
Venkat.uploadImage("Coffee.png")
Venkat.like() 
print()
Mohit=StatusV3()
Mohit.uploadImage("Mountain and Trees.png")
Mohit.addCaption("Nature Lover")
Mohit.like()
Mohit.addMusic("Pranamam.mp3")"""
""""
#Multilevel Inheritance

class Status:
    def uploadImage(self,image_url):
        self.image=image_url
        print(f"'{self.image}' is uploaded to your status")

class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')

class StatusV2(Status):
    def like(self):
        print("You can Like status")

class StatusV3(StatusV1,StatusV2):
    def addMusic(self,music):
        self.music=music
        print(f"{self.music}... is added to your status")

class StatusV4(StatusV3):
    def videolength(self,video):
        self.video=video
        print(f"{self.video} is uploaded to your status")

Sanjay=Status()
Sanjay.uploadImage('selfie.png')
print()
Raghava=StatusV1()
Raghava.uploadImage("Good Morning.png")
Raghava.addCaption("Morning Friends!!!")
print()
Venkat=StatusV2()
Venkat.uploadImage("Coffee.png")
Venkat.like() 
print()
Mohit=StatusV3()
Mohit.uploadImage("Mountain and Trees.png")
Mohit.addCaption("Nature Lover")
Mohit.like()
Mohit.addMusic("Pranamam.mp3")
print()
Ananda=StatusV4()
Ananda.uploadImage("Sunrise.png")
Ananda.addCaption("Morning_person")
Ananda.like()
Ananda.addMusic("Suryudeee godugu patti.mp3")
Ananda.videolength("Sunrising_video.mp4")
"""

class Instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,"-")}")
    
    def uploadPost(self,image):
        self.post.append(image)
        print(f"{image} is posted")

class InstagramVI(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print("bio uploaded")

    def uploadPost(self, image,music):
        super().uploadPost(image)
        self.music=music
        print(f"{self.music} is added to the post ")

Dinesh=Instagram("Dinesh123")
Dinesh.uploadPost("GoodMorning.png")
Sanjay=InstagramVI("orrey_sanjuu","Live everyday of your life as a new chapter")
Sanjay.uploadPost("GoodEvening.png","Melody")
