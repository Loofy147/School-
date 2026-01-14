# Key Concepts for Vision & Architecture
# المفاهيم الأساسية للرؤية والهندسة المعمارية

- **Business Mission:** A clear and concise statement that defines the purpose of the system. What is the problem we are solving, and for whom?
- **Success Metrics (KPIs):** Key Performance Indicators are quantifiable measures that the business uses to track progress towards its goals. Technical decisions should ultimately serve these metrics. Examples include "Increase user engagement by 15%" or "Reduce customer churn by 5%."
- **Architecture Decision Record (ADR):** A document that captures an important architectural decision, its context, and its consequences. ADRs provide a historical record of *why* the system is the way it is.
- **C4 Model:** A "map" of your software architecture, showing it at different levels of detail (Context, Containers, Components, and Code). It helps to communicate the architecture to different audiences, from business stakeholders to developers.

### The Four Levels of the C4 Model / المستويات الأربعة لنموذج C4

1.  **Level 1: System Context Diagram:** The highest level of abstraction. It shows your system as a single box and illustrates its relationships with users (actors) and other external systems. It's a great starting point for a non-technical audience.
2.  **Level 2: Container Diagram:** This level zooms into the system box from the Context diagram. It shows the high-level technical building blocks of your system. Each "container" is a separately deployable unit, such as a web application, an API service, a database, or a file system.
3.  **Level 3: Component Diagram:** This level zooms into an individual container to show its internal components. A component is a logical grouping of related code, like a "user management" component or a "payment processing" component.
4.  **Level 4: Code Diagram (Optional):** This is the most detailed level, showing how a single component is implemented in code. This level is often represented by a UML class diagram and is typically only created for the most important or complex components.

### المستويات الأربعة لنموذج C4

1.  **المستوى الأول: مخطط سياق النظام:** أعلى مستوى من التجريد. يُظهر نظامك كمربع واحد ويوضح علاقاته مع المستخدمين (الجهات الفاعلة) والأنظمة الخارجية الأخرى. إنها نقطة انطلاق رائعة لجمهور غير تقني.
2.  **المستوى الثاني: مخطط الحاوية:** يقوم هذا المستوى بتكبير مربع النظام من مخطط السياق. يُظهر اللبنات الأساسية الفنية عالية المستوى لنظامك. كل "حاوية" هي وحدة قابلة للنشر بشكل منفصل، مثل تطبيق ويب أو خدمة API أو قاعدة بيانات أو نظام ملفات.
3.  **المستوى الثالث: مخطط المكون:** يقوم هذا المستوى بتكبير حاوية فردية لإظهار مكوناتها الداخلية. المكون هو تجميع منطقي للكود ذي الصلة، مثل مكون "إدارة المستخدم" أو مكون "معالجة الدفع".
4.  **المستوى الرابع: مخطط الكود (اختياري):** هذا هو المستوى الأكثر تفصيلاً، حيث يوضح كيفية تنفيذ مكون واحد في الكود. غالبًا ما يتم تمثيل هذا المستوى بمخطط فئة UML ويتم إنشاؤه عادةً فقط للمكونات الأكثر أهمية أو تعقيدًا.
- **Constraints:** The limitations and restrictions that the system must operate within. These can be business constraints (e.g., budget, timeline), legal constraints (e.g., GDPR), or technical constraints (e.g., must integrate with a legacy system).

- **مهمة العمل:** بيان واضح وموجز يحدد الغرض من النظام. ما هي المشكلة التي نحلها، ولمن؟
- **مقاييس النجاح (مؤشرات الأداء الرئيسية):** مؤشرات الأداء الرئيسية هي مقاييس قابلة للقياس يستخدمها العمل لتتبع التقدم نحو أهدافه. يجب أن تخدم القرارات الفنية في النهاية هذه المقاييس. ومن الأمثلة على ذلك "زيادة تفاعل المستخدم بنسبة 15٪" أو "تقليل تراجع العملاء بنسبة 5٪".
- **سجل قرار الهندسة المعمارية (ADR):** مستند يلتقط قرارًا معماريًا مهمًا وسياقه وعواقبه. توفر سجلات قرار الهندسة المعمارية سجلاً تاريخيًا *لسبب* كون النظام على ما هو عليه.
- **نموذج C4:** "خريطة" لهندسة البرمجيات الخاصة بك، تعرضها بمستويات مختلفة من التفاصيل (السياق والحاويات والمكونات والتعليمات البرمجية). يساعد على توصيل الهندسة المعمارية لجماهير مختلفة، من أصحاب المصلحة في الأعمال إلى المطورين.
- **القيود:** القيود والقيود التي يجب أن يعمل النظام في إطارها. يمكن أن تكون هذه قيودًا تجارية (مثل الميزانية والجدول الزمني)، أو قيودًا قانونية (مثل اللائحة العامة لحماية البيانات)، أو قيودًا فنية (مثل وجوب التكامل مع نظام قديم).
