x , y = input().split()
x, y = int(x), int(y)

#x menyatakan kode -> key
#y menyatakan jumlah -> value
price = {
	1 : 4.00,
	2 : 4.50,
	3 : 5.00,
	4 : 2.00,
	5 : 1.50
}

result = price[x]*y

print("Total: R$ %.2f" % (result))