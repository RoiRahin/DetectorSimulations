for ((i=1; i<=$3; i++)) do
	qsub -V -v THETA=$1,PHI=$2,job_num=$i,SOURCEFILE=TestSource.source -o /storage/ph_behar/roir/outerr -e /storage/ph_behar/roir/outerr -l mem=1gb,vmem=2gb -q S run_test.sh
	sleep 2
done