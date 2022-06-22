input = input()
croa_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for croa in croa_list:
    if croa in input:
        input = input.replace(croa,'*')

print(len(input))




# 정답코드
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()
#
# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))