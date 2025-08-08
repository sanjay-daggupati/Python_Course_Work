class normaluser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with : \n1.Normal Qulaity \n2.Ads run \n3.No Background play \n4.Limited videos download \n5.Music with adds " )
    def comments(self):
        pass
    def share(self):
        pass
    def title(self):
        pass 
    def description(self):
        pass
    def subscribe(self):
        pass


class PremiumUser(normaluser):
    def playvideo(self,name):
        print(f"\n{name} is playing video with : \n1.High Quality \n2.Ads Free\n3.Background play\n4.Download anything \n5.Muisc without adds")

def play_video(name,username):
    name.playvideo(username)
    
dinesh=normaluser()
sanjay=PremiumUser()
play_video(sanjay,"Sanjay")
play_video(dinesh,"dinesh")