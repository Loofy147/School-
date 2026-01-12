# Capstone Brief - Top-Down Systems Engineering (Student Capstone)
# بيان مشروع التخرج - هندسة النظم من القمة إلى القاعدة

## Vision (given to student) / الرؤية (مقدمة للطالب)
Design and deliver a **Privacy-aware Intelligent Service Platform** that accepts user requests, applies a recommendation or classification ML model, and returns results while satisfying security and compliance constraints.
صمّم وسلّم **منصة خدمية ذكية مهتمة بالخصوصية** تستقبل طلبات المستخدم، تطبّق نموذج توصية أو تصنيف، وتعيد النتائج مع الامتثال لمتطلبات الأمان والامتثال.

## Acceptance Criteria (minimum) / معايير القبول (الحد الأدنى)
1. A Vision document (1-2 pages) describing the business goal and KPIs. / وثيقة رؤية 1-2 صفحة تصف الهدف التجاري ومقاييس الأداء.
2. At least one ADR describing a major architectural decision (ADR-ID). / على الأقل ADR واحد يصف قرار معماري رئيسي.
3. A Traceability Matrix (RTM) showing how Vision requirements map to ADRs, Services, APIs and Tests. / مصفوفة تتبّع تبين ربط متطلبات الرؤية بالـ ADRs والخدمات والواجهات والاختبارات.
4. OpenAPI spec for the main service with at least 2 endpoints and contract tests (consumer/provider). / مواصفة OpenAPI للخدمة الرئيسية مع نقطتي نهاية على الأقل واختبارات عقود.
5. An implemented service (one container) with: / خدمة منفّذة (حاوية واحدة) تشمل:
   - Unit tests (code coverage >= 60%) / اختبارات وحدية (تغطية كود >= 60%)
   - CI pipeline that runs unit tests and contract verification / خط CI يشغّل الاختبارات والتحقق من العقود
   - A basic deployment manifest (Kubernetes manifest or Docker Compose) / مخطط نشر أساسي
6. An ML pipeline stub (train/infer) or simulated model integrated with the service. / مسودة خط أنابيب ML أو نموذج محاكاة مدمج.
7. Monitoring dashboard (basic SLO/SLI) and a runbook for one failure scenario. / لوحة مراقبة ومجموعة إجراءات للحالة الطارئة.
8. Final presentation (slides) showing traceability proof: change in Vision -> ADR -> Service -> Test. / عرض نهائي يوضح دليل التتبّع: تغيير في الرؤية -> ADR -> الخدمة -> الاختبار.

## Deliverables (files to submit) / المخرجات المطلوبة
- vision.pdf or vision.md / ADRs in `adrs/` folder / RTM CSV / openapi.yaml / service source code / CI config / pact pacts or broker link / monitoring screenshots
- vision.pdf أو vision.md / سجلات ADR في مجلد `adrs/` / ملف RTM بصيغة CSV / ملف openapi.yaml / الكود المصدري للخدمة / إعدادات CI / ملفات pact أو رابط broker / لقطات شاشة للمراقبة

## Rubric (grading) / معيار التقييم
- Vision & ADRs completeness: 25% / اكتمال الرؤية وADRs: 25%
- RTM & Traceability Proof: 25% / مصفوفة التتبع والدليل: 25%
- Implementation quality & tests: 30% / جودة التنفيذ والاختبارات: 30%
- Monitoring & runbook: 10% / المراقبة ودليل التشغيل: 10%
- Presentation & explanations: 10% / العرض والشرح: 10%
