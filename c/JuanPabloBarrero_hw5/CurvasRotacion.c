#include <time.h> 
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float likelihood(float *yobs,float *ymodel);
float *model(float *Robs, float mb, float md, float mh);

int main(){
	int N = 301;		
	//Declaro los vectores	
	float *R = malloc(N*sizeof(float));
	float *v = malloc(N*sizeof(float));
	float *mb_walk = malloc(N*sizeof(float));
	float *md_walk = malloc(N*sizeof(float));
	float *mh_walk = malloc(N*sizeof(float));
	float *l_walk = malloc(N*sizeof(float));
	float *vinicial = malloc(N*sizeof(float));
	float *vprima = malloc(N*sizeof(float));
	float l_prima;
	float l_inicial;
	float mb_prima;
	float mh_prima;
	float md_prima;
	float db = 0.1;
	float dd = 1;
	float dh = 3;
	//inicializo los vectores (eliminando la información que habia antes)	
	int i;
	for(i = 0; i<N; i++){
		R[i] = 0.0;
		v[i] = 0.0;
		mb_walk[i] = 0.0;
		md_walk[i] = 0.0;
		mh_walk[i] = 0.0;		
		l_walk[i] = 0.0;
		vinicial[i] = 0.0;
		vprima[i] = 0.0;
	}
	
	mb_walk[0] = 300;
	md_walk[0] = 7000;
	mh_walk[0] = 10000;
 		
	
	// Leo el punto dat
	FILE *dat;
	
	dat = fopen("RadialVelocities.dat", "r");
		
	for(i = 0; i<N; i++){	
		fscanf(dat,"%f %f", &x[i], &y[i]);
	}
	fclose(dat);
	
	//Pongo las condiciones inicales
	vinicial = model(R, mb_walk[0], md_walk[0], mh_walk[0]);
	l_walk[0] = likelihood(v, vinicial);	

	//Uso el metodo para avanzar en el tiempo 
	for(i = 0; i<N; i++){
		float mb_prima = mb_walk[i] + db*((rand()/RAND_MAX)-0.5);
		float md_prima = md_walk[i] + dd*((rand()/RAND_MAX)-0.5);
		float mh_prima = mh_walk[i] + dh*((rand()/RAND_MAX)-0.5);
		
		vinicial = model(R, mb_walk[i], md_walk[i], mh_walk[i]);
		vprima = model(R, mb_prime, md_prime, mh_prime);
		
		l_prima = likelihood(v, vprima);
		l_inicial = likelihood(v, vinicial);
		
		float a = l_prima/l_inicial;
		if(a >= 1.0){
			mb_walk[i+1] = mb_prima;
			md_walk[i+1] = md_prima;
			mh_walk[i+1] = mh_prima;
			l_walk[i+1] = l_prima;
		}
		else{
			float b = rand()/RAND_MAX;
			if(b<=a){
				mb_walk[i+1] = mb_prima;
				md_walk[i+1] = md_prima;
				mh_walk[i+1] = mh_prima;
				l_walk[i+1] = l_prima;
			}
			else{
				mb_walk[i+1] = mb_walk[i];
				md_walk[i+1] = md_walk[i];
				mh_walk[i+1] = mh_walk[i];
				l_walk[i+1] = l_inicial; 
			}		 
		}
	}	
	
	//Creo las variables para comparar los valores de las masas con el likelihood mas alto 
	float lc = l_walk[0];
	float mbc;
	float mdc;
	float mhc;
	
	for(i = 0; i<N; i++){
		if(lc < l_walk[i+1]){
			lc = l_walk[i+1];
			mbc = mb_walk[i+1];
			mdc = md_walk[i+1];
			mhc = mh_walk[i+1];	
		}
	}

	// Impresión en consola de los parametros encontrados 
	
	printf ("%s %f %s %f %s %f \n", "La masa del bulbo es", mbc, "La del disco es", mdc, "y la masa del h es", mhc )
	
	
}

//creo la función likelihood y la inicializo como se vio en clase
float likelihood(float *yobs,float *ymodel){
	int N = 301;	
	int i;
	float chic = 0.0;	
	for(i = 0; i<N; i++){
		chic += (1.0/2.0)*((yobs - ymodel)**2);
	}
	
	return exp(-chic);	
} 

//Creo la función de potencial dada en la guía.
float *model(float *Robs, float mb, float md, float mh){
	int i;
	int bb = 0.2497;
	int bd = 5.16;
	int ad = 0.3105;
	int ah = 64.3;
	int N = 301;
	float *v = malloc(N*sizeof(float)); 
	for( i = 0; i<N; i++){
		v[i] = ((pow(mb, 0.5)*Robs[i])/(pow(pow(Robs[i], 2.0) + pow(bb,2.0), 3.0/4.0))) + ((pow(md, 0.5)*Robs[i])/(pow(pow(Robs[i], 2.0) + pow(bd + ad,2.0), 3.0/4.0))) + ((pow(mh, 0.5)/(pow(pow(Robs[i], 2.0) + pow(ah,2.0), 1.0/4.0)));
	} 
	return v;
}












