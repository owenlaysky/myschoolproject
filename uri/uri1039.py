n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

avg = (2*n1+3*n2+4*n3+1*n4)/10
if avg >= 7.0 :
	print("Media: %.1f" % (avg))
	print("Aluno aprovado.")
elif avg >= 5.0:
	n5 = float(input())
	print("Media: %.1f" % (avg))
	print("Aluno em exame.")
	print("Nota do exame: %.1f" % (n5))
	print("Aluno aprovado.")
	avg = (avg+n5)/2
	print("Media final: %.1f" % (avg))
else:
	print("Media: %.1f" % (avg))
	print("Aluno reprovado.")