import time

TEST_DATA = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def factorial_iter(n):
    if n < 0:
        raise ValueError("음수 불가능")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_rec(n):
    if n < 0:
        raise ValueError("음수 불가능")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    elapsed = end - start
    return result, elapsed

def main():
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 를 입력하세요.")
    
    while True:
        print("===========Factorial Tester===========")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("-"*50)
        choice = input("선택 : ")

        if choice == 'q':
            print("종료합니다.")
            break
        elif choice in {"1", "2", "3"}:
            n_str = input("n 값(정수, 0 이상)을 입력하세요: ")
            if not n_str.isdigit():
                print("정수(0 이상의 숫자)만 입력하세요.")
                continue
            n = int(n_str)
            

            try:
                if choice == "1":
                    res, t = run_with_time(factorial_iter, n)
                    print(f"[반복] {n}! = {res}")
                    print(f"실행 시간: {t:.6f} s")
                elif choice == "2":
                    res, t = run_with_time(factorial_rec, n)
                    print(f"[재귀] {n}! = {res}")
                    print(f"실행 시간: {t:.6f} s")
                elif choice == "3":
                    res1, t1 = run_with_time(factorial_iter, n)
                    res2, t2 = run_with_time(factorial_rec, n)
                    print(f"[반복] {n}! = {res1}")
                    print(f"[재귀] {n}! = {res2}")
                    if res1 == res2:
                        print("결과 일치 여부 : 일치")
                    else:
                        print("결과 일치 여부 : 불일치")
                    print(f"[반복] 시간 : {t1:.6f} s | [재귀] 시간 : {t2:.6f} s")
            except ValueError as e:
                print("오류:", e)
        
        elif choice == "4":
            print("\n[테스트 데이터 실행]")
            for n in TEST_DATA:
                print(f"\n>> n = {n}")
                try:
                    res1, t1 = run_with_time(factorial_iter, n)
                    res2, t2 = run_with_time(factorial_rec, n)
                    if res1 == res2:
                        tf = "True"
                    else:
                        tf = "False"
                    print(f"n = {n} | same : {tf} | iter : {t1:.6f}s | rec : {t2:.6f}s")
                    print(f"    {n}! = {res1}")
                    
                except Exception as e:
                    print("오류:", e)
        else:
            print("잘못된 선택입니다. 다시 입력하세요.")
        
if __name__ == "__main__":
    main()

