import turtle
import random
import math

def reset(numC):
    while numC>255:
        numC = 255
    return numC

def grass(t,length,color):
    t.penup()
    while length>0:
        travel = 5*math.sin(random.random()*math.pi)
        length -= travel
        print(length)
        
        bladeLength = 20*math.sin(random.random()*math.pi)+5
        t.forward(travel)
        t.left(90)
        tree(bladeLength,t,color)
        t.right(90)

def cloud(t,length):
    baseColor = 200+50*math.sin(random.random()*2*math.pi)
    while length>0:
        travelH = 5*math.sin(random.random()*math.pi)
        travelV = 5*math.sin(random.random()*2*math.pi)
        radius = 20*math.sin(random.random()*math.pi)
        color = (baseColor+10*math.sin(random.random()*2*math.pi),baseColor+10*math.sin(random.random()*2*math.pi),baseColor+10*math.sin(random.random()*2*math.pi))
        
        length -= travelH
        
        t.color(color)
        t.forward(travelH)
        t.left(90)
        t.forward(travelV)
        t.fill(True)
        t.circle(radius,360)
        t.fill(False)
        t.right(90)
    
def tree(length,t,color):
    if length>=5:
        newColor = (reset(color[0]+20*math.sin(random.random()*math.pi)),reset(color[1]+20*math.sin(random.random()*math.pi)),reset(color[2]+20*math.sin(random.random()*math.pi)))
        
        print(newColor)
        t.color(newColor)
        
        #Generate 2 angles
        angle1 = 1+10*math.sin(random.random()*math.pi)
        angle2 = 1+10*math.sin(random.random()*math.pi)
        
        length += 5*math.sin(random.random()*2*math.pi)
        
        t.width((length+15)//15)
        t.pendown()
        
        t.forward(length)
        
        #Draw branch 1
        t.right(angle1)
        tree(length-(5+10*math.sin(random.random()*math.pi)),t,newColor)
        t.left(angle1+angle2)
        
        #Draw branch 2
        tree(length-(5+10*math.sin(random.random()*math.pi)),t,newColor)
        t.right(angle2)
        t.penup()
        
        t.backward(length)
t = turtle.Turtle()

t.speed(0)
t.penup()
t.shape("classic")

t.goto(-1000,-1000)
grass(t,2000,(0,140,0))
t.left(90)
t.goto(-300,-1000)
for x in range(random.randint(1,5)):
    t.right(90)
    t.forward(random.random()*200+20)
    t.left(90)
    tree(random.random()*100+50,t,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
t.goto(-1000,-200)
t.right(90)
for x in range(3,8):
    t.forward(random.random()*200+20)
    t.right(90)
    t.forward(50*math.sin(random.random()*2*math.pi))
    t.left(90)
    cloud(t,random.random()*200+150)