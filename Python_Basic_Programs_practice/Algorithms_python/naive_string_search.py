def naivePatternSearch(mainString, pattern):
    patLen = len(pattern)
    strLen = len(mainString)
    position = []
    for i in range(strLen - patLen + 1):
        match_found = True
        for j in range(patLen):
            if mainString[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            position.append(i)
    return position

mainString = "ABAAABCDBBABCDDEBCABC"
pattern = "ABC"
position = naivePatternSearch(mainString, pattern)
print("Pattern found in position ")
for x in position:
    print(x)
