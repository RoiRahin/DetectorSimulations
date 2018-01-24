#this is an auto simulator. It only works for BurstSource.source and very similar files
rm *.burst.out
width="Constant det_H 2.54"
sed -i "17s/.*/$width/" GTM_Single_Full.geo.setup

echo "now simulating for 1 inch width"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" BurstSource.source
		cosima -v 0  BurstSource.source > /dev/null
		grep "^HTsim" single_det_burst.inc1.id1.sim | wc -l >> single_det_1_count.burst.out
		grep "^HTsim" single_det_burst.inc1.id1.sim | cut -d ";" -f 5 > single_det_1_$THETA.burst.out
		rm single_det_burst.inc1.id1.sim
		let THETA=THETA+$1
done

width="Constant det_H 1.27"
sed -i "17s/.*/$width/" GTM_Single_Full.geo.setup

echo "now simulating for 0.5 inch width "
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" BurstSource.source
		cosima -v 0  BurstSource.source > /dev/null
		grep "^HTsim" single_det_burst.inc1.id1.sim | wc -l >> single_det_0.5_count.burst.out
		grep "^HTsim" single_det_burst.inc1.id1.sim | cut -d ";" -f 5 > single_det_0.5_$THETA.burst.out
		rm single_det_burst.inc1.id1.sim
		let THETA=THETA+$1
done

echo "now simulating for 1 inch width with background"
width="Constant det_H 2.54"
sed -i "17s/.*/$width/" GTM_Single_Full.geo.setup
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="Burst.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" Burst_And_Background.source
		cosima -v 0  Burst_And_Background.source > /dev/null
		grep "^HTsim" single_det_burst_and_background.inc1.id1.sim | wc -l >> sing_det_1_wb_count.burst.out
		grep "^HTsim" single_det_burst_and_background.inc1.id1.sim | cut -d ";" -f 5 > sing_det_1_wb_$THETA.burst.out
		rm single_det_burst_and_background.inc1.id1.sim
		let THETA=THETA+$1
done

width="Constant det_H 1.27"
sed -i "17s/.*/$width/" GTM_Single_Full.geo.setup

echo "now simulating for 0.5 inch width with background"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="Burst.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" Burst_And_Background.source
		cosima -v 0  Burst_And_Background.source > /dev/null
		grep "^HTsim" single_det_burst_and_background.inc1.id1.sim | wc -l >> sing_det_0.5_wb_count.burst.out
		grep "^HTsim" single_det_burst_and_background.inc1.id1.sim | cut -d ";" -f 5 > sing_det_0.5_wb_$THETA.burst.out
		rm single_det_burst_and_background.inc1.id1.sim
		let THETA=THETA+$1
done

