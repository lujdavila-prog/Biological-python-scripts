# Biological-python-scripts
This repository contains Python and Biopython scripts for reading genome sequences, counting nucleotide composition, and identifying non-standard characters in the input.

DNA.seq.count.py: Uses a dictionary to track counts of A, T, C, and G, and an error-catching dictionary to identify non-nucleotide characters in the input sequence. This script is also available in the py.scripts.learning repository, and is included here as the origin for the scripts that follow.

DNA.Seqv2.py: A refined version of DNA.seq.count.py that performs the same analysis but uses argparse to accept a file path as a command line argument, eliminating the need to hardcode input files.

biopython1.py: Uses Biopython to parse a FASTQ file and output the ID and sequence length of the first five records. Built for the SRR37176627 accession from the NCBI Sequence Read Archive, but compatible with other FASTQ.gz files if the file path is updated in the script.

biopythonV2.py: Does the same as biopython1.py but the major difference is that it does not output duplicates, only unique IDs.

Python and Biopython are required to run these scripts.
