# igaworks_bot

main.py를 실행함으로써 봇 프로그램을 실행합니다.

./config/config.ini의 설정을 통해 봇 실행 수 등을 설정할 수 있습니다.  
다음은 config.ini의 각 항목을 설명한 것입니다.

> ;event Collect Server의 주소입니다.  
EC2HOST = ec2-52-79-98-181.ap-northeast-2.compute.amazonaws.com

> ;Event Collect Server의 포트입니다.  
EC2PORT = 8080

> ;collect API 경로입니다.  
EVENT_COLLECT_ROUTE = api/collect

> ;"BOT_BASE_ID" + "0 ~ BOT_NAME_SUFFIX_MAX_NUMBER" 의 형태로 사용자 아이디를 생성합니다. 기본값은 user 입니다.  
BOT_BASE_ID = test

> ;사용자 아이디 뒤의 넘버링 최대값입니다. 기본값은 10 입니다.  
BOT_NAME_SUFFIX_MAX_NUMBER = 10

> ;봇을 실행할 횟수입니다.  
BOT_LOOP_COUNT = 10
