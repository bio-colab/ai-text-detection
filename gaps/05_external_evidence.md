# الثغرة 5: أدلة المصدر خارج النص نفسه (الأقوى عملياً)

## المشكلة
ركز كلا الوكيلين (أ وب) على الإشارات **الداخلية** في النص فقط (statistical, linguistic, semantic). 

لكن في النزاهة الأكاديمية الحقيقية، الأدلة الخارجية غالباً **أقوى وأكثر موثوقية**:
- سجل التعديلات في Google Docs / Word (edit history, paste events, timing).
- بيانات التعريف (metadata) في الملف.
- مقارنة مع كتابات سابقة للطالب نفسه (stylistic fingerprint).
- سلوك الطالب في الامتحان الشفوي أو المناقشة.
- استخدام أدوات "AI humanizer" معروفة (يمكن كشف بعضها عبر artifacts معينة).

## ما أضفناه (جديد)
- قسم كامل في الـ README الرئيسي يؤكد أن "Internal signals هي أضعف حلقة".
- توصية ببناء "Student Writing Profile" system (جمع baseline writings + metadata analysis).
- اقتراح دمج أدوات مثل " originality reports + version history + oral defense".

## التوصيات العملية لـ مِحَكّ / الجامعات
1. **الأولوية الأولى:** اطلب version history أو Google Doc link دائماً.
2. أنشئ قاعدة بيانات لأسلوب كل طالب عبر السنوات.
3. استخدم الإشارات الداخلية كـ "flag للمراجعة البشرية" وليس كـ "دليل إدانة".
4. في الامتحانات عالية الخطورة: oral defense إلزامي لأي flag.

هذا يجعل النظام أكثر عدلاً وأقل عرضة للخطأ.

---

## Brain links
- Doctrine hub: [[moc-Gaps]] → [[00_FULL_BRAIN]]
- Decision: [[fn-Making Decision]] → [[protocol-Human Review]]
- Pipeline: [[pipeline-Detect Text Cycle]]
