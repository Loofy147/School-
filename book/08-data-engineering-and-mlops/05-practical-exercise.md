# Practical Exercise for Layer 8
# تمرين عملي للطبقة الثامنة

## Goal / الهدف

To design a basic data and MLOps pipeline for the fictional "Smart Home Hub" system.

لتصميم خط أنابيب بيانات و MLOps أساسي لنظام "مركز المنزل الذكي" الخيالي.

## Exercise Steps / خطوات التمرين

1.  **Design an ETL/ELT Pipeline:**
    -   Imagine you need to collect device usage data from all the Smart Home Hubs in the field and load it into a central data warehouse for analysis.
    -   Sketch out the key stages of an ETL or ELT pipeline for this process.
    -   Example stages: "Hubs upload daily usage data to a cloud storage bucket," "A daily batch job extracts the data," "The data is cleaned and transformed (e.g., anonymized, aggregated)," "The transformed data is loaded into a 'device_usage' table in the data warehouse."

2.  **Design a Continuous Training Pipeline:**
    -   Building on the previous step, design a simple continuous training pipeline that automatically retrains a "usage prediction" model whenever new data is available.
    -   Example stages: "A trigger fires when the 'device_usage' table is updated," "A training job is launched," "The new model is evaluated against a test dataset," "If the new model is better, it is promoted to production."

3.  **Define a Data Quality Monitoring Strategy:**
    -   For the `device_usage` table, list three data quality checks you would implement to ensure the data is reliable.
    -   Example checks: "The 'user_id' column should never be null," "The 'event_timestamp' should always be within the last 24 hours," "The 'device_type' column should only contain valid device types."

## Deliverables / المخرجات

-   A `data-pipeline.md` file with your ETL/ELT pipeline design.
-   An `mlops-pipeline.md` file with your continuous training pipeline design.
-   A `data-quality.md` file with your data quality monitoring strategy.

## 1. تصميم خط أنابيب ETL / ELT:
    -   تخيل أنك بحاجة إلى جمع بيانات استخدام الجهاز من جميع مراكز المنزل الذكي في الميدان وتحميلها في مستودع بيانات مركزي للتحليل.
    -   ارسم المراحل الرئيسية لخط أنابيب ETL أو ELT لهذه العملية.
    -   أمثلة على المراحل: "تقوم المراكز بتحميل بيانات الاستخدام اليومية إلى دلو تخزين سحابي"، "تقوم وظيفة دفعية يومية باستخراج البيانات"، "يتم تنظيف البيانات وتحويلها (على سبيل المثال، إخفاء الهوية، والتجميع)"، "يتم تحميل البيانات المحولة في جدول 'device_usage' في مستودع البيانات".

## 2. تصميم خط أنابيب تدريب مستمر:
    -   بناءً على الخطوة السابقة، قم بتصميم خط أنابيب تدريب مستمر بسيط يعيد تدريب نموذج "تنبؤ الاستخدام" تلقائيًا كلما توفرت بيانات جديدة.
    -   أمثلة على المراحل: "يتم إطلاق مشغل عند تحديث جدول 'device_usage'"، "يتم إطلاق مهمة تدريب"، "يتم تقييم النموذج الجديد مقابل مجموعة بيانات اختبار"، "إذا كان النموذج الجديد أفضل، يتم ترقيته إلى الإنتاج".

## 3. تحديد استراتيجية مراقبة جودة البيانات:
    -   لجدول `device_usage`، اذكر ثلاثة فحوصات لجودة البيانات ستنفذها لضمان موثوقية البيانات.
    -   أمثلة على الفحوصات: "يجب ألا يكون عمود 'user_id' فارغًا أبدًا"، "يجب أن يكون 'event_timestamp' دائمًا خلال الـ 24 ساعة الماضية"، "يجب أن يحتوي عمود 'device_type' فقط على أنواع أجهزة صالحة".

## المخرجات

-   ملف `data-pipeline.md` مع تصميم خط أنابيب ETL / ELT الخاص بك.
-   ملف `mlops-pipeline.md` مع تصميم خط أنابيب التدريب المستمر الخاص بك.
-   ملف `data-quality.md` مع استراتيجية مراقبة جودة البيانات الخاصة بك.
