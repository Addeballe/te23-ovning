#import time
print("Välkommen till kasper!")
#time.sleep(2)
print("Spelet går ut på att räkna upp från 1..")
#time.sleep(3)
print("och när man når ett nummer som innehåller eller är delbart med 7 eller 11, ska man klappa istället för att fortsätta att räkna.")
#time.sleep(6)
print("Lycka till!")
#time.sleep(1)

while True:
    print("Vad vill du göra?\n[1]Lägg till namn\n[2]Visa namn\n[3]Börja spela!\n[4]Sluta spela")
    choice = input()
    if choice == "1":
        names = []
        newname = input("Vilket namn vill du lägga till?")
        names.append("newname")
        names.sort
    elif choice == "2":
        for x in names:
            print(x)
    
    elif choice == "3":
        count = 0
        print("Låt oss börja!")
        while True:
            count += 1
            input()
            if count%7==0 or count%11==0:
                print("Klapp!")
            elif str(7) in str(count):
                print("Klapp!")            
            else:
                print(f"{count}!")

    elif choice == "4":
        break
    else:
        print("Stavfel, försök igen.")
        input()

