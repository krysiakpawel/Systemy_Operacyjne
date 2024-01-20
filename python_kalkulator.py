a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))

def dodaj(a,b):
	return a + b
def odejmij(a,b):
	return a - b
def pomnoz(a,b):
	return a * b
def podziel(a,b):
	return a / b
print ("Suma {} + {} = {}".format(a,b,dodaj(a,b)))
print ("Roznica {} - {} = {}".format(a,b,odejmij(a,b)))
print ("Iloczyn {} * {} = {}".format(a,b,pomnoz(a,b)))
if a  == 0.0 or b == 0.0:
	print ("Nie mozna dzielic przez 0")
else:
	print( "Iloraz {} / {} = {}".format(a,b,podziel(a,b)))
