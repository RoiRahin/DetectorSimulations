#this is an auto simulator. It only works for TestSource.source and very similar files
rm single_det_32_sil.out
rm single_det_662_sil.out
rm single_det_32.out
rm single_det_662.out
rm single_det_32_wall.out
rm single_det_662_wall.out
rm single_det_32_rotate_source.out
rm single_det_662_rotate_source.out

GEO="Geometry         GTM_Single_Silicon.geo.setup" 
sed -i "5s/.*/$GEO/" TestSource.source
spec="One.Spectrum            Mono  32"
sed -i "22s/.*/$spec/" TestSource.source
beam="One.Beam                FarFieldPointSource 0. 0." 
sed -i "21s/.*/$beam/" TestSource.source

echo "now simulating for 32 KeV with silicon"

THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	geo="DetectorVolume.Rotation 0. $THETA 0." 
	sed -i "39s/.*/$geo/" GTM_Single_Silicon.geo.setup
	cosima -v 1  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_32_sil.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done

spec="One.Spectrum            Mono  662"
sed -i "22s/.*/$spec/" TestSource.source

echo "now simulating for 662 KeV with silicon"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	geo="DetectorVolume.Rotation 0. $THETA 0." 
	sed -i "39s/.*/$geo/" GTM_Single_Silicon.geo.setup
	cosima -v 0  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_662_sil.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done

GEO="Geometry         GTM_Single_No_Silicon.geo.setup" 
sed -i "5s/.*/$GEO/" TestSource.source
spec="One.Spectrum            Mono  32"
sed -i "22s/.*/$spec/" TestSource.source

echo "now simulating for 32 KeV no silicon"

THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	geo="DetCyl.Rotation 0. $THETA 0." 
	sed -i "41s/.*/$geo/" GTM_Single_No_Silicon.geo.setup
	cosima -v 1  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_32.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done

spec="One.Spectrum            Mono  662"
sed -i "22s/.*/$spec/" TestSource.source

echo "now simulating for 662 KeV no silicon"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	geo="DetCyl.Rotation 0. $THETA 0." 
	sed -i "41s/.*/$geo/" GTM_Single_No_Silicon.geo.setup
	cosima -v 0  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_662.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done



GEO="Geometry         GTM_Single_wall.geo.setup" 
sed -i "5s/.*/$GEO/" TestSource.source
spec="One.Spectrum            Mono  32"
sed -i "22s/.*/$spec/" TestSource.source

echo "now simulating for 32 KeV with wall"

THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	geo="DetectorVolume.Rotation 0. $THETA 0." 
	sed -i "39s/.*/$geo/" GTM_Single_wall.geo.setup
	cosima -v 1  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_32_wall.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done

spec="One.Spectrum            Mono  662"
sed -i "22s/.*/$spec/" TestSource.source

echo "now simulating for 662 KeV with wall"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	geo="DetectorVolume.Rotation 0. $THETA 0." 
	sed -i "39s/.*/$geo/" GTM_Single_wall.geo.setup
	cosima -v 0  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_662_wall.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done

spec="One.Spectrum            Mono  32"
sed -i "22s/.*/$spec/" TestSource.source
geo="DetectorVolume.Rotation 0. 0. 0." 
sed -i "39s/.*/$geo/" GTM_Single_wall.geo.setup
echo "now simulating for 32 KeV while changing source angle"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	beam="One.Beam                FarFieldPointSource $THETA 0." 
	sed -i "21s/.*/$beam/" TestSource.source
	cosima -v 0  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_32_rotate_source.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done

spec="One.Spectrum            Mono  662"
sed -i "22s/.*/$spec/" TestSource.source

echo "now simulating for 662 KeV while changing source angle"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
	beam="One.Beam                FarFieldPointSource $THETA 0." 
	sed -i "21s/.*/$beam/" TestSource.source
	cosima -v 0  TestSource.source > /dev/null
	grep "^HTsim" single_det.inc1.id1.sim | wc -l >> single_det_662_rotate_source.out
	rm single_det.inc1.id1.sim
	let THETA=THETA+$1
done

