import re
from collections import defaultdict
def convert_each(match):
    num = match.group(1)
    num = 1 if num == "" else int(num)
    char = match.group(2)
    spec_dic = {"sp": " ", "bS": "\\", "sQ": "'", "nl": "\n"}
    if char in spec_dic:
        char = spec_dic[char]
    return num * char


print(re.sub(r"(\d*)(sp|bS|sQ|nl|\S) ?", convert_each, input()))