#!/bin/bash
#exec &> error.out
bin="test.bin"
cur_config=$1
test=$3
#echo $cur_config 
#echo $test

ret=`python3 ./release/update_exclude.py -f ./test.emProject`
if [[ $ret =~ "success" ]]
then
	echo "sync config ok"
else
	echo "sync config failed"
fi

cur_tag=`git describe --tags --always --abbrev=0 HEAD`

cur_comment=`git log --pretty="%h - %s" -n 1`
cur_comment=${cur_comment#* - }
echo $cur_comment
cur_comment=`echo $cur_comment | sed 's/[[:space:]]/@/g'`
#echo $cur_comment

current=`date "+%Y%m%d_%H%M%S_%N"`
current=${current:0:18}
echo $current

bat_version=`cat ./Battery/version`
echo $bat_version

gps_version=`cat ./GPS/version`
echo $gps_version
#echo $gps_version | sed 's/[[:space:]]/@/g'
gps_version=`echo $gps_version | sed 's/[[:space:]]/@/g'`
#echo $gps_version

type=""
paramfile=""

if [[ "Ov2f7_CI" =~ $cur_config ]]
then
    type="Newton22"
    paramfile="ParamList_Newton2.2.csv"
fi

if [[ "Ov2h7_CI" =~ $cur_config ]] 
then
    type="Newton23"
    paramfile="ParamList_Newton2.3.csv"
fi

if [[ "Ov3_CI" =~ $cur_config ]]
then 
    type="Newton30"
    paramfile="ParamList_Newton3.0.csv"
fi

if [[ "Iv2h7_CI" =~ $cur_config ]] 
then
    type="Euler20"
    paramfile="ParamList_Euler.csv"
fi

echo $type
echo $paramfile

echo "compile bin"
#compile_cmd="/usr/share/segger_embedded_studio_for_arm_6.30/bin/emBuild  -config "$cur_config" ./test.emProject -rebuild -echo -verbose"
compile_cmd="/usr/share/segger_embedded_studio_for_arm_6.30/bin/emBuild  -config "$cur_config" ./test.emProject -echo -verbose"
echo $compile_cmd

ret=`eval $compile_cmd > build.out` 
# for test ret=$bin
#echo $ret
ret=""

echo "compile done"
if [[ $ret =~ $bin ]]
then
	echo "compile bin ok"

	# close encrypt
	# echo "encrypt bin"
	# python3 ./test_encrypt/bin_encrypt.py "$cur_config($cur_tag).bin"
    # rm "$cur_config($cur_tag).bin"
    
    # # check if encrypt ok
    # if [ -e $cur_config"("$cur_tag")_encrypt.bin" ]; then
    #     echo "encrypt bin ok"
    # else
    #     echo "encrypt failed"
	#     exit 2
    # fi
    
	#echo "gen mav link"
	## genrate mav link
	#python2 ./pymavlink/gen_mav.py
	#echo "gen mav link ok"
	
	## checkout the companion repository
	#if [[ "Ov3_CI" =~ $cur_config ]]
	#then 
	#	echo "check repository"
	#	cd ./test_companion
	#	git checkout .
	#	git checkout onion3
	#	git pull origin onion3
	#	cd ..
	#fi
	
	#if [[ "Ov2h7_CI" =~ $cur_config ]] || [[ "Ov2f7_CI" =~ $cur_config ]] || [[ "Iv2h7_CI" =~ $cur_config ]] 
	#then 
	#	echo "check repository"
	#	cd ./test_companion
	#	git checkout .
	#	git checkout pi2
	#	git pull origin pi2
	#	cd ..
	#fi
	
	# genrate test companion
	#mv ./pymavlink/out/test.py ./test_companion/test.py -f

	echo "gen test companion ok"
	# get companion version
	test_companion_version=`cat ./test_companion/GIT_COMMIT_ID`
	
    mkdir -p FC
    #mv $cur_config"("$cur_tag")_encrypt.bin" ./FC/test.bin
	mv $cur_config"("$cur_tag").bin" ./FC/test.bin

    mkdir -p ParamList
    cp ./test_param/$paramfile ./ParamList/ParamList.csv

	# output zip
    if [ -e $cur_config".zip" ]; then
	    echo "find old zip,delete it"
	    rm $cur_config".zip"
    fi

	echo "zip all"
	zip -r $cur_config".zip" ./test_companion/ -x "./test_companion/.git" "./test_companion/.gitignore" "./test_companion/readme.txt" "./test_companion/release.sh" "./test_companion/.gitattributes" 
	if [[ "Ov3_CI" =~ $cur_config ]]
	then
		zip -g $cur_config".zip" ./GPS/GPS.bin
	else
		zip -g $cur_config".zip" ./Battery/battery.bin ./GPS/GPS.bin 
	fi
	# add param file
	zip -g $cur_config".zip" ./ParamList/ParamList.csv -m
    # add firmware
    zip -g $cur_config".zip" ./FC/test.bin -m
	echo "zip all ok"
	
	echo "push new firmware"
	# push zip
    
    if [ ! -n "$test" ] ;then
        if [[ "Ov2h7_CI" =~ $cur_config ]]
        then
            ret=`python3 ./release/push.py -t "Newton23" -v $current -f $cur_tag -b $bat_version -g $gps_version -c $test_companion_version -p $cur_tag -r $cur_comment -o $cur_config".zip" `

			ret=`python3 ./release/push.py -t "Newton24" -v $current -f $cur_tag -b $bat_version -g $gps_version -c $test_companion_version -p $cur_tag -r $cur_comment -o $cur_config".zip" `	

		elif [[ "Ov3_CI" =~ $cur_config ]]
		then
			ret=`python3 ./release/push.py -t $type      -v $current -f $cur_tag                 -g $gps_version -c $test_companion_version -p $cur_tag -r $cur_comment -o $cur_config".zip" `
        else
            ret=`python3 ./release/push.py -t $type      -v $current -f $cur_tag -b $bat_version -g $gps_version -c $test_companion_version -p $cur_tag -r $cur_comment -o $cur_config".zip" `
        fi
    else
        echo "test no push"
        ret="test"
    fi

    echo $ret
    if [[ $ret =~ "success" ]]
    then
        echo "push new firmware ok"
    else
        echo "push new firmware failed"
    fi

	echo "report CI message"
	python3 ./release/push.py -t $type -v $current -e ./error.out -m ./build.out -s 1

else
	echo "compile bin error"
	echo "no bin release"
	echo "report error message"
	python3 ./release/push.py -t $type -v $current -e ./error.out -m ./build.out -s 0
	exit 1
fi



