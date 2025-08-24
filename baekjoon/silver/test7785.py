import sys

log = int(sys.stdin.readline())
member_set = set()

for i in range(log):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        member_set.add(name)
    elif state == 'leave':
        member_set.discard(name)

for name in sorted(member_set, reverse=True):
    print(name)