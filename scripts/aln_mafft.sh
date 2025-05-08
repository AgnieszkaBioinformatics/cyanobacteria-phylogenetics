#!/usr/bin/env bash
#DIR="./genomika"
source ~/miniconda3/etc/profile.d/conda.sh
conda activate maft
DIR="/home/students/bioinf/a/am467109/cyanobacteria/sinice/gene_families/orthologs"

for file in ${DIR}/*fasta; do
        mafft --auto "$file" > "${file}_msa"
done
