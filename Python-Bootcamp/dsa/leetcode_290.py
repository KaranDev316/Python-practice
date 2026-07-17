from os.path import split

pattern = "abba"
s = "dog cat cat fish"
map_pattern_to_s = {}
map_s_to_pattern = {}

for a, b in zip(s.split(), pattern):

    if a in map_pattern_to_s:
        if map_pattern_to_s[a] != b:
            print(False)
    if b in map_s_to_pattern:
        if map_pattern_to_s[b] != a:
            print(False)
    map_pattern_to_s[a] = b
    map_pattern_to_s[b] = a
print(True)