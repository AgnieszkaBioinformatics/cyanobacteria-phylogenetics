#!/usr/bin/env bash
DIR="/home/students/bioinf/a/am467109/cyanobacteria"
SEQ="${DIR}/wszystkie_sekwencje2"

cat ${SEQ}/*faa > ${DIR}/combined.fasta
