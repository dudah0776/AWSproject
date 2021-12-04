# 클라우드 컴퓨팅 텀 프로젝트 보고서

A. 프로젝트 명
# 이미지 텍스트 추출 및 번역 웹
B. 프로젝트 멤버 이름 및 담당한 파트에 대한 소개
## 1인 프로젝트
### 20165302 구영모
* AWS기반 서버 구축
* 웹 프론트엔드 및 백엔드 작업 수행
* API 소스코드 수정
* 프로그램 디버깅
---
C. 프로젝트 소개 및 개발 내용 소개
## 작품 소개
* 웹 사이트에서 문자가 포함된 사진을 업로드 합니다.
* 사진을 업로드 하고 submit 버튼을 누르게 되면 그 사진에서 어떠한 문자가 있는지 추출해줍니다.
* 추출된 문자를 번역해 줍니다.
* 최종적으로 사용자는 사진에서 추출된 텍스트와 한국어로 번역된 텍스트를 얻게 됩니다.
## 동작 환경 및 개발언어
* 동작환경 : 웹 브라우저
* 개발언어 : python, html, css, javascript, jquery
* 사용된 모듈 : AWS SDK(boto3), Flask, AWS Rekognition, Naver papago

---

D. 프로젝트 개발 결과물 소개(+다이어그램)
## 과정
* 사용자가 사진을 서버에 보냅니다.
* 업로드 된 사진을 S3버킷에 전송하게 됩니다.
* S3 버킷에 업로드된 사진을 서버에서 텍스트를 추출합니다.
* 추출된 텍스트를 번역기로 번역합니다.

![동작과정](https://user-images.githubusercontent.com/66133109/144724737-623d278a-9f24-4627-8ae3-3cb686c9f401.PNG)

## 서버 구축 과정
* ubuntu 기반의 EC2 사용
* Flask 서버 구동을 위해 EC2 포트 범위 5000으로 설정
* S3 버킷과 Rekognition 사용을 위해 IAM 역할 설정
![설정1](https://user-images.githubusercontent.com/66133109/144724894-46d9e279-57fb-4598-8be6-15c15d4feab7.PNG)
* 웹과 버킷간 이미지 교환을 위해 버킷 정책 설정
![버킷정책](https://user-images.githubusercontent.com/66133109/144724922-c8bfc7ae-9cdc-427b-953c-a4d6f3f10f4d.PNG)
## 폴더 구성
*  Flask웹 서버 기반에 맞게 폴더를 구성하였습니다.
* templates 폴더에 html 파일로 구성
* static 폴더에 css와 js파일로 구성
![폴더구조](https://user-images.githubusercontent.com/66133109/144724935-1a5a0da2-925f-418f-a114-ce3b46e9a027.PNG)

---

E. 개발 결과물을 사용하는 방법 소개 (+프로그램 구동 화면 스크린샷 첨부)
![사용법1](https://user-images.githubusercontent.com/66133109/144724967-d8b743c0-837b-4044-baf1-7de5567bb652.PNG)


![사용법2](https://user-images.githubusercontent.com/66133109/144724979-a012622d-2ea0-4adf-8ac2-d25090af455b.PNG)

### 긴 텍스트도 추출 및 번역 가능
![사용법3](https://user-images.githubusercontent.com/66133109/144725001-4cca84a0-80ea-41ef-92be-461c326a3c32.PNG)

---
F. 개발 결과물의 필요성 및 활용방향
1. 웹 서핑을 하다 궁금한 이미지 속 단어가 보이면 번역할 수 있다.
2. 여러가지 다른 언어로 된 웹 문서 이미지를 캡처해서 번역할 수 있다.(ex : 외국 신문 등)
3. 기타 등등

---
