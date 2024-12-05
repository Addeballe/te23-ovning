equipment = []

print("Du vaknar upp i ett kallt, och mörk rum gjort av sten.\nDu tittar runt och inser att rummet liknar en cell, och att det ligger någonting på golvet.")
input("ENTER")
wait_tries = 0
cellkey = True
while True:
    print("Det skulle vara en bra idé om du utforskar cellen mer noggrant.")
    print("[1] Titta närmare på föremålet på marken\n[2] Försök öppna cellgallret\n[3] Vänta")
    choice = int(input())
   
    if choice == 1:
        if cellkey == True:
            print("Du tar en närmare titt på föremålet..")
            input("ENTER")
            print("Det verkar vara en nyckel!\nNyckel finns nu i ditt inventory!")
            equipment.append("Nyckel")
            cellkey = False
            input("ENTER")
        elif cellkey == False:
            print("Du har redan hittat en nyckel.")
            input("ENTER")
    elif choice == 2:
        print("Du vandrar till cellgallret och försöker öppna det, men du inser att det är lönlöst")
        input("ENTER")
    elif choice == 3:
        wait_tries += 1
        if wait_tries == 10:
            print("Det verkar som att du har väntat för länge.\nDu faller ihop på golvet, och dör av svält.")
            break
        else:
            print("Du väntar, men ingenting händer")
            input("ENTER")
    else:
        print("Stavfel!")
     