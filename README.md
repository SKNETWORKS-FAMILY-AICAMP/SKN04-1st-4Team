# 👑Enco 자동차👑
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/logo.png" width="1000" height="300"/></p>

<hr>

### 🤗 팀명 : 한번만 봐조
 
### 🤭 팀원

<p align="center">
	<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/%ED%8C%80%EC%9B%90.png" width="800" height="200"/>
</p>

<div align="center">
	
|🐰오정연 |🐱김현재|🐹권오셈|🐶오종수|
|:-------:|:-------:|:-------:|:-------:|
|[Jungyunn](https://github.com/Jungyunn)|[97now](https://github.com/97now)|[Kwonohs](https://github.com/Kwonohs)|[Quliy303](https://github.com/Quliy303)|
</div>

<hr>

### 👨‍🏫 프로젝트 개요  

  한번만 봐조(엔코 자동차)의 시스템은 전국 자동차 등록 현황 및 기업 FAQ 조회 라는 주제를 자동차 기업의 입장에서 자동차 관련된 FAQ를 시스템을 만든다고 생각한 서비스 구현했습니다.


<hr>


### 👩‍🏫 서비스 목표

  1. 13년도부터 24년 7월까지의 지역별 자동차 분포 현황 그래프 시각화.
  
  2. 연도별 국내 자동차 현황의 지도 시각화.
  
  3. 타 기업의 FAQ와 엔코 자동차의 FAQ를 기업별로 보여준다.

<hr>

### 🔨 기술 스택
<div>
<img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/%EA%B8%B0%EC%88%A0%EC%8A%A4%ED%83%9D.png">

* Prerequisites
```cmd
pip install -r requirements.txt
```
  	
* Usage
1. car_data_crawl 경로에서 <br>
```cmd
    python run_all_scripts.py
```

2. streamlit 경로에서 <br>
```cmd
 	streamlit run CompanyProfile.py
```
</div>

<hr>

### 💻 DB 테이블 - ERD

<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/ERD.png"/></p>



### 주요 기능 및 화면 구성


1. 회사 소개
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/1%EB%B2%88%20%ED%99%94%EB%A9%B4%EA%B5%AC%ED%98%84.png"></p>

2. 데이터 분석 (그래프) - 연도별 전국 자동차 등록 현황 
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/2%EB%B2%88%20%ED%99%94%EB%A9%B4%EA%B5%AC%ED%98%84.png"></p>

2.1 데이터 분석 (그래프) - 입력한 지역을 기준으로 연도별 데이터 시각화
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/3%EB%B2%88%20%ED%99%94%EB%A9%B4%EA%B5%AC%ED%98%84.png"></p>

3. 데이터 분석 (지도) - 입력한 연도를 기준으로 전국 데이터 시각화
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/4%EB%B2%88%20%ED%99%94%EB%A9%B4%EA%B5%AC%ED%98%84.png"></p>

3.1 데이터 분석 (지도) - 지도 상 지역에 수치를 나타냄
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/5%EB%B2%88%20%ED%99%94%EB%A9%B4%EA%B5%AC%ED%98%84.png"></p>

4. FAQ 기본 화면
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/7%EB%B2%88%20%ED%99%94%EB%A9%B4%EA%B5%AC%ED%98%84.png"></p>

4-1. FAQ 상세 화면
<p align="center"><img src="https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN04-1st-4Team/blob/main/src/6%EB%B2%88%20%ED%99%94%EB%A9%B4%EA%B5%AC%ED%98%84.png"></p>




### 한 줄 회고
오정연: 계획대로 하는것이 제일 어렵구나 <br>
김현재: 주어진 시간안에 최선을 다한것 같아서 뿌듯합니다 <br>
권오셈: 신나요 <br>
오종수: 매일 조금씩, 나아가는 제 모습을 확인했습니다 <br>

