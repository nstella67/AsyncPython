# https://2.python-requests.org/en/master/user/advanced/#id1
# pip install requests

import requests # 동기적
import time


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    # url = "https://naver.com"
    # session = requests.Session()
    # session.get(url)
    # session.close()
    # => 위 세줄을 아래와 같이 두 줄로 변경 가능
    # with requests.Session() as session:
    #     session.get(url)

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 12s