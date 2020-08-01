# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print(re.sub(r'(?<= )(\&\&|\|\|)(?= )', (lambda m: 'and' if m.group(1) == '&&' else 'or'), input()))