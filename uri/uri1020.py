bagi = [365,30,1]
N = int(input())
ano = []
for hari in bagi :
	pengingat = N//hari
	N-=(pengingat*hari)
	ano.append(pengingat)

print("%i ano(s)"% (ano[0]))
print("%i mes(es)"% (ano[1]))
print("%i dia(s)"% (ano[2]))