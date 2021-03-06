# FCM서버에 파이썬 프로그램으로 API 호출(기기 푸시알림 전송 요청)
import requests
import json

from pyfcm import FCMNotification
from requests.packages.urllib3.util import Url


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
    result = requests.post(url=fcm_url, data=json.dumps(content), headers=fcm_headers)
    print(f'FCM발송 결과 : {result}')
    
# send_fcm_notification('안녕하세요', '파이썬 통해서 보내기')


def send_fcm_by_library(title, body):
    push_service = FCMNotification(api_key='AAAA5KK-mvQ:APA91bGfDkYHgt4ihRKsgQGY9IYkl4a7rawsS0_Hmyz77KiO-SIz8ymd4j1KjEht3uCWbS0VnMChtwqk5LKOCadzyQlQdX6GOfuZEBUufTAd6xdB3V6BziX080vh5kNmAjZqJwbfn1gM')
    
    device_token = 'dmsIsoVpSWy__3REXQXVmP:APA91bFeLGvPm0AkY1YyF25pwDW3PQXcRK0aZO-0oVtaXklIbajFNERVFePjytnt2aS5DDK_cDHFT3IXZhy5hs27PonueoBq0IK5pU7DXEHnM0b8GQfeEA_I_dE72t4shNLj4qAIaQFF'
    
    result = push_service.notify_single_device(registration_id=device_token, message_title=title, message_body=body)
    print(result)
    
send_fcm_by_library('안녕하세요', '파이썬 pyFCM라이브러리로 전송합니다')

def send_sms_message(phone, message):
    aligo_url = 'https://apis.aligo.in/send/'
    aligo_api_key = '알리고 키'

    data = {
        'key' : aligo_api_key,
        'user_id' : '알리고아이디',
        'sender' : '알리고등록된전화번호',
        'receiver' : phone,
        'msg' : message,
        'testmode_yn' : 'y',
    }    
    
    requests.post(url=aligo_url, data=data)
send_sms_message('연락처적기 01090110390', '파이썬으로 문자간다 슝')