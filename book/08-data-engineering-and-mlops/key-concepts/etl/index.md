# ETL (Extract, Transform, Load)
# استخراج، تحويل، تحميل (ETL)

ETL is a three-step process for moving data from a source system to a destination system (like a data warehouse).

1.  **Extract:** Reading data from a source (e.g., a database, an API, a set of log files).
2.  **Transform:** Cleaning, enriching, and restructuring the data into a desired format. This can include anything from simple data type conversions to complex aggregations and joins.
3.  **Load:** Writing the transformed data to a destination.

A modern variation of this is **ELT (Extract, Load, Transform)**, where raw data is first loaded into a data lake or warehouse and then transformed in place using the power of modern cloud data warehouses. This approach is often more flexible and scalable.

**Why it matters:** ETL/ELT pipelines are the fundamental building blocks of any data-driven system. They are the "plumbing" that ensures data is available where and when it's needed.

---

ETL هي عملية من ثلاث خطوات لنقل البيانات من نظام مصدر إلى نظام وجهة (مثل مستودع بيانات).

1.  **استخراج:** قراءة البيانات من مصدر (على سبيل المثال، قاعدة بيانات، واجهة برمجة تطبيقات، مجموعة من ملفات السجل).
2.  **تحويل:** تنظيف البيانات وإثرائها وإعادة هيكلتها إلى التنسيق المطلوب. يمكن أن يشمل ذلك أي شيء من تحويلات أنواع البيانات البسيطة إلى التجميعات والصلات المعقدة.
3.  **تحميل:** كتابة البيانات المحولة إلى وجهة.

شكل حديث من هذا هو **ELT (استخراج، تحميل، تحويل)**، حيث يتم تحميل البيانات الأولية أولاً في بحيرة بيانات أو مستودع ثم يتم تحويلها في مكانها باستخدام قوة مستودعات البيانات السحابية الحديثة. غالبًا ما يكون هذا النهج أكثر مرونة وقابلية للتطوير.

**لماذا هو مهم:** تعد خطوط أنابيب ETL / ELT اللبنات الأساسية لأي نظام يعتمد على البيانات. إنها "السباكة" التي تضمن توفر البيانات أينما ومتى احتجت إليها.
