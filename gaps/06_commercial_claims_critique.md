# الثغرة 6: نقد ادّعاءات الدقة التجارية ومنهجية القياس

## المشكلة
الأدوات التجارية (GPTZero, Originality.ai, Turnitin, Winston AI...) تنشر أرقاماً مثل "99.98% accuracy" أو "1% FPR".

هذه الأرقام:
- محسوبة على datasets "نظيفة" (AI كامل vs Human أصلي) — لا تعكس الواقع المختلط أو non-native.
- غالباً ما تكون على نماذج قديمة (GPT-3.5) وليس الأحدث.
- لا تفصح عن الـ base rate أو الـ domain أو معدل الخطأ حسب طول النص.
- تتغير باستمرار مع تحديثات النماذج (الدقة تنخفض).

Turnitin مثلاً يعتمد على "segmentation + RoBERTa" لكن دراسات مستقلة تظهر FPR أعلى على non-native academic writing.

## ما أضفناه
- قسم في الـ core/06_commercial_detectors.json يحذر من "claimed vs independent eval".
- في الـ gaps: دعوة لـ "independent auditing" للأدوات التجارية في السياق العربي.

## التوصيات
- لا تصدق الأرقام التجارية كما هي. اطلب تقارير مستقلة (مثل من HuggingFace Open LLM Leaderboard style للكشف).
- للمؤسسات: اختبر أي أداة على عينة محلية (طلاب عراقيين) قبل الشراء.
- الأفضل: ensemble مفتوح (Binoculars + Fast-DetectGPT + TTR + human review) + transparency.

**خلاصة:** "الدقة" بدون سياق = تسويق. الشفافية والمعايرة المحلية أهم.

---

## Brain links
- Doctrine hub: [[moc-Gaps]] → [[00_FULL_BRAIN]]
- Decision: [[fn-Making Decision]] → [[protocol-Human Review]]
- Pipeline: [[pipeline-Detect Text Cycle]]
