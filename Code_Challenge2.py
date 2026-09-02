Money = int(input("Enter amount to deposit ----> "))
print("===================== PH PESO DENOMINATION BREAK DOWN ==========================")
print("CURRENT MONEY IS --> ", Money,"php")

oneki = Money // 1000
oneki_sukli = Money % 1000
paybhun = oneki_sukli // 500
paybhun_sukli = Money % 500
twohun = paybhun_sukli // 200
twohun_sukli = Money % 200
onehun =twohun_sukli // 100
onehun_sukli = Money % 100
pebte = onehun_sukli // 50
pebte_sukli = Money % 50
bente = pebte_sukli // 20
bente_sukli = Money % 20
ten = bente_sukli // 10
ten_sukli = Money % 10
payb = ten_sukli // 5
payb_sukli = Money % 5
uno = payb_sukli // 1
uno_sukli = Money % 1

print("\n1000 :", oneki)
print(" 500 :", paybhun)
print(" 200 :", twohun)
print(" 100 :", onehun)
print("  50 :", pebte)
print("  20 :", bente)
print("  10 :", ten)
print("   1 :", uno)
