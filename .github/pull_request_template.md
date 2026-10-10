## وصف المساهمة / Description of Changes
<!-- صف بإيجاز ما تم تعديله أو إضافته / Briefly summarize the changes made -->

## نوع التغيير / Type of Change
- [ ] توثيق مصدر لنمط موجود / Sourcing an existing pattern (`core/*.json`)
- [ ] إضافة أو تحسين إشارة أسلوبية في مِجْهَر / Signal update in `src/mijhar`
- [ ] تحديث أو إضافة في الثغرات والدراسات العربية / Arabic gap update (`gaps/03_*.md`)
- [ ] إصلاح خطأ برمجي / Bug fix
- [ ] تحسين التوثيق أو الأمثلة / Documentation or examples improvement

## قائمة التحقق الإلزامية / Mandatory Checklist
- [ ] تم تشغيل سكربت النزاهة بنجاح: `python scripts/validate_corpus.py` (جميع الفحوصات خضراء).
- [ ] تم تشغيل جميع الاختبارات بنجاح: `pytest tests/` (15+ tests pass).
- [ ] **عقيدة مِجْهَر**: التغيير خالٍ تماماً من أي حكم آلي (verdict) أو احتمالية $P(\text{AI})$ أو جمع درجات الثقة كاحتمالات.
- [ ] في حال إضافة أو تعديل إشارة: تم تضمين `caveat` علمي صريح يوضح حالات الخطأ (الإيجابيات الكاذبة لدى البشر).
- [ ] في حال إضافة مراجع: تم التأكد من صحة معرّفات arXiv في `arxiv.org`.
