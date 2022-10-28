# event_bot

이벤트 데이터를 생성하여 AWS SQS에 전송하는 봇 프로그램입니다.  
쇼핑몰 홈페이지를 가정하고 간단한 봇 이벤트 시나리오를 작성하였습니다.

#### 이벤트(상태) 종류
1. 로그인
2. 상품목록
3. 상품상세
4. 구매
5. 성공
6. 실패
7. 로그아웃

#### 이벤트 시나리오
> 로그인과 상품목록 진입까지는 고정이며 그 이후는 난수를 통해 결정됩니다.  
봇을 통한 이벤트 생성 시 구매와 구매성공, 구매실패 이벤트를 제외한 나머지 이벤트는 order 데이터가 생성되지 않습니다.

![image](https://user-images.githubusercontent.com/39260975/198247669-c18e6566-3d8a-4643-9360-0e4a510667cd.png)

0. 데이터 폼 생성 + 초기화
1. 로그인 : 시작 이벤트
2. 상품목록
3. 상품상세 or 로그아웃
4. 상품목록(뒤로가기) or 구매 or 로그아웃
5. 구매
6. 성공 or 실패
- 6-1 성공 : 상품상세 or 로그아웃(확률 낮음)
- 6-2 실패 : 상품상세 or 로그아웃(확률 높음)
7. 로그아웃 : 종료 이벤트

#### 실행 방법
main.py를 실행함으로써 봇 프로그램을 실행합니다.

./config/config.ini의 설정을 통해 봇 실행 수 등을 설정할 수 있습니다.  
다음은 config.ini의 각 항목에 대한 설명입니다.

> ;event Collect Server의 주소입니다.  
EC2HOST = ec2-52-79-98-181.ap-northeast-2.compute.amazonaws.com

> ;Event Collect Server의 포트입니다.  
EC2PORT = 8080

> ;collect API 경로입니다.  
EVENT_COLLECT_ROUTE = api/collect

> ;"BOT_BASE_ID" + "0 ~ BOT_NAME_SUFFIX_MAX_NUMBER" 의 형태로 사용자 아이디를 생성합니다. 기본값은 user 입니다.  
BOT_BASE_ID = tester

> ;사용자 아이디 뒤의 넘버링 최대값입니다. 기본값은 10 입니다.  
BOT_NAME_SUFFIX_MAX_NUMBER = 10

> ;봇을 실행할 횟수입니다.  
BOT_LOOP_COUNT = 100
