local mydir=${0:a:h}
export PROJECT_PATH=$mydir/make_alias.sh

if [[ ! -e $PROJECT_PATH ]]
then
    echo "Creating make_alias.sh file."
    touch $PROJECT_PATH
fi

function edit_projects() {
    open $PROJECT_PATH
}

projs=()
function add_project() {
    if [ $# -eq 0 ]; then
        echo "No arguments provided."
        return 1
    fi

    local name=$1

    if [ $# -eq 1 ]; then
        local dest=$(pwd)
    elif [[ $2 == \/* ]]; then
        local dest=$2
    else
        local dest="~/${2}"
    fi

    local cmd="alias $name='cd $dest'"
    eval $cmd

    projs+=($name:$dest)

    if [ $# -eq 1 ]; then
        echo "Adding alias for $name"
        echo "add_project $name $dest" >> $PROJECT_PATH
    fi
}

function projects() {
    local len=${#projs[@]}
    if [ "$len" -eq 0 ]; then
        echo "There are no projects yet. Please add with 'add_project' function."
        return 1
    fi

    for i in $projs
    do
        echo $i
    done
}

# Sourcing the file to create the alias for navigation
source $PROJECT_PATH
