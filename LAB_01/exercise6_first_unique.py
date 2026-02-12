def first_unique_char_v1(s: str) -> int:
    if not s:
        return -1
    # First traversal
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    # Second traversal
    for idx, char in enumerate(s):
        if freq[char] == 1:
            return idx
    return -1



def first_unique_char_v2(s: str) -> int:
    if not s:
        return -1
    char_info = {}
    for idx, char in enumerate(s):
        if char in char_info:
            char_info[char] = (char_info[char][0] + 1, char_info[char][1])
        else:
            # Record the current index
            char_info[char] = (1, idx)
    # Traversing the dictionary
    for char, (count, idx) in char_info.items():
        if count == 1:
            return idx
    return -1



# test
test_cases = [
    "leetcode",
    "loveleetcode",
    "aabb",
    "dddccdbba",
    "",
    "x"
]

print("Two pass method:")
for s in test_cases:
    print(s, "->", first_unique_char_v1(s))

print("\nOrderedDict method:")
for s in test_cases:
    print(s, "->", first_unique_char_v2(s))