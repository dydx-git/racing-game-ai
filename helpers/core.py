
import sys
import os
import constants.constants as vals

class Car:
    # Car class is representing common values of all cars in the game
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # width is originating from car image width
        self.width = vals.CAR_WIDTH
        # height is originating from car image width
        self.height = vals.CAR_HEIGHT


class My_car(Car):
    # My_car class specifies distinct features of player's car
    def __init__(self, x, y):
        super().__init__(x, y)
        self.distanceBack = 0.7
        self.distanceFront = 0.7

    def move(self, direction):
        # move method allows to move the car to the left or right
        # 40 is the distance form the left wall to the center of the 1st road line
        print(direction)
        if direction == "left":
            # 80 is the distance between the road lines
            # self.x = self.x - vals.CAR_HEIGHT MYCODE
            self.y = self.y - vals.CAR_HEIGHT/8/self.distanceFront
            self.distanceFront /= 1.1
        if direction == "right":
            self.y = self.y - vals.CAR_HEIGHT/8/self.distanceBack
            self.distanceBack *= 1.1
            pass

        if direction == "stay":
            self.y = self.y - 0.6*vals.CAR_HEIGHT/8


class Enemy_car(Car):
    # Enemy_car class specifies distinct features of all enemy cars
    def __init__(self, x, y):
        super().__init__(x, y)
        # active bool will help to remove the car from the state
        self.active = True

    def move(self):
        # move method descends a car by its height ( 80px )
        # self.y = self.y + self.height MYCODE
        self.y = self.y - 0.6*self.height/8

    def deactivate(self):
        # deactivate method changes car's state to be removed later
        self.active = False
