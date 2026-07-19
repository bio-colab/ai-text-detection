# دليل شامل لإشارات كشف النصوص الإنجليزية المولدة بالذكاء الاصطناعي

تاريخ: 2026-07-18 00:07
إجمالي الأنماط: 174 نمط عبر 9 ملفات تخصصية + taxonomy
المصادر: arxiv 2023-2026, HuggingFace, GitHub, Wikipedia, أدوات تجارية

## آلية منع التوقف المبكر
كما طلبت:
1. عداد تغطية كل ملف >=15 نمط
2. checklist مصادر: arxiv + GitHub + HF + Wiki + commercial >=3 per file
3. حلقة مراجعة ذاتية بعد كل بحث: هل غطيت كل الجوانب؟ هل أتممت كل المهام؟ هل صنفتها بشكل صحيح؟
4. 9 وكلاء فرعيين متوازيين كل واحد 3-5 استعلامات browser.search
5. إعادة بحث عند النقص

```
while total_patterns < 150 or coverage <0.95:
    search()
    classify()
    review()
    if not covered: refine_query()
```

## تصنيف الملفات

| رقم | ملف | فئة | ماذا يحتوي | نوع الكشف |
|-----|------|------|-------------|------------|
| 01 | 01_linguistic_markers.json | العلامات | delve tapestry crucial moreover em dash | علامات |
| 02 | 02_statistical_signals.json | إحصائية | Perplexity Burstiness GLTR DetectGPT Binoculars Min-K% | statistical |
| 03 | 03_green_box_watermark.json | الصندوق الأخضر | KGW green/red gamma delta z-score SynthID tournament attacks | green box |
| 04 | 04_black_box_detection.json | الصندوق الأسود | DetectGPT Fast-DetectGPT DNA-GPT Ghostbuster Binoculars RoBERTa | black box |
| 05 | 05_white_box_detection.json | الصندوق الأبيض | log prob rank LogRank LRR NPR Min-K% watermark key | white box |
| 06 | 06_commercial_detectors.json | تجارية | GPTZero Turnitin Originality Copyleaks Winston ZeroGPT | commercial |
| 07 | 07_open_source_detectors.json | مفتوحة | roberta MAGE M4 HC3 GLTR Binoculars | open source |
| 08 | 08_structural_formatting_signals.json | بنيوية | emoji bullet tricolon uniform paragraph bold em dash | formatting |
| 09 | 09_semantic_coherence_signals.json | دلالية | hallucination fabricated citations generic no personal hedging safe | semantic |
| 10 | 10_master_taxonomy.json | رئيسي | يجمع كل شيء + cross-reference + mechanism | taxonomy |

## المصادر الرئيسية

arxiv: 2412.11385 Delve, 2510.05136 Survey, 2301.11305 DetectGPT, 2310.05189 Fast-DetectGPT, 1906.04043 GLTR, 2401.12070 Binoculars, 2306.05540 DetectLLM, 2305.17359 DNA-GPT, 2305.15047 Ghostbuster, 2301.10226 KGW Watermark, 2402.14083 SynthID, 2603.03410 SynthID Analysis, 2310.10669 Unigram, 2409.16914 TOCSIN, 2310.16789 Min-K%

HuggingFace: roberta-base/large-openai-detector, chatgpt-detector-roberta HC3, desklib RAID, MAGE 27 LLMs, RADAR, Falcon-7B, GPT-2/Neo-2.7B/J-6B, T5-3B, synthid-text, Gemma-7B

GitHub: CWOnline/AIWords, yotamgutman/ai-free-writing-checklist, lm-watermarking, WaterBench, detect-gpt, fast-detect-gpt, Binoculars, DNA-GPT, ghostbuster, gltr, MAGE, chatgpt-comparison-detection, human_detectors, StyleDecipher, StealthHumanizer

Wikipedia: Perplexity, Burstiness, Stylometry, Entropy, AI content detection, Digital watermarking, Hash, Bernoulli, Tricolon, Markdown, Five-paragraph essay

Commercial: GPTZero 3.3M sample 50-269x words, Turnitin 200M papers 1% FPR, Originality, Copyleaks 30+ lang, Winston 99.98% HUMN-1, ZeroGPT

## استخدام

import json
with open('03_green_box_watermark.json') as f:
    green = json.load(f)
# z = (green_count - gamma*T)/sqrt(T*gamma*(1-gamma)) >4 => watermarked
# Binoculars B = PPL_M1 / X-PPL <0.9 => AI
# Perplexity <40 => AI

## ملاحظات
- Perplexity تفشل ضد non-native
- RoBERTa لا تعمم على نماذج جديدة
- إضافة typos تقلل Turnitin 27%
- Paraphrase 5 rounds PEGASUS يكسر KGW
- أفضل ensemble: Binoculars + Fast-DetectGPT + TTR + z-score

ZIP يحتوي 10 JSON + README
