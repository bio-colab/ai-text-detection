# CONTRIBUTING · دليل المساهمة

**العلم للجميع — والمساهمة الصادقة الصغيرة خير من الادّعاء الكبير.**

This project accepts contributions in **Arabic or English** equally.

---

## القاعدة الذهبية / The golden rule

كل ادّعاء في هذا المستودع يجب أن يكون واحداً من اثنين: **مُنفَّذاً** يمكن لسكربت التحقق إثباته، أو **موسوماً صراحةً** بأنه تقدير تحريري / دين توثيقي. لا وسط بينهما.

Every claim in this repository must be either **enacted** (provable by `scripts/validate_corpus.py`) or **explicitly labeled** as an editorial estimate / documentation debt. Nothing in between. The repository's own history (v1.1 → v2 → v3, see `CHANGELOG.md`) is the cautionary tale.

## قبل أي Pull Request / Before any PR

```bash
python3 scripts/validate_corpus.py    # يجب أن يخرج أخضر / must exit green
python3 -m pytest tests/ -q           # يجب أن تنجح كلها / all must pass
```

CI runs both; a red guard blocks merge.

## أثمن أنواع المساهمات (مرتّبة) / Most valuable PR types (ranked)

1. **توثيق مصدر نمط واحد** — أكبر دين على المستودع: 153 نمطاً فريداً، الموثَّق منها بمصدر لكل نمط ~1%. خذ نمطاً واحداً من `core/`, جد ورقته أو دليله التجريبي، أضف `"sources": ["arxiv:XXXX.XXXXX"]` مع التحقق من المعرّف على arxiv.org فعلاً. **One sourced pattern per PR is the ideal PR.**
2. **بيانات عربية موسومة** — أي عيّنة (بشري مؤكد / مولَّد مؤكد بنموذج معروف) تُقرّبنا من سدّ `gaps/03`، أخطر ثغرة في الحزمة.
3. **إشارة جديدة قابلة للتنفيذ** في `src/mijhar/signals.py`: حتمية، stdlib فقط، مربوطة بـ `corpus_ref` حقيقي، مع اختبار، ومع `caveat` صادق عن مخاطر الإيجابيات الكاذبة.
4. **تحديث تقادم**: إشارة ماتت (نموذج جديد كفّ عن "delve")؟ حدّث `estimated_half_life_months` بدليل، لا تحذف النمط — التاريخ معرفة.
5. **ترجمة أو تحرير لغوي** لأي ملف `gaps/`.

## ما لن يُقبل أبداً / Never accepted

- أي كود أو نص يُخرج **حكماً** (human/AI verdict) أو **احتمالاً** (`P(AI)`, score, percentage). المذهب: مِجْهَر لا قاضٍ. / Any code or doc that outputs a verdict or probability. Doctrine: microscope, not judge.
- جمع أو ضرب قيم `confidence` كأنها احتمالات (اقرأ `gaps/07`).
- معرّف arXiv غير مُتحقَّق منه، أو رقم دقة تجاري بلا مصدر مستقل (اقرأ `gaps/06`).
- إضعاف أيّ تحذير من تحذيرات `_v2_meta` أو `doctrine` — تشديدها بدليل مرحَّب به، تخفيفها لا.
- محتوى يُعين على معاقبة طالب بناءً على درجة كاشف وحدها.

## أسلوب / Style

- Python: stdlib فقط في `src/` و`scripts/` (قابلية التشغيل في أي مكان جزء من الرسالة). pytest في `tests/` فقط.
- JSON: طابق `schema/pattern_file.schema.json`؛ معرّفات الأنماط `XX-NNN`.
- العربية: التنوين على الحرف الأخير دائماً (حقاً لا حقًا).
- التواضع المعرفي إلزامي: كل إشارة جديدة تُشحن مع `caveat` يشرح متى تكذب.

## الترخيص / License

بمساهمتك توافق على ترخيص مساهمتك بـ MIT. / By contributing you agree to license your contribution under MIT.
