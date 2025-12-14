# 여행 짐 꾸리기 최적 패킹 프로그램
# =======================================
def backpack(W):
    # 물건 데이터 (이름, 무게(kg), 만족도)
    items = [
        ("노트북", 3, 12),
        ("카메라", 1, 10),
        ("책", 2, 6),
        ("옷", 2, 7),
        ("휴대용 충전기", 1, 4)
    ]
    # 물건의 개수
    n = len(items)  
    
    # 테이블 생성
    table = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Bottom-up 방식으로 테이블 채우기
    for i in range(1, n + 1):
        item_name, weight, satisfaction = items[i - 1]  # 현재 물건 정보
        
        for w in range(W + 1):  # 모든 무게 경우 확인
            # 현재 물건을 넣을 수 없는 경우
            if weight > w:
                table[i][w] = table[i - 1][w]  # 이전 물건까지의 만족도 유지
            # 현재 물건을 넣을 수 있는 경우(두 가지 선택지 중 좋은 결과 선택)
            else:
                table[i][w] = max(table[i - 1][w], # 현재 물건 넣지 않기
                              table[i - 1][w - weight] + satisfaction) # 현재 물건 넣기
    
    # 최대 만족도
    max_satisfaction = table[n][W]
    
    # 선택한 물건 역추적하기
    select_items = []
    w = W  # 현재 남은 용량
    
    # 마지막 물건부터 거꾸로 확인
    for i in range(n, 0, -1):
        # 현재 물건이 선택되었는지 확인
        if table[i][w] != table[i - 1][w]:
            item_name, weight, satisfaction = items[i - 1]
            select_items.append(item_name)  # 물건 추가
            w -= weight  # 남은 용량 감소시키기
    
    # 역순으로 선택된 물건을 원래 순서대로 정렬
    select_items.reverse()
    
    return max_satisfaction, select_items

# =======================================
# 메인 프로그램
if __name__ == "__main__":
    # 배낭 용량 입력
    W = int(input("배낭 용량을 입력 하세요 : "))
    
    # 0/1 배낭 문제 해결
    max_satisfaction, select_items = backpack(W)
    
    # 결과 출력
    print(f"최대 만족도 : {max_satisfaction}")
    print(f"선택된 물건 : {select_items}")