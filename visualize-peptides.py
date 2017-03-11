import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--full')
parser.add_argument('-p', '--part')
args = parser.parse_args()

# Open polypeptide file
with open(args.full, 'r') as f: polypeptide = f.read().replace('\n', '')

print polypeptide

# Read file containing list of peptides
peptides = [line.strip() for line in open(args.part, 'r')]

# Find matches of peptides within polypeptide
for p in peptides:
    print (' ' * polypeptide.find(p)) + p

