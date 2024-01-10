import sys
import stdio
import math
import random



		
	
#moving to first room
def livingroom():
	print("Your first room you enter is the living room")
	
	userInput = ""
	userInput = input()
	

	if userInput == "help":
		livinghelp()
	
	elif userInput == "look":
		livinglook()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(kitchen())
	else:
		livingwrong()

def livinghelp():
	print("Inputs you can do for this room","Left","\n", "Right","\n", "Look","\n")
	userInput = input()
	if userInput == "help":
		livinghelp()
	
	elif userInput == "look":
		livinglook()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(kitchen())
	else:
		livingwrong()
        


def livinglook():
	print("you look around the lavish living room, you turn your scanner on to see if the chip could be anywhere in here. Nothing. You look and see a hallway to you left and the kitchen to your right, which way do your choose to go?","\n")
	userInput = input()
	if userInput == "help":
		livinghelp()
	
	elif userInput == "look":
		livinglook()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(kitchen())
	else:
		livingwrong()
        
def livingwrong():
	print("Wrong Input, try again")
	userInput = input()
	if userInput == "help":
		livinghelp()
	
	elif userInput == "look":
		livinglook()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(kitchen())
	else:
		livingwrong()
    
    


	
#hallway room with gaurd

def hallway():
	print("You enter the hallway of the mansion.")
	userInput = input()
	if userInput == "look":
		hallwaylook()
	elif userInput == "help":
		hallwayhelp()
	elif userInput =="left":
		return(livingroom())
	elif userInput == "right":
		return(kitchen())
	elif userInput == "forward":
		return(bedroom())
	elif userInput == "attack":
		attack()
	elif userInput == "sneak":
		sneak()
	else:
		hallwaywrong()
def hallwayhelp():
	print("Inputs you can do for this room","Left","\n", "Right","\n","Foward","\n", "Look","\n","Sneak\n","Attack\n")
	userInput = input()
	if userInput == "look":
		hallwaylook()
	elif userInput == "help":
		hallwayhelp()
	elif userInput =="left":
		return(livingroom())
	elif userInput == "right":
		return(kitchen())
	elif userInput == "forward":
		return(bedroom())
	elif userInput == "attack":
		attack()
	elif userInput == "sneak":
		sneak()
	else:
		hallwaywrong()

def hallwaylook():
	print("In the hallway you see a gaurd patrolling up and down. There are two options you can do, sneak around him or attack him stealthly, what do you choose?")
	userInput = input()
	
	if userInput == "help":
		hallwayhelp()
	elif userInput == "look":
		hallwaylook()
	elif userInput =="left":
		return(livingroom())
	elif userInput == "right":
		return(kitchen())
	elif userInput == "forward":
		return(bedroom())
	elif userInput == "attack":
		attack()
	elif userInput == "sneak":
		sneak()
	else:
		hallwaywrong()

def hallwaywrong():
	print("Wrong input Try again")
	userInput = input()
	if userInput == "look":
		hallwaylook()
	elif userInput == "help":
		livinghelp()
	elif userInput =="left":
		return(livingroom())
	elif userInput == "right":
		return(kitchen())
	elif userInput == "forward":
		return(bedroom())
	elif userInput == "attack":
		attack()
	elif userInput == "sneak":
		sneak()
	else:
		hallwaywrong()

def attack():
	print("You attack the gaurd the next time he turns his back, you see a bedroom infront of you and the kitchen to your right, before someone else comes what do you decide to do?")
	userInput = input()
	if userInput == "look":
		hallwaylook()
	elif userInput == "help":
		livinghelp()
	elif userInput =="left":
		return(livingroom())
	elif userInput == "right":
		return(kitchen())
	elif userInput == "forward":
		return(bedroom())
	else:
		hallwaywrong()

def sneak():
	print("You sneak around the gaurd sneaking in between the shadows, you see a bedroom infront of you and the kitchen to your right, where do you go?")
	userInput = input()
	if userInput == "look":
		hallwaylook()
	elif userInput == "help":
		livinghelp()
	elif userInput =="left":
		return(livingroom())
	elif userInput == "right":
		return(kitchen())
	elif userInput == "forward":
		return(bedroom())
	else:
		hallwaywrong()



#kitchen functions
def kitchen():
	print("you are now in the kitchen")
	userInput = input()

	if userInput == "look":
		kitchenlook()
	elif userInput == "help":
		kitchenhelp()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(livingroom()) 
	elif userInput == "forward":
		return(study())
	else:
		kitchenwrong()

def kitchenlook():
	print("you look in the kitchen for the chip, you look and scan all the cabinets and see no sign of the chip. You look in the fridge and take a snack, yummy. To you left is the hallway, behind you is the living room and in front of you is the study where would you like to go?")
	userInput = input()
	if userInput == "look":
		kitchenlook()
	elif userInput == "help":
		kitchenhelp()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(livingroom()) 
	elif userInput == "forward":
		return(study())
	else:
		kitchenwrong()


