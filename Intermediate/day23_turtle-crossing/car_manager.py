from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            car.goto(x=350, y=new_y)
            self.all_cars.append(car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT













