import 'package:flutter/material.dart';


class TestApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Gradient Background',
      home: Scaffold(
        body: Container(
          decoration: const BoxDecoration(
            gradient: LinearGradient(
              colors: [
                Color.fromARGB(255, 27, 137, 226), // 시작 색상
                Color.fromARGB(255, 236, 242, 247), // 끝 색상
              ],
              begin: Alignment.topLeft, // 그라데이션 시작 위치
              end: Alignment.bottomRight, // 그라데이션 끝 위치
            ),
          ),
        ),
      ),
    );
  }
}
