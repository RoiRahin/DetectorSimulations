source /Local/MEGAlib/setup.sh

cp $SOURCEFILE /storage/ph_behar/roir/tempsource/temp_source_test_${job_num}.source
tmpdir=/storage/ph_behar/roir/temp_sim/${job_num}
mkdir $tmpdir
simfile="FFPS.FileName           $tmpdir/test_burst"
for ((i=1; i<=$RUN_NUM; i++)) do
	cosima -v 0 -S $RANDOM /storage/ph_behar/roir/tempsource/temp_source_test_${job_num}.source
	grep "^HTsim" $tmpdir/test_burst.inc1.id1.sim | cut -d ";" -f 2-5 > full_conf_test_${job_num}_$i.angle.tst
	rm $tmpdir/test_burst.inc1.id1.sim
done
rm  /storage/ph_behar/roir/tempsource/temp_source_test_${job_num}.source
rm -r $tmpdir
