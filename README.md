# otherprogram
---
업무 도중 자잘하게 시간을 잡아먹는 업무를 스크립트화 한 것입니다.

### sbs 특정 게시판에 엽력 날짜의 게시물이 갱신되었는지 확인하는 스크립트입니다.  

sbs 특정 게시판에서 원하는 날짜의 게시물이 갱신되었다면 갱신되었다는 메시지를 출력하고 메일로 발송해줍니다.  
(gmail.smtp 를 이용하였습니다. 구글 계정이 필요합니다.)  

갱신되지 않았다면 5초 간격으로 갱신 재확인을 합니다.

또한 메일을 보내는 과정에서 정보를 잘못 입력하면 재확인하여 진행합니다.

> ### 업데이트 예정  
> 갱신이 확인되면 갱신된 게시물의 내용중에서 원하는 정보를 입력받아서 존재 여부를 확인합니다.

---
