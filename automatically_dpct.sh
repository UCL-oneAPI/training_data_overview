# test folder iteration functionality
rootdir=$(cd $(dirname $0); pwd)
source /opt/intel/oneapi/setvars.sh
cd oneAPI-DirectProgramming
x=$(find . -name "*-cuda")
for folder in $x;do
    folder_name=${folder#*/}
    new_folder_name=${folder_name%'-cuda'}
    cd $rootdir
    pwd
    ./auto_dpct_script.sh $new_folder_name
    # ./auto_dpct_script.sh affine
done