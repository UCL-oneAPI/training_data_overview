parent_dir=$(cd $(dirname $0); pwd)
cd scripts_output
mkdir $1
cd ../oneAPI-DirectProgramming
source /opt/intel/oneapi/setvars.sh

# cd oneAPI-DirectProgramming

function read_dir(){
current_dir=$(cd $(dirname $0); pwd) 
for file in `ls $1` 
do
if [ -d $1"/"$file ] 
    then
        read_dir $1"/"$file
    else
        if [ "${file##*.}"x = "cu"x ];then
            # dpct --in-root=. $file --out-root=${current_dir}/dpcpp
            dpct --in-root=. $file --out-root=${2}/scripts_output/${3}/dpcpp
            # echo /${2}/scripts_output/${3}/dpcpp
        fi
fi
done
} 

root_dir=$(cd $(dirname $0); pwd)
cd ${1}-cuda
echo $parent_dir
x=$(find . -name "*.cu")
workdir=$(cd $(dirname $0); pwd)
if [ -d "dpcpp" ];then
    echo "this project has been translated"
else
    # echo "no folder"
    # for i in $x;do 
    #     # echo "$i"
    #     dpct --in-root=. $i --out-root=dpcpp
    # done
    
    read_dir $workdir $parent_dir $1
fi

# cd $workdir
# testPath=../${1}-dpct
# if [[ ! -d "$testPath" ]]; then
#     echo "the dpct folder is not existed"
# else
#     cp -rvf ../${1}-dpct dpct-version
# fi

cd $parent_dir/scripts_output/${1}
cp -rvf ../../oneAPI-DirectProgramming/${1}-dpct dpct-version
# testPath=../${1}-dpct
# if [[ ! -d "$testPath" ]]; then
#     echo "the dpct folder is not existed"
# else
#     cp -rvf ../${1}-dpct dpct-version
# fi


cd $root_dir
pwd
