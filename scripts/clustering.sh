#!/usr/bin/env bash
source ~/miniconda3/etc/profile.d/conda.sh
conda activate mmseqs

DIR="/home/students/bioinf/a/am467109/cyanobacteria/sinice"

mmseqs easy-cluster ${DIR}/combined.fasta clusterRes tmp
