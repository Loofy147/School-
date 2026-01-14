# API Versioning Strategies
# استراتيجيات إصدار API

When an API changes, you need a strategy for rolling out the changes without breaking existing clients. Common strategies include:

- **URI Path Versioning:** Include the version number in the URL path (e.g., `/api/v1/users`). This is the most common and straightforward approach.
- **Header Versioning:** Include the version number in a custom request header (e.g., `Accepts-version: v1`).
- **Query Parameter Versioning:** Include the version number as a query parameter (e.g., `/api/users?version=1`).

---

عندما تتغير واجهة برمجة التطبيقات، فأنت بحاجة إلى استراتيجية لطرح التغييرات دون كسر العملاء الحاليين. تشمل الاستراتيجيات الشائعة ما يلي:

- **إصدار مسار URI:** قم بتضمين رقم الإصدار في مسار URL (على سبيل المثال، `/api/v1/users`). هذا هو النهج الأكثر شيوعًا ومباشرة.
- **إصدار الرأس:** قم بتضمين رقم الإصدار في رأس طلب مخصص (على سبيل المثال، `Accepts-version: v1`).
- **إصدار معلمة الاستعلام:** قم بتضمين رقم الإصدار كمعلمة استعلام (على سبيل المثال، `/api/users?version=1`).
