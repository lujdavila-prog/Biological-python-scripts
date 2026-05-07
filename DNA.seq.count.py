base = (["A","T","C","G"])
counts = {"A": 0,"T": 0,"C": 0,"G": 0}
mistakes = []
DNA_seq = input("Input DNA sequence")
for base in DNA_seq:
    if base in counts:
        counts [base] += 1
    else:
        mistakes.append(base)
print(f"{counts}")
print(f"{mistakes}")