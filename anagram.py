def anagram(s:str,t:str)->bool:
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)
print(anagram("silent","listen"))
print(anagram("rat","car"))

