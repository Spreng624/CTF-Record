v11 = [
    95477623,
    -251535511,
    -104771852,
    670053776,
    2113090127,
    775040372,
    -1893070404,
    -1411211049,
    204081662,
    898182066,
    1403763218,
    1517703050,
    85988116,
    1375809856,
]

v11 = [x & 0xFFFFFFFF for x in v11]

t = [hex(v11[i])[2:] for i in range(0, len(v11))]
t = "".join(t)
# 转字符串
t = [chr(int(t[i : i + 2], 16)) for i in range(0, len(t), 2)]
t = "".join(t)

# 输出结果
print(t)
