#!/usr/bin/env bash
fast="/home/students/bioinf/a/am467109/tools/pgor17-fasturec-2596d9ead945/pgor17-fasturec-2596d9ead945"
trees="/home/students/bioinf/a/am467109/cyanobacteria/sinice/trees_o_400.nwk"

${fast}/fasturec -G $trees -Z -e -a
