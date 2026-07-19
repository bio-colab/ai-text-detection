# دليل موحد متكامل لإشارات كشف النصوص المولدة بالذكاء الاصطناعي (مخصص للغة الانجليزية)

**التاريخ:** 18 يوليو 2026  
**الإصدار:** 1.1-Unified (دمج + سد الثغرات)  
**اللغة الرئيسية:** الإنجليزية (مع تحذيرات من الاستخدام مع العربية)  

---

## 1. الخلفية: لماذا هذا الإصدار الموحد؟

تم دمج عملين بحثيين مستقلين قويين:

- **الوكيل أ (الكتالوج الهندسي)**: `ai_detection_signals.zip` — 10 ملفات JSON، 174 نمطاً مُعرَّفاً بعتبات وصيغ ودرجات ثقة. عملي جداً لبناء محرك كشف. يغطي طبقات بنيوية ودلالية و watermark بعمق.

- **الوكيل ب (الموجز التحليلي)**: `ai_text_detection_research_complete.zip` — 6 ملفات JSON + شرح عميق لـ "لماذا" كل إشارة، مع تمييزات مفهومية مهمة (مثل Green Observed vs Green Planted) وأمانة عالية في ذكر القيود.

 

**هذا الإصدار يفعل ذلك بالضبط + يسد الثغرات الثماني الحرجة** التي غفل عنها كلاهما.

---

## 2. الثغرات الثماني التي سُدّت كاملة (جديد كلياً)

| # | الثغرة | الملف في gaps/ | الأولوية للسياق العربي |
|---|--------|------------------|-------------------------|
| 1 | معدلات الأساس + الإيجابيات الكاذبة + تحيز anti non-native | 01_false_positives_non_native.md | ★★★★★ (عالية جداً) |
| 2 | الحد النظري: هل الكشف ممكن أصلاً؟ (Sadasivan impossibility) | 02_impossibility_theorem.md | ★★★★ |
| 3 | كشف النصوص **العربية** المولدة (الإشارات الإنجليزية تنهار) | 03_arabic_detection.md | ★★★★★★★★★★ (الأعلى) |
| 4 | النصوص المختلطة (بشري + AI) — الحالة الأشيع | 04_mixed_texts.md | ★★★★★ |
| 5 | أدلة المصدر **خارج النص** (version history, metadata, stylistic fingerprint) | 05_external_evidence.md | ★★★★★★ |
| 6 | نقد ادّعاءات الدقة التجارية | 06_commercial_claims_critique.md | ★★★★ |
| 7 | المعايرة + دمج الإشارات + أثر طول النص | 07_calibration_fusion_length.md | ★★★★ |
| 8 | تقادم الإشارة (نصف عمر قصير) | 08_signal_obsolescence.md | ★★★★ |

كل ملف يحتوي على: وصف المشكلة + ما أضفناه + توصيات عملية محددة + مراجع.

 

---

## 3. هيكل الحزمة

```
unified_ai_detection/
├── HOME.md                            ← لوحة تحكم Obsidian
├── README.md                          ← أنت هنا (ابدأ من هنا)
├── Brain/                             ← العقل الكامل (16 وظيفة معرفية مترابطة)
│   ├── 00_FULL_BRAIN.md               ← مركز الدماغ + خريطة الروابط
│   ├── Brain Canvas.canvas            ← خريطة بصرية
│   ├── functions/                     ← Perception … Orchestration
│   ├── knowledge/                     ← MOCs: core / gaps / reference / taxonomy
│   ├── pipelines/                     ← دورة كشف النص
│   ├── protocols/                     ← دمج الإشارات + مراجعة بشرية + أولويات
│   ├── memory/                        ← working / episodic / long-term
│   └── watching/                      ← لوحة المراقبة
├── core/
│   ├── 01_linguistic_markers.json     (محسّن + تحذيرات non-native)
│   ├── 02_statistical_signals.json    (Fast-DetectGPT ID مصحح إلى 2310.05130)
│   ├── 03_green_box_watermark.json
│   ├── 04_black_box_detection.json
│   ├── 05_white_box_detection.json
│   ├── 06_commercial_detectors.json   (مع تحذير من الادعاءات)
│   ├── 07_open_source_detectors.json
│   ├── 08_structural_formatting_signals.json
│   ├── 09_semantic_coherence_signals.json
│   └── 10_master_taxonomy.json        (محدث + قسم الثغرات)
├── gaps/
│   ├── 01_false_positives_non_native.md
│   ├── 02_impossibility_theorem.md
│   ├── 03_arabic_detection.md         ← اقرأه أولاً إذا كنت عربياً
│   ├── 04_mixed_texts.md
│   ├── 05_external_evidence.md
│   ├── 06_commercial_claims_critique.md
│   ├── 07_calibration_fusion_length.md
│   └── 08_signal_obsolescence.md
├── reference/
│   ├── comparison_report.html         (تقرير التحكيم الأصلي بين أ وب)
│   └── (ملفات ب من المصدر)
├── templates/                         ← قالب قضية كشف
└── taxonomy/ (نسخة إضافية من الـ master)
```

