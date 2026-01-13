# Practical Exercise for Vision & Architecture
# تمرين عملي للرؤية والهندسة المعمارية

## Objective / الهدف

To create a high-level vision document, including a C4 Context diagram and the first Architecture Decision Record (ADR) for a new system.
لإنشاء مستند رؤية عالي المستوى، بما في ذلك مخطط سياق C4 وأول سجل قرار معماري (ADR) لنظام جديد.

## Scenario / سيناريو

You have been tasked with leading the development of a new system: the "Privacy-aware Intelligent Service Platform."
لقد تم تكليفك بقيادة تطوير نظام جديد: "منصة الخدمة الذكية المدركة للخصوصية".

The initial high-level requirements are:
*   The system must provide personalized recommendations to users.
*   The system must be built with user privacy as a core principle.
*   The system will be used by both end-users (via a web app) and internal data analysts.

المتطلبات الأولية عالية المستوى هي:
*   يجب أن يقدم النظام توصيات مخصصة للمستخدمين.
*   يجب بناء النظام مع خصوصية المستخدم كمبدأ أساسي.
*   سيتم استخدام النظام من قبل المستخدمين النهائيين (عبر تطبيق ويب) ومحللي البيانات الداخليين.

## Tasks / المهام

1.  **Create a Vision Document (`vision.md`):**
    *   Write a clear mission statement for the platform.
    *   Define at least three key success metrics (KPIs).
    *   Identify the primary users and external systems.

2.  **Create a C4 Context Diagram:**
    *   Using a tool like PlantUML or simply a text description, create a Level 1 C4 diagram.
    *   It should show your new platform as a single box in the center, and show the users and any key external systems it interacts with.

3.  **Write Your First ADR:**
    *   The first major architectural decision is whether to build the system as a single monolith or as a collection of microservices.
    *   Write an ADR that documents your decision. Choose either "Monolith First" or "Microservices First" and justify your choice. Consider the context (small team, new product) and the consequences of your decision.

1.  **إنشاء مستند رؤية (`vision.md`):**
    *   اكتب بيان مهمة واضحًا للمنصة.
    *   حدد ثلاثة مقاييس نجاح رئيسية على الأقل (مؤشرات أداء رئيسية).
    *   حدد المستخدمين الأساسيين والأنظمة الخارجية.

2.  **إنشاء مخطط سياق C4:**
    *   باستخدام أداة مثل PlantUML أو مجرد وصف نصي، قم بإنشاء مخطط C4 من المستوى 1.
    *   يجب أن يُظهر منصتك الجديدة كمربع واحد في الوسط، وأن يُظهر المستخدمين وأي أنظمة خارجية رئيسية يتفاعل معها.

3.  **اكتب أول سجل قرار معماري لك:**
    *   القرار المعماري الرئيسي الأول هو ما إذا كان سيتم بناء النظام ككتلة متجانسة واحدة أو كمجموعة من الخدمات المصغرة.
    *   اكتب سجل قرار معماري يوثق قرارك. اختر إما "المتجانسة أولاً" أو "الخدمات المصغرة أولاً" وبرر اختيارك. ضع في اعتبارك السياق (فريق صغير، منتج جديد) وعواقب قرارك.
