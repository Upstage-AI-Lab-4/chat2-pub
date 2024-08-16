[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yoHXt_g5)
# 프로젝트 이름
TESLA를 사랑한 서학개미
  

<br>

## 프로젝트 소개
<프로젝트 소개>

코로나 팬데믹 동안 넘치는 유동성이 주식시장에 유입되면서 전 세계적으로 개미 투자자들의 활약이 두드러졌습니다. 한국에서는 동학농민운동을 본뜬 "동학개미"라는 별칭이 등장했으며, 국내 주식시장에서 주요 플레이어로 부상했습니다.

이와 동시에, 미국 주식시장에 발을 들인 개인 투자자들은 "서학개미"로 불리며, 미국 주식에 대한 관심과 투자 열풍이 매년 가속화되고 있습니다. 서학개미는 특히 테슬라, 애플, 아마존과 같은 미국 대표 기업에 대한 열정을 보여주고 있으며, 이 트렌드에 맞춰 저희는 사용자에게 최적화된 정보를 제공하고자 하는 목표를 설정하였습니다.

따라서, 저희는 미국 주식에 관심이 있거나 이미 투자하고 있는 투자자들을 위해 실시간 투자 정보를 제공하고, 나아가 워런 버핏의 투자 철학과 명언을 반영한 투자 조언을 제공하는 스마트 챗봇을 협업하여 개발하였습니다.


<서학개미의 페르소나>

서학개미는 그 어떤 캐릭터보다 강력합니다. 주요 성격적 특성은 트럼프 전 대통령처럼 카리스마 넘치고 직설적입니다. 거기에 더해, 워런 버핏의 투자 철학을 기반으로 한 냉철한 투자 조언을 결합하여, 사용자들에게 확신과 자신감을 심어줍니다.

- 강력한 리더십과 자신감을 바탕으로, 투자자들이 올바른 결정에 도달하도록 돕는 가이드 역할을 수행합니다.
- 필요할 때는 단호한 조언을 통해 투자자들이 직면한 불확실성을 해결할 수 있도록 돕습니다.
- 워런 버핏의 철학을 바탕으로, 투자자들에게 전략적인 방향성을 제시합니다. 


<챗봇의 주요 기능>

1. 미국 주식 실시간 정보 제공 <br>
   서학개미는 실시간으로 야후 파이낸스 API를 통해 최신 주식 시장 데이터와 분석 자료를 제공합니다.  

2. 워런 버핏의 투자 철학을 활용한 조언 제공 <br>
   버핏의 투자 명언을 인용하며 심도 있는 투자 조언을 제공하고, 사용자가 스스로 올바른 결정을 내리도록 도와줍니다.  
  
3. 강력한 투자 방향 제시 <br>
   서학개미는 마치 트럼프처럼 확신에 찬 목소리로, 때로는 과감한 투자 조언을 제공합니다.  
  
4. 사용자 맞춤형 대응<br>
   사용자가 불안감을 느낄 때마다, 서학개미는 격려와 단호한 조언으로 대응합니다. 사용자가 느낄 수 있는 불안감을 풀어주며, 긍정적인 투자 심리를 유지할 수 있도록 돕습니다.  
  

'테슬라를 사랑한 서학개미'는 미국 주식 시장에 발을 내딛는 모든 투자자들에게 힘을 실어줍니다. 워런 버핏의 투자 철학과 트럼프의 강력한 리더십을 결합한 이 챗봇은 단순한 정보 제공을 넘어서, 투자자로 하여금 명확한 판단과 자신감을 얻게 하는 최고의 가이드입니다.

서학개미는 사용자에게 단호하면서도 지혜로운 투자 조언을 제공하며 성공적인 투자 여정을 함께할 것입니다.


## 팀원 구성

<div align="center">

