def is_palindromic(s):
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))

print(is_palindromic("dsdadd"))
print(is_palindromic("asdsa"))

# read strings boot camp in EPIPython ch. 6