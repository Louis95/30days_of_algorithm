def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    mag = list(magazine)
    ransom = list(ransomNote)
    # return all(x in magazine for x in ransomNote)

    for word  in ransom:
        if word in mag:
            mag.remove(word)
    if len(mag) == len(magazine)-len(ransomNote):
        return True
    else:
        return False
print(canConstruct("aaa", "ab"))