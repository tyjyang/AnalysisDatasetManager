#!/bin/bash

function getUserName {
    userName=$1
    repoName=$2
    if ! git ls-remote git@github.com:${userName}/${repoName}.git >& /dev/null; then
        echo "WARNING: Didn't find a repo at git@github.com:${userName}/${repoName}.git."
        echo "    falling back to git@github.com:kdlong/${repoName}.git."
        userName="kdlong"
    fi
}

if [[ $# -lt 1 ]]; then
    echo "Must pass the name of the sparse checkout config (in SparseCheckouts/<file>) as an argument"
    exit 1
fi
configFile=$1

if [[ $# -eq 2 ]]; then
    userName=$2
else
    userName=$USER
fi

repoName=AnalysisDatasetManager
path=$(git rev-parse --show-toplevel)
basepath=$(basename $path)
if [[ "$?" && "$basepath" == "$repoName" ]]; then
    cd $path
else
    mkdir $repoName
    cd $repoName
    git init
    getUserName $userName $repoName
    git remote add origin git@github.com:${userName}/${repoName}.git
fi
git config core.sparsecheckout true
getFile=false
if [[ ! -f "$configFile" ]]; then
    getUserName $userName $repoName
    wget https://raw.githubusercontent.com/${userName}/${repoName}/master/SparseCheckouts/${configFile}
    getFile=true
fi

cp ${configFile} .git/info/sparse-checkout

if [ "$getFile" = true ]; then
    rm ${configFile}

git read-tree --reset -u HEAD
