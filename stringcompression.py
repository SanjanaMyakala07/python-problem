def compress(chars):
    index = 0
    i = 0
    while i < len(chars):
        current_char = chars[i]
        count = 0
        while i < len(chars) and chars[i] == current_char:
            count += 1
            i += 1
        chars[index] = current_char
        index += 1
        if count > 1:
            for digit in str(count):
                chars[index] = digit
                index += 1

    return index
chars1 = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
length = compress(chars1)
print("Compressed length:", length)
print("Compressed string:", ''.join(chars1[:length]))
