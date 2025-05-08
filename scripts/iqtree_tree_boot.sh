#!/usr/bin/env bash
DIR="/home/students/bioinf/a/am467109/cyanobacteria/sinice/msa/o_boot"
source ~/miniconda3/etc/profile.d/conda.sh
conda activate iqtree

for file in ${DIR}/*fasta_msa
do
	iqtree -T 5 -s "$file" -b 50
done

