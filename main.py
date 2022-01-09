# FCM서버에 파이썬 프로그램으로 API 호출(기기 푸시알림 전송 요청)
import requests
import json

# 함수 제작 : 보내줄 문구/본문 내용을 받아서 전송

def send_fcm_notification(title, body):
    # FCM 서버에 요청하려면
    # 1. 호스트주소/기능주소 => 실제 기능 URL
    fcm_url = 'https://fcm.googleapis.com/fcm/send'
    
    # 2. 첨부해야할 파라미터 (보내줄 데이터)
    
    
    # 헤더에, 인증키(token)를 담아서 전달
    fcm_headers = {
        'Authorization' : 'key=AAAA5KK-mvQ:APA91bGfDkYHgt4ihRKsgQGY9IYkl4a7rawsS0_Hmyz77KiO-SIz8ymd4j1KjEht3uCWbS0VnMChtwqk5LKOCadzyQlQdX6GOfuZEBUufTAd6xdB3V6BziX080vh5kNmAjZqJwbfn1gM',
        'Content-Type' : 'application/json; UTF-8',
    }
    
    content = {
        'registration_ids' : 'dmsIsoVpSWy__3REXQXVmP:APA91bFeLGvPm0AkY1YyF25pwDW3PQXcRK0aZO-0oVtaXklIbajFNERVFePjytnt2aS5DDK_cDHFT3IXZhy5hs27PonueoBq0IK5pU7DXEHnM0b8GQfeEA_I_dE72t4shNLj4qAIaQFF', # 어느 기기에 보낼건지, 디바이스 토큰  cf) 리스트로 넣으면 여러기기에 동시전송
        'notification' : {
            
            'title' : title,
            'body' : body,
            }, # 기본양식의 알림. data-message로 보내면 커스터마이징할수있는 지원을 해주는 알림
    }
    
    # 3. 어떤 방식 + 실제 API 호출
    requests.post(fcm_url, data=json.dumps(content), headers=fcm_headers)