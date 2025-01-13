#!/bin/bash
#$ -cwd
#$ -pe openmp 4
##$ -pe mpi 12
#$ -N W.7l.vacc
#$ -q all.q
#$ -S /bin/bash

#set -x
export OMP_NUM_THREADS=$NSLOTS

cd $SGE_O_WORKDIR

name=vacuum
input=tungsten.bcc.fdf
output=${input%.fdf}.out

printf "#%10s	%15s	%15s\n" "${name}" "Energy(eV)" "Volume(Ang**3)" > ${name}.out

for ((j=5;j<=11;j+=1)); do
	vv=$(echo "scale=4; ($j-3)*1.00/1" | bc -l)
	mm=$(echo "scale=4; $j*1.00/1" | bc -l)
	em=310
	kf=4
	kk=$(echo "scale=0; $kf/$mm" | bc -l)
	[ "$kk" -lt "1" ] && kk=1
	aa=$(echo "scale=4; 0.5/$mm" | bc -l)
	bb=$(echo "scale=4; 1.0/$mm" | bc -l)
	cc=$(echo "scale=4; 1.5/$mm" | bc -l)
	dd=$(echo "scale=4; 2.0/$mm" | bc -l)
	ee=$(echo "scale=4; 2.5/$mm" | bc -l)
	ff=$(echo "scale=4; 3.0/$mm" | bc -l)
	folder=${name}${j}
	mkdir ${folder}
	sed -e "s/MM/$mm/g" -e "s/EMEM/$em/g" -e "s/KFKF/$kf/g" -e "s/KK/$kk/g" -e "s/AA/$aa/g" -e "s/BB/$bb/g" -e "s/CC/$cc/g" -e "s/DD/$dd/g" \
		-e "s/EE/$ee/g" -e "s/FF/$ff/g" ${input} > ${folder}/${input}
	cp *.psf ${folder}
	cd ${folder}
	##mpirun -np $SLURM_NTASKS siesta < ${input} > ${output}
	#mpirun --mca btl vader,self -np $NSLOTS siesta-mpi-i2015.1 < ${input} > ${output}
	siesta-openmp < ${input} > ${output}
	Energy=`cat ${output} | awk '$1=="siesta:"&&$2=="Total"{print $4}'`
	Vol=`cat ${output} | awk '$1=="siesta:"&&$2=="Cell"&&$3=="volume"{print $5}'`
	printf " %10s	%15.4f	%15.4f\n" "$vv" "$Energy" "$Vol"
	cd ..
done >> ${name}.out
exit 0;
