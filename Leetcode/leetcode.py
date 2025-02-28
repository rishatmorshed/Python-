from collections import defaultdict
def canConstruct(ransomNote, magazine):
    magazine_count = defaultdict(int)
    for letter in magazine:
        magazine_count[letter] += 1
        
    for letter in ransomNote:
        if magazine_count[letter] == 0:
            return False
        magazine_count[letter] -= 1
        
    return True
ransom = "aa"
magazine = "aba"
ans = canConstruct(ransom, magazine)
print(ans)

