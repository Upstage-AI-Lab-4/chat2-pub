import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup


class TeslaStockData:
    def __init__(self):
        self.tsla_yf = yf.Ticker('TSLA')

    def get_tesla_news(self):
        # Google 뉴스 검색 URL
        url = 'https://news.google.com/search?q=Tesla&hl=en-US&gl=US&ceid=US:en'
        # 요청을 보내고 응답을 받습니다.
        response = requests.get(url)
        # 응답 내용을 HTML 파서로 파싱합니다.
        soup = BeautifulSoup(response.text, 'html.parser')
        # 특정 클래스를 가진 모든 <a> 태그를 찾습니다. (Google 뉴스의 구조에 따라 변경될 수 있음)
        articles = soup.find_all('a', class_='JtKRv')
        # 뉴스 제목을 추출하여 리스트에 추가
        news_list = [{'Title': article.get_text()} for article in articles]
        # 리스트를 데이터 프레임으로 변환
        news_df = pd.DataFrame(news_list)
        # 데이터 프레임을 텍스트 파일로 저장
        file_path = 'tesla_news.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            for index, row in news_df.iterrows():
                file.write(f"{row['Title']}\n")

        print(f"News data has been saved to '{file_path}'.")

    def get_tesla_stock_prices(self):
        # 야후 파이낸스로 데이터를 불러옵니다
        tsla_df = self.tsla_yf.history(start='2023-08-01')[["Close"]]
        # 인덱스를 초기화 시키고 컬럼의 이름을 day, price로 바꿉니다.
        tsla_df = tsla_df.reset_index().rename(columns={'Date': 'day', 'Close': 'price'})
        # Pandas DataFrame 열을 Python datetime 으로 변환한다.
        tsla_df['day'] = pd.to_datetime(tsla_df['day'])
        # 가격 데이터를 소수점 한 자리로 포매팅
        tsla_df['price'] = tsla_df['price'].round(1)

        # 데이터 프레임을 텍스트 파일로 저장
        file_path = 'tesla_stock_prices.txt'
        tsla_df.to_csv(file_path, index=False, date_format='%Y-%m-%d')
        print(f"Tesla stock prices have been saved to '{file_path}'.")

    def get_tesla_info(self):
        # 테슬라의 주식 정보 가져오기
        tsla_info = self.tsla_yf.info
        # 사전 데이터를 데이터 프레임으로 변환 (행과 열을 전환하여 출력)
        tsla_info_df = pd.DataFrame([tsla_info])
        # 데이터 프레임을 텍스트 파일로 저장
        file_path = 'tesla_info.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            # 데이터 프레임 내용을 파일에 쓰기
            for column in tsla_info_df.columns:
                file.write(f"{column}: {tsla_info_df[column].iloc[0]}\n")

        print(f"Tesla stock information has been saved to '{file_path}'.")


# 사용 예제
tsla_data = TeslaStockData()
tsla_data.get_tesla_news()
tsla_data.get_tesla_stock_prices()
tsla_data.get_tesla_info()

### 코드 설명:
## - TeslaStockData 클래스 : 테슬라 주식 정보를 관리하는 클래스입니다. 이 클래스에는 테슬라 뉴스, 주가 정보, 및 기업 정보를 수집하고 파일로 저장하는 세 가지 메소드가 포함되어 있습니다.
## - 초기화 메서드 `__init__` : `yfinance`의 `Ticker` 객체를 생성하여 클래스 인스턴스에 저장합니다.
## - 뉴스 수집 메서드 `get_tesla_news : Google 뉴스에서 테슬라 관련 뉴스 제목을 수집하고 텍스트 파일로 저장합니다.
## - 주가 정보 수집 메서드 `get_tesla_stock_prices` : yfinance를 사용하여 주가 정보를 수집하고 파일로 저장합니다.
## - 기업 정보 수집 메서드 `get_tesla_info` : yfinance를 통해 얻은 기업 정보를 파일로 저장합니다.