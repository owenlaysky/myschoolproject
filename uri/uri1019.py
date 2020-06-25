bagi = [3600,60,1]
N = int(input())
anslist = []
for time in bagi :
	pengingat = N//time
	N-=(pengingat*time)
	anslist.append(pengingat)

print("%i:%i:%i"% (anslist[0],anslist[1],anslist[2]))