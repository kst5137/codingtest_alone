# 벌집 문제
#
# 각 시기의 마지막
# 마지막
# 1, 7, 19, 37, 61
# 공식
# 이전항 + 6n
#
#
# N = int(input)
#
# xi = 1
# xi = xi + 6i
n = int(input())
x= 1
cnt = 1
while n > x:
    x = x+ 6*int(cnt)
    cnt += 1
print(cnt)