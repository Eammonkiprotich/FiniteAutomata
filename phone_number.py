import re
phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
mo = phoneNumRegex.search('My number is 0798234510.')
print('Phone number found: ' + mo.group())
