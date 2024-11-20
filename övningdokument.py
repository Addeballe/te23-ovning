äpple = 7
päron = 13

äpplen_såldes = int(input("Hur många äpplen sålde Axel?"))
päron_såldes = int(input("Hur många päron sålde Petra?"))

äpplen_pengar = äpplen_såldes * äpple
päron_pengar = päron_såldes * päron

print(f"Äpplerna såldes för {äpplen_pengar}kr, och päronen såldes för {päron_pengar}kr.")

if äpplen_pengar > päron_pengar:
    print("Axel stjänade mer pengar.")
else:
    print("Petra tjänade mer pengar.")