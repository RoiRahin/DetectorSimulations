PHI=0
THETA=0
i=0
PHISTEP=$1*$2
while [  $THETA -le 90 ]; do
	qsub -V -v STEP=$1,RUN_NUM=$2,THETA=$THETA,PHI=$PHI,job_num=$i,SOURCEFILE=$3 -o /storage/ph_behar/roir/outerr -e /storage/ph_behar/roir/outerr -l mem=1gb,vmem=2gb -q S remote_simulate.sh
	sleep 2
	let i=$i+1
	let PHI=$PHI+$PHISTEP
	if [  $THETA -eq 0 ]
	then
		let THETA=$THETA+$1
		let PHI=$PHI-$1
	fi
	if [  $PHI -ge 360 ]
	then
		let PHI=$PHI-360
		let THETA=$THETA+$1
	fi
done