[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yoHXt_g5)
# 프로젝트 이름
<예시 1>
- 증권 배당 데이터 및 관련 세법 QA Engine
<br>

<예시 2>
- 유재석 페르소나 Chatbot
  

<br>

## 프로젝트 소개
<예시 1>
- 이 프로젝트는 증권 배당 데이터와 관련된 정보를 효율적으로 관리하고, 관련 세법에 대한 질문과 답변을 제공하는 QA(Question-Answering) 엔진을 구축하는 것입니다.
- 사용자는 이 엔진을 통해 특정 기업의 배당 정보나 세법 관련 질문에 대한 답변을 신속하게 얻을 수 있습니다.
<br>

<예시 2>
- 이 프로젝트는 유명 인물인 유재석의 페르소나를 바탕으로 한 Chatbot을 개발하는 것입니다.
- 이 Chatbot은 유재석의 말투, 스타일 등 유재석이 나온 프로그램 텍스트 대화를 반영하여 사용자와 자연스러운 대화를 나누도록 설계됩니다. 
<br>

## 팀원 구성

<div align="center">

| **팀장** | **팀원 1** | **팀원 2** |                                                            **팀원 3**                                                             | **팀원 4** |
| :------: |  :------: | :------: |:-------------------------------------------------------------------------------------------------------------------------------:| :------: |
|[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) | [<img src="https://avatars.githubusercontent.com/u/1223020?v=4" height=150 width=150> <br/> @deptno](https://github.com/deptno) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |
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
├── .gitignore
└── src
     ├── App.py
     ├── index.py
     ├── api
     │     └── GoogleAPI.jsx
     └── styles
           └── Globalstyled.jsx
...

```

<br>

## 4. 역할 분담

### 팀원 1
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 팀원 2
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 팀원 3
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 이봉균
- 자기소개
  - 전 개발자
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

### 팀원 1
프로젝트 후기 작성

### 팀원 2
프로젝트 후기 작성
<br>

### 이봉균
- `langchain` 이라는 하이레벨 프레임워크를 통해 rag 를 지원하는 프로젝트를 수행함으로써 전체 적인 플로우에 대한 이해를 가져갈 수 있어 이해에 도움이 되었습니다.
<br>
