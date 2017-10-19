mkdir Tolima 

cd Tolima	

cp ../DatosTolima.dat .
	
cp ../plotsTolima.py .

grep -i March DatosTolima.dat | awk '{print $(NF-2) " " $NF}' > DatosMarzo.txt

awk '{print $(NF-2) " " $NF}' DatosTolima.dat| tail -n +2  > GRF_VS_EQ.txt

python plotsTolima.py

rm -r DatosTolima.dat
