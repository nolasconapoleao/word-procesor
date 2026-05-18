# Word bank processor
This utility:
 - reads from a word bank
 - filters words with specified length (eg. 5 letters for wordle)
 - removes accentuation and remaps characters to ascii compatible values
 - (optional) excludes words witg forbidden letters
 - (optional) includes exclusively words containing allowed letters
 - (optional) filters out matching regex words
 - (optional) includes only matching regex words
 - (optional) excludes words with repeating letters

I've included pt word bank from [pt-br](https://github.com/fserb/pt-br) and eng [wordlist-diff](https://github.com/en-wl/wordlist-diff)

## Limitations
Attempting to use C++ or Golang resulted in complications in the count section. As you can see:
```
#include <iostream>

int main() {
  const std::string word{"joão"};
  std::cout << "Word 'João' is " << word.size() << " characters long.\n";
  return 0;
}
```
Produces:
```
Word 'João' is 5 characters long.
```

Same happens for Golang.
```
package main

import "fmt"

func main() {
	var word = "joão"
	fmt.Println("Word 'João' is ", len(word), " characters long.\n")
}
```

In order to accurately count the length of words with utf8 encoding a wide char string is necessary. Latin languages using accentuation like ñ, ã, é, etc count length 2 for these characters since ascii does not encode these.Fortunately python comes off the box with wide char strings parsing.

# Solution
The solution includes:
```
filter.py : Produces a digest file with words matching the rules

freq-rel.py : Calculates relative letter frequency for the digest file
```
