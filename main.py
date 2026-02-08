import turtle
import time
import random 
WIDTH = 500
HEIGHT = 500
COLORS = ["red", "green", "blue", "orange", "yellow", "gray", "black", "purple", "brown", "pink"] 

def get_number_of_racers():
    while True:
        racers = input("Введите количество черепах для гонки от 2 до 10: ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Вы ввели не число, попробуйте ещё раз")
            continue

        if racers <= 1 and racers >= 11:
            print("Число черепах должно быть больше 1 и меньше 11.")

        elif 2 <= racers <= 10:
            print("Количество черепах достаточное")
            return racers
        

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')
    time.sleep(10)

    
def create_turtles(colors):
    ready_tutles = []
    spacing = WIDTH // (len(colors)+1)
    for index, color in enumerate(colors):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.left(90)
        t.penup()
        t.setpos(-WIDTH//2+(index+1) * spacing, -HEIGHT//2 +20)
        t.pendown()
        ready_tutles.append(t)
    return ready_tutles

def race(colors):
    turtles = create_turtles(colors)   
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x,y = racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)]

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"Победила черепаха {winner}")