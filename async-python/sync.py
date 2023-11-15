import time

# 서브루틴
def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    time.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")

# 서브루틴
def main():
    delivery("A", 5)
    delivery("B", 3)
    delivery("C", 4)
    # return / return None 생략   # 탈출점


# 메인루틴
if __name__ == "__main__":
    start = time.time()
    print(main())  # None
    end = time.time()
    print(end - start)  # 총 걸린 시간