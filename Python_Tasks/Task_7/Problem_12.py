

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    from collections import Counter
    freq = Counter(s)
    count = Counter(freq.values())
    
    if len(count) == 1:
        return "YES"
        
    if len(count) == 2:
        first,second = count.items()
        
        if first[1] ==1 and (first[0] == 1 or first[0]- second[0] ==1):
            return "YES"
            
        if second[1] == 1 and (second[0] == 1 or second[0] - first[0] == 1):
            return "YES"
            
        
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    count = 0
    
    for char in set(s1 + s2):
        count += abs(s1.count(char) - s2.count(char))
        
        return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
