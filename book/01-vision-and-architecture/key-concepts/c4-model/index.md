# The C4 Model for Visualizing Architecture
# نموذج C4 لتصور الهندسة المعمارية

The C4 model is a lean, hierarchical approach to visualizing software architecture. It allows you to tell the story of your system at different levels of detail, making it accessible to various audiences, from non-technical stakeholders to developers.

نموذج C4 هو نهج رشيق وهرمي لتصور هندسة البرمجيات. يسمح لك بسرد قصة نظامك بمستويات مختلفة من التفاصيل، مما يجعله متاحًا لجماهير متنوعة، من أصحاب المصلحة غير التقنيين إلى المطورين.

We will explore the four levels of the C4 model in detail:

- **[Level 1: System Context](./context/index.md):** A high-level, zoomed-out view showing your system and its interactions with users and other systems.
- **[Level 2: Containers](./containers/index.md):** Zooms into the system to show the high-level technical building blocks (services, databases, etc.).
- **[Level 3: Components](./components/index.md):** Zooms into a container to show its internal logical components.
- **[Level 4: Code](./code/index.md):** (Optional) Zooms into a component to show its code-level implementation.

---

سوف نستكشف المستويات الأربعة لنموذج C4 بالتفصيل:

- **[المستوى الأول: سياق النظام](./context/index.md):** عرض عالي المستوى ومكبر يوضح نظامك وتفاعلاته مع المستخدمين والأنظمة الأخرى.
- **[المستوى الثاني: الحاويات](./containers/index.md):** تكبير النظام لإظهار اللبنات الفنية عالية المستوى (الخدمات، قواعد البيانات، إلخ).
- **[المستوى الثالث: المكونات](./components/index.md):** تكبير حاوية لإظهار مكوناتها المنطقية الداخلية.
- **[المستوى الرابع: الكود](./code/index.md):** (اختياري) تكبير مكون لإظهار تنفيذه على مستوى الكود.

### Practical Example: System Context Diagram / مثال عملي: مخطط سياق النظام

Here is a simple example of a System Context diagram for an "Internet Banking System" created using PlantUML. This diagram shows the system at the center, the users (actors) that interact with it, and the other systems it depends on.

فيما يلي مثال بسيط لمخطط سياق النظام لـ "نظام الخدمات المصرفية عبر الإنترنت" تم إنشاؤه باستخدام PlantUML. يوضح هذا المخطط النظام في المنتصف والمستخدمين (الجهات الفاعلة) الذين يتفاعلون معه والأنظمة الأخرى التي يعتمد عليها.

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(customer, "Personal Banking Customer", "A customer of the bank, with personal bank accounts.")
System(internetBankingSystem, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

System_Ext(emailSystem, "E-mail System", "The internal Microsoft Exchange e-mail system.")
System_Ext(mainframe, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

Rel(customer, internetBankingSystem, "Uses")
Rel_Back(customer, emailSystem, "Sends e-mails to")
Rel(internetBankingSystem, emailSystem, "Sends e-mails using")
Rel(internetBankingSystem, mainframe, "Uses")

@enduml
```
