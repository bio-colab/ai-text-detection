# الثغرة 7: المعايرة (Calibration)، دمج الإشارات، وأثر طول النص

## المشكلة
- **المعايرة:** معظم الكواشف تعطي "score" غير معاير (ليس احتمالاً حقيقياً). score=0.9 لا يعني P(AI)=90%.
- **الدمج:** كيف تدمج 10-20 إشارة؟ الجمع البسيط (كما في بعض commercial) ساذج. يحتاج weights + meta-classifier أو Bayesian fusion.
- **طول النص:** الإشارات الإحصائية (PPL, curvature, burstiness) غير موثوقة على نصوص <300-500 كلمة. الإشارات البنيوية (emoji, bold) أقوى على نصوص قصيرة. الدلالية (hallucination) تحتاج سياق كافٍ.

## ما أضفناه
- في الـ taxonomy: حقل جديد "text_length_sensitivity" لكل نمط.
- اقتراح إطار دمج بسيط: weighted average مع calibration layer (Platt scaling أو isotonic regression).
- تحذير: لا تستخدم statistical signals وحدها على نصوص قصيرة (<250 كلمة).

## التوصيات العملية
1. قسم النص إلى segments وقيم كل segment على حدة.
2. استخدم meta-model بسيط (logistic regression) مدرب على features + labels محلية.
3. للنصوص القصيرة: ركز على linguistic + structural + semantic (الثغرات 1,8,9).
4. أضف "uncertainty" band: إذا كان الـ confidence منخفضاً → human review إلزامي.

هذا يجعل النظام أكثر نضجاً وأقل عرضة للـ overconfidence.

---

## Brain links
- Doctrine hub: [[moc-Gaps]] → [[00_FULL_BRAIN]]
- Decision: [[fn-Making Decision]] → [[protocol-Human Review]]
- Pipeline: [[pipeline-Detect Text Cycle]]
