# Data_engineer
Data_engineer_project

### 
# 나에게 꼭 맞는 충전소를 찾아줘 (앱 개발)

---
### 사용 기술
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Folium-77B829?style=flat-square&logo=Python&logoColor=white"/>



1주차 ~ 2주차
- - - 
### [데이터 수집]
![image](https://github.com/HongkyuRyu/Data_engineer/assets/69923886/69ca51be-e14d-47ec-a59f-df2147a828b8)

![image](https://github.com/HongkyuRyu/Data_engineer/assets/69923886/bcc8b96a-330b-49da-a9e7-8849607d64d6)

- - - 
### [데이터 파이프라인]
클라이언트가 API요청 -> Source Database(mysql)(on_premise) -> kafka(broker) -> kafka(sink_connector) 
->  GCP Data lake -> GCP big query -> Google looker stuido 시각화

![image](https://github.com/HongkyuRyu/Data_engineer/assets/69923886/5e55b7e2-5132-4239-b55d-e56d0f242e6d)

-> tableau 시각화를 해보고 싶었는데, 금액이 너무 비싸서 고민 중이다.
-> airflow를 활용해서, 배치 기반(매일 오후 8시에 일괄 수집) 으로 진행을 하려고 했으나
  -> api 요청은 startNum과 endNum으로 파라미터를 받는데
  -> 일별로 해당 페이지 넘버가 달라지는 문제가 있었다.
  -> 따라서, 아쉽지만 airflow는 특정 시간대의 특정 데이터를 추출하는 것은 어렵겠다고 판단을 해서 airflow는 기각했다.
  -> 그래도, airflow 공부는 지속적으로 하고 있는 중이다.
-> 실시간 데이터 처리는 웹 소켓 방식으로 진행한다고 하는데 api 요청 방식이라 지연 시간이 존재한다.
  -> 따라서, 이를 해결하기 위해 클라이언트가 API를 요청하는 그 시점을 기준으로 데이터를 받아오는 것으로 방법을 바꿨다.
  -> 클라이언트가 특정 시점에 데이터 요청을 보내면, 가장 최근 정보을 받아온다.
    -> (수정) 최근 정보는 약 10분 이전까지 포함하도록 한다. (전기차 충전 현황 등)


### [데이터 분석]

| 8/11(목) | 8/12(금) | 8/15(월) | 8/16(화) | 8/17(수) |
| --- | --- | --- | --- | --- |
| 크롤링 | 크롤링 | 판다스 시각화 | MYSQL 데이터 추출 | 대시보드 시각화 |
1. 하루가 끝날 때 즈음, 데이터 크롤링
    - page 1 ~ 가능한 많이
        - 최대 api 호출 횟수에 제한이 걸릴 정도로, 최대한 많이 하루 데이터 수집
        - page 1 ~ 50 / page 51 ~ 100 … 이런식으로 분배
2. 판다스로 데이터 분석
    - 분석하고 싶은 주제 토의
        - ex) 출/퇴근 시간대의 이용 가능한 충전소는 어디일까?
        - ex) 충전소에서 고장난 충전기 번호는 무엇일까?
        - ex) 가장 붐비는 충전소는 어디일까?
        - ex) 어떤 충전소가 충전속도가 빠른 충전기를 가지고 있을까? … 등등
3. 데이터 분석한 부분 시각화
    - seaborn
    - folium (지도 시각화)
4. 전체 테이블 외에도, 분석할만한 주제를 가진 테이블 만들기
5. SQL쿼리문을 통해 대시보드에 시각화

---

### [추천시스템]

- 사용자 위치 기반 대기시간이 적은 충전소 추천
- 속도가 빠르며 내 자동차 충전 규격에 적합한 충전소 추천(속도 빠른 충전기 보유)
- 요금이 저렴한 충전소 추천
- Flutter로 앱 개발

---

- 데이터가 적으면, pandas로 진행
- 데이터가 많아져서 SQL 조회 성능이 떨어지면, 분산시스템 구축 계획
