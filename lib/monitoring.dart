import 'dart:async';

import 'package:embeddedsystem_5th_project/mqtt.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

// 전역 변수 선언
String distance = ''; // distance 값
String temperature = '12'; // temperature 값
String humidity = '12'; // humidity 값
String touch = ''; // touch 값

bool RedLed = false;
bool YellowLed = false;
bool GreenLed = false;
bool isAutoMode = true; // 자동 모드 여부

class Monitoring extends StatefulWidget {
  const Monitoring({super.key});

  @override
  State<Monitoring> createState() => _MonitoringState();
}

class _MonitoringState extends State<Monitoring> {
  @override
  void initState() {
    super.initState();
    Mqtt mqtt = Mqtt();
    mqtt.connect('start/0/0/0/0/0'); // 구독만 하면 됨

    // Timer를 사용하여 매초 UI를 갱신 및 자동 모드 동작 처리
    Timer.periodic(Duration(seconds: 1), (timer) {
      setState(() {
        double temp = double.parse(temperature);
        double hum = double.parse(humidity);

        //자동모드
        if (isAutoMode) {
          Mqtt mqtt = Mqtt(); // MQTT 객체 생성

          // 온도에 따른 에어컨과 히터 자동 제어
          if (temp != null && hum != null) {
            if (temp >= 30 && hum >= 60) {
              RedLed = true;
              YellowLed = false;
              GreenLed = true;
              mqtt.connect('RedLed/true/YellowLed/false/GreenLed/true');
            } else if (temp >= 30 && hum < 60) {
              RedLed = true;
              YellowLed = false;
              GreenLed = false;
              mqtt.connect('RedLed/true/YellowLed/false/GreenLed/false');
            } else if (temp < 30 && hum >= 60) {
              RedLed = false;
              YellowLed = true;
              GreenLed = true;
              mqtt.connect('RedLed/false/YellowLed/true/GreenLed/true');
            } else if (temp < 30 && hum < 60) {
              RedLed = false;
              YellowLed = true;
              GreenLed = false;
              mqtt.connect('RedLed/false/YellowLed/true/GreenLed/false');
            }
          }
        }
      });
    });
  }

  void LedOFF(String LED) {
    setState(() {
      if (LED == 'RedLed') {
        RedLed = !RedLed;
      } else if (LED == 'YellowLed') {
        YellowLed = !YellowLed;
      } else if (LED == 'GreenLed') {
        GreenLed = !GreenLed;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    // UI 구성
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color.fromARGB(255, 39, 204, 116),
        title: Text(
          'Sensor Monitoring',
          style: GoogleFonts.lato(fontSize: 19.0),
        ),
      ),
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Expanded(
                flex: 2, // 1/3 공간
                child: Container(
                    alignment: Alignment.centerLeft, // 왼쪽 정렬
                    padding: const EdgeInsets.all(16.0), // 여백 추가
                    child: Column(
                      children: [
                        const Text(
                          "<Monitor>",
                        ),
                        Text("온도 : $temperature"),
                        Text("습도 : $humidity"),
                        Text("거리 : $distance"),
                        Text("터치 : $touch"),
                      ],
                    )),
              ),
              Expanded(
                flex: 1,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text("Auto Mode"),
                    Switch(
                      value: isAutoMode,
                      onChanged: (value) {
                        setState(() {
                          isAutoMode = value;
                        });
                      },
                    ),
                  ],
                ),
              ),
              Expanded(
                  flex: 3,
                  child: Container(
                    alignment: Alignment.center,
                    padding: const EdgeInsets.all(10.0),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Icon(Icons.lightbulb,
                            size: 100.0,
                            color: RedLed ? Colors.red : Colors.grey),
                        const SizedBox(width: 10),
                        Icon(Icons.lightbulb,
                            size: 100.0,
                            color: YellowLed ? Colors.yellow : Colors.grey),
                        const SizedBox(width: 10),
                        Icon(Icons.lightbulb,
                            size: 100.0,
                            color: GreenLed ? Colors.green : Colors.grey),
                        const SizedBox(width: 10),
                      ],
                    ),
                  )),
              Expanded(
                  flex: 3,
                  child: Container(
                      alignment: Alignment.center,
                      padding: const EdgeInsets.all(10.0),
                      child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: <Widget>[
                            SwitchListTile(
                              title: const Text('Aircon'),
                              value: RedLed,
                              onChanged: isAutoMode
                                  ? null
                                  : (value) {
                                      LedOFF('RedLed');
                                      print('RedLed is $RedLed');
                                      Mqtt mqtt = Mqtt();
                                      mqtt.connect('RedLed/$RedLed/YellowLed/$YellowLed/GreenLed/$GreenLed');
                                    },
                              activeColor: Colors.red,
                            ),
                            SwitchListTile(
                              title: const Text('Heater'),
                              value: YellowLed,
                              onChanged: isAutoMode
                                  ? null
                                  : (value) {
                                      LedOFF('YellowLed');
                                      print('YellowLed YellowLedis $YellowLed');
                                      Mqtt mqtt = Mqtt();
                                      mqtt.connect('RedLed/$RedLed/YellowLed/$YellowLed/GreenLed/$GreenLed');
                                    },
                              activeColor: Colors.yellow,
                            ),
                            SwitchListTile(
                              title: const Text('Dehumidifier'),
                              value: GreenLed,
                              onChanged: isAutoMode
                                  ? null
                                  : (value) {
                                      LedOFF('GreenLed');
                                      print('GreenLed is $GreenLed');
                                      Mqtt mqtt = Mqtt();
                                      mqtt.connect('RedLed/$RedLed/YellowLed/$YellowLed/GreenLed/$GreenLed');
                                    },
                              activeColor: Colors.green,
                            )
                          ]))),
            ],
          ),
        ),
      ),
    );
  }
}
