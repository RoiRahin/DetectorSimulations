rm *.angle.tst

GEO="Geometry         4_flower.geo.setup" 
sed -i "5s/.*/$GEO/" TestSource_NoBG.source

THETA=$(echo "scale=2 ; $RANDOM*90/32767" | bc)
beam="One.Beam                FarFieldPointSource $THETA 0." 
sed -i "21s/.*/$beam/" TestSource_NoBG.source
cosima -v 0  TestSource_NoBG.source > /dev/null
grep "^HTsim" test_burst.inc1.id1.sim | cut -d ";" -f 2-5 > 4_flower_test.angle.tst
rm test_burst.inc1.id1.sim

GEO="Geometry         5_flower.geo.setup" 
sed -i "5s/.*/$GEO/" TestSource_NoBG.source

cosima -v 0  TestSource_NoBG.source > /dev/null
grep "^HTsim" test_burst.inc1.id1.sim | cut -d ";" -f 2-5 > 5_flower_test.angle.tst
rm test_burst.inc1.id1.sim