| **팀장** | **팀원 1** | **팀원 2** |                                                            **팀원 3**                                                             | **팀원 4** |
| :------: |  :------: | :------: |:-------------------------------------------------------------------------------------------------------------------------------:| :------: |
|[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/11969925?v=4" height=150 width=150> <br/> @misule0423](https://github.com/misule0423) | [<img src="https://avatars.githubusercontent.com/u/1223020?v=4" height=150 width=150> <br/> @deptno](https://github.com/deptno) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |
</div>

<br>

## 1. 개발 환경

- 주 언어 : python
- 버전 및 이슈관리 : git
- 협업 툴 : github, slack, zoom

<br>

## 2. 채택한 개발 기술과 브랜치 전략
<예시>

### Pandas, NumPy

- Pandas
  - 기업의 배당 데이터를 Pandas DataFrame으로 불러온 후, 각 기업의 배당 수익률을 계산하고, 연도별로 그룹화하여 평균 배당 수익률을 계산합니다.
  - 필터링 조건을 적용하여 특정 기업의 배당 데이터를 분석하거나, 원하는 형태로 데이터를 변형할 수 있습니다.  

- Numpy
  - 벡터화 연산을 사용하여, 3000여개 데이터를 효율적으로 처리합니다.

### Beautifulsoup, Selenium

- Beautifulsoup
  - 네이버 증권 페이지에서 배당률, 주가 등의 정보를 포함한 HTML 테이블에서 데이터를 추출합니다.

- Selenium
  - 웹 페이지에서 동적 콘텐츠를 로드합니다.
  - 특정 종목의 배당 데이터를 얻기 위해 종목 검색 후, 관련 페이지로 이동해야 할 때, 이 과정을 자동화합니다. 

### 브랜치전략 
- `git` 에 대한 지식 차이와 효율성을 고려하여 가장 단순한 trunk based 전략을 취했습니다.
  - `main` 브랜치와 `topic` 브랜치를 운영한다
    - **main** 실행 가능한 상태를 유지합니다.
    - **topic** 기능을 개발하고 완료되면 *pr* 을 통해 `main` 브랜치로 머지됩니다.
- 머지 전략 과 코드리뷰
  - 코드리뷰를 강제 하지 않고 각자 기능이 준비되면 작업 브랜치인 *topic* 브랜치를 머지하는 방식으로 진행하였습니다.

<br>

## 3. 프로젝트 구조
```
├── README.md
├── Pipfile
├── Pipfile.lock
├── requirements.txt
├── main.py
├── crawler
│   └── TeslaStockData.py
├── documents
│   ├── tesla_info.txt
│   ├── tesla_news.txt
│   └── tesla_stock_prices.txt
├── indexing
│   ├── index.faiss
│   ├── index.pkl
│   └── vector_store.py
├── retriever
│   ├── retriever.py
│   └── test.py
├── history
│   ├── __init__.py
│   └── history.py
├── logger
│   ├── __init__.py
│   └── logger.py
├── memory
│   ├── __init__.py
│   └── memory.py
├── chain
│   ├── __init__.py
│   └── create_chat_text_chain.py
├── template
│   ├── __init__.py
│   └── buffet_trump.py
├── llm
│   ├── __init__.py
│   ├── openai.py
│   └── upstage.py
└── ui
    ├── __init__.py
    ├── page.py
    └── stream_text.py
...

```

<br>

## 4. 역할 분담

### 권희수
- **역할**
    - 총괄, 프로젝트 주제 선정 및 persona 구축, 발표
- **기능**
    - yfinance, google을 통한 crawler 모듈 구현
<br>

### 팀원 2
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 이민석
- **역할**
    - 벡터 스토어 모듈 개발
- **기능**
    - 데이터 로딩 및 전처리(청킹), 임베딩 생성, 벡터 스토어 저장 및 로드
<br>

### 이봉균
- **역할**
  - `git` 오리지널 레포지터리 생성 및 upstage 레포로 추후 이전
  - `branch` 전략 공유
- **기능**
  - user input -> event handler -> ui 결과 노출까지의 스켈레톤을 구현
  - 모듈 디렉토리 스켈레톤 작성
  - gradio 를 활용한 ui 채팅 작성
<br>

## 5. 개발 기간 및 작업 관리

### 개발 기간
- 전체 개발 기간 : 2024-08-12 ~ 2024-08-16
- 기능 구현 : 2024-08-12 ~ 2024-08-14
- 그외 기간 작성
  
<br>

### 작업 관리
<예시>

- 아래와 같은 오류가 발생했습니다.

```python
C:\Users\yong\AppData\Local\Programs\Python\Python311\Lib\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The class `langchain_community.llms.openai.OpenAI` was deprecated in langchain-community 0.0.10 and will be removed in 0.2.0. An updated version of the class exists in the langchain-openai package and should be used instead. To use it run `pip install -U langchain-openai` and import as `from langchain_openai import OpenAI`.
  warn_deprecated(
```

### 설명

- langchain_community.llms.openai.OpenAI는 langchain-community 0.0.10에서 deprecate되었으며 0.2.0에서 제거될 예정입니다.
- 업데이트된 버전의 클래스가 langchain-openai 패키지에 있으며 이것을 사용해야 합니다.


### 해결

- 명령 프롬프트(또는 터미널)에서 다음 명령을 실행해 langchain-openai 패키지를 설치합니다.

```python
pip install -U langchain-openai
```

- 아래와 같이 import문 변경하면 해결됩니다.
```python
from langchain_openai import OpenAI
```


<br>

## 5. 프로젝트 후기

### 권희수
- 하나의 공통된 주제로 팀원들과 co work을 통해 project를 완성하였다는 것에 감격을 느꼈고, 짧은 시간이었지만 다른 분들의 knowhow를 배울수 있어서 아주 유익한 시간이었습니다.

### 이민석
- 랭체인 프레임워크를 사용하여 RAG 시스템을 구축하면서 이론적으로 배운 내용을 실제로 구현해 보면서 전체 시스템을 개략적으로 이해할 수 있었습니다. 이 과정을 통해 RAG 시스템의 부족한 부분을 직접 확인하고, 이를 어떻게 해결할지에 대한 고민을 함꼐 나눌 수 있어서 좋았습니다.
<br>

### 이봉균
- `langchain` 이라는 하이레벨 프레임워크를 통해 rag 를 지원하는 프로젝트를 수행함으로써 전체 적인 플로우에 대한 이해를 가져갈 수 있어 이해에 도움이 되었습니다.
<br>