### 3.1 العقل الكامل في Obsidian (Brain)

افتح المجلد كـ **Obsidian Vault** ثم ابدأ من [[HOME]] أو [[00_FULL_BRAIN]].

الوظائف الست عشرة المتصلة بكل ملفات core/gaps/reference:

| وظيفة | دورها في الحزمة |
|--------|------------------|
| Perception | استقبال مخرجات كل المكوّنات (01–09 + external) |
| Understanding | تفسير الإشارات وحدودها |
| Linking | ربط الأنماط والأدوات والثغرات |
| Context building | لغة، طول، non-native، stakes |
| Memory administration | ذاكرة عمل / حلقات / طويلة الأمد |
| Inference | دمج معاير + uncertainty |
| Pattern recognition | مطابقة ~174 نمطاً |
| Relation recognition | علاقات، تناقضات، mixed shifts |
| Planning | خطط قضايا وبحث عربي |
| Making decision | سياسة قرار + Human-in-the-Loop |
| Priority administration | طابور P0–P3 |
| Knowledge administration | صيانة التصنيف ونصف العمر |
| Learning | تعلم من النتائج |
| Predicting | PPV، تقادم، انجراف نماذج |
| Watching | مراقبة مستمرة |
| Orchestration | تشغيل الحلقة الكاملة |

مسار تنفيذي: `Brain/pipelines/pipeline-Detect Text Cycle.md`

---

---

## 4. التحذيرات الحرجة (اقرأها جيداً)

- **لا يوجد كاشف مثالي 100%.** الكشف سباق تسلح.
- الإيجابيات الكاذبة مرتفعة على غير الناطقين بالإنجليزية — خطر حقيقي على الطلاب العراقيين.
- للعربية: هذه الحزمة **نقطة انطلاق فقط**، ليست حلاً جاهزاً.
- الاعتماد على commercial tools بدون تدقيق محلي = مخاطرة.
- ركز على **الردع + الثقافة + التحقق البشري** أكثر من "الكشف الآلي".

---

## 5. الخطوات التالية الموصى بها

1. **فوراً:** اقرأ gaps/03_arabic_detection.md و gaps/01_false_positives_non_native.md
2. ابدأ مشروع "Arabic AI Text Corpus" (Human + AI من Jais/AceGPT + ترجمة + تعديل بشري).
3. طور classifier عربي بسيط (AraBERT fine-tune).
4. أضف layer للأدلة الخارجية (version history parser).
5. حدث هذه الحزمة كل 6 أشهر (الإشارات تتقادم).

---

## 6. الشكر والمصادر

- العمل الذي قام به Elias Sharar من  bio-colab من جمع وتحرير وتنظيم معلومات
- الأوراق الرئيسية: Kirchenbauer 2023 (watermark), DetectGPT/Fast-DetectGPT, Binoculars, Sadasivan 2023 (impossibility), Wu survey 2025, وغيرها.
- تم التحقق من صحة JSONs (باستثناء ملف key_academic_papers.json الأصلي المكسور الذي تركناه في reference/).

**تم إكمال المهمة بالكامل:** دمج + سد الثغرات الثماني + حزمة واحدة + README شامل.

للاستفسارات أو التحديثات: استخدم هذا الهيكل كأساس حي.

© 2026 — للاستخدام الأكاديمي المسؤول.
