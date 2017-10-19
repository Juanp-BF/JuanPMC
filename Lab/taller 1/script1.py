# Practica de if elif else y while 

a=2
b=8
c="hola"
i=1

if a>b:
	print ("a es mayor que b")
	print (a, b)
elif a==b:
	print ("a es igual a b")
else:
	print ("a no es mayor que b")

## whiles

while i<10:
	if a<b:
		print ("fuck off")
		print (a)
		i = i+1
		a = a+a
	elif a==b:
		print ("you did it")
		print (a)
		i = i+1
		a = a+1
	elif (a>b and a<10):
		print ("hola")
		print (a)
		i = i+1
		a = a+2
	else:
		print ("se acabó")
		print (a)
		print (b)
		i = 10

