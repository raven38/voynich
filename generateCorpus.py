import sys
import re

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.split()
        if not line[1] == 'B':
            continue;
        words = line[2]
        print(' '.join(re.split(r'[-=,.]', words)))
        
