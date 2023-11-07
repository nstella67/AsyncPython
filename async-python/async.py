import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():

    # 동시성
    await asyncio.gather(
        delivery("A", 5),
        delivery("B", 3),
        delivery("C", 4),
    )
    # result = await asyncio.gather(
    #     delivery("A", 1),
    #     delivery("B", 2),
    #     delivery("C", 3),
    # )

    # print(result)
    
    #sync.py와 같음
    await delivery("A", 5)
    await delivery("B", 3)
    await delivery("C", 4)
    # await을 기점으로 동기적으로 처리

    # 태스크
    task1 = asyncio.create_task(delivery("A", 2))
    task2 = asyncio.create_task(delivery("B", 1))

    await task2
    await task1


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)