*.pdf:grafica
	pdflatex Results_hw5.tex

grafica:datos.dat
	python Plots.py

datos.dat:correr
	./CurvasRotacion.x

correr:RadialVelocities.dat
	cc CurvasRotacion.c -lm -o CurvasRotacion.x
