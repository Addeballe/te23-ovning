from time import sleep

print("Välkommen till ...!\n")
sleep(0.5)

level_1 = False
level_2 = False
level_select = 0


while True:
    
    if level_select == 1 or 2:
        break
    
    print("[1] Starta spel \n[2] Level select \n[3] Avsluta spelet \n")
    action = input()

    if action == 1:
        level_1 = True
        break
    if action == 2:
        while True:
            print("[1] Level 1 \n[2] Level 2 \n[3] Återvänd till menyn")
            level_select = input()
            if level_select == 1:
                level_1 = True
                break
            if level_select == 2: 
                level_2 = True
                break
            if level_select == 3:
                break