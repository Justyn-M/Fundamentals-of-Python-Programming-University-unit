#!/bin/bash

exp_dir = dosage`date "+%Y-%m-%d+%H:%M:%S"`

mkdir $exp_dir
cp dosagebase.py $exp_dir
cp dosage_sweep.sh $exp_dir
cd $exp_dir

low_int=$1
hi_int=$2
step_int=$3
low_dose=$4
hi_dose=$5
step_dose=$6

echo 'Parameters are: '
echo 'Interval : ' $low_int $hi_int $step_int
echo 'Dosage : ' $low_dose $hi_dose $step_dose

for i in `seq $low_int $step_int $hi_int`;
do
	for d in `seq $low_dose $step_dose $hi_dose`;
	do 
		echo 'Experiment: ' $i $d
		outfile = 'dosage_I'$i'_D'$d'.txt'
		python3 dosagebase.py $i $d > $outfile
	done
done
