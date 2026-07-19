# الثغرة 8: تقادم الإشارة (نصف عمر الإشارات)

## المشكلة
الإشارات لها "نصف عمر" قصير:
- "delve" و "tapestry" و "crucial" كانت قوية 2023-2024 → أصبحت أضعف 2025-2026 لأن النماذج (و prompt engineering) تتجنبها الآن.
- em-dash overuse تم تقليله في Claude/GPT-4o بعد أن اشتهر كعلامة.
- أي إشارة أسلوبية أو إحصائية تُكتشف → تُستهدف في الجيل التالي أو عبر "humanizer" prompts.

هذا يجعل أي "قائمة ثابتة" من الإشارات (مثل هذه الحزمة) **تنتهي صلاحيتها** خلال 6-18 شهراً بدون صيانة مستمرة.

## ما أضفناه (جديد)
- آلية "self-review + update loop" موصى بها في الـ README.
- حقل "estimated_half_life_months" في بعض الأنماط الرئيسية في الـ JSONs.
- دعوة لـ "living taxonomy" يُحدث كل 3-6 أشهر.

## التوصيات العملية
- لا تبنِ نظاماً صلباً على إشارات 2026 فقط.
- أنشئ فريق "رصد إشارات" (أو استخدم community مثل هذا المشروع).
- ركز على الإشارات الأساسية الأكثر استقراراً: 
  - Watermark z-score (إذا وجد)
  - Binoculars / Fast-DetectGPT (أكثر مقاومة نسبياً)
  - External evidence (version history)
  - Human judgment + oral defense
- راقب أوراق arXiv الجديدة (خاصة surveys 2025-2026) وحدث القائمة.

**الخلاصة النهائية:** أفضل "كاشف" هو نظام متكامل يجمع بين التكنولوجيا المتطورة + الإجراءات البشرية + الردع الثقافي + الشفافية، وليس قائمة إشارات ثابتة.

---

## Brain links
- Doctrine hub: [[moc-Gaps]] → [[00_FULL_BRAIN]]
- Decision: [[fn-Making Decision]] → [[protocol-Human Review]]
- Pipeline: [[pipeline-Detect Text Cycle]]
