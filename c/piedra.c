#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){	
	FILE *in;
	float lista1[61];
	float var;
	int i;
	in = fopen("Piedra.dat", "r");
	for(i=0;i<61;i++){
//		fscanf(in, "%f", lista1[i]);
		fscanf(in, "%f", &var);
		lista1[i] = var;
		printf("%f\n", lista1[i]);
	}
}
