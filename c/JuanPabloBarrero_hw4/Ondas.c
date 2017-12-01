#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define pi 3.1416


int g(int i,int j){
	return i + 101*j;
}

int main(){
	int N = 129;		
	float L = 0.64;
	float c = 250;
	int tiempo;
	//Declaro los vectores	
	float *u_inicial = malloc(N*sizeof(float));
	float *x = malloc(N*sizeof(float)); 
	float *u_futuro = malloc(N*sizeof(float));
	float *u_pasado = malloc(N*sizeof(float));
	float *u_presente = malloc(N*sizeof(float));
	float *UT4 = malloc(N*sizeof(float));
	float *UT2 = malloc(N*sizeof(float));
	float *UT8 = malloc(N*sizeof(float));
	float *u_inicial1 = malloc(N*sizeof(float));
	float *u_futuro1 = malloc(N*sizeof(float));
	float *u_pasado1 = malloc(N*sizeof(float));
	float *u_presente1 = malloc(N*sizeof(float));
	float *UT41 = malloc(N*sizeof(float));
	float *UT21 = malloc(N*sizeof(float));
	float *UT81 = malloc(N*sizeof(float));
	//inicializo los vectores (eliminando la información que habia antes)	
	int i;
	for(i = 0; i<N; i++){
		u_inicial[i] = 0.0;
		u_inicial1[i] = 0.0;
	}
	for(i = 0; i<N; i++){
		x[i] = 0.0;
	}

	for(i = 0; i<N; i++){
		u_futuro[i] = 0.0;
		u_futuro1[i] = 0.0;
	}
	
	for(i = 0; i<N; i++){
		u_pasado[i] = 0.0;
		u_pasado1[i] = 0.0;
	}
	for(i = 0; i<N; i++){
		u_presente[i]=0.0;
		u_presente1[i]=0.0;
	}
	
	
	//leo el .dat y guardo la información en los vectores
	FILE *dat;
	
	dat = fopen("cond_ini_cuerda.dat", "r");
		
	for(i = 0; i<N; i++){	
		fscanf(dat,"%f %f", &x[i], &u_inicial[i]);
	}
	fclose(dat);

	u_inicial[0] = 0.0;
	u_inicial[N-1] = 0.0;

	float dt = 0.00001;
	float dx = x[1]-x[0];
	float r = c * dt / dx;
	
	u_futuro[0] = 0.0;
	u_futuro[N-1] = 0.0;	
		
	for(i = 1; i<N-1; i++){
		u_futuro[i] = u_inicial[i] + (pow(r,2)/2.0) * (u_inicial[i+1] - 2.0 * u_inicial[i] + u_inicial[i-1]);
	}
	
	for(i = 0; i<N; i++){
		u_pasado[i] = u_inicial[i];
	}
	for(i = 0; i<N; i++){
		u_presente[i] = u_futuro[i];
	}
	
	int j;
	scanf("%d", &tiempo);	
	for(j = 0; j<tiempo; j++){
		for(i = 1; i<N-1; i++){
			u_futuro[i] = (2.0*(1.0-pow(r,2)))*u_presente[i] - u_pasado[i] + (pow(r,2))*(u_presente[i+1] +  u_presente[i-1]);			
		}
		for(i = 0; i<N; i++){
			u_pasado[i] = u_presente[i];		
		}
		for(i = 0; i<N; i++){
			u_presente[i] = u_futuro[i];
		}
		if(j == 64){
			for(i = 0; i<N; i++){			
				UT8[i] = u_presente[i];
			}
		}
		if(j == 128){
			for(i = 0; i<N; i++){			
				UT4[i] = u_presente[i];
			}
		}
		if(j == 256){
			for(i = 0; i<N; i++){			
				UT2[i] = u_presente[i];
			}
		}
			

	}

	
	dat = fopen("datos.txt", "w");
	if(!dat){
		printf("no sirve %s\n", "datos.txt");
	}
	for(i = 0; i<N; i++){
		fprintf(dat, "%f %f %f %f %f %f \n", x[i], u_presente[i], u_inicial[i], UT8[i], UT4[i], UT2[i]);
	}
	

	
	float l = 0.64;
// segundo ejercicio 
	
	u_futuro1[0] = 0.0;
	u_futuro1[N-1] = 0.0;	
		
	for(i = 1; i<N-1; i++){
		u_futuro1[i] = u_inicial1[i] + (pow(r,2)/2.0) * (u_inicial1[i+1] - 2.0 * u_inicial1[i] + u_inicial1[i-1]);
	}
	
	for(i = 0; i<N; i++){
		u_pasado1[i] = u_inicial1[i];
	}
	for(i = 0; i<N; i++){
		u_presente1[i] = u_futuro1[i];
	}
	
	for(j = 0; j<tiempo; j++){
		u_futuro1[0] = sin(2*pi*c/l*j*dt);
		for(i = 1; i<N-1; i++){
			u_futuro1[i] = (2.0*(1.0-pow(r,2)))*u_presente1[i] - u_pasado1[i] + (pow(r,2))*(u_presente1[i+1] +  u_presente1[i-1]);			
		}
		for(i = 0; i<N; i++){
			u_pasado1[i] = u_presente1[i];		
		}
		for(i = 0; i<N; i++){
			u_presente1[i] = u_futuro1[i];
		}
		if(j == 64){
			for(i = 0; i<N; i++){			
				UT81[i] = u_futuro1[i];
			}
		}
		if(j == 128){
			for(i = 0; i<N; i++){			
				UT41[i] = u_futuro1[i];
			}
		}
		if(j == 256){
			for(i = 0; i<N; i++){			
				UT21[i] = u_futuro1[i];
			}
		}
	}

	
	dat = fopen("datos1.txt", "w");
	if(!dat){
		printf("no sirve %s\n", "datos1.txt");
	}
	for(i = 0; i<N; i++){
		fprintf(dat, "%f %f %f %f %f %f \n", x[i], u_presente1[i], u_inicial1[i], UT81[i], UT41[i], UT21[i]);
	}
	
////// EJERCICIO 3 Tambor

//// TODO FUNCIONA SIN EL TAMBOR NO SE PORQUE CUANDO LO PONGO ME DICE SEGMENTATION FAULT

	int N2 = 101;
	int k;
	//defino la matriz de la forma:
	float *u_inicial2 = malloc(N2*N2*sizeof(float));
	float *u_futuro2 = malloc(N2*N2*sizeof(float));
	float *u_pasado2 = malloc(N2*N2*sizeof(float));
	float *u_presente2 = malloc(N2*N2*sizeof(float));
	float *UT43 = malloc(N2*N2*sizeof(float));
	float *UT23 = malloc(N2*N2*sizeof(float));
	float *UT83 = malloc(N2*N2*sizeof(float));
	
	//inicializo la matriz 

	dat = fopen("cond_ini_tambor.dat", "r");
	
	for(j = 0; j<N2; j++){
		for(i = 0; i<N2; i++){	
			fscanf(dat,"%f", &u_inicial[g(i, j)]);
		}
	}
	fclose(dat);	
	float dx1 = 0.000005		
	int r2 = c*dt/dx1;
	for(j = 1; j<N2-1; j++){	
		for(i = 1; i<N2-1; i++){
			u_futuro2[g(i, j)] = u_inicial2[g(i,j)] + (pow(r,2)/2.0) * (u_inicial2[g(i+1,j)] + u_inicial2[g(i, j+1)] - 4.0 * u_inicial2[g(i,j)] + u_inicial2[g(i-1,j)] + u_inicial2[g(i,j-1)]);
		}
	}
	
	for(j = 0; j<N2; j++){
		for(i = 0; i<N2; i++){
			u_pasado2[g(i,j)] = u_inicial2[g(i,j)];
		}
	}
	for(j = 0; j<N2; j++){	
		for(i = 0; i<N2; i++){
			u_presente2[g(i,j)] = u_futuro2[g(i,j)];
		}
	}
	
	
	for(k = 0; k<tiempo; k++){
		for(j = 1; j<N2-1; j++){
			for(i = 1; i<N2-1; i++){
				u_futuro2[g(i,j)] = (2.0*(1.0-2.0*pow(r,2)))*u_presente2[g(i,j)] - u_pasado2[g(i,j)] + (pow(r,2))*(u_presente2[g(i+1,j)] + u_presente2[g(i,j+1)] +  u_presente2[g(i-1,j)] +  u_presente2[g(i,j-1)]);			
			}
			for(j = 0; j<N2; j++){
				for(i = 0; i<N2; i++){
					u_pasado2[g(i,j)] = u_presente2[g(i,j)];		
					}			
			}
			for(j = 0; j<N2; j++){			
				for(i = 0; i<N2; i++){
					u_presente2[g(i,j)] = u_futuro2[g(i,j)];
				}
			}
			if(j==50){
				for(j=0; j<N2;j++){
					for(i=0; i<N2; i++){
						UT23[g(i,j)] = u_futuro2[g(i,j)];
					}
				}
			}
			if(j==25){
				for(j=0; j<N2;j++){
					for(i=0; i<N2; i++){
						UT43[g(i,j)] = u_futuro2[g(i,j)];
					}
				}
			}
			if(j==12){
				for(j=0; j<N2;j++){
					for(i=0; i<N2; i++){
						UT83[g(i,j)] = u_futuro2[g(i,j)];
					}
				}
			}
		}
	}
	dat = fopen("datos2.txt", "w");	
	if(!dat){
		printf("no sirve %s\n", "datos2.txt");
	}
	for(j = 0; j<N2; j++){	
		for(i = 0; i<N2; i++){
			fprintf(dat, "%f %f %f %f %f \n", u_presente2[g(i,j)], u_inicial2[g(i,j)], UT23[g(i,j)], UT43[g(i,j)], UT83[g(i,j)]);
		}
	}
}


