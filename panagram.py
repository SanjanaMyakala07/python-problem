def check_if_pangram(sentence: str) -> bool:
    for c in range(ord('a'), ord('z') + 1):
        found = False
        for char in sentence:
            if char.lower() == chr(c):
                found = True
                break  
        if not found:
            return False
    return True
sentence1 = "the quick brown fox jumps over the lazy dog"
print(check_if_pangram(sentence1))  

sentence2 = "hello world"
print(check_if_pangram(sentence2))  
