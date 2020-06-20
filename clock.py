print("Enter the time in 24 hour format\n")
hr = int(input("hour : "))
min = int(input("minute : "))
sec = int(input("second : "))
import turtle
#import time
wn = turtle.Screen()
wn.bgcolor("Black")
# turtle for rectangle
box = turtle.Turtle()
box.speed(0)
box.setpos(-170,-20)
box.begin_fill()
box.fillcolor("Cyan")
box.forward(400)
box.left(90)
box.forward(100)
box.left(90)
box.forward(400)
box.left(90)
box.forward(100)
box.end_fill()
box.up()
#turtle for display of time
_time = turtle.Turtle()
_time.up()
_time.setpos(-150,0)
_time.color("Black")
#turtle for Text
point = turtle.Turtle()
point.up()
point.setpos(-250,-200)
point.color("Cyan")
#this is not a real time clock but a kind of 
point.write("! REAL TIME CLOCK",font = ("Times New Roman",50,"normal")) 
while True:
	for h in range(hr,24):
		for m in range(min,60):
			for s in range(sec,60):
				_time.clear()
				if h<12:
					_time.write(("{}:{}:{} AM").format(h,m,s),font = ("Times New Roman",50,"normal"))
				elif h==12:
					_time.write(("{}:{}:{} PM").format(h,m,s),font = ("Times New Roman",50,"normal"))
				elif h>=13:
					_time.write(("{}:{}:{} PM").format(h-12,m,s),font = ("Times New Roman",50,"normal"))
	#			time.sleep(1)
				for wait in range(2300):
						_time.write("",font = ("Times New Roman",50,"normal"))
			sec = 0
		min = 0	
	hr = 0
