#베이스 이미지를 명시
FROM node:10
#추가적으로 필요한 파일을 다운받는다.

COPY ./ ./

RUN npm install
#컨테이너 시작시 실행될 명령어를 명시해준다.
CMD [ "node","server.js" ]
