mening = input("Skriv in din mening här:")
vokal_antal = 0
vokallista = ["a", "e", "o", "i", "u", "y", "å", "ä", "ö"]

for x in mening:
    if x in vokallista:
        vokal_antal += 1
        print (f"{vokal_antal}")

print(f"Det finns {vokal_antal} vokaler i din mening!")
