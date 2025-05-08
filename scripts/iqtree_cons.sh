#!/usr/bin/env bash
DIR="/home/students/bioinf/a/am467109/cyanobacteria/sinice"
source ~/miniconda3/etc/profile.d/conda.sh
conda activate iqtree

iqtree -nt 10 -con ${DIR}/all_paralogs.nwk -minsup 0.5 -pre ${DIR}/consensus/iqtree_paralogs
