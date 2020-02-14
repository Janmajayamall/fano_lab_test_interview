from collections import Counter
import re
from itertools import chain
import os

def counting_words(file_path, k):
    final_counter = Counter()
    with open(file_path) as f:
        for line in f:
            line = re.sub("\n","",line)
            temp = Counter(re.findall(r"[^,.:;'’ ]+|[,.:;'’]", line))
            final_counter+=temp

    return(final_counter.most_common(k))


dir_path = os.getcwd()    
print(counting_words(os.path.join(dir_path, 'test.txt'), 4))   #args filename, k

# Time complexity: O(n*m) --> m = number of lines