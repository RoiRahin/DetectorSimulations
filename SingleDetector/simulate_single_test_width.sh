#this is an auto simulator. It only works for TestSource2.source and very similar files
rm single_det2_32_1.out
rm single_det2_662_1.out
rm single_det2_662_0.5.out
rm single_det2_32_0.5.out
spec="One.Spectrum            Mono  32"
sed -i "22s/.*/$spec/" TestSource2.source
width="Constant det_H 2.54"
sed -i "17s/.*/$width/" GTM_Single_Test_Width.geo.setup

echo "now simulating for 32 KeV 1 inch width"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" TestSource2.source
		cosima -v 0  TestSource2.source > /dev/null
		grep "^HTsim" single_det2.inc1.id1.sim | wc -l >> single_det2_32_1.out
		rm single_det2.inc1.id1.sim
		let THETA=THETA+$1
done

spec="One.Spectrum            Mono  662"
sed -i "22s/.*/$spec/" TestSource2.source

echo "now simulating for 662 KeV 1 inch width "
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" TestSource2.source
		cosima -v 0  TestSource2.source > /dev/null
		grep "^HTsim" single_det2.inc1.id1.sim | wc -l >> single_det2_662_1.out
		rm single_det2.inc1.id1.sim
		let THETA=THETA+$1
done

width="Constant det_H 1.27"
sed -i "17s/.*/$width/" GTM_Single_Test_Width.geo.setup

echo "now simulating for 662 KeV 0.5 inch width "
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" TestSource2.source
		cosima -v 0  TestSource2.source > /dev/null
		grep "^HTsim" single_det2.inc1.id1.sim | wc -l >> single_det2_662_0.5.out
		rm single_det2.inc1.id1.sim
		let THETA=THETA+$1
done

echo "now simulating for 32 KeV 0.5 inch width"
spec="One.Spectrum            Mono  32"
sed -i "22s/.*/$spec/" TestSource2.source
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" TestSource2.source
		cosima -v 0  TestSource2.source > /dev/null
		grep "^HTsim" single_det2.inc1.id1.sim | wc -l >> single_det2_32_0.5.out
		rm single_det2.inc1.id1.sim
		let THETA=THETA+$1
done
