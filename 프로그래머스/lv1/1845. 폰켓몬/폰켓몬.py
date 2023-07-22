def solution(nums):
    # 리스트의 갯수를 절반으로 나누는 set 함수 사용
    answer = len(set(nums))

    # 만약 nums의 길이가 절반으로 나눈 리스트보다 크다면 answer을 반환
    if len(nums) / 2 > answer:
        return answer
    # 아니라면 원래 nums의 길이를 절반으로 나눈 값을 반환
    else:
        return len(nums) / 2
