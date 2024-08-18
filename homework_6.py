def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(0, len(text) + 1 - i):
            yield text[j:j+i]

a = all_variants("abcd")
for i in a:
    print(i)