
import re

regex = re.compile(r'(?P<id>\d+)abc(?P=id)')
print(regex.findall('999abc999'))
