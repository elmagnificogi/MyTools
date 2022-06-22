bin="test.bin"
cur_path=$1
#echo $cur_path 
cur_tag=`git describe --tags --always --abbrev=0 HEAD`

cur_config="test_config"
compile_cmd="/usr/share/segger_embedded_studio_for_arm_6.30/bin/emBuild  -config "$cur_config" ./test.emProject -rebuild -echo -verbose"
#echo $compile_cmd
ret=`eval $compile_cmd`
#echo $ret
if [[ $ret =~ $bin ]]
then
	echo "release bin"
	# push and excrypt
	python3 ../test_encrypt/bin_encrypt.py $cur_config"("$cur_tag").bin"
	python3 push.py
else
	echo "no bin release"
fi