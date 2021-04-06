# Regex
'''
You have a test string S. Your task is to match the string hackerrank. This is case sensitive.
'''

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

# Matching Anything But a Newline
'''
You have a test string S. 
Your task is to write a regular expression that matches only and exactly strings of form: abc.def.ghi.jkx, 
where each variable a, b, c, d, e, f, g, h, i, j, k, x can be any single character except the newline.
'''

regex_pattern = r"...\....\....\....$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())

# Matching Digits & Non-Digit Characters
'''
You have a test string S. Your task is to match the pattern xxXxxXxxxx
Here x denotes a digit character, and X denotes a non-digit character.
'''

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Matching Whitespace & Non-Whitespace Character
'''
You have a test string S. Your task is to match the pattern XXxXXxXX
Here, x denotes whitespace characters, and X denotes non-white space characters.
'''

Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Matching Word & Non-Word Character
'''
You have a test string S. Your task is to match the pattern xxxXxxxxxxxxxxXxxx
Here, x denotes word character, and X denotes non-word character.
'''

Regex_Pattern = r"\w\w\w\W\w{10}\W\w\w\w"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Matching Start & End
'''
You have a test string S. Your task is to match the pattern Xxxxx.
Here, x denotes a word character, and X denotes a digit. 
S must start with a digit X and end with . symbol. 
S should be 6 characters long only.
'''

Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())