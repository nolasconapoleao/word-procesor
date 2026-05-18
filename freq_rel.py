import os
import re

def main():
    # Read word bank
    in_file = 'out/digest'
    if not os.path.exists(in_file):
        print("Run the main.py before running the frequency analysis")
        return

    # Initialize counters
    frequency = [0] * 26

    infile = open(in_file, 'r')

    out_dir = 'out/'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    freq = open('out/freq', 'w')

    for line in infile:
        word = line.strip()[2:7]

        # Remap letters
        word = re.sub(r'ñ', 'n', word)
        word = re.sub(r'ç', 'c', word)
        word = re.sub(r'á|à|â|â|ã|ä',   'a', word)
        word = re.sub(r'é|è|ê|ê|ẽ|ë',   'e', word)
        word = re.sub(r'í|ì|î|î|ĩ|ï',   'i', word)
        word = re.sub(r'ó|ò|ô|ô|õ|ö',   'o', word)
        word = re.sub(r'ú|ù|û|û|ũ|ü',   'u', word)

        # Count letters
        # for c in word:
        #     frequency[ord(c)-ord("a")] += 1

        # Match regular expression
        match = re.search(r".*(.)\1.*", word)
        if match:
            frequency[ord(match.group(1))-ord("a")] += 1

    for k in range(len(frequency)):
        freq.write("{:05d}: {}\n".format(frequency[k], chr(ord("a")+k)))

    # File cleanup
    infile.close()
    freq.close()

if __name__ == "__main__":
    import sys
    sys.exit(main())
