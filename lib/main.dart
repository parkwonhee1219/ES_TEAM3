import 'package:embeddedsystem_5th_project/monitoring.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(),
      routes: {
        "/monitoring": (context) => const Monitoring(),
      },
      home: const MyHomePage(title: 'Embedded System TEAM3'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      //backgroundColor: Colors.transparent,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        //backgroundColor: Colors.transparent,
        backgroundColor: Colors.green,
        elevation: 0,
        title: Text(widget.title,style:GoogleFonts.lato(fontSize: 19.0,color: Colors.black),)
      ),
      // body: Container(
      //   decoration: const BoxDecoration(
      //     gradient: LinearGradient(colors: [
      //        Color.fromARGB(255, 255, 91, 65), // 시작 색상
      //        Color.fromARGB(255, 230, 147, 92),
      //     ],
      //     begin: Alignment.topCenter,
      //     end: Alignment.bottomCenter,)
      //   ),
      // ),
      body:  Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(onPressed: (){
              Navigator.of(context).pushNamed("/monitoring");
            }, child: Text('monitoring'))
          ],
        ),
      ),
    );
  }
}
