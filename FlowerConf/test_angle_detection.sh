rm *.angle.tst

GEO="Geometry         ${1}_flower.geo.setup" 
sed -i "5s/.*/$GEO/" TestSource.source

THETA=$(echo "scale=2 ; $RANDOM*90/32767" | bc)
beam="One.Beam                FarFieldPointSource $THETA 0." 
sed -i "21s/.*/$beam/" TestSource.source
cosima -v 0  TestSource.source > /dev/null
grep "^HTsim" test_burst.inc1.id1.sim | cut -d ";" -f 2-5 > ${1}_flower_test.angle.tst
rm test_burst.inc1.id1.sim
