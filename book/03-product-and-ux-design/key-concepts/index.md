# Key Concepts for Product/UX System Design
# المفاهيم الأساسية لتصميم المنتج وتجربة المستخدم على مستوى النظام

- **User Journeys:** Mapping out the complete path a user takes to accomplish a goal, from initial contact to final outcome. This helps identify all the touchpoints and interactions with the system.
    - **Example:** A user journey for a food delivery app might include: "opens the app," "searches for a restaurant," "adds items to the cart," "checks out," "tracks the delivery," and "receives the food."
- **Service Blueprint:** A detailed diagram that visualizes the relationships between different service components (e.g., user actions, frontend interfaces, backend processes, and support systems) and how they combine to create the user experience.
    - **Example:** A service blueprint for the same food delivery app would show how the user's actions (e.g., "adds items to the cart") trigger frontend events, which in turn call backend APIs, which then update the database and notify the restaurant.
- **Minimum Viable Product (MVP):** Defining the smallest set of features that delivers value to the end-user and can be shipped. This allows for iterative development and learning from user feedback.
- **Acceptance Criteria:** A formal list of requirements that must be met for a user story to be considered complete. They are often written in a Gherkin format (Given/When/Then).
- **End-to-End Scenarios:** Detailed descriptions of how a user will interact with the system to complete a specific task, covering the entire workflow from start to finish.

- **رحلات المستخدم:** تخطيط المسار الكامل الذي يسلكه المستخدم لتحقيق هدف ما، من الاتصال الأولي إلى النتيجة النهائية. يساعد هذا في تحديد جميع نقاط الاتصال والتفاعلات مع النظام.
    - **مثال:** قد تتضمن رحلة المستخدم لتطبيق توصيل الطعام ما يلي: "يفتح التطبيق" ، "يبحث عن مطعم" ، "يضيف عناصر إلى عربة التسوق" ، "يدفع" ، "يتتبع التسليم" ، و "يستلم الطعام".
- **مخطط الخدمة:** رسم تخطيطي مفصل يصور العلاقات بين مكونات الخدمة المختلفة (على سبيل المثال، إجراءات المستخدم، وواجهات الواجهة الأمامية، وعمليات الواجهة الخلفية، وأنظمة الدعم) وكيفية دمجها لإنشاء تجربة المستخدم.
    - **مثال:** سيوضح مخطط الخدمة لنفس تطبيق توصيل الطعام كيف تؤدي إجراءات المستخدم (على سبيل المثال ، "إضافة عناصر إلى عربة التسوق") إلى تشغيل أحداث الواجهة الأمامية ، والتي بدورها تستدعي واجهات برمجة التطبيقات الخلفية ، والتي تقوم بعد ذلك بتحديث قاعدة البيانات وإخطار المطعم.
- **الحد الأدنى من المنتج القابل للتطبيق (MVP):** تحديد أصغر مجموعة من الميزات التي تقدم قيمة للمستخدم النهائي ويمكن شحنها. يسمح هذا بالتطوير التكراري والتعلم من ملاحظات المستخدم.
- **معايير القبول:** قائمة رسمية بالمتطلبات التي يجب الوفاء بها حتى تكتمل قصة المستخدم. غالبًا ما تتم كتابتها بتنسيق Gherkin (بالنظر إلى / متى / ثم).
- **سيناريوهات شاملة:** أوصاف تفصيلية لكيفية تفاعل المستخدم مع النظام لإكمال مهمة محددة، تغطي سير العمل بأكمله من البداية إلى النهاية.
