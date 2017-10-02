#!/usr/local/bin/python3

# 입력: 천장의 가로 길이, 천장의 세로 길이
# 프로세스: 천장의 넓이 계산, 필요한 페인트의 양 계산
# 출력: 필요한 페인트의 양 출력

import math

length = float(input("ceiling length(m): "))
width = float(input("ceiling width(m): "))

area = length * width
amount_of_paint = math.ceil(area / 9)
result = "\nYou will need to purchase " + str(amount_of_paint) + " liter(s) of paint to cover " + str(area) + " square meter(s)."

print(result)
