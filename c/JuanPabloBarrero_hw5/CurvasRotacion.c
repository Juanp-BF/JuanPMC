#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float likelyhood(float *yobs,float *ymodel);
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
	float vinicial;
	float vprima;
	float l_prima;
	float l_inicial;
	//inicializo los vectores (eliminando la información que habia antes)	
	int i;
	for(i = 0; i<N; i++){
		x[i] = 0.0;
		y[i] = 0.0;
		mb_walk[i] = 0.0;
		md_walk[i] = 0.0;
		mh_walk[i] = 0.0;		
		l_walk[i] = 0.0;
	}
	
	mb_walk[0] = 250;
	md_walk[0] = 700;
	mh_walk[0] = 1000;
 		
	
	FILE *dat;
	
	dat = fopen("RadialVelocities.dat", "r");
		
	for(i = 0; i<N; i++){	
		fscanf(dat,"%f %f", &x[i], &y[i]);
	}
	fclose(dat);

	vinicial = model(R, mb_walk[0], md_walk[0], mh_walk[0]);
	l_walk[0] = likelihood(v, vinicial);	

	for(i = 0; i<N; i++){
		float mb_prima = mb_walk[i] + db*((rand()/RAND_MAX)-0.5);
		float md_prima = md_walk[i] + dd*((rand()/RAND_MAX)-0.5);
		float mh_prima = mh_walk[i] + dh*((rand()/RAND_MAX)-0.5);
		
		vinicial = model(R, mb_walk[i], md_walk[i], mh_walk[i]);
		vprima = model(R, mb_prime, md_prime, mh_prime);
		
		l_prima = likelihood(v, vprima);
		l_inicial = likelihood(v, vinicial);
		
		float alpha = l_prima/l_inicial;
		if(alpha >= 1.0){
			mb_walk[i+1] = mb_prima;
			md_walk[i+1] = md_prima;
			mh_walk[i+1] = mh_prima;
			l_walk[i+1] = l_prima;
		}
		else{
			float beta = rand()/RAND_MAX;
			if(beta<=alpha){
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
	
}


float likelihood(float *yobs,float *ymodel){
	int N = 301;	
	int i;
	float chic = 0.0;	
	for(i = 0; i<N; i++){
		chic += (1.0/2.0)*((yobs - ymodel)**2);
	}
	
	return exp(-chic);	
} 

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












