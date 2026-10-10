# مِحَكّ كشف النصوص المولّدة · AI Text Detection — Open Knowledge Base + Engine

**v3.1-open** · 2026-10-11 · MIT · العربية والإنجليزية · [English summary below](#english-summary)

> **مِجْهَرٌ لا قاضٍ.** هذا المشروع يجمع الدليل ولا يُصدر الحكم — لأن الحكم الآلي في هذا المجال، بحدوده النظرية المبرهَنة وإيجابياته الكاذبة الموثّقة، ظلمٌ يلبس ثوب التقنية.

---

## ما هذا المشروع؟

ثلاث طبقات مفتوحة المصدر بالكامل، كلٌّ تسند الأخرى:

**1. قاعدة المعرفة** (`core/`) — **153 إشارة فريدة** (164 مُجمَّعة عبر الطبقات المنهجية) لكشف النصوص المولّدة، موزّعة على عشرة ملفات JSON مهيكلة: العلامات اللغوية، الإشارات الإحصائية، العلامة المائية (green list)، الكشف الأسود والأبيض، الكواشف التجارية والمفتوحة، الإشارات البنيوية والدلالية، والتصنيف الرئيس. كل نمط له معرّف وآلية كشف ودرجة `confidence` **مصرَّحٌ أنها تقدير تحريري لا احتمال معاير**.

**2. ملفات الثغرات** (`gaps/`) — جوهرة الحزمة: تسعة ملفات تشرح **لماذا يفشل الكشف** قبل أن تشرح كيف ينجح:

| # | الثغرة | لماذا تهمّك |
|---|--------|-------------|
| 1 | الإيجابيات الكاذبة على غير الناطقين | Liang et al. (*Patterns* 2023): متوسط FPR **61.22%** على مقالات TOEFL بشرية — خطر مباشر على كل طالب عربي |
| 2 | حدّ الاستحالة النظري | Sadasivan (TMLR): كلما اقترب توزيع النموذج من البشري تلاشت ميزة أفضل كاشف ممكن |
| 3 | **كشف العربية** | الإشارات الإنجليزية تنهار على العربية — اقرأه أولاً إن كنت عربياً (محدث بأبحاث ومعايير 2026) |
| 4 | النصوص المختلطة | بشري + AI هي الحالة الأشيع واقعياً وأصعبها كشفاً (M4GT-Bench) |
| 5 | الأدلة خارج النص | version history والمسودّات والمناقشة الشفوية أقوى من أي إشارة أسلوبية |
| 6 | نقد الادّعاءات التجارية | RAID (ACL 2024): كل الكواشف المختبَرة تنخدع بهجمات بسيطة |
| 7 | المعايرة ودمج الإشارات | لماذا يحرم جمع درجات الثقة كأنها احتمالات |
| 8 | تقادم الإشارة | "delve" تموت حين يُعاد ضبط النماذج — نصف عمر قصير |
| 9 | **نماذج التفكير وإعادة الصياغة** | حوسبة وقت الاستدلال (o1/R1) وأدوات الـ Humanizers تُسقط الكواشف الإحصائية والمعجمية الصرفة |

**3. المحرك التنفيذي مِجْهَر** (`src/mijhar/`) — **جديد في v3**: قاعدة المعرفة صارت كوداً يعمل. 16 إشارة حتمية، كل واحدة مربوطة بمعرّف نمط حقيقي في `core/`، بلا أي تبعية خارجية:

```bash
# من جذر المستودع — لا تثبيت، لا تبعيات، بايثون ≥3.9 فقط:
PYTHONPATH=src python3 -m mijhar examples/sample_ai_like.txt          # تقرير بشري
PYTHONPATH=src python3 -m mijhar your_document.txt --json             # تقرير JSON
echo "نص للفحص" | PYTHONPATH=src python3 -m mijhar -                  # من stdin

# أو تثبيت دائم:
pip install .   →   mijhar file.txt
```

ماذا يُخرج؟ **دليلاً لا حكماً**: كل إشارة اشتعلت تأتي مع مقتطف من النص يتحقق منه الإنسان بعينه، ومرجعها في القاعدة، و`caveat` يشرح متى تكذب هذه الإشارة تحديداً. وكل تقرير — دون استثناء — يحمل تحذير الإيجابيات الكاذبة على غير الناطقين، ويرفض الاستنتاج على النص القصير، ويشغّل للعربية المسار التجريبي الموسوم فقط.

ما **لن** يُخرجه أبداً، بحكم التصميم والاختبارات: نسبة "احتمال AI"، أو حكم بشري/آلي، أو أي درجة قابلة للاستخدام عتبةَ عقوبة.

---

## لماذا تثق بهذا المستودع؟

لأنه لا يطلب ثقتك — بل يقدّم البرهان الآلي:

**حارس النزاهة** (`scripts/validate_corpus.py`) يشغّل عشرة فحوص حتمية على كل push عبر GitHub Actions، وكل فحص منها يشفّر صنف عطل **شُحن فعلاً** في إصدارات سابقة من هذا المستودع نفسه كي لا يعود: صلاحية كل JSON، مطابقة كل عددٍ مكتوب في النثر للعدّ الفعلي، وجود كل حقل مُعلَن، موت أي رابط ويكي، حذف ما ادُّعي حذفه من git فعلاً، اتساق الإصدار، واكتمال كل ورقة يسمّيها هذا الملف «رئيسية» في المكتبة المرجعية بمعرّف arXiv سليم.

```bash
python3 scripts/validate_corpus.py   # يجب أن يخرج: all integrity checks green
python3 -m pytest tests/ -q          # 12 اختباراً تشمل اختبارات المذهب نفسه
```

تاريخ المستودع نفسه (`CHANGELOG.md`) درسٌ محفوظ عمداً: v1.1 أعلنت ما لم تنفّذ، وv2 أصلحت ثم أخطأت الصنف ذاته، وv3 جعلت التكرار مستحيلاً آلياً. الشفافية عن أخطائنا جزء من المنهج لا اعتذاراً عنه.

---

## المكتبة المرجعية

`reference/key_academic_papers.json`: **14 ورقة محورية**، كل معرّف arXiv فيها تُحقّق منه خارجياً قبل الإدراج، ويحرسه الفحص C9: من GLTR (2019) وKirchenbauer watermark وDetectGPT وFast-DetectGPT وBinoculars وGhostbuster، إلى ورقة الاستحالة (Sadasivan) وورقة التحيز ضد غير الناطقين (Liang) ومعيار RAID العدائي وSynthID-Text المنشور في *Nature*. ولطبقة Obsidian المعرفية الكاملة (16 وظيفة إدراكية مترابطة) افتح المجلد Vault وابدأ من [[HOME]].

---

## الاستخدام المسؤول — غير قابل للتفاوض

1. **لا عقوبة على درجة كاشف، أبداً.** لا من هذا المشروع ولا من غيره.
2. القرار الأكاديمي يتطلب **أدلة خارج النص**: مسودّات، version history، مناقشة شفوية، خط أساس كتابي للطالب (`gaps/05`).
3. للعربية: هذه **نقطة انطلاق بحثية**، لا أداة جاهزة (`gaps/03`). أولوية المجال كلها: بناء متن عربي موسوم.
4. غياب الإشارات لا يثبت بشرية النص، ووجودها لا يثبت آليته — اقرأ `gaps/02` قبل أي نشر.

## المساهمة

اقرأ `CONTRIBUTING.md`. أثمن PR على الإطلاق: **توثيق مصدر نمط واحد** — فالدين التوثيقي الأكبر أن ~1% فقط من الأنماط موثّقة بمصدر لكل نمط. يليه: بيانات عربية موسومة، وإشارات جديدة قابلة للتنفيذ مع اختباراتها.

---

<a name="english-summary"></a>
## English summary

**A microscope, not a judge.** This repository is a fully open, bilingual (Arabic/English) resource for investigating AI-generated text, built on one doctrine: automated verdicts in this domain are unjust — provably bounded in theory (Sadasivan, arXiv:2303.11156) and discriminatory in practice (Liang et al., *Patterns* 2023: 61.22% average false-positive rate on human-written TOEFL essays).

It ships three layers: **(1)** a structured knowledge base of **153 unique documented signals** (164 aggregated across methodological layers) in ten JSON files with an enforced schema; **(2)** nine critical-limitation dossiers covering non-native false positives, the impossibility bound, Arabic detection, mixed human/AI texts, out-of-text evidence, commercial-claims critique, calibration, signal obsolescence, and reasoning models/paraphrasers; **(3)** **mijhar** (مِجْهَر), a deterministic, stdlib-only Python engine implementing 16 signals bound to corpus pattern IDs. It outputs human-verifiable evidence excerpts with per-signal caveats — never a verdict, never P(AI), by design and by test.

Integrity is machine-enforced: `scripts/validate_corpus.py` runs ten checks in CI, each encoding a defect class this repo actually shipped in earlier versions, so declared-vs-enacted drift can never silently recur. Every arXiv ID in the key-papers library was externally verified. Quickstart: `PYTHONPATH=src python3 -m mijhar examples/sample_ai_like.txt`. Most valuable contribution: sourcing a single pattern (see `CONTRIBUTING.md`).

---

**الإسناد:** جمع وتحرير وبناء: Elias Sharar — bio-colab. الاستشهاد: `CITATION.cff`.
**الترخيص:** MIT — والعلم للجميع.
