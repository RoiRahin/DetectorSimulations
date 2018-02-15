source /Local/MEGAlib/setup.sh

cp $SOURCEFILE /storage/ph_behar/roir/tempsource/temp_test_source_${job_num}.source
tmpdir=/storage/ph_behar/roir/temp_sim/${job_num}
mkdir $tmpdir
simfile="FFPS.FileName           $tmpdir/test_burst"
sed -i "15s|.*|$simfile|"  /storage/ph_behar/roir/tempsource/temp_test_source_${job_num}.source
beam="One.Beam                FarFieldPointSource $THETA $PHI" 
sed -i "21s/.*/$beam/"  /storage/ph_behar/roir/tempsource/temp_test_source_${job_num}.source

seed=$(od -An -N4 -t u < /dev/urandom)
cosima -v 0 -s $seed /storage/ph_behar/roir/tempsource/temp_test_source_${job_num}.source
grep "^HTsim" $tmpdir/test_burst.inc1.id1.sim | cut -d ";" -f 2-5 > /storage/ph_behar/roir/results/full_conf_test_${job_num}.angle.tst
rm $tmpdir/test_burst.inc1.id1.sim
out=$(python localize.py 10 1000 $THETA $PHI /storage/ph_behar/roir/results/full_conf_test_${job_num}.angle.tst)
flock -e -w200 mylockfile o >> /storage/ph_behar/roir/results/test_results
rm /storage/ph_behar/roir/tempsource/temp_test_source_${job_num}.source
rm -r $tmpdir
