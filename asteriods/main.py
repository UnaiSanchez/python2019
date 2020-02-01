from arcade import *
from random import choice, randint
from meteor import Meteor
from player import Player
class Window(Window):
    def __init__(self):
        super().__init__(800,600,"Window arcade")
        self.meteor = Meteor(100,100)
        self.meteors=SpriteList()
        for i in range(15):
            new_meteor = Meteor(randint(0,self.width),randint(0,self.height))
            self.meteors.append(new_meteor)

        self.player = Player(self.width/2,self.height/2,"trdu","blue")
        self.a_pressed = False
        self.d_pressed = False
        self.w_pressed = False
        self.s_pressed = False
        
    def on_draw(self):
        start_render()
        self.meteor.draw()
        for i in range(len(self.meteors)):
            self.meteors[i].draw()
        self.player.draw()
    def on_mouse_motion(self, x, y, dx, dy):
        self.meteor.center_x=x
        self.meteor.center_y=y
    def on_key_press(self, symbol, modifiers):
        if symbol == key.A or symbol == key.LEFT:
            self.a_pressed = True
        elif symbol == key.D or symbol == key.RIGHT:
            self.d_pressed = True
        random_meteor= choice(self.meteors)
        new_meteor_1,new_meteor_2 = random_meteor.break_apart()
        if new_meteor_1:
            self.meteors.append(new_meteor_1)
        if new_meteor_2:
            self.meteors.append(new_meteor_2)
    def on_update(self,delta_time):
        for meteor in self.meteors:
            meteor.update(self.width, self.height)

        if self.a_pressed==True:
            self.player.turn_left()
        if self.d_pressed==True:
            self.player.turn_right()
    def on_key_release(self, symbol, modifiers):
        if symbol == key.A or symbol == key.LEFT:
            self.a_pressed = False
        elif symbol == key.D or symbol == key.RIGHT:
            self.d_pressed = False
Window()
run()