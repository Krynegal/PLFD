s = "hannah"

for i in range(len(s)):
    if s[i] != s[-1 - i]:
        print(f"{s} is not a palindrome")
        break
else:
    print(f"{s} is a palindrome")
