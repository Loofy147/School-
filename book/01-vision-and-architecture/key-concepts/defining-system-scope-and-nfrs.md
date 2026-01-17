# Defining System Scope and Non-Functional Requirements (NFRs)
# تحديد نطاق النظام والمتطلبات غير الوظيفية (NFRs)

## 1. Beyond Features: Defining "How" a System Should Be / ما وراء الميزات: تحديد "كيف" يجب أن يكون النظام

Before writing a single line of code for a complex system, architects must answer two fundamental questions:
1.  **What** should the system do? (Functional Requirements)
2.  **How** should the system *be*? (Non-Functional Requirements)

While functional requirements define the specific features of a system (e.g., "the user shall be able to log in"), Non-Functional Requirements (NFRs) define its operational qualities and constraints. They are the critical "-ilities" that determine a system's viability and long-term success. Getting NFRs wrong can be catastrophic, often leading to costly rework or complete project failure, far more so than missing a single feature.

NFRs are not an afterthought; they are foundational architectural concerns that must be defined at the very beginning of a project, as they directly influence all subsequent design decisions.

---

قبل كتابة سطر واحد من التعليمات البرمجية لنظام معقد، يجب على المهندسين المعماريين الإجابة على سؤالين أساسيين:
1.  **ماذا** يجب أن يفعل النظام؟ (المتطلبات الوظيفية)
2.  **كيف** يجب أن *يكون* النظام؟ (المتطلبات غير الوظيفية)

بينما تحدد المتطلبات الوظيفية الميزات المحددة للنظام (على سبيل المثال، "يجب أن يكون المستخدم قادرًا على تسجيل الدخول")، فإن المتطلبات غير الوظيفية (NFRs) تحدد صفاته التشغيلية وقيوده. إنها "-ilities" الحاسمة التي تحدد قابلية النظام للنجاح على المدى الطويل. قد يكون الخطأ في تحديد المتطلبات غير الوظيفية كارثيًا، مما يؤدي غالبًا إلى إعادة عمل مكلفة أو فشل كامل للمشروع، أكثر بكثير من فقدان ميزة واحدة.

المتطلبات غير الوظيفية ليست فكرة لاحقة؛ إنها اهتمامات معمارية أساسية يجب تحديدها في بداية المشروع، لأنها تؤثر بشكل مباشر على جميع قرارات التصميم اللاحقة.

---

## 2. Core Categories of Non-Functional Requirements / الفئات الأساسية للمتطلبات غير الوظيفية

NFRs are often called the "quality attributes" of a system. Here are some of the most critical categories that must be considered for any large-scale systems engineering project.

غالبًا ما تسمى المتطلبات غير الوظيفية "سمات الجودة" للنظام. فيما يلي بعض الفئات الأكثر أهمية التي يجب مراعاتها في أي مشروع هندسة أنظمة واسع النطاق.

| **Category / الفئة** | **Description / الوصف** | **Example for our Capstone Project** |
| :--- | :--- | :--- |
| **Reliability / الموثوقية** | The ability of the system to operate without failure under specified conditions. Often measured in Mean Time Between Failures (MTBF). | "The core data processing service must have an MTBF of at least 10,000 hours." |
| **Availability / الإتاحة** | The proportion of time the system is operational and accessible. Often expressed as a percentage of uptime (e.g., "five nines"). | "The public-facing API must have 99.99% availability, allowing for no more than 5 minutes of unplanned downtime per month." |
| **Scalability / قابلية التوسع** | The system's ability to handle increased load (e.g., more users, more data) without a degradation in performance. | "The system must support a 10x growth in concurrent users (from 1,000 to 10,000) over two years with a maximum of 20% increase in response time." |
| **Performance / الأداء** | The speed and responsiveness of the system under a particular workload. Measured in terms of latency and throughput. | "The p95 latency for the recommendation API endpoint must be less than 200ms under a load of 1,000 requests per second." |
| **Security / الأمن** | The system's ability to protect data and itself from unauthorized access, use, disclosure, disruption, modification, or destruction. | "All Personally Identifiable Information (PII) must be encrypted at-rest using AES-256 and in-transit using TLS 1.3." |
| **Maintainability / قابلية الصيانة** | The ease with which the system can be modified to fix defects, improve performance, or adapt to changing requirements. | "A new developer with domain expertise should be able to ship a minor bug fix to production within their first week." |
| **Usability / قابلية الاستخدام** | The ease with which users can learn and operate the system to achieve their goals. | "A new user (Amir Khan persona) should be able to set up their account and get their first AI-driven insight within 15 minutes without consulting documentation." |
| **Compliance / الامتثال** | The degree to which the system adheres to relevant laws, regulations, and standards. (This is so important it has its own Layer 4). | "The system must be fully compliant with GDPR, including the 'right to be forgotten'." |

---

## 3. The Role of Stakeholder Analysis / دور تحليل أصحاب المصلحة

Defining NFRs is not a purely technical exercise. It is a process of negotiation and prioritization that must involve all key stakeholders. An architect must ask probing questions to translate business needs into testable, quantitative requirements.

تحديد المتطلبات غير الوظيفية ليس تمرينًا تقنيًا بحتًا. إنها عملية تفاوض وتحديد أولويات يجب أن تشمل جميع أصحاب المصلحة الرئيسيين. يجب على المهندس المعماري طرح أسئلة استقصائية لترجمة احتياجات العمل إلى متطلبات كمية قابلة للاختبار.

-   **Don't ask the business owner:** "What availability do you want?"
    -   **They will say:** "It should always be available!"
-   **Instead, ask:** "How much revenue would the business lose per hour of downtime?"
    -   **This allows the architect to calculate:** The cost of downtime versus the cost of building a 99.999% available system, leading to a rational, data-driven decision.

The process looks like this:
1.  **Identify Stakeholders:** Who are the key users, business owners, operators, and legal teams? (Our Capstone Personas are a good start).
2.  **Elicit Business Goals:** What are their definitions of success? What are their fears?
3.  **Translate to NFRs:** Convert those qualitative goals into quantitative, measurable, and testable NFRs.
4.  **Prioritize:** No system can be perfect in all dimensions. There are always trade-offs. Is performance more critical than cost? Is security more important than speed? These priorities, driven by the stakeholders, will shape the entire architecture of the system.

By grounding the architecture in a clear, well-defined, and stakeholder-approved set of Non-Functional Requirements, we lay the foundation for a system that doesn't just *work*, but works *well* for the people who depend on it.
