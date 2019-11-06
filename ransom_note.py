import collections

def testRansom(ransomeNote , magazine):
    mag_dict = collections.defaultdict(int)
    for char in magazine:
        mag_dict[char] += 1
    for char in ransomeNote:
        mag_dict[char] -= 1
        if mag_dict[char] < 0:
            return False
    return True

ransomeNote = "helloooo" 
magazine    = "hellooo"
print testRansom(ransomeNote , magazine) , ransomeNote , magazine

ransomeNote = "helloo"
magazine    = "hellooo"
print testRansom(ransomeNote , magazine) , ransomeNote , magazine
