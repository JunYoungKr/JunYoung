# 입력을 받은 후 대문자 처리
word = input().upper()

# 입력된 문자열을 set함수를 통해 중복된 요소들을 제거
word_list = list(set(word))

# print(word, word_list)

cnt = []

# 입력받은 문자열을 돌면서 word_list에 저장된 요소들이 있는지 검사하며 cnt라는 새 배열에 추가
for i in word_list:
    cnt.append(word.count(i))

# 만약 cnt 배열에 count의 최댓값이 2개 이상이라면 ? 출력
if cnt.count(max(cnt)) > 1:
    print("?")
# 아니라면 word_list의 해당되는 요소의 인덱스를 찾아 그것에 해당하는 알파벳 출력
else:
    print(word_list[(cnt.index(max(cnt)))])
