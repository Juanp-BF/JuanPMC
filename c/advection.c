#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//Comentarios se hacen de esta forma 
int main(){
	int n_points = 1000;
	int N = n_points;
	//Declaro un vector	
	float * a = malloc(N*sizeof(float));  
	//inicializo el vector (eliminando la información que habia antes)	
	int i;
	int j;
	for( i = 0; i<N; i++);
		a[i] = 0.0;
	//Declaro una matriz
	int M = 700;
	float ** matriz = malloc(N*sizeof(float*));
	//inicializo la matriz 
	for( i = 0; i<N; i++);
		matriz[i] = malloc(M*sizeof(float));

	for(j = 0; j<N-1; j++){
		for(i = 0; i<M-1; i++){
			matriz[j][i] = 0.0;
		}
	}

	



// para despues 

	u_futuro2[0] = 0.0;
	u_futuro2[N2-1] = 0.0;	
	
	for(j = 1; j<N2-1; i++){	
		for(i = 1; i<N2-1; i++){
			u_futuro2[g(i, j)] = u_inicial2[g(i,j)] + (pow(r,2)/2.0) * (u_inicial2[i+1] - 2.0 * u_inicial2[i] + u_inicial2[i-1]);
		}
	}
	
	for(j = 0; j<N2; j++){
		for(i = 0; i<N2; i++){
			u_pasado2[i] = u_inicial2[i];
		}
	}
	for(j = 0; j<N2; j++){	
		for(i = 0; i<N2; i++){
			u_presente2[i] = u_futuro2[i];
		}
	}
	
	scanf("%d", &t);
	
	for(k = 0; k<t; k++){
		for(j = 0; j<N2; j++){
			for(i = 1; i<N2-1; i++){
				u_futuro2[i] = (2.0*(1.0-pow(r,2)))*u_presente2[i] - u_pasado2[i] + (pow(r,2))*(u_presente2[i+1] +  u_presente2[i-1]);			
			}
			for(j = 0; i<N2; j++){
				for(i = 0; i<N2; i++){
					u_pasado2[i] = u_presente2[i];		
				}			
			}
			for(j = 0; j<N2; j++)			
				for(i = 0; i<N2; i++){
					u_presente2[i] = u_futuro2[i];
				}
			}		
		}
	}
	
		dat = fopen("datos1.txt", "w");
	if(!dat){
		printf("no sirve %s\n", "datos.txt");
	}
	for(i = 0; i<N; i++){
		fprintf(dat, "%f %f %f \n", x[i], u_presente1[i], u_inicial1[i]);
	}
}


}



