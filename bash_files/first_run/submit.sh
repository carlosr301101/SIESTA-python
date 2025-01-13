#!/bin/bash
#$ -cwd
#$ -pe openmp 2
#$ -N W.bcc.a1.latt
#$ -q all.q
#$ -S /bin/bash

#set -x
export OMP_NUM_THREADS=$NSLOTS

cd $SGE_O_WORKDIR

name=latt
input=tungsten.bcc.fdf
output=${input%.fdf}.out

printf "#%10s	%15s	%15s\n" "${name}" "Energy(eV)" "Volume(Ang**3)" > ${name}.out

for ((j=50;j<=150;j+=1)); do
	i=$(echo "scale=2; $j/100" | bc -l)
	#k=$(echo "scale=0; 15/$i" | bc -l)
	k=12
	#k=15
	coff=310
	folder=${name}${i}
	mkdir ${folder}
	sed -e "s/MM/$i/g" -e "s/KK/$k/g" -e "s/COFF/$coff/g" ${input} > ${folder}/${input}
	cp *.psf ${folder}
	cd ${folder}
	###mpirun -np $NSLOTS siesta < ${input} > ${output}
	siesta-openmp < ${input} > ${output}
	Energy=`cat ${output} | awk '$1=="siesta:"&&$2=="Total"{print $4}'`
	#E=$(echo "$Energy+578.0297"| bc -l)
	Vol=`cat ${output} | awk '$1=="siesta:"&&$2=="Cell"&&$3=="volume"{print $5}'`
	printf " %10s	%15.4f	%15.4f\n" "$i" "$Energy" "$Vol"
	cd ..
done >> ${name}.out

exit 0;
