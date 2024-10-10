import 'package:embeddedsystem_5th_project/monitoring.dart'; // 전역 변수를 가져옵니다.
import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';

class Mqtt {
  final client = MqttServerClient('broker.hivemq.com', '');

  Future<void> connect(String message) async {
    client.port = 1883;
    client.logging(on: true);
    client.keepAlivePeriod = 20;

    //콜백함수
    client.onConnected = _onConnected;
    client.onDisconnected = _onDisconnected;
    client.onSubscribed = _onSubscribed;
    client.onSubscribeFail = _onSubscribeFail;
    client.pongCallback = _pong;

    final connMessage = MqttConnectMessage()
        .withClientIdentifier('ES_TEAM3') // 클라이언트 식별자
        .withWillTopic('willtopic') // 유언 주제
        .withWillMessage('My Will message') // 유언 메세지
        .startClean()
        .withWillQos(MqttQos.atLeastOnce); // 유언 메시지의 QoS 수준

    client.connectionMessage = connMessage;

    try {
      await client.connect(); // 브로커와 연결 시도
    } catch (e) {
      print('Exception: $e');
      client.disconnect();
    }
    subscribeToTopic('5th_proj/ES_TEAM3/SensorValue');
    publishMessage('5th_proj/ES_TEAM3', message);
  }

  void _onConnected() {
    print('Connected');
  }

  void _onDisconnected() {
    print('Disconnected');
  }

  void _onSubscribed(String topic) {
    print('Subscribed to $topic');
  }

  void _onSubscribeFail(String topic) {
    print('Failed to subscribe $topic');
  }

  void _pong() {
    print('Ping response client callback invoked');
  }

  void subscribeToTopic(String topic) {
    //'topic'을 구독하고 구독한 주제로부터 받은 메세지를 출력하는 메서드.
    client.subscribe(
        topic, MqttQos.atLeastOnce); // topic을 구독한다. QoS : atLeastOnce
    client.updates!.listen((List<MqttReceivedMessage<MqttMessage?>> c) {
      // 콜백 함수
      final MqttPublishMessage message = c[0].payload
          as MqttPublishMessage; // 구독한 주제로 부터 받은 메세지 리스트의 첫번째 요소 내용을 message 변수에 저장.
      final payload = MqttPublishPayload.bytesToStringAsString(
          message.payload.message); // 데이터를 문자열로 변환하여 변수 payload에 저장.

      print(
          'Received message:$payload from topic: ${c[0].topic}>'); // 수신된 데이터의 첫 번째 메시지 내용과 주제를 출력한다.
      // 메시지를 '/'로 분리
      final parts = payload.split('/');

      // 메시지 배열의 길이 확인
      if (parts.length >= 8) {
        // 센서 값 할당
        distance = parts[1]; // distance 값
        temperature = parts[3]; // temperature 값
        humidity = parts[5]; // humidity 값
        touch = parts[7]; // touch 값

        // // LED 상태 업데이트
        // RedLed = parts[8] == '1'; // redLed 값이 '1'이면 true, 아니면 false
        // YellowLed = parts[9] == '1'; // yellowLed 값이 '1'이면 true, 아니면 false
        // GreenLed = parts[10] == '1'; // greenLed 값이 '1'이면 true, 아니면 false

        print(
            'Distance: $distance, Temperature: $temperature, Humidity: $humidity, Touch: $touch');
        // print('Red LED: $RedLed, Yellow LED: $YellowLed, Green LED: $GreenLed');
      } else {
        print('Received unexpected message format: $payload');
      }
    });
  }

  void publishMessage(String topic, String message) {
    //특정 주제로 메세지를 발행하는 메서드
    final builder =
        MqttClientPayloadBuilder(); // MqttClientPayloadBuilder 객체를 생성. 메세지 페이로드를 구성하는데 사용된다.
    builder.addString(message); // builder 객체에 발행할 문자열 메세지를 추가한다.

    client.publishMessage(
        topic, MqttQos.atLeastOnce, builder.payload!); //메세지를 발행한다.
  }
}
