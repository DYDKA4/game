import random, time, colorama, os
from colorama import Fore,Back,Style,init




#f open('text',r)
#r открытие на чтение 
#w открытие на апись, если файл не существует создется новый
#inv.append(element)
#len(inv)>10
#
#
#
#

def menu():
	inv = []
	clear = lambda: os.system('cls')
	init()
	my_property = ""
	my_property_int = 0
	items = ""
	chatacter = ""
	start = 0
	print ("Добро пожаловать в игру.\n1. Начать новую игру \n2. Загрузить сохранение \n3. Выйти")
	answer = input()
	clear()
	if (answer == "2"):
		f = open ('save.txt','r')
		w = f.read()
		list = w.split("\n")
		for q in list:
			l = q.split(' ')
			if l[0]=='life':
				life = int(l[1])
			if l[0]=='hp':
				hp = int(l[1])
			if l[0]== 'strength':
				strength = int(l[1])
			if l[0]== 'agility':
				agility = int(l[1])
			if l[0]== 'gold':
				gold = int(l[1])
			if l[0]== 'exp':
				exp = int(l[1])
			if l[0]== 'hexpp':
				hexpp = int(l[1])
			if l[0]== 'expp':
				expp = int(l[1])
			if l[0]== 'name':
				name = l[1]
			if l[0]== 'race':
				race = l[1]
			if l[0]== 'inventory':
				for x in l:
					if x =='inventory':
						pass
					else:
						inv.append(x)
		f.close() 
		print ("Сохранение успешно загружено")
		start = 1# загрузка профиля
	if(answer == "1"):
		print ("Твое Имя")
		name = input()
		clear()
		print ("Твоя раса")
		print ("Расы: \n1. Ельф \n2. Орк \n3. Человек ")
		rac = input()
		clear()
		if (rac == "3"):
			strength = 5
			agility = 5
			hp = 150
			race = "Человек"
		if (rac == "1"):
			agility = 7
			strength = 3
			hp = 100
			race = "Ельф"
		if (rac == "2"):
			agility = 3
			strength = 7;
			hp = 200
			race = "Орк"
		exp = 1 
		hexpp = 0
		expp = 8
		life = hp
		gold = 0
		start = 1 # создание новго персоеажа

	if (answer == "3"):
		print("Спасибо за игру")

	if (start == 1):
		print(Fore.GREEN + "Твой герой:")
		print("Имя:",name)
		print("Раса:",race)
		print("Сила:",strength)
		print("Ловкость:",agility)
		print("Золото:",gold)
		print("Уровень: ", exp," ",hexpp , "из" , expp)
		print ("Что бы выйти введи используйте сочетание CTRL + C", Style.RESET_ALL)
		stamina = 10
		choice = input()
		clear()
		while (True):
			

			level = random.randint(0, 4)
			if (stamina < 10):
				stamina = stamina + 1
			if (level == 0):
				print("Ты встретил человека, ты можешь просто уйти или начать драку\n 1. Начать драку \n 2. Уйти")
				enemyhp = 150
				enemystrength = random.randint(5,10)
				enemyagility = random.randint(5,10)
				choice = input()
				clear()
				if(choice == "1"):
					while (enemyhp > 0):
						print(Fore.RED + "Выбери стиль атаки: \n 1. Тяжелый удар\n 2. Средний удар\n 3. Легкий удар \n 4. Попытаться убежать "+ Style.RESET_ALL)
						choice = input()
						clear()
						if (choice == "1" and stamina -3 >= 0):
							stamina = stamina - 3
							enemyhp = enemyhp - strength*20
						if (choice == "2" and stamina-2 >= 0):
							stamina = stamina - 2
							enemyhp = enemyhp - strength*15
						if (choice == "3" and stamina-1 >= 0):
							stamina = stamina - 1
							enemyhp = enemyhp - strength*10	
						elif(stamina<1):
							print("У тебя кончилась стамина, пора бежать")
						if(enemyhp > 0):
							print("Тебя атакуют")	
							hp = hp - enemystrength*15
						print("Хп врага:",enemyhp,"Твои хп и стамина",hp,", ",stamina)
						choice = input()
						clear()
						if(hp < 0 ):
							print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
							break
						if (enemyhp < 0):
							print (Back.CYAN + "Ты выиграл" + Style.RESET_ALL)
							gold = gold + 1
							hexpp = hexpp + 2
							if (hexpp >= expp):
								exp = exp +1 
								expp = expp + 4
								hexpp = 0
								agility = agility + 1
								strength = strength + 1

						if (choice == "4"):
							if(agility < enemyagility):
								print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
								break	
				choice = input()
				clear()
				if (choice == "stop"):
						break#встреча с человеком

			if (level == 1):
				print("Ты встретил орка, он сильный, но тупой.\n 1. Начать драку \n 2. Убежать")
				enemyhp = 200
				enemystrength = random.randint(7,12)
				enemyagility = random.randint(1,6)
				choice = input()
				clear()
				if(choice == "1"):
					while (enemyhp > 0):
						print(Fore.RED + "Выбери стиль атаки: \n 1. Тяжелый удар\n 2. Средний удар\n 3. Легкий удар \n 4. Попытаться убежать "+ Style.RESET_ALL)
						choice = input()
						clear()
						if (choice == "1" and stamina -3 >= 0):
							stamina = stamina - 3
							enemyhp = enemyhp - strength*20
						if (choice == "2" and stamina-2 >= 0):
							stamina = stamina - 2
							enemyhp = enemyhp - strength*15
						if (choice == "3" and stamina-1 >= 0):
							stamina = stamina - 1
							enemyhp = enemyhp - strength*10	
						elif(stamina < 1 ):
							print("У тебя кончилась стамина, пора бежать")
						if(enemyhp > 0):
							print("Тебя атакуют")	
							hp = hp - enemystrength*20
						print("Хп врага: ",enemyhp,"Твое хп и стамина: ",hp,", ",stamina)
						choice = input()
						clear()
						if(hp < 0 ):
							print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
							break
						if (enemyhp < 0):
							print (Back.CYAN + "Ты выиграл" + Style.RESET_ALL)
							gold = gold + 3
							hexpp = hexpp + 3
							if (hexpp >= expp):
								exp = exp +1 
								expp = expp + 4
								agility = agility + 1
								hexpp = 0
								strength = strength + 1
						if (choice == "4"):
							if(agility < enemyagility):
								print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
								break	
				else:
					if(enemyagility > agility):
						print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
						break
					else:
						print("Ты убежал")
				choice = input()
				clear()#встреча с огроморк



			if (level == 2):
				print("Ты встретил эльфа, ты можешь убить его или сбежать от него \n1. Начать драку \n2. Убежать")
				enemyhp = 100
				enemystrength = random.randint(1,6)
				enemyagility = random.randint(7,12)
				choice = input()
				if(choice == "1"):
					while (enemyhp > 0):
						print(Fore.RED +"Выбери стиль атаки \n 1. Тяжелый удар\n 2. Средний удар\n 3. Легкий удар \n 4. Попытаться убежать"+ Style.RESET_ALL)
						choice = input()
						clear()
						if (choice == "1" and stamina -3 >= 0):
							stamina = stamina - 3
							enemyhp = enemyhp - strength*20
						if (choice == "2" and stamina-2 >= 0):
							stamina = stamina - 2
							enemyhp = enemyhp - strength*15
						if (choice == "3" and stamina-1 >= 0):
							stamina = stamina - 1
							enemyhp = enemyhp - strength*10	
						elif(stamina < 1):
							print("У тебя кончилась стамина, пора бежать")
						if(enemyhp > 0):
							print("Тебя атакуют")	
							hp = hp - enemystrength*10
						print("Enemy hp: ",enemyhp,"your hp, stamina: ",hp,", ",stamina)
						choice = input()
						clear()
						if(hp < 0 ):
							print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
							break
						if (enemyhp <= 0):
							print (Back.CYAN + "Ты выиграл" + Style.RESET_ALL)
							gold = gold + 1
							hexpp = hexpp + 1
							if (hexpp >= expp):
								exp = exp +1 
								expp = expp + 4
								agility = agility + 1
								strength = strength + 1
								hexpp = 0
						if (choice == "4"):
							if(agility < enemyagility):
								print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
								break	
				else:
					if(enemyagility > agility):
						print(Fore.MAGENTA + "Ты умер"+ Style.RESET_ALL)
						break
					else:
						print("Ты спас свою жизнь")
				choice = input()
				clear()
				if (choice == "stop"):
					break#встреча с эльфомельф



			if (level == 3):
				print (Fore.YELLOW + "Ты нашел заброшенный лагерь \n1. Обыскать лагерь \n2. Не обыскивать" + Style.RESET_ALL)
				t = input()
				clear()
				if (t == "1"):
					randgold = random.randint(0,3)
					if (randgold == 0):
						print ("Ты ничего не нашел")
					elif(randgold == 1 or 2 or 3 ):
						print ("Ты нашел золотую монету")
						gold = gold+1
					print("Хочешь продолжить искать хабар? \n1. Да \n2. Нет")
					choice = input()
					clear()
					if (choice == "1"):
						randproperty = random.randit(1,100)
						if (randproperty < 51 ):
							f = open ('property.txt','r')
							w = f.read()
							list = w.split("\n")
							for q in list:
								l = q.split(' ')
								if l[0]=='common':
									my_property = (l[0])
									my_property_int = (l[1])
						if (randproperty > 50 and randproperty < 76):
							f = open ('property.txt','r')
							w = f.read()
							list = w.split("\n")
							for q in list:
								l = q.split(' ')
								if l[0]=='uncommon':
									my_property = (l[0])
									my_property_int = (l[1])
						if (randproperty > 75 and randproperty < 89):
							f = open ('property.txt','r')
							w = f.read()
							list = w.split("\n")
							for q in list:
								l = q.split(' ')
								if l[0]=='rare':
									my_property = (l[0])
									my_property_int = (l[1])
						if (randproperty > 88 and randproperty < 98):
							f = open ('property.txt','r')
							w = f.read()
							list = w.split("\n")
							for q in list:
								l = q.split(' ')
								if l[0]=='epic':
									my_property = (l[0])
									my_property_int = (l[1])
						if (randproperty > 97 ):
							f = open ('property.txt','r')
							w = f.read()
							list = w.split("\n")
							for q in list:
								l = q.split(' ')
								if l[0]=='legendary':
									my_property = (l[0])
									legendary = (l[1])
				print(my_property)

				while (t != "3"):
					clear()
					print ("1. Использовать аптечку. \n2. Поспать (сохраниться)\n3. Покинуть лагерь")
					t = input()
					clear()
					if (t == "1" ):
						for x in range(0,len(inv)):
							if(inv[x]=="healing"):
								print("Ты успешно полечился")
								inv[x] = ""
								if(hp+50>=life):
									hp=life
								else:
									hp=hp+50
								break
							else:
								print("У тебя нет аптечки")


					if (t == "2"):
						f = open('save.txt','w')
						n = ""
						for word in inv:
							n = n + word + " "
						s = "life " + str(life)+"\nhp "+str(hp) + "\nstrength " + str(strength) + "\nagility " + str(agility) + "\ngold " + str(gold) + "\nexp " + str(exp) + "\nhexpp " + str(hexpp) + "\nexpp " + str(expp) + "\nname " + name + "\nrace " + race + "\ninventory " + n
						f.write(s)
						f.close()
						print("Ты успешно поспал")


			if (level==4):
				t = ""
				while (t!="7"):
					 
					print(Fore.MAGENTA +"Ты в магазине ты можешь купиь: \n1. Броню(1)\n2. Ботинок(1)\n3. Оружие(2) \n4. Вылечить раны(2)\n5. Хилку(1)\n6. Посмотреть инвентарь \n7. Выйти"+Style.RESET_ALL)
					print(Fore.GREEN + "Your hero:")
					print("Name:"+name)
					print("Race:"+race)
					print("Strength:",strength)
					print("Agility:",agility)
					print("Gold:",gold)
					print("HP:",hp)
					print("Уровень: ", exp," ",hexpp , "из" , expp, Style.RESET_ALL)
					t = input()
					clear()
					if (t == "1" and gold-1 > 0):
						strength = strength + 1
						gold = gold - 1
						print("Ты купил броню")
						t = input()
					if (t == "2" and gold-1 > 0):
						agility = agility + 1
						gold = gold - 1
						print("Ты купил ботинки")
						t = input()
					if (t == "3" and gold-2 > 0):
						strength = strength +2
						gold = gold - 2
						t = input()
						print("Ты купил оружие")
					if (t == "4" and gold-2 > 0):
						gold = gold - 2
						hp = life
						print("Ты вылечил раны")
						t = input()
					if (t == "5" and gold-1 > 0):
						if "" in inv: 
							for x in range(0,len(inv)):
								if(inv[x]==""):
									gold = gold - 1
									inv[x] = "healing"
									print ("Ты купил аптечку")
						else:
							inv.append("healing")
						
					elif (gold < 1 and t != "exit"):
						print("Нужно больше золота")
					if (t == "6"):
						print ("Твои вещи")
						for x in range(0,len(inv)):
							print(inv[x])
				if (t == "stop"):
						break# магазинмагазин
			if (hp < 0):
				print ("GG")
				break

menu()