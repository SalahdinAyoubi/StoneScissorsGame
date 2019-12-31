from designs import *

import random ,  os  ,  time , sys

# Colors

green ='\033[92m'

red ='\033[91m'

blue ='\033[94m'

yellow ='\033[93m'

white = '\033[0m'

mov = '\033[95m'

blueli  = '\033[96m'

# list Colors

colors = [green ,  red ,  blue , yellow , white , mov,  blueli]

# Colos results

draw = yellow+draw

winner = green+winner

loser =  red+loser

result = 0

list = [stone ,  sheet , sciss]

# this is function About me 

def about():

	z=my.replace("Ø", "∞")	
	for i in range(1):

		for i in colors: 

			print(i+my)

			time.sleep(0.1)

			os.system("clear")

			print(z)

			time.sleep(0.3)

			os.system("clear")

	print(z)

	

	abou = yellow+" Creat by :  Python Dz  \n Github   :  SalahdinAyoubi \n Facebook :  sami.rabih.925\n update   :  31-12-2019\n\n"

	

	for i in abou:

	    time.sleep(0.1)

	    sys.stdout.write(i)

	    sys.stdout.flush()

	time.sleep(1.5)

	print(white)

	os.system("clear")

	

	

def rando():

	for i in list:

		for i in list: 

			print(blueli+i)

			time.sleep(0.2)

			os.system("clear")

#about()

while True: 

	r_choice = random.choice(list)

	print(" 1 - Stone                  4 - About \n 2 - Sheet                  5 - Exit\n 3 - Scissors")

	#print(r_choice)

	choice = input(" - Enter number your choice: ")

	rando()

	#  number 1= Stone

	if choice == "1" and r_choice == stone:

		print(draw)

		print(yellow+stone)

		result = result+0

	elif choice =="1" and r_choice == sheet:

		print(loser)

		print(green+sheet)

		result = result-1

	elif choice =="1" and r_choice == sciss:

		print(winner)

		print(red+sciss)

		result = result+1

	

	# numbr 2 = sheet

	elif choice == "2" and r_choice == stone:

		print(winner)

		print(red+stone)

		result = result+1

	elif choice =="2" and r_choice == sheet:

		print(draw)

		print(yellow+sheet)

		result = result+0

	elif choice == "2" and r_choice == sciss:

		print(loser)

		print(green+sciss)

		result = result-1

	

	#  number 3 =  scissors

	elif choice == "3" and r_choice == stone:

		print(loser)

		print(green+stone)

		result = result-1

	elif choice =="3" and r_choice == sheet:

		print(winner)

		print(red+sheet)

		result = result+1

	elif choice == "3" and r_choice == sciss:

		print(draw)

		print(yellow+sciss)

		result = result+0		

	elif choice == "4":

		about()	

	elif choice == "5":

		print("\n\n  ^__^   Good Bey my friend \n")

		exit()

	

	if result ==  0: 

	 	print(yellow+N0)

	elif result == -1:

	 	print(red+N_1)

	elif result == -2:

	 	print(red+N_2)

	elif result == - 3:

	 	print(red+N_3)

	elif result < -3:

	 	print(mov+y_loser)

	 	

	elif result == 1:

	 	print(green+N1)

	elif result == 2:

	 	print(green+N2)

	elif result == 3:

	 	print(green+N3)

	elif result > 3:

	 	print(green+y_win)

	print(white+"  -  Your choice : ", choice)

 
