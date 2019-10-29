#!/usr/bin/env python

import time,click
from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

f1South =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

# Write the code below of a function verticalSegmentS() that creats a vertical line of height h at given x,y coordinate
# going toward the bottom of the screen (South)
# If not specified in the argument list, use the default values x=0 y=0 and h=5
# Your line should not go past y = 63
# Write the function using a for loop
####################### Add your code below #########################

def verticalSegmentS(x=0,y=0,h=5):
    i=0
    for i in range (0,h):
        lcd.set_pixel(x,y,1)
        i=i+1
        y=y+1
        if y > 63:
            break
    lcd.show()


# Write the code below of a function horizontalSegmentE() that creates an horizontal line of width w at given x,y coordinate
# going to the right of the screen (East)
# If not specified in the argument list, use the default values x=0 y=0 and w=5
# Your line should not go past x=127
# Write the function using a while loop
####################### Add your code below #########################

def horizontalSegmentE(x=0,y=0,w=5):
    i=0
    while i < w:
        lcd.set_pixel(x,y,1)
        i=i+1
        x=x+1
        if x > 127:
            break
    lcd.show()


# Create the code below of a function drawSquare() that draws a square of side s starting at x,y
# If not specified in the argument list, use the default values x=0 y=0 and s=5
# The code must call the functions created above. Do not do any edg detection in the function, let the called functions do it
####################### Add your code below #########################

def drawSquare(x=0,y=0,s=5):
    startX=x
    startY=y
    verticalSegmentS(x,y,s)
    horizontalSegmentE(x,y,s)
    y=startY + s - 1
    horizontalSegmentE(x,y,s)
    y= startY
    x=startX + s - 1
    verticalSegmentS(x,y,s)


# Write the code below on a function drawRectangle() that draws a rectangle of width w and height h starting a x,y
# If not specified in the argument list, use the default values x=0 y=0 w=5 and h=5
# The code must call the functions created above. Do not do any edg detection in the function, let the called functions do it
####################### Add your code below #########################

def drawRectangle(x=0,y=0,w=5,h=5):
    startX=x
    startY=y
    verticalSegmentS(x,y,h)
    horizontalSegmentE(x,y,w)
    y=startY + h - 1
    horizontalSegmentE(x,y,w)
    y= startY
    x=startX + w - 1
    verticalSegmentS(x,y,h)


# Write the code below of a function diagonalSegmentNE() that creates a diagonal line of length l given at x,y coordinate
# The line goes from x y towards the right of the screen going north of the screen
# If not specified in the argument list, use the default values x=0 y=63 and l=5
# Your line should not go past x=127 and below y=0
####################### Add your code below #########################

def diagonalSegmentNE(x=0,y=63,l=5):
    for i in range (0,l):
        lcd.set_pixel(x,y,1)
        x=x+1
        y=y-1
        i=i+1
        if x > 127 or y < 0:
            break
    lcd.show()


def rotateObject(obj):
    rotated_image = [[] for x in range(len(obj))]
    for i in range(len(obj)):
        for j in range(len(obj[i])):
          rotated_image[len(obj) - j - 1].append(obj[i][j])
    return rotated_image

def displayObject(obj,x,y):
    i=0
    for line in obj:
        j=0
        for pixel in line:
            lcd.set_pixel(x+j,y+i,pixel)
            j=j+1
        i=i+1
    lcd.show()

def moveObject(obj,x,y,vx,vy):
    x=x+vx
    y=y+vy
    return(x,y)

def eraseObject(obj,x,y):
    i=0
    for line in obj:
        j=0
        for pixel in line:
            lcd.set_pixel(x+j,y+i,0)
            j=j+1
        i=i+1
    lcd.show()

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 38)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

def eraseText(text,lcd,x,y):
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 38)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            lcd.set_pixel(x1, y1, 0)
    lcd.show()

clearScreen(lcd)
backlight.set_all(0,255,0)
backlight.show()
displayText("Spaceship",lcd,25,1)
time.sleep(2)
eraseText("Spaceship",lcd,25,1)

f1East=rotateObject(f1South)
f1North=rotateObject(f1East)
f1West=rotateObject(f1North)

x=y=0
w=h=8
vx=vy=3
f1=f1South
displayObject(f1,x,y)

# Write the code to initialize a string variable studNumb to your personal student number

# Write the code below to
# 1. Convert the variable studNumb to a list
# 2. Loop through the list to calculate the sum o every digit of your student number and print it
# As and example 040 111 222 will print 13 (0+4+0+1+1+1+2+2+2)

studNumb = "040900506"
print("My personal student number is", studNumb)
studNumb = list(studNumb)
sum=0
i=0
for i in range (0,9):
    sum = sum + int(studNumb[i])
    i=i+1
print("The sum of all the digits is", sum)


# Write the code to draw a vertial segment going south starting at x=20 y=20 and a height of 16

verticalSegmentS(20,20,16)


# Write the code to draw a horizontal segment going east starting at x=20 y=20 and a width of 16

horizontalSegmentE(20,20,16)


# Write the code to draw a horizontal diagonal segment going north east starting at x=20 y=20 and a length of 16

diagonalSegmentNE(20,20,16)


# Write the code to draw a square at x=34 y=5 of side 12

drawSquare(34,5,12)


# Write the code to draw a rectangle at x=0 y=0 w=5 and h=7

drawRectangle(0,0,5,7)


quit=False
while not quit:
    c = click.getchar()

    #Erase Everything
    eraseObject(f1,x,y)

    #Move everything
    if c == 'q':
        quit=True

    elif c == '\x1b[A': #up
        f1=f1North
        y=y-vy

    elif c == '\x1b[B': #down
        f1=f1South
        y=y+vy

    elif c == '\x1b[C': #right
        f1=f1East
        x=x+vx

    elif c == '\x1b[D': #left
        f1=f1West
        x=x-vx

    #Collision Detection
    if y < 0 or y+h>63 or x + w>127 or x < 0:
        displayText("Ouch Boom",lcd,5,1)
        time.sleep(0.4)
        eraseText("Ouch Boom",lcd,5,1)
        if y<0:y=0
        if y+h>63:y=63-h
        if x<0:x=0
        if x+w>127:x=127-w

    #Display Everything
    displayObject(f1,x,y)

backlight.set_all(0,0, 0)
backlight.show()
lcd.clear()
lcd.show()
