#this is an auto simulator. It only works for TestSource.source and very similar files
spec="One.Spectrum            Mono  32"
sed -i "22s/.*/$spec/" TestSource.source
GEO="Geometry         GTM_Single_No_Silicon.geo.setup " 
sed -i "5s/.*/$GEO/" TestSource.source

echo "now simulating for 32 KeV no silicon"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" TestSource.source
		cosima -v 0  TestSource.source > /dev/null
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
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" TestSource.source
		cosima -v 0  TestSource.source > /dev/null
		grep "^HTsim" single_det.inc1.id1.sim | wc -l >>  single_det_662.out
		rm single_det.inc1.id1.sim
		let THETA=THETA+$1
done

