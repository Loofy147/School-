# Practical Exercise for Layer 9
# تمرين عملي للطبقة التاسعة

## Goal / الهدف

To implement a small feature for the fictional "Smart Home Hub" system, following clean code principles and the testing pyramid.

لتنفيذ ميزة صغيرة لنظام "مركز المنزل الذكي" الخيالي، باتباع مبادئ الكود النظيف وهرم الاختبار.

## Exercise Steps / خطوات التمرين

1.  **Choose a Language and Framework:**
    -   Based on the needs of the Smart Home Hub and the architectural decisions you've made in the previous layers, choose a programming language and a web framework for the cloud backend. Justify your choice.

2.  **Write Clean Code for a Simple Feature:**
    -   Implement a simple feature, such as a "Get Device Status" endpoint that returns the current status (e.g., "on," "off") of a smart light bulb.
    -   Pay close attention to the principles of clean code: use meaningful names, keep your functions small and focused, and avoid duplication.

3.  **Implement the Testing Pyramid:**
    -   **Unit Test:** Write a unit test for the core logic of your feature. For example, if you have a function that determines the device status, test that function in isolation.
    -   **Integration Test:** Write an integration test that checks the interaction between your new endpoint and the database or service that stores the device status.
    -   **E2E Test (Conceptual):** You don't need to implement a full E2E test, but describe in words how you would test this feature from the user's perspective (e.g., "A user logs into the mobile app, taps on the 'living room light' icon, and sees that the status is 'on'").

## Deliverables / المخرجات

-   A `implementation-choice.md` file with your choice of language and framework and your justification.
-   A `feature.py` (or equivalent) file with your clean code implementation.
-   A `tests.py` (or equivalent) file with your unit and integration tests.
-   An `e2e-test.md` file with your conceptual description of the E2E test.

## 1. اختيار لغة وإطار عمل:
    -   بناءً على احتياجات مركز المنزل الذكي والقرارات المعمارية التي اتخذتها في الطبقات السابقة، اختر لغة برمجة وإطار عمل ويب للواجهة الخلفية السحابية. برر اختيارك.

## 2. كتابة كود نظيف لميزة بسيطة:
    -   قم بتنفيذ ميزة بسيطة، مثل نقطة نهاية "الحصول على حالة الجهاز" التي تُرجع الحالة الحالية (على سبيل المثال، "تشغيل"، "إيقاف") لمصباح إضاءة ذكي.
    -   انتبه جيدًا لمبادئ الكود النظيف: استخدم أسماء ذات معنى، واجعل وظائفك صغيرة ومركزة، وتجنب التكرار.

## 3. تنفيذ هرم الاختبار:
    -   **اختبار الوحدة:** اكتب اختبار وحدة للمنطق الأساسي لميزتك. على سبيل المثال، إذا كان لديك وظيفة تحدد حالة الجهاز، فاختبر تلك الوظيفة بمعزل عن غيرها.
    -   **اختبار التكامل:** اكتب اختبار تكامل يفحص التفاعل بين نقطة النهاية الجديدة وقاعدة البيانات أو الخدمة التي تخزن حالة الجهاز.
    -   **اختبار E2E (مفاهيمي):** لست بحاجة إلى تنفيذ اختبار E2E كامل، ولكن صف بالكلمات كيف ستختبر هذه الميزة من منظور المستخدم (على سبيل المثال، "يقوم المستخدم بتسجيل الدخول إلى تطبيق الهاتف المحمول، والنقر على أيقونة 'مصباح غرفة المعيشة'، ويرى أن الحالة 'تشغيل'").

## المخرجات

-   ملف `implementation-choice.md` مع اختيارك للغة والإطار والتبرير.
-   ملف `feature.py` (أو ما يعادله) مع تنفيذ الكود النظيف الخاص بك.
-   ملف `tests.py` (أو ما يعادله) مع اختبارات الوحدة والتكامل الخاصة بك.
-   ملف `e2e-test.md` مع وصفك المفاهيمي لاختبار E2E.
