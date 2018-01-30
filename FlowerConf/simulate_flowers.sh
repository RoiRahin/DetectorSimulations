#this is an auto simulator. It only works for BurstSource.source and very similar files
rm *.burst.out

GEO="Geometry         4_flower.geo.setup" 
sed -i "5s/.*/$GEO/" BurstSource.source
echo "now simulating for 4-flower"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" BurstSource.source
		cosima -v 0  BurstSource.source > /dev/null
		grep "^HTsim" flower_burst.inc1.id1.sim | wc -l >> 4_flower.burst.count
		grep "^HTsim" flower_burst.inc1.id1.sim | cut -d ";" -f 2-5 > 4_flower_$THETA.burst.out
		rm flower_burst.inc1.id1.sim
		let THETA=THETA+$1
done

GEO="Geometry         5_flower.geo.setup" 
sed -i "5s/.*/$GEO/" BurstSource.source
echo "now simulating for 5-flower"
THETA=0
while [  $THETA -le 90 ]; do
	echo "now simulating for theta = $THETA"
		beam="One.Beam                FarFieldPointSource $THETA 0." 
		sed -i "21s/.*/$beam/" BurstSource.source
		cosima -v 0  BurstSource.source > /dev/null
		grep "^HTsim" flower_burst.inc1.id1.sim | wc -l >> 5_flower.burst.count
		grep "^HTsim" flower_burst.inc1.id1.sim | cut -d ";" -f 2-5 > 5_flower_$THETA.burst.out
		rm flower_burst.inc1.id1.sim
		let THETA=THETA+$1
done

