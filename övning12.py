

while True:
    dålig_dag = input("Har du en dålig dag? [Y/N]")
    if dålig_dag == "Y":
        hjälp = input("Vill du ha en bättre dag? [Y/N]")
        if hjälp == "Y":
            print("Vad bra!")
            dålig_dag == "N"
            break
        elif hjälp == "N":
            print("Vad träkigt :(")
            break
    elif dålig_dag == "N":
        print("Vad bra!")
        break
    else:
        print("Stavfel")
        
