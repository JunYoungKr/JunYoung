import sys

n = int(sys.stdin.readline())

record_dict = dict()

for i in range(n):
    name, record = sys.stdin.readline().split()
    if record == 'enter':
        record_dict[name] = True
    else:
        record_dict[name] = False

for i in sorted(record_dict.keys(), reverse=True):
    if record_dict[i]:
        print(i)
