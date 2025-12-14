# 계단 오르는 방법의 수 계산하는 프로그램
# =======================================
def count_stair(n):
    # 계단이 1개일 때
    if n == 1:
        return 1
    # 계단이 2개일 때
    if n == 2:
        return 2
    
    # 테이블 생성
    table = [0] * (n + 1)
    # 초기값
    table[1] = 1  # 1개 계단 : 1가지
    table[2] = 2  # 2개 계단 : 2가지
    
    # 반복문을 이용한 Bottom-up 테이블 방식
    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    
    # 계단을 오르는 방법의 수 반환
    return table[n]

# =======================================
# 메인 프로그램
if __name__ == "__main__":
    # 계단 개수 입력
    n = int(input("계단의 개수를 입력하시오 : "))
    
    # 계단 오르는 방법의 수 계산
    result = count_stair(n)
    
    # 결과 출력
    print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")