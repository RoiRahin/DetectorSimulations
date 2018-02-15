
for ((i=0; i<=$2; i++)) do
	qsub -V -v RUN_NUM=$1,job_num=$i,SOURCEFILE=$3 -o /storage/ph_behar/roir/outerr -e /storage/ph_behar/roir/outerr -l mem=1gb,vmem=2gb -q S remote_simulate.sh
	sleep 2
done
