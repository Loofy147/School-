# Practical Exercise for Product/UX System Design
# تمرين عملي لتصميم المنتج وتجربة المستخدم على مستوى النظام

## Objective / الهدف

To create a high-level user journey map and a set of acceptance criteria for a new feature.
لإنشاء خريطة رحلة مستخدم عالية المستوى ومجموعة من معايير القبول لميزة جديدة.

## Scenario / سيناريو

Imagine you are working on the "Privacy-aware Intelligent Service Platform" from our capstone project. The business (Layer 1) has decided to add a new feature that allows users to view their data and explicitly manage their consent for how it's used by the AI models.

تخيل أنك تعمل على "منصة الخدمة الذكية المدركة للخصوصية" من مشروعنا النهائي. قرر العمل (الطبقة الأولى) إضافة ميزة جديدة تتيح للمستخدمين عرض بياناتهم وإدارة موافقتهم بشكل صريح على كيفية استخدامها بواسطة نماذج الذكاء الاصطناعي.

## Tasks / المهام

1.  **Create a User Journey Map:** Using a tool like Miro or even just a simple text file, map out the steps a user would take to find their data, understand how it's being used, and change their consent settings.
2.  **Define Acceptance Criteria:** Write at least three acceptance criteria for this new feature using the Gherkin `Given/When/Then` format. For example:
    *   **Scenario:** User revokes consent for a specific data type.
    *   **Given** a user is logged in and is on the "Manage My Data" page,
    *   **When** the user unchecks the box for "Use my location data for recommendations",
    *   **Then** the system should immediately stop using their location data for all future recommendations, AND a confirmation message should be displayed.
3.  **Traceability:** For each acceptance criterion, identify which service (Layer 7) would be responsible for implementing it.

1.  **إنشاء خريطة رحلة المستخدم:** باستخدام أداة مثل Miro أو حتى مجرد ملف نصي بسيط، قم بتخطيط الخطوات التي سيتخذها المستخدم للعثور على بياناته، وفهم كيفية استخدامها، وتغيير إعدادات الموافقة الخاصة به.
2.  **تحديد معايير القبول:** اكتب ثلاثة معايير قبول على الأقل لهذه الميزة الجديدة باستخدام تنسيق Gherkin `Given/When/Then`. على سبيل المثال:
    *   **سيناريو:** يسحب المستخدم الموافقة على نوع بيانات معين.
    *   **بالنظر إلى** أن المستخدم قام بتسجيل الدخول وهو في صفحة "إدارة بياناتي"،
    *   **عندما** يقوم المستخدم بإلغاء تحديد مربع "استخدام بيانات موقعي للتوصيات"،
    *   **ثم** يجب على النظام التوقف فورًا عن استخدام بيانات موقعه لجميع التوصيات المستقبلية، ويجب عرض رسالة تأكيد.
3.  **التتبع:** لكل معيار قبول، حدد الخدمة (الطبقة السابعة) التي ستكون مسؤولة عن تنفيذه.
