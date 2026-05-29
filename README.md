# Biological-python-scripts
This repository contains Python and Biopython scripts for reading genome sequences, counting nucleotide composition, and analyzing sequencing reads. These scripts are designed for .fastq.gz files from Illumina sequencing.

DNA.seq.count.py: Uses a dictionary to track counts of A, T, C, and G, and a second dictionary to identify and count non-nucleotide characters in the input sequence. This script is the origin for the scripts that follow.

DNA.Seqv2.py: A refined version of DNA.seq.count.py that performs the same analysis but uses argparse to accept a file path as a command line argument, eliminating the need to hardcode input files.

biopython1.py: Uses Biopython to parse a .fastq.gz file and output the ID and sequence length of the first five records. Requires the filename to be hardcoded in the script.

biopythonV2.py: Extends biopython1.py by filtering duplicate read IDs using a set, printing only the first five unique IDs and their lengths. Requires the filename to be hardcoded in the script.

biopythonV3.py: Extends biopythonV2.py by accepting the input file as a command line argument via argparse, making it compatible with any .fastq.gz file without modifying the script.

bioPAVG.py: Calculates the average read length across all records in a .fastq.gz file. Accepts the input file via argparse and prints a single float representing the average read length in base pairs.

bioPLT.py: Counts reads by length and categorizes them at or under 150bp and over 150bp. Accepts the input file via argparse and prints two counts as output.

Requirements: Python, Biopython, gzip
