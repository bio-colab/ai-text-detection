# Security Policy · سياسة الأمان

## Supported Versions · الإصدارات المدعومة

| Version | Supported |
| ------- | --------- |
| 3.1.x   | :white_check_mark: |
| < 3.0   | :x:       |

---

## Security Principles & Threat Model · المبادئ الأمنية ونموذج التهديدات

1. **Zero-Telemetry & 100% Offline (عدم الاتصال التام بالشبكة)**
   - أداة `mijhar` ومكتبة المعجم تعملان محلياً بنسبة 100%. لا تُجري الأداة أي طلبات HTTP، ولا ترسل أي بيانات أو نصوص أو تتبع تحليلي لأي خادم خارجي.
   - All analysis is performed entirely in memory locally. No data leaves your machine.

2. **File Parsing Safety (أمان معالجة الملفات)**
   - دعم ملفات Word (`.docx`) مبني باستخدام مكتبات بايثون القياسية فقط (`zipfile` و`xml.etree.ElementTree`).
   - `xml.etree` في بايثون محمي افتراضياً ضد هجمات الكيانات الخارجية (XXE Injection).
   - نوصي دائماً بمعالجة الملفات الموثوقة لتجنب القنابل المضغوطة (Zip Bombs).

3. **ReDoS (Regular Expression Denial of Service)**
   - تخضع التعبيرات النمطية (Regexes) في محرك `mijhar` لفحص يمنع التراجع الأسي (Catastrophic Backtracking) لضمان عدم استهلاك المعالج عند استقبال نصوص ضخمة أو مكررة.

---

## Reporting a Vulnerability · الإبلاغ عن ثغرة أمنية

إذا اكتشفت ثغرة أمنية أو خطأً قد يسبب تعطيل الخدمة أو تسريب البيانات:
- يُرجى عدم فتح Issue عام للثغرات الأمنية الحساسة.
- تواصل عبر البريد الإلكتروني للمشروع أو افتح [Security Advisory](https://github.com/bio-colab/ai-text-detection/security/advisories/new) خاصاً على GitHub.
- سيتم الرد والتحقق من المشكلة خلال 48 ساعة وإصدار تصحيح في أقرب وقت.
