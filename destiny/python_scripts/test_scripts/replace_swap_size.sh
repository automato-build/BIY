#!/bin/sh

# search_result=$(grep '# CONF_SWAPSIZE' TestSwapFile)
# echo $search_result

# remove comment if there is a comment
sed -i '/CONF_SWAPSIZE=100/s/^#*\s*//g' TestSwapFile
sed -i 's/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=4096/' file.txt