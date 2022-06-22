# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
#
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
#
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.



# 주어진 단어를 리스트로 쪼개기
alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

word = input()
total_time = 0
for unit in alphabet_list:
    for i in unit:
        for x in word:
            if i == x :
                total_time += alphabet_list.index(unit) +3
print(total_time)

# 2번 방법
#
# li = list(input())
# total_time = 0
#
# for i in li:
#     for j in alphabet_list:
#         if i in j:
#             total_time += alphabet_list.index(j) + 3

