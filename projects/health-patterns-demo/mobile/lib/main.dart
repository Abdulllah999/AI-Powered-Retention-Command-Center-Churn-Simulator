import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
void main() => runApp(const MaterialApp(home: PatternDemo()));
class PatternDemo extends StatefulWidget {
  const PatternDemo({super.key});
  @override
  State<PatternDemo> createState() => _PatternDemoState();
}
class _PatternDemoState extends State<PatternDemo> {
  final names = ['Fever', 'Cough', 'Sneezing', 'Itchy eyes', 'Fatigue'];
  final values = List<bool>.filled(5, false);
  String output = 'Use fictional cases only. This is not a diagnosis.';
  bool busy = false;
  Future<void> explore() async {
    setState(() { busy = true; });
    try {
      const base = String.fromEnvironment('API_BASE', defaultValue: 'http://10.0.2.2:5003');
      final response = await http.post(Uri.parse('$base/api/pattern'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'features': values.map((v) => v ? 1 : 0).toList()}))
        .timeout(const Duration(seconds: 10));
      if (mounted) setState(() { output = const JsonEncoder.withIndent('  ').convert(jsonDecode(response.body)); });
    } catch (_) {
      if (mounted) setState(() { output = 'Cannot reach the local demo server. Check API_BASE.'; });
    } finally {
      if (mounted) setState(() { busy = false; });
    }
  }
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Health Pattern Explorer')),
    body: ListView(padding: const EdgeInsets.all(24), children: [
      const Text('Synthetic educational model. Not a clinical tool or AI clinician.'),
      ...List.generate(5, (i) => CheckboxListTile(title: Text(names[i]), value: values[i],
        onChanged: busy ? null : (v) => setState(() { values[i] = v ?? false; }))),
      ElevatedButton(onPressed: busy ? null : explore, child: Text(busy ? 'Loading…' : 'Explore fictional pattern')),
      const SizedBox(height: 20), SelectableText(output),
    ]));
}
