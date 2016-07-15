# -*- coding: utf-8 -*-

print "Mi equipo es:\nChichil Hernandez Juan\nMiguel Angel Vazquez (Alias: Samanta)\nRosas Colula Luiz Angel\nMarina Ramirez Jaime\n"

l = raw_input("ingresa el tamaño del arreglo: ")

arreglo = []
for i in range(0, int(l)):
	arreglo.append(raw_input("ingresar el elemento: "))

print "X^0 = E"


a = "{"
for i in range(0, len(arreglo)):
	a = a + arreglo[i] +","
a = a + "}"
print "X ^1 = "+a
print "\n"

b = "{"
for i in range(0, len(arreglo)):
	for j in range(0, len(arreglo)):	
		b = b + arreglo[i] + arreglo[j] +","
b = b + "}"
print "X ^2 = "+b
print "\n"

c = "{"
for i in range(0, len(arreglo)):
	for j in range(0, len(arreglo)):	
		for k in range(0, len(arreglo)):
			c = c + arreglo[i] + arreglo[j] + arreglo[k] +","
c = c + "}"
print "X ^3 = "+c
print "\n"

d = "{"
for i in range(0, len(arreglo)):
	for j in range(0, len(arreglo)):	
		for k in range(0, len(arreglo)):
			for l in range(0, len(arreglo)):
				d = d + arreglo[i] + arreglo[j] + arreglo[k] + arreglo[l] +","
a = len(d)
d = d + "}"
print "X ^4 = "+d
print "\n"

print "¡Ya quedo profe!"
