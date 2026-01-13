# Practical Exercise for SRE / DevOps
# تمرين عملي لـ SRE / DevOps

## Objective / الهدف

To define Service Level Indicators (SLIs) and Service Level Objectives (SLOs) for a service and create a basic CI/CD pipeline configuration.
لتحديد مؤشرات مستوى الخدمة (SLIs) وأهداف مستوى الخدمة (SLOs) لخدمة وإنشاء تكوين أساسي لخط أنابيب CI / CD.

## Scenario / سيناريو

Let's focus on the `recommendation-service` from our capstone project. This service provides product recommendations to users and is a critical part of the user experience. The business (Layer 1) has stated that the user experience should be "fast and reliable."

دعنا نركز على `recommendation-service` من مشروعنا النهائي. توفر هذه الخدمة توصيات بالمنتجات للمستخدمين وهي جزء حاسم من تجربة المستخدم. ذكر العمل (الطبقة الأولى) أن تجربة المستخدم يجب أن تكون "سريعة وموثوقة".

## Tasks / المهام

1.  **Define SLIs and SLOs:**
    *   Translate the vague business requirement "fast and reliable" into concrete SLIs and SLOs.
    *   Define at least one **availability** SLI/SLO (e.g., based on the success rate of API calls).
    *   Define at least one **latency** SLI/SLO (e.g., based on the time it takes to respond to a request).
    *   Justify your choice of SLOs. For example, why did you choose 99.9% availability instead of 99%?

2.  **Create a Basic CI/CD Pipeline:**
    *   Write a simple CI/CD pipeline configuration in the syntax of a tool you are familiar with (like GitHub Actions or GitLab CI).
    *   The pipeline should have at least three stages:
        1.  **Build:** Build a Docker image for the service.
        2.  **Test:** Run the unit tests (you can use a placeholder command like `pytest`).
        3.  **Deploy:** Deploy the new image (you can use a placeholder command like `kubectl apply -f k8s/deployment.yaml`).

3.  **Traceability:**
    *   How does your latency SLO relate to the user experience defined in Layer 3?
    *   Where in your CI/CD pipeline would you add a security scanning (SAST) step as required by Layer 5?

1.  **تحديد مؤشرات مستوى الخدمة وأهداف مستوى الخدمة:**
    *   ترجم متطلبات العمل الغامضة "سريع وموثوق" إلى مؤشرات مستوى خدمة وأهداف مستوى خدمة ملموسة.
    *   حدد على الأقل **مؤشر/هدف توفر** واحد (على سبيل المثال، بناءً على معدل نجاح استدعاءات API).
    *   حدد على الأقل **مؤشر/هدف زمن انتقال** واحد (على سبيل المثال، بناءً على الوقت الذي يستغرقه الرد على طلب).
    *   برر اختيارك لأهداف مستوى الخدمة. على سبيل المثال، لماذا اخترت توفر بنسبة 99.9٪ بدلاً من 99٪؟

2.  **إنشاء خط أنابيب CI / CD أساسي:**
    *   اكتب تكوينًا بسيطًا لخط أنابيب CI / CD بصيغة أداة مألوفة لك (مثل GitHub Actions أو GitLab CI).
    *   يجب أن يحتوي خط الأنابيب على ثلاث مراحل على الأقل:
        1.  **بناء:** بناء صورة Docker للخدمة.
        2.  **اختبار:** تشغيل اختبارات الوحدة (يمكنك استخدام أمر نائب مثل `pytest`).
        3.  **نشر:** نشر الصورة الجديدة (يمكنك استخدام أمر نائب مثل `kubectl apply -f k8s/deployment.yaml`).

3.  **التتبع:**
    *   كيف يرتبط هدف مستوى الخدمة الخاص بزمن الانتقال بتجربة المستخدم المحددة في الطبقة الثالثة؟
    *   أين في خط أنابيب CI / CD الخاص بك ستضيف خطوة فحص أمان (SAST) كما هو مطلوب في الطبقة الخامسة؟
