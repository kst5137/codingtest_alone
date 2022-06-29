# 손익분기점

#
# when
# fixed_money + unfixed_money * cnt =< price * cnt


#
# fixed_money, unfixed_money, price = input().split()
#
# for i in range:
#     print(i)
#     if int(fixed_money) + int(unfixed_money) * i <= int(price) * i:
#         print(i)
#         break
#     elif int(unfixed_money) >= int(price):
#         print('-1')
#         break




fixed_money, unfixed_money, price = map(int,input().split())
if unfixed_money >= price:
    print(-1)
else:
    print(int(fixed_money/(price-unfixed_money)+1))

