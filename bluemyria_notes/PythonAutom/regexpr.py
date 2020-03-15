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

# {3,5} , NON greedy matches!
# match the shortest string!
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())
