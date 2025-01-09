from random import randint
equipment = []

print("Du vaknar upp i ett kallt, och mörk rum gjort av sten.\nDu tittar runt och inser att rummet liknar en cell, och att det ligger någonting på golvet.")
input("ENTER")
wait_tries = 0
death = False

## ACT 1

while True:
    print("Det skulle vara en bra idé om du utforskar cellen mer noggrant.")
    print("[1] Titta närmare på föremålet på marken\n[2] Försök öppna cellgallret\n[3] Vänta")
    choice = int(input()) 
    if choice == 1:
            if "Nyckel" in equipment:
                print("Du har redan tagit upp nyckeln.")
                input("ENTER")
            else:
                print("Du tar en närmare titt på föremålet..")
                input("ENTER")
                print("Det verkar vara en nyckel!\nNyckel finns nu i ditt inventory!")
                equipment.append("Nyckel")
                input("ENTER")
    elif choice == 2:
            if "Nyckel" in equipment:
                print("Du går fram till cellgallret och försöker öppna det..")
                input("ENTER")
                print(".. och du lyckas öppna det!")
                break
            else:
                print("Du går fram till cellgallret och försöker öppna det..")
                input("ENTER")
                print("Men du har ingenting att öppna det med")
                input("ENTER")
    elif choice == 3:
            wait_tries += 1
            if wait_tries == 10:
                print("Det verkar som att du har väntat för länge.\nDu faller ihop på golvet, och dör av svält.")
                death = True
                break
            else:
                print("Du väntar, men ingenting händer")
                input("ENTER")
    else:
        print("Stavfel!")

 ## ACT 2   

    if death == False:
        print("Du tar dig ut ur cellen.. äntligen.\nRummet du nu befinner dig i liknar cellen, fuktiga stenväggar och kallt golv.\nNågonting annourlunda fångar dock din uppmärksamhet, solljus från ett hål i väggen.")
        print("Du bestämer dig för att göra något")
        while True:
            print("[1] Kolla närmare hålet i väggen\n[2] Utforska rummet ytterligare\n[3] Skrik ")

