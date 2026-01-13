# Practical Exercise for Compliance, Privacy & Ethics
# تمرين عملي للامتثال والخصوصية والأخلاقيات

## Objective / الهدف

To create a compliance checklist for a new feature and identify Personally Identifiable Information (PII) in a data model.
لإنشاء قائمة تحقق من الامتثال لميزة جديدة وتحديد المعلومات الشخصية المحددة للهوية (PII) في نموذج البيانات.

## Scenario / سيناريو

Let's return to the "Privacy-aware Intelligent Service Platform." The product team (Layer 3) wants to add a feature that allows users to upload a profile picture and share their location to get more personalized recommendations. The service will operate in the European Union, so GDPR applies.

دعنا نعود إلى "منصة الخدمة الذكية المدركة للخصوصية". يريد فريق المنتج (الطبقة الثالثة) إضافة ميزة تتيح للمستخدمين تحميل صورة ملف شخصي ومشاركة موقعهم للحصول على توصيات أكثر تخصيصًا. ستعمل الخدمة في الاتحاد الأوروبي، لذلك تنطبق اللائحة العامة لحماية البيانات.

## Tasks / المهام

1.  **Identify PII:** Look at the proposed data model for this feature:
    ```json
    {
      "userId": "user-123",
      "profileImageURL": "https://example.com/images/user-123.jpg",
      "lastKnownLocation": {
        "latitude": 52.5200,
        "longitude": 13.4050
      },
      "preferences": {
        "theme": "dark"
      }
    }
    ```
    List all the fields that you consider to be PII. Justify your answer for each.

2.  **Create a Compliance Checklist:** Based on the scenario and your PII analysis, create a short checklist of at least 4 compliance requirements that the development team must implement. These should be specific and actionable. For example:
    *   "Obtain explicit user consent before uploading the profile picture."
    *   "Encrypt the `profileImageURL` and `lastKnownLocation` fields at rest in the database."
    *   "Ensure the user can delete their profile picture and location data at any time."

3.  **Traceability:** For each item on your checklist, name the primary layer that would be responsible for implementing it (e.g., Layer 5 for encryption, Layer 9 for the delete function).

1.  **تحديد المعلومات الشخصية المحددة للهوية:** انظر إلى نموذج البيانات المقترح لهذه الميزة:
    ```json
    {
      "userId": "user-123",
      "profileImageURL": "https://example.com/images/user-123.jpg",
      "lastKnownLocation": {
        "latitude": 52.5200,
        "longitude": 13.4050
      },
      "preferences": {
        "theme": "dark"
      }
    }
    ```
    ضع قائمة بجميع الحقول التي تعتبرها معلومات شخصية محددة للهوية. برر إجابتك لكل منها.

2.  **إنشاء قائمة تحقق من الامتثال:** بناءً على السيناريو وتحليل المعلومات الشخصية المحددة للهوية، قم بإنشاء قائمة تحقق قصيرة من 4 متطلبات امتثال على الأقل يجب على فريق التطوير تنفيذها. يجب أن تكون هذه محددة وقابلة للتنفيذ. على سبيل المثال:
    *   "الحصول على موافقة صريحة من المستخدم قبل تحميل صورة الملف الشخصي."
    *   "تشفير حقلي `profileImageURL` و `lastKnownLocation` في حالة عدم النشاط في قاعدة البيانات."
    *   "التأكد من أن المستخدم يمكنه حذف صورة ملفه الشخصي وبيانات الموقع في أي وقت."

3.  **التتبع:** لكل عنصر في قائمة التحقق الخاصة بك، قم بتسمية الطبقة الأساسية التي ستكون مسؤولة عن تنفيذه (على سبيل المثال، الطبقة الخامسة للتشفير، الطبقة التاسعة لوظيفة الحذف).
