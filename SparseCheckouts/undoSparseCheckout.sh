echo "*" > .git/info/sparse-checkout
git config core.sparsecheckout true
git read-tree --reset -u HEAD
rm .git/info/sparse-checkout
git config core.sparsecheckout false
