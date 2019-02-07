def rabin_karp(s, subs):
    len_subs = len(subs)
    hash_subs = hash(subs)

    for i in range(len(s) - len_subs + 1):
        if hash_subs == hash(s[i:i + len_subs]):
            return i
    return -1

s_1 = input("Введите строку: ")
s_2 = input("Введите подстроку: ")
answer = rabin_karp(s_1, s_2)
print(answer)
