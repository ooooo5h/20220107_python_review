# FCM서버에 파이썬 프로그램으로 API 호출(기기 푸시알림 전송 요청)
import requests

# 함수 제작 : 보내줄 문구/본문 내용을 받아서 전송

def send_fcm_notification(title, body):
    # FCM 서버에 요청하려면
    # 1. 호스트주소/기능주소 => 실제 기능 URL
    url = 'https://fcm.googleapis.com/fcm/send'
    
    # 2. 첨부해야할 파라미터 (보내줄 데이터)
    
    
    # 헤더에, 인증키(token)를 담아서 전달
    headers = {
        'Authorization' : 'key=AAAA5KK-mvQ:APA91bGfDkYHgt4ihRKsgQGY9IYkl4a7rawsS0_Hmyz77KiO-SIz8ymd4j1KjEht3uCWbS0VnMChtwqk5LKOCadzyQlQdX6GOfuZEBUufTAd6xdB3V6BziX080vh5kNmAjZqJwbfn1gM',
        'Content-Type' : 'application/json; UTF-8',
    }
    # 3. 어떤 방식