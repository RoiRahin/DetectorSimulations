source /Local/MEGAlib/setup.sh

cp $SOURCEFILE /storage/ph_behar/roir/tempsource/temp_source_${job_num}.source
tmpdir=/storage/ph_behar/roir/temp_sim/${job_num}
mkdir $tmpdir
simfile="FFPS.FileName           $tmpdir/flower_burst"
sed -i "15s|.*|$simfile|"  /storage/ph_behar/roir/tempsource/temp_source_${job_num}.source
for ((i=1; i<=$RUN_NUM; i++)) do
	beam="One.Beam                FarFieldPointSource $THETA $PHI" 
	sed -i "21s/.*/$beam/"  /storage/ph_behar/roir/tempsource/temp_source_${job_num}.source
	cosima -v 0 -s $RANDOM /storage/ph_behar/roir/tempsource/temp_source_${job_num}.source
	grep "^HTsim" $tmpdir/flower_burst.inc1.id1.sim | cut -d ";" -f 2-5 > /storage/ph_behar/roir/results/5_flower_${THETA}_$PHI.burst.out
	rm $tmpdir/flower_burst.inc1.id1.sim
	let PHI=$PHI+$STEP
	if [  $PHI -ge 360 ] || [  $THETA -eq 0 ]
	then
		if [  $THETA -ge 90 ]
		then
			break
		fi
		let PHI=0
		let THETA=$THETA+$STEP
	fi
done

rm  /storage/ph_behar/roir/tempsource/temp_source_${job_num}.source
rm -r $tmpdir
