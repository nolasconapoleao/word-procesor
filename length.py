import os
import re

def main():
    out_dir = 'out/'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    count = open('out/count', 'w')

    # Read word bank
    infile = open('wordbank/icf', 'r')
    sizes = [0] * 50
    for word in infile:
        if ',' in word:
            word = word.split(",")[0]

        # Remove contraction or possessive in english
        if re.search("'", word):
            continue

        # Capitalization occurs for acronyms or names
        if any(c.isupper() for c in word):
            continue

        sizes[len(word)-1] += 1

    for k in range(len(sizes)):
        if(sizes[k] != 0):
            count.write("{:2d} letters : {:05d} words\n".format(k, sizes[k]))

    # File cleanup
    infile.close()
    count.close()

if __name__ == "__main__":
    import sys
    sys.exit(main())
