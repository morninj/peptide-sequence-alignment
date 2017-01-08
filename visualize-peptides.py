# Open polypeptide file
filename = 'polypeptide.txt'
with open(filename, 'r') as f: polypeptide = f.read().replace('\n', '')

print polypeptide

# Read file containing list of peptides
filename = 'peptides.txt'
peptides = [line.strip() for line in open(filename, 'r')]

# Find matches of peptides within polypeptide
for p in peptides:
    print (' ' * polypeptide.find(p)) + p

