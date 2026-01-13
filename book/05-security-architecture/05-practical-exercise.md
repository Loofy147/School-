# Practical Exercise for Security Architecture
# تمرين عملي لهندسة الأمن

## Objective / الهدف

To conduct a simple threat modeling exercise using the STRIDE framework.
لإجراء تمرين بسيط لنمذجة التهديدات باستخدام إطار STRIDE.

## Scenario / سيناريو

Consider the authentication flow for our "Privacy-aware Intelligent Service Platform." The high-level process is as follows:
1.  The user enters their username and password into a login form.
2.  The frontend client sends the credentials to the backend `auth-service` via an HTTPS POST request.
3.  The `auth-service` checks the credentials against the `users-table` in the database.
4.  If the credentials are valid, the service generates a JSON Web Token (JWT) and returns it to the client.
5.  The client stores the JWT and includes it in the header of all subsequent requests to other services.

ضع في اعتبارك تدفق المصادقة لـ "منصة الخدمة الذكية المدركة للخصوصية". العملية عالية المستوى هي كما يلي:
1.  يقوم المستخدم بإدخال اسم المستخدم وكلمة المرور في نموذج تسجيل الدخول.
2.  يرسل عميل الواجهة الأمامية بيانات الاعتماد إلى `auth-service` الخلفية عبر طلب HTTPS POST.
3.  تقوم `auth-service` بفحص بيانات الاعتماد مقابل `users-table` في قاعدة البيانات.
4.  إذا كانت بيانات الاعتماد صالحة، تقوم الخدمة بإنشاء رمز ويب JSON (JWT) وإعادته إلى العميل.
5.  يقوم العميل بتخزين JWT وتضمينه في رأس جميع الطلبات اللاحقة للخدمات الأخرى.

## Tasks / المهام

1.  **Identify Threats with STRIDE:** For each of the STRIDE categories, identify at least one potential threat in the scenario described above.
    *   **S**poofing: How could a user or service be impersonated?
    *   **T**ampering: What data could be tampered with, and where?
    *   **R**epudiation: Could a user deny performing an action?
    *   **I**nformation Disclosure: Where could sensitive data be leaked?
    *   **D**enial of Service: How could this authentication flow be disrupted?
    *   **E**levation of Privilege: How could a regular user gain admin privileges?

2.  **Propose Mitigations:** For three of the threats you identified, propose a specific technical control or design change to mitigate it.

3.  **Traceability:** For each mitigation you proposed, identify the layer(s) that would be responsible for implementing it.

1.  **تحديد التهديدات باستخدام STRIDE:** لكل فئة من فئات STRIDE، حدد تهديدًا محتملاً واحدًا على الأقل في السيناريو الموضح أعلاه.
    *   **S**poofing (الانتحال): كيف يمكن انتحال شخصية مستخدم أو خدمة؟
    *   **T**ampering (العبث): ما البيانات التي يمكن العبث بها، وأين؟
    *   **R**epudiation (الإنكار): هل يمكن للمستخدم إنكار قيامه بإجراء ما؟
    *   **I**nformation Disclosure (الكشف عن المعلومات): أين يمكن تسريب البيانات الحساسة؟
    *   **D**enial of Service (رفض الخدمة): كيف يمكن تعطيل تدفق المصادقة هذا؟
    *   **E**levation of Privilege (تصعيد الامتيازات): كيف يمكن لمستخدم عادي الحصول على امتيازات المسؤول؟

2.  **اقتراح إجراءات التخفيف:** لثلاثة من التهديدات التي حددتها، اقترح ضابطًا فنيًا محددًا أو تغييرًا في التصميم للتخفيف منه.

3.  **التتبع:** لكل إجراء تخفيف اقترحته، حدد الطبقة (الطبقات) التي ستكون مسؤولة عن تنفيذه.
