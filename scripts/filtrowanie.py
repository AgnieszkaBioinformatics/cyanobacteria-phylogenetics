from Bio import SeqIO
import glob
import re
from collections import Counter
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def read_in_clusters(file): # dict[cluster: seq_6ids]
    result = dict()
    with open(file, "r") as f:
        for line in f:
            cluster = line.split("\t")[0]
            member = line.split("\t")[1].strip()
            if cluster not in result:
                result[cluster] = []
                result[cluster].append(member)
            else:
                result[cluster].append(member)
    return result


def species_info(file, mags = None):    # dict[seq_id: organism_name]
    if mags:
        species = mags
    else:
        species = dict()

    for record in SeqIO.parse(file, "fasta"):
        match = re.search(r"\[(.+?)\]", record.description)
        if match:
            match = match.group(1)
            species[record.id] = match
    return species


def filtering_clusters(clusters, species, min_size, paralogs = False):  # dict[cluster: seq_ids]
    result = dict()
    count = 0
    for cluster, ids in clusters.items():
        if len(ids) >= min_size:
                if paralogs:
                     result[cluster] = ids
                else:
                    names = [species[id] for id in ids]
                    name_counts = Counter(names)
                    if all(count == 1 for count in name_counts.values()):
                        result[cluster] = ids
    return clusters


def genome_map(file):   # dict[seq_id: seq]
    result = dict()
    for record in SeqIO.parse(file, "fasta"):
        if record.seq == None: continue
        result[record.id] = record.seq
    return result

def get_families(filtered_clusters, gen_map, species, outdir, paralogs = False):
    records = []
    for cluster, ids in filtered_clusters.items():
        for i in ids:
            with open(f"{outdir}\\{cluster}.fasta", "a") as file:
                if paralogs:
                    file.write(f">{species[i]}_{i}" + "\n")
                else:
                    file.write(f">{species[i]}" + "\n")
                file.write(str(gen_map[i]) + "\n")


def main(clusters_dir, cluster_seq_dir, combined_fasta, outdir, paralogs = True, orthologs = True):
    clusters = read_in_clusters(clusters_dir)
    species = species_info(combined_fasta)
    gen_map = genome_map(cluster_seq_dir)
    if orthologs:
        filtered_cl_orthologs = filtering_clusters(clusters, species, min_size=22, paralogs=False)
        get_families(filtered_cl_orthologs, gen_map, species, outdir=f"{outdir}//orthologs_gene_families")
    if paralogs:
        filtered_cl_paralogs = filtering_clusters(clusters, species, min_size=22, paralogs=True)
        get_families(filtered_cl_paralogs, gen_map, species, outdir=f"{outdir}//paralogs_gene_families")



cl_dir = "/home/students/bioinf/a/am467109/cyanobacteria/sinice/clusterRes_cluster.tsv"
cl_seq_dir = "/home/students/bioinf/a/am467109/cyanobacteria/sinice/clusterRes_all_seqs.fasta"
combined = "/home/students/bioinf/a/am467109/cyanobacteria/sinice/combined.fasta"
outdir = "/home/students/bioinf/a/am467109/cyanobacteria/sinice/"
main(clusters_dir=cl_dir, cluster_seq_dir=cl_seq_dir, combined_fasta=combined, paralogs=True, orthologs=True)