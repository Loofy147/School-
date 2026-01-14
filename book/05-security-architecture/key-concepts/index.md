# Key Concepts for Security Architecture & Threat Modeling
# المفاهيم الأساسية لهندسة الأمن ونمذجة التهديدات

- **Threat Modeling:** A proactive process where potential threats and vulnerabilities are identified, quantified, and mitigated during the design phase. A common framework for this is **STRIDE**, which stands for:
    - **S**poofing: Impersonating another user or service. (e.g., using stolen credentials to log in as another user).
    - **T**ampering: Modifying data without authorization. (e.g., changing the price of a product in an e-commerce database).
    - **R**epudiation: Denying that an action was taken. (e.g., a user denying that they made a purchase).
    - **I**nformation Disclosure: Exposing sensitive data to unauthorized parties. (e.g., a bug that allows a user to see another user's personal information).
    - **D**enial of Service: Making a system unavailable to legitimate users. (e.g., flooding a server with so many requests that it crashes).
    - **E**levation of Privilege: Gaining higher-level access than authorized. (e.g., a regular user finding a way to gain admin privileges).
- **Defense in Depth:** The principle of using multiple, layered security controls. If one layer fails, another is there to stop the attack. For example, using a firewall, network segmentation, and application-level authentication together.
- **Principle of Least Privilege:** A user or service should only have the absolute minimum permissions required to perform its function, and nothing more.
- **Identity and Access Management (IAM):** The framework of policies and technologies for ensuring that the right entities (users, services) have the appropriate access to technical resources.
- **Encryption (at-rest and in-transit):**
    - **Encryption in-transit:** Protecting data as it moves between systems (e.g., using TLS/SSL for API calls).
    - **Encryption at-rest:** Protecting data when it is stored on a disk or in a database.
- **Secrets Management:** The secure storage, distribution, and rotation of "secrets" like API keys, database passwords, and private certificates. Secrets should never be hard-coded in the source code.

- **نمذجة التهديدات:** عملية استباقية يتم فيها تحديد التهديدات ونقاط الضعف المحتملة وقياسها وتخفيفها أثناء مرحلة التصميم. الإطار الشائع لهذا هو **STRIDE**، والذي يرمز إلى:
    - **S**poofing (الانتحال): انتحال شخصية مستخدم أو خدمة أخرى. (على سبيل المثال ، استخدام بيانات اعتماد مسروقة لتسجيل الدخول كمستخدم آخر).
    - **T**ampering (العبث): تعديل البيانات دون إذن. (على سبيل المثال ، تغيير سعر منتج في قاعدة بيانات التجارة الإلكترونية).
    - **R**epudiation (الإنكار): إنكار اتخاذ إجراء ما. (على سبيل المثال ، مستخدم ينكر أنه قام بعملية شراء).
    - **I**nformation Disclosure (الكشف عن المعلومات): كشف البيانات الحساسة لأطراف غير مصرح لها. (على سبيل المثال ، خطأ يسمح للمستخدم برؤية المعلومات الشخصية لمستخدم آخر).
    - **D**enial of Service (رفض الخدمة): جعل النظام غير متاح للمستخدمين الشرعيين. (على سبيل المثال ، إغراق الخادم بعدد كبير من الطلبات التي تؤدي إلى تعطله).
    - **E**levation of Privilege (تصعيد الامتيازات): الحصول على وصول بمستوى أعلى من المصرح به. (على سبيل المثال ، مستخدم عادي يجد طريقة للحصول على امتيازات المسؤول).
- **الدفاع في العمق:** مبدأ استخدام ضوابط أمنية متعددة ومتدرجة. إذا فشلت طبقة واحدة، فهناك طبقة أخرى لإيقاف الهجوم. على سبيل المثال، استخدام جدار حماية وتقسيم الشبكة ومصادقة على مستوى التطبيق معًا.
- **مبدأ الامتياز الأقل:** يجب أن يكون لدى المستخدم أو الخدمة الحد الأدنى المطلق من الأذونات المطلوبة لأداء وظيفته، ولا شيء أكثر.
- **إدارة الهوية والوصول (IAM):** إطار السياسات والتقنيات لضمان أن الكيانات الصحيحة (المستخدمون والخدمات) لديها الوصول المناسب إلى الموارد التقنية.
- **التشفير (في حالة السكون وأثناء النقل):**
    - **التشفير أثناء النقل:** حماية البيانات أثناء انتقالها بين الأنظمة (على سبيل المثال، استخدام TLS / SSL لمكالمات API).
    - **التشفير في حالة السكون:** حماية البيانات عند تخزينها على قرص أو في قاعدة بيانات.
- **إدارة الأسرار:** التخزين الآمن وتوزيع وتدوير "الأسرار" مثل مفاتيح API وكلمات مرور قاعدة البيانات والشهادات الخاصة. لا ينبغي أبدًا ترميز الأسرار بشكل ثابت في الكود المصدري.
