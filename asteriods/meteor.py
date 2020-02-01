from arcade import Sprite, load_texture
from random import choice, randint
class Meteor(Sprite):
    def __init__(self, x, y,colour=None, size=4):
        super().__init__("asteriods\spaceshooter\PNG\Meteors\meteorBrown_big1.png",center_x=x,center_y=y)      
        if colour:
            self.colour= colour
        else:
            self.colour = choice(["g","b"])
        self.size = size
        self.angle = randint(0,360)
        self.velocity_x = randint(-4,4)
        self.velocity_y = randint(-4,4)
        if self.colour == "g":
            if self.size == 4:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_big1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_big2.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_big3.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_big4.png"
                ]
                self.texture = load_texture(choice(images))                                             
            elif self.size == 3:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_med1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_med2.png"
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 2:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_small1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_small2.png"
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 1:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_tiny1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorGrey_tiny2.png",
                ]
                self.texture = load_texture(choice(images))
        else:
            if self.size == 4:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_big1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_big2.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_big3.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_big4.png"
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 3:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_med1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_med2.png"
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 2:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_small1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_small2.png"
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 1:
                images=[
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_tiny1.png",
                    "asteriods\spaceshooter\PNG\Meteors\meteorBrown_tiny2.png",
                ]
                self.texture = load_texture(choice(images))
    def break_apart(self):
        self.kill()
        meteor_1 = None
        meteor_2 = None
        if self.size > 1:
            meteor_1 = Meteor(self.center_x,self.center_y,colour=self.colour,size=self.size -1)
            if choice([0,1,2,3])!=0:
                meteor_2 = Meteor(self.center_x,self.center_y,colour=self.colour,size=self.size -1)
            else:
                meteor_2 = None
        return meteor_1,meteor_2
    def update(self,width, height):
        if self.left > width:
            self.right=0
        elif self.right < 0:
            self.left=width 
        if self.bottom > height:
            self.top=0 
        elif self.top < 0:
            self.bottom=height
        self.center_x = self.center_x + self.velocity_x
        self.center_y = self.center_y + self.velocity_y