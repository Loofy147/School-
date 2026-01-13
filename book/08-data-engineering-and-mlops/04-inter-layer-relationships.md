# Inter-Layer Relationships for Data Engineering & MLOps
# العلاقات بين الطبقات لهندسة البيانات و MLOps

Layer 8 (Data Engineering & MLOps) is the factory floor for your system's intelligence. It builds the data pipelines and model lifecycle processes that are defined by the AI strategy in Layer 2.

الطبقة الثامنة (هندسة البيانات و MLOps) هي أرض المصنع لذكاء نظامك. تقوم ببناء خطوط أنابيب البيانات وعمليات دورة حياة النموذج التي تحددها استراتيجية الذكاء الاصطناعي في الطبقة الثانية.

## How Layer 8 Influences Other Layers / كيف تؤثر الطبقة الثامنة على الطبقات الأخرى

- **Layer 2 (AI Strategy):** The capabilities and limitations of your data pipelines and MLOps platform can influence your AI strategy. If you have a real-time data streaming infrastructure, you can pursue an AI strategy that relies on real-time features.
- **Layer 7 (Service Design):** The structure of your data pipelines and the availability of your models will define the data contracts and API contracts for the services that consume them. A feature store, for example, will have a clear data contract with the models that use its features.
- **Layer 6 (SRE/DevOps):** Data pipelines and ML training jobs are often resource-intensive and need to be carefully monitored and managed. They are a key input for the observability and SRE practices in Layer 6.

- **الطبقة الثانية (استراتيجية الذكاء الاصطناعي):** يمكن أن تؤثر قدرات وقيود خطوط أنابيب البيانات ومنصة MLOps الخاصة بك على استراتيجية الذكاء الاصطناعي الخاصة بك. إذا كان لديك بنية تحتية لدفق البيانات في الوقت الفعلي، فيمكنك اتباع استراتيجية ذكاء اصطناعي تعتمد على الميزات في الوقت الفعلي.
- **الطبقة السابعة (تصميم الخدمة):** ستحدد بنية خطوط أنابيب البيانات الخاصة بك وتوافر نماذجك عقود البيانات وعقود API للخدمات التي تستهلكها. على سبيل المثال، سيكون لمتجر الميزات عقد بيانات واضح مع النماذج التي تستخدم ميزاته.
- **الطبقة السابعة (SRE / DevOps):** غالبًا ما تكون خطوط أنابيب البيانات ووظائف تدريب تعلم الآلة كثيفة الاستخدام للموارد وتحتاج إلى مراقبة وإدارة دقيقة. إنها مدخل رئيسي لممارسات الملاحظة و SRE في الطبقة السادسة.

## How Other Layers Influence Layer 8 / كيف تؤثر الطبقات الأخرى على الطبقة الثامنة

- **Layer 2 (AI Strategy):** This is the primary input for Layer 8. The AI strategy dictates what data needs to be collected, what models need to be trained, and how they need to be managed.
- **Layer 4 (Compliance):** Compliance and privacy requirements will place strict constraints on the data pipelines. For example, the principle of "data minimization" means you should only collect the data you need, and regulations like GDPR might require you to build pipelines for deleting user data.
- **Layer 7 (Service Design):** The data contracts defined in Layer 7 provide the formal specification for what the data pipelines in Layer 8 must produce.

- **الطبقة الثانية (استراتيجية الذكاء الاصطناعي):** هذا هو المدخل الأساسي للطبقة الثامنة. تملي استراتيجية الذكاء الاصطناعي البيانات التي يجب جمعها، والنماذج التي يجب تدريبها، وكيفية إدارتها.
- **الطبقة الرابعة (الامتثال):** ستضع متطلبات الامتثال والخصوصية قيودًا صارمة على خطوط أنابيب البيانات. على سبيل المثال، يعني مبدأ "تقليل البيانات" أنه يجب عليك فقط جمع البيانات التي تحتاجها، وقد تتطلب منك لوائح مثل GDPR بناء خطوط أنابيب لحذف بيانات المستخدم.
- **الطبقة السابعة (تصميم الخدمة):** توفر عقود البيانات المحددة في الطبقة السابعة المواصفات الرسمية لما يجب أن تنتجه خطوط أنابيب البيانات في الطبقة الثامنة.

## Further Reading / قراءات إضافية

- **"Hidden Technical Debt in Machine Learning Systems" by D. Sculley et al. (NIPS 2015):** A seminal paper that highlights the unique challenges of maintaining machine learning systems in production. It's a foundational text for the MLOps discipline.
- **"The Data Dichotomy: Rethinking the Way We Treat Data and Services" by C. Thompson (2019):** This article explores the relationship between data and services and makes a strong case for treating data as a product, a core principle behind the idea of data contracts.

- **"الديون الفنية الخفية في أنظمة تعلم الآلة" بقلم د. سكالي وآخرون. (NIPS 2015):** ورقة بحثية أساسية تسلط الضوء على التحديات الفريدة لصيانة أنظمة تعلم الآلة في الإنتاج. إنه نص أساسي لتخصص MLOps.
- **"ثنائية البيانات: إعادة التفكير في الطريقة التي نتعامل بها مع البيانات والخدمات" بقلم سي. طومسون (2019):** يستكشف هذا المقال العلاقة بين البيانات والخدمات ويقدم حجة قوية لمعاملة البيانات كمنتج، وهو مبدأ أساسي وراء فكرة عقود البيانات.
