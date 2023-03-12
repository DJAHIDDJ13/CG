import re

cyborgs = {}
cyborg_count = int(input())
for i in range(cyborg_count):
    cyborg_name = input()
    cyborgs[cyborg_name] = {}

mayhem = {}
mayhem_report_count = int(input())
for i in range(mayhem_report_count):
    mayhem_report = input()
    attribute, value = re.findall(r"Mayhem's (\w+) is(?: an?)? \"?(.*)\"?", mayhem_report)[0]
    mayhem[attribute] = value
cyborg_report_count = int(input())
for i in range(cyborg_report_count):
    cyborg_report = input()
    cyborg, attribute, value = re.findall(r"(\w+)'s (\w+) is(?: an?)? \"?(.*)\"?", cyborg_report)[0]
    cyborgs[cyborg][attribute] = value
suspects = []
for cyborg in cyborgs:
    attributes = cyborgs[cyborg]
    if 'catchphrase' in attributes and 'word' in mayhem:
        if mayhem['word'] in attributes['catchphrase']:
            for attr in (set(attributes)-{'catchphrase'}):
                if attr not in mayhem:
                    continue
                if mayhem[attr] != attributes[attr]:
                    break
            else:
                suspects += [cyborg]
    else:
        for attr in (set(attributes)-{'catchphrase'}):
            if attr not in mayhem:
                continue
            if mayhem[attr] != attributes[attr]:
                break
        else:
                suspects += [cyborg]
if len(suspects) > 1:
    print('INDETERMINATE')
elif len(suspects) == 0:
    print('MISSING')
else:
    print(suspects[0])