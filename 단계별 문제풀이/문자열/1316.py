# 그룹단어체커
# 문자가 연속해서 나타나는 경우를 그룹단어라고 함


# 단어의 개수
N = int(input())
cnt = N
# 그룹단어체크
for i in range(0,cnt):
    word = input()
    for j in range(0,len(word)-1):
        print(j)
        if word[j] == word[j+1]:
            pass
            print('pass?')
        elif word[j] in word[j+1:]:
            print('다름')
            cnt -= 1
            break
        print('if elif')
print(cnt)

