sentences = [
    "vej;n; wdqclj qdwcpuve cqwdcq",
    "pqweur qcsv;knv 3 v;dkvm;;qwdco",
    "ertyui vbnm99 wcd;, 322 fw;klfmc,ds'c",
    "jnccmkmo cdw;.cdnvcx ewiuhwf cdce",
]

cnt = 0
numbers = list(str(x) for x in range(0, 9))
for s in sentences:
    for c in s:
        if c in numbers:
            cnt += 1
            break

print(cnt)