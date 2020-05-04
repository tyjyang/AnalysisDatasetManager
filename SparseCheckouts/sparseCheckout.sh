#!/bin/bash
set -x
set -e

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

repName=AnalysisDatasetManager
mkdir $repoName; cd $repoName
git init
if !git ls-remote git@github.com:${userName}/VVAnalysis.git >& /dev/null; then
    echo "WARNING: Didn't find a repo at git@github.com:${userName}/VVAnalysis.git."
    echo "    falling back to git@github.com:kdlong/VVAnalysis.git."
    userName="kdlong"
fi
git remote add origin git@github.com:${userName}/VVAnalysis.git
git config core.sparsecheckout true
wget origin https://raw.githubusercontent.com/${userName}/VVAnalysis/master/SparseCheckouts/${configFile}
cp ${configFile} .git/info/sparse-checkout
git pull origin master
