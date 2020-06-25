uangkertas = [100,50,20,10,5,2,1]
uangkamu = int(input())
print(uangkamu)
for uang in uangkertas :
	pengingat = uangkamu//uang
	uangkamu-=(pengingat*uang)
	print("%i nota(s) de R$ %i,00"%(pengingat,uang))