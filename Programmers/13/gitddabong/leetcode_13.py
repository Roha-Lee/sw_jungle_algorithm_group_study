# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I 뒤에 V나 X가 오면 4 또는 9가 된다
# X 뒤에 L이나 C가 오면 40이나 90이 된다
# C 뒤에 D나 M이 오면 400이나 900이 된다

# 당장 만난 알파벳에 맞는 수를 sum에 더해주고
# 위의 조건에 맞는 키워드가 나온 경우 아까 더해준 수를 뺀 다음에 그에 맞는 수를 더함

s = "MCMXCIV"

total = 0
l_str = ""

dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

for _str in list(s):
    if l_str == 'I' and (_str == 'V' or _str == 'X'):
        total -= dict[l_str]
        total += dict[_str] - dict[l_str]

    elif l_str == 'X' and (_str == 'L' or _str == 'C'):
        total -= dict[l_str]
        total += dict[_str] - dict[l_str]
    
    elif l_str == 'C' and (_str == 'D' or _str == 'M'):
        total -= dict[l_str]
        total += dict[_str] - dict[l_str]

    else:
        total += dict[_str]

    l_str = _str


print(total)


