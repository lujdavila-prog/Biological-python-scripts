import argparse
parser = argparse.ArgumentParser(description = "process .txt file")
parser.add_argument("filename", help = "path to file")
args = parser.parse_args()
def report(sequence):
    counts = {"A": 0,"T": 0,"C": 0,"G": 0}
    mistakes = {}
    for base in sequence:
        if base in counts:
            counts [base] += 1  
        else:
            mistakes[base] = mistakes.get(base, 0) + 1
    return counts, mistakes
with open(args.filename, 'r') as f:
    sequence = f.read()
result_counts, result_mistakes = report(sequence)
print(f"{result_counts}")
print(f"{result_mistakes}")