#this is an auto simulator. It only works for BurstSource.source and very similar files
rm *.background.out

GEO="Geometry         4_flower.geo.setup" 
sed -i "5s/.*/$GEO/" BackgroundSource.source
echo "now simulating for 4-flower"
cosima -v 0  BackgroundSource.source > /dev/null
grep "^HTsim" Noise.inc1.id1.sim | cut -d ";" -f 2-5 > 4_flower.background.out
rm Noise.inc1.id1.sim

GEO="Geometry         5_flower.geo.setup" 
sed -i "5s/.*/$GEO/" BackgroundSource.source
echo "now simulating for 5-flower"
cosima -v 0  BackgroundSource.source > /dev/null
grep "^HTsim" Noise.inc1.id1.sim | cut -d ";" -f 2-5 > 5_flower.background.out
rm Noise.inc1.id1.sim
