Money = 5883
print("Your Money Balance is:", Money)
print("\n\t\t\tYOUR MONEY STILL HAVE")

oneki = Money//1000
Money = Money - oneki*1000
paybhun = Money//500
Money = Money - paybhun*500
twohun = Money//200
Money = Money - twohun*200
onehun = Money//100
Money = Money - onehun*100
pebte = Money//50
Money = Money - pebte*50
bente = Money//20
Money = Money - bente*20
ten = Money//10
Money = Money - ten*10
payb = Money//5
Money = Money - payb*5
uno = Money//1
Money = Money - uno

print("1000 :", oneki)
print("500 :", paybhun)
print("200 :", twohun)
print("100 :", onehun)
print("50 :", pebte)
print("20 :", bente)
print("10 :", ten)
print("1 :", uno)
