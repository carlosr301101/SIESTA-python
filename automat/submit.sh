#!/bin/bash
#$ -cwd
#$ -pe openmp 2
##$ -pe mpi 12
#$ -N W.3layer_V15
#$ -q all.q
#$ -S /bin/bash

#set -x
export OMP_NUM_THREADS=$NSLOTS

#cd $SGE_O_WORKDIR

mamba activate

name=3layer
input=tungsten.bcc.fdf
output=${input%.fdf}.out

printf "#%10s	%15s	%15s\n" "${name}" "Energy(eV)" "Volume(Ang**3)" > ${name}.out

for ((j=1;j<10;j+=1)); do
	vv=$(echo "scale=4; 10" | bc -l)
	mm=$(echo "scale=4; $j*1.00/1" | bc -l)
	em=310
	kf=8
	kk=$(echo "scale=0; $kf/$mm" | bc -l)
	[ "$kk" -lt "1" ] && kk=1
	aa=$(echo "scale=4; 0.5/$mm" | bc -l)
	bb=$(echo "scale=4; 1.0/$mm" | bc -l)
	folder=${name}${j}
	mkdir ${folder}

#Esta seccion cambia el fichero de entrada
	python automat.py
	python modif.py
	cat salida.out >> listpos.out
##########################################

#Esta linea de comando cambia las cosas del input y los pone pa la carpeta 
	sed -e "s/MM/$mm/g" -e "s/EMEM/$em/g" -e "s/KFKF/$kf/g" -e "s/KK/$kk/g" -e "s/AA/$aa/g" -e "s/BB/$bb/g" ${input} > ${folder}/${input}
###########################################################################

	cp *.psf ${folder}
	cd ${folder}
	##mpirun -np $SLURM_NTASKS siesta < ${input} > ${output}
	#mpirun --mca btl vader,self -np $NSLOTS siesta-mpi-i2015.1 < ${input} > ${output}
	siesta-openmp < ${input} > ${output}
	Energy=`cat ${output} | awk '$1=="siesta:"&&$2=="Total"{print $4}'`
	Vol=`cat ${output} | awk '$1=="siesta:"&&$2=="Cell"&&$3=="volume"{print $5}'`
	printf " %10s	%15.4f	%15.4f\n" "$j" "$Energy" "$Vol"
	cd ..
done >> ${name}.out
exit 0;
