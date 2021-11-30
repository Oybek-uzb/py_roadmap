import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith 
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

print('\tTab') # R:     Tab
print(r'\tTab') # R: \tTab

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r'abc') # just string "abc"
pattern = re.compile(r'.') # any character axcept New Line!!!
pattern = re.compile(r'\.') # only dot - ".". Also character listed above: . ^ $ * + ? { } [ ] \ | ( ).
pattern = re.compile(r'coreyms\.com') # for URLs of web-sites
pattern = re.compile(r'\d') # all digits [0:9]
pattern = re.compile(r'\D') # all characters (also New Line) except digits [0:9].
pattern = re.compile(r'\w') # word characters (a-z, A-Z, 0-9, _)
pattern = re.compile(r'\W') # not word characters
pattern = re.compile(r'\s') # whitespaces (space, tab, newline)
pattern = re.compile(r'\S') # not whitespaces

pattern = re.compile(r'\bHa') # finds all "Ha"s which has a word boundary before it 
pattern = re.compile(r'\BHa') # finds all "Ha"s which has no word boundary before it
pattern = re.compile(r'^Start') # beginning of a string
pattern = re.compile(r'end$') # end of a string

pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') # [] is used for character set
pattern = re.compile(r'[1-5]') # a digit in range [1:5]
pattern = re.compile(r'[a-g]') # a letter in range [a:g]
pattern = re.compile(r'[a-zA-Z]') # any lower or upper case letter
pattern = re.compile(r'[^a-g]') # a letter which is not in range [a-g]
pattern = re.compile(r'[^b]at') # a word not beginning with "b" but ending with "at"
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}') # equals to (r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')

# Quantifiers
# *     - 0 or More char
# +     - 1 or More char
# ?     - 0 or 1 char
# {3}   - exact number
# {3,4} - range of numbers

pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# Brackets
# |   - either or
# ( ) - Group  

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# Examples

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

email_pattern = re.compile(r'[a-zA-Z]+@[a-z]{3,5 }\.[a-z]{3,4}')

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://youtubes.com
'''
url_pattern = re.compile(r'https?://(www\.)?(\w{7,})(\.[a-z]{3,4})') # (!!!) pay ettention to (www\.)? and {7,} (it means at least 7 chars)

matches = url_pattern.finditer(urls)

for match in matches:
    print(match)

    # In the example above in variable url_pattern we devided the regex into many groups.
    # They are (www\.), (\w{7,}) and (\.[a-z]{3,4}).
    # But also there is another one. A global (https?://(www\.)?(\w{7,})(\.[a-z]{3,4})) group!
    # The variable match above has the method group() showing into that groups.
    # The global group's index is 0. Other groups comes one after the other.
    # Let's look at this ...

    print(match.group(0)) # Booom!


subbed_urls = url_pattern.sub(r'\2\3', urls) # makes substitutions from 2- and 3- groups of urls
print(subbed_urls)