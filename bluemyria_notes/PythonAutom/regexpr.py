import re

message = 'call me 415-555-1011 tomorrow or at 415-555-1234 office line'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# create a match object
m1 = phoneNumberRegex.search(message)
# get the matched string
print(m1.group())
# return list of string matches
print(phoneNumberRegex.findall(message))

# define groups with ( ) pairs
phoneNumberRegexGroups = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# create a match object
m2 = phoneNumberRegexGroups.search(message)
# get the matched strings / groups
print(m2.group())
print(m2.group(0)) # same as m2.group()
print(m2.group(1))
print(m2.group(2))

# look for ( ) in the string like this
phoneNumberRegexParenthesis = re.compile(r'(\(\d\d\d\))-\d\d\d-\d\d\d\d')
message2 = 'call me (415)-555-1011 tomorrow or at (415)-555-1234 office line'

m3 = phoneNumberRegexParenthesis.search(message2)
# get the matched strings / groups
print(m3.group())
print(m3.group(1))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
# mo --> None!!!!!!
mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo == None)


# ? zero or one
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
# mo --> None!!!!!!
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo == None)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('my number is 415-555-1234')
print(mo.group())
mo = phoneRegex.search('my number is 555-1234')
print(mo.group())

# * zero or more
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())

# +   one or more
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
print(mo == None)
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())

# masking * + ?
regex = re.compile(r'\+\?\*')
mo = regex.search('learned about +?*')
print(mo.group())

# repetitions {3}, minimum & maximum {3,5}
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search("he said HaHaHa")
print(mo.group())

# {3,5} , greedy matches!
# match the maximum longest string!
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group())

# {3,5}?, NON greedy matches!
# match the shortest string!
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())

# findall
resume = """Maria phone 234-234-2345
and another 456-456-4567
and again 678-678-6788 lalalalla
"""

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall(resume))

# if there are groups in the regexObj you get a list of tuples of (sub)strings:
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))
# if you also need the whole strings, add an "outer" group:
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))

# common character classes
# \d \D, \w \W, \s, \S
lyrics = """12 drummers drumming, 11 pipers piping, 
10 lords-a-leaping, 9 ladies dancing, 8 maids-a-milking, 7 swans-a-swimming, 
6 geese-a-laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves,
and 1 partrigde in a pear tree
"""
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# Your Own character classes (incl NOT)
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food!'))
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food!'))
NonVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(NonVowelRegex.findall('Robocop eats baby food!'))

beginsHelloRegex = re.compile(r'^Hello')
print(beginsHelloRegex.search("Hello world!!"))
print(beginsHelloRegex.search("He said Hello") == None) 

endsWorldRegex = re.compile(r'world!$')
print(endsWorldRegex.search("Hello world!"))
print(endsWorldRegex.search("Hello world!sdfsdfs") == None) 

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('8732427346823764736824'))
print(allDigitsRegex.search('873242734x6823764736824') == None)

atRegex = re.compile(r'.at')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

atRegex = re.compile(r'.*at')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

atRegex = re.compile(r'.*at$')
print(atRegex.findall('the cat in the hat sat on the flat mat'))

# .* is greedy
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Adriana Last Name: Smith'))

# .*? for NONgreedy!
nonGreedy = re.compile(r'<(.*?)>')
print(nonGreedy.findall('<To serve humans> for dinner.>'))
greedy = re.compile(r'<(.*)>')
print(greedy.findall('<To serve humans> for dinner.>'))

# .* is greedy until newline
prime = "Serve the public trust.\nProtect the innocent.\nUpload the law."
dotStar = re.compile(r'.*')
print(dotStar.search(prime))

# .* re.DOTALL for including newline
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

# re.IGNORECASE or re.I
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?'))

########################### SUBstitute ############################
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the docs to Agent Bob.'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the docs to Agent Bob.'))

# use of groups to repeat a pattern in the sub
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the docs to Agent Bob.'))
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the docs to Agent Carl.'))

# add comments and newlines to complicated regexprs w/ re.VERBOSE 
re.compile(r'''
\d\d\d    # area code (without parens)
-         # first dash
\d\d\d    #first 3 digits   
-         # second dash
\d\d\d\d  # last 4 digits''', re.VERBOSE)

# Using multiple options | Bitwise OR operators
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE | re.DOTALL | re.VERBOSE)

