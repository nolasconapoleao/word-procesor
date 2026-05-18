import re

WORDLEN = 5

remove_repeated_letters = False
regex_check = True

# Count utility
def count_vowels(word):
    count = 0
    for c in word:
        # Ignore accentuation
        if(c not in "bcçdfghjklmnñpqrstvwxyz"):
            count+=1
    return count

# Great filter
def great_filter(word):
    # Remove contraction or possessive in english
    if re.search("'", word):
        return False

    # Capitalization occurs for acronyms or names
    if any(c.isupper() for c in word):
        return False

    # Distinct utility
    word = re.sub(r'ñ', 'n', word)
    word = re.sub(r'ç', 'c', word)
    word = re.sub(r'á|à|â|â|ã|ä',   'a', word)
    word = re.sub(r'é|è|ê|ê|ẽ|ë',   'e', word)
    word = re.sub(r'í|ì|î|î|ĩ|ï',   'i', word)
    word = re.sub(r'ó|ò|ô|ô|õ|ö',   'o', word)
    word = re.sub(r'ú|ù|û|û|ũ|ü',   'u', word)

    # Remove any character in forbidden word
    to_remove = ''
    for c in to_remove:
            if c in word:
                return False

    # Remove words that don't have these letters
    to_include = ''
    for c in to_include:
        if c not in word:
            return False

    if regex_check:
        # Discard match
        regex_discard = [""" r'.*pr.*' """]
        for rgx in regex_discard:
            if re.search(rgx, word):
                return False

        # Match only
        regex_match = [r".*(.)\1.*"]
        for rgx in regex_match:
            if not re.search(rgx, word):
                return False

    if remove_repeated_letters:
        return len(set(word)) == WORDLEN

    # Passed all filters
    return True

import os
def main():
    out_dir = 'out/'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    digest = open('out/digest', 'w')

    # Read word bank
    infile = open('wordbank/en_GB-large.txt', 'r')
    matches = 0
    for line in infile:
        # Check for 5 character words
        if  (',' not in line and len(line) == WORDLEN+1) or (',' in line and line[WORDLEN] == ','):
            word = line.strip()[0:WORDLEN]
            cnt = count_vowels(word)
            if great_filter(word):
                matches += 1
                digest.write("{} {}\n".format(cnt, word))

    print("Found {} matches.\n".format(matches))

    # File cleanup
    infile.close()
    digest.close()

if __name__ == "__main__":
    import sys
    sys.exit(main())

# Run in vscode task
# sort out/digest -o out/digest