def kitchenhelp():
	print("Inputs you can do for this room","Left","\n", "Right","\n","Foward","\n", "Back","\n","Look\n")
	userInput = input()
	if userInput == "look":
		kitchenlook()
	elif userInput == "help":
		kitchenhelp()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(livingroom()) 
	elif userInput == "forward":
		return(study())
	else:
		kitchenwrong()

def kitchenwrong():
	print("Wrong input Try again")
	userInput = input()
	
	if userInput == "look":
		kitchenlook()
	elif userInput == "help":
		kitchenhelp()
	elif userInput == "left":
		return(hallway())
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(livingroom()) 
	elif userInput == "forward":
		return(study())
	else:
		kitchenwrong()


#bedroom functions
def bedroom():
	print("you are now in the bedroom")
	userInput = input()
	if userInput == "look":
		bedroomlook()
	elif userInput == "help":
		bedroomhelp()
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(hallway()) 
	else:
		bedroomwrong()

def bedroomlook():
	print("In the bedroom you see hump in th bed, somone is sleeping. Sneakily you look around an check to see if the silver hand chip is in here. No dice. The only way to go is the the study on your right or the hallway behind you. Where do you go?")
	userInput = input()
	if userInput == "look":
		bedroomlook()
	elif userInput == "help":
		bedroomhelp()
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(hallway()) 
	else:
		bedroomwrong()

def bedroomhelp():
	print("Inputs you can do for this room","\n", "Right","\n", "Back","\n","Look\n")
	userInput = input()
	if userInput == "look":
		bedroomlook()
	elif userInput == "help":
		bedroomhelp()
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(hallway()) 
	else:
		bedroomwrong()

def bedroomwrong():
	print("Wrong input, try again.")
	userInput = input()
	if userInput == "look":
		bedroomlook()
	elif userInput == "help":
		bedroomhelp()
	elif userInput == "right":
		return(study())
	elif userInput == "back":
		return(hallway()) 
	else:
		bedroomwrong()	

#study functions
def study():
	print("you are now in the study")
	userInput = input()
	if userInput == "look":
		studylook()
	elif userInput == "help":
		studyhelp()
	elif userInput == "left":
		return(bedroom())
	elif userInput == "back":
		return(kitchen()) 
	elif userInput == "forward":
		return(office())
	else:
		studywrong()

def studylook():
	print("You look around the study and tons of bookshelves, you see a desk, you look inside and find... nothing. You check your scanner and see there is only one more room you can check. The office that is infront of you, do you want to move foward, back toward the kitchen or left toward the bedroom?")
	userInput = input()
	if userInput == "look":
		studylook()
	elif userInput == "help":
		studyhelp()
	elif userInput == "left":
		return(bedroom())
	elif userInput == "back":
		return(kitchen()) 
	elif userInput == "forward":
		return(office())
	else:
		studywrong()

def studyhelp():
	print("Inputs you can do for this room","\n", "Left","\n", "Back","\n","Forward","\n","Look\n")
	userInput = input()
	if userInput == "look":
		studylook()
	elif userInput == "help":
		studyhelp()
	elif userInput == "left":
		return(bedroom())
	elif userInput == "back":
		return(kitchen()) 
	elif userInput == "forward":
		return(office())
	else:
		studywrong()

def studywrong():
	print("Wrong input, try again.")
	userInput = input()
	if userInput == "look":
		studylook()
	elif userInput == "help":
		studyhelp()
	elif userInput == "left":
		return(bedroom())
	elif userInput == "back":
		return(kitchen()) 
	elif userInput == "forward":
		return(office())
	else:
		studywrong()

def office():
	print("you now are in the office")
	userInput = input()
	if userInput == "look":
		officelook()
	elif userInput == "help":
		officehelp()
	elif userInput == "back":
		return(study()) 
	else:
		officewrong()

#type look in office to "win"
def officelook():
	print("You look around the office and you see it, the silverhand chip inside the computer ontop of the office desk, you grab the chip and you book it to the nearst window where you jump outside and run, time to get paid!")
	print("You WIN!")

def officehelp():
	print("Inputs you can do for this room","\n", "Back","\n","Look\n")
	userInput = input()
	if userInput == "look":
		officelook()
	elif userInput == "help":
		officehelp()
	elif userInput == "back":
		return(study()) 
	else:
		officewrong()

def officewrong():
	print("Wrong input, try again.")
	userInput = input()
	if userInput == "look":
		officelook()
	elif userInput == "help":
		officehelp()
	elif userInput == "back":
		return(study()) 
	else:
		officewrong()
	

	

if __name__ == "__main__":
	print("Welcome to the game!")
	print("You are a cyberpunk assassin hired to find the silverhand chip. You snuck into the mansion where it was the chips last known location")
	print("you may type help in every room to see what inputs you can use!\n")
	livingroom()

	
