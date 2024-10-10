import time
import RPi.GPIO as GPIO
import board
import adafruit_dht
import sys
import db
import paho.mqtt.client as mqtt

DHT11_SENSOR = adafruit_dht.DHT11(board.D26)

#센서 pin 설정
ledPin=[17,27,22] #[red_led,yellow_led,green_led]
ledState=[0,0,0]


TrigPin = 23
EchoPin = 24

TouchSensorPin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin[0], GPIO.OUT)
GPIO.setup(ledPin[1], GPIO.OUT)
GPIO.setup(ledPin[2], GPIO.OUT)
GPIO.setup(TrigPin, GPIO.OUT)
GPIO.setup(EchoPin, GPIO.IN)
GPIO.setup(TouchSensorPin, GPIO.IN)

def upadateLeds_all():
     for num, value in enumerate(ledState):
         GPIO.output(ledPin[num],value)



#LED 상태 업데이트 함수
def updateLeds(num):

    GPIO.output(ledPin[num],ledState[num])
    
    if num == 0 :
        db.insert_aircon_info(ledState[0])
    elif num == 1 :
        db.insert_heater_info(ledState[1])
    elif num == 2 :
        db.insert_dehumidifier_info(ledState[2])


#초음파 센서를 이용한 거리 측정 함수
def get_distance():
    GPIO.output(TrigPin, True)
    time.sleep(0.00001)
    GPIO.output(TrigPin, False)

    while GPIO.input(EchoPin) == 0:
        start_time = time.time() #시작시간 기록

    while GPIO.input(EchoPin) == 1:
        stop_time = time.time() #정지시간 기록

    check_time = stop_time - start_time #시간 차를 계산하여 거리 계산
    distance = (check_time * 34300) / 2  # cm
    distance = round(distance,2) #소수점 둘째 자리까지 반올림
    return distance

#DHT11 센서를 이용한 온도 측정 함수
def get_temperature():
    temperature_data = DHT11_SENSOR.temperature
    return temperature_data

#DHT11 센서를 이용한 습도 측정 함수
def get_humidity():
    humidity_data = DHT11_SENSOR.humidity
    return humidity_data

#터치센서 상태 확인 함수
def get_touch():
    if GPIO.input(TouchSensorPin)==GPIO.HIGH :
        return 'ON'
    elif GPIO.input(TouchSensorPin)==GPIO.LOW :
        return 'OFF'

                
# MQTT
broker = "broker.hivemq.com" #HiveMQ 브로커 사용
port = 1883
subscribe_topic = "5th_proj/ES_TEAM3" #구독할 topic
publish_topic = "5th_proj/ES_TEAM3/SensorValue" #발행할 topic

def on_message(clien, userdata, message):
    payload = message.payload.decode()  # 바이트를 문자열로 변환
    print(f"message : {payload} / topic : {message.topic}")

    # 메시지 파싱
    parts = payload.split("/")  # "RedLed/true" 형식으로 파싱
    # 문자열을 boolean으로 변환
    ledState[0] = int(parts[1]=='true')
    updateLeds(0)
    ledState[1] = int(parts[3]=='true')
    updateLeds(1)
    ledState[2] = int(parts[5]=='true')
    updateLeds(2)

    #  LED 상태 업데이트
    # if led == "RedLed":
    #     ledState[0] = int(state)
    #     updateLeds(0)
    # elif led == "YellowLed":
    #     ledState[1] = int(state)
    #     updateLeds(1)
    # elif led == "GreenLed":
    #     ledState[2] = int(state)
    #     updateLeds(2)


# MQTT 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정
client.on_message = on_message

# 브로커에 연결
client.connect(broker, port)

# 구독 시작
client.subscribe(subscribe_topic)

# 메시지 루프 
client.loop_start()

#----------------------------------------
#1초마다 센서값 읽어서 db와 app에 전송

try:
    while True:
        print("start")
        distance = get_distance()
        temp=get_temperature()
        humi=get_humidity()
        touch=get_touch()
        #db에 저장
        db.insert_temperature_info(temp)
        db.insert_humidity_info(humi)
        db.insert_distance_info(distance)
        db.insert_touch_info(touch)
        #app에 전송
        client.publish(publish_topic,"start")
        client.publish(publish_topic,f"distance/{distance}/temperature/{temp}/humidity/{humi}/touch/{touch}")

        time.sleep(2)

except KeyboardInterrupt:
    db.db_sensors.close()
    print("Goodbye, Have a nice day!")