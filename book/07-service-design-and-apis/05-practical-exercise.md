# Practical Exercise for Service Design & API Contracts
# تمرين عملي لتصميم الخدمة وعقود API

## Objective / الهدف

To create a basic OpenAPI 3.0 specification for a new service.
لإنشاء مواصفات OpenAPI 3.0 أساسية لخدمة جديدة.

## Scenario / سيناريو

A new service, `user-profile-service`, is being added to the "Privacy-aware Intelligent Service Platform." The product team (Layer 3) has provided the following requirements:
*   Users should be able to fetch their own profile information.
*   Users should be able to update their profile information.
*   The profile information includes a `displayName` (string) and a `theme` preference (string, either "light" or "dark").

متطلبات فريق المنتج (الطبقة الثالثة):
*   يجب أن يكون المستخدمون قادرين على جلب معلومات ملفهم الشخصي.
*   يجب أن يكون المستخدمون قادرين على تحديث معلومات ملفهم الشخصي.
*   تتضمن معلومات الملف الشخصي `displayName` (سلسلة) وتفضيل `theme` (سلسلة، إما "فاتح" أو "داكن").

## Tasks / المهام

1.  **Design the API:**
    *   What HTTP methods and URL paths should be used for the two operations (fetch and update)?
    *   What should the request body look like for the update operation?
    *   What should the response body look like for both operations?
    *   What are the possible success and error HTTP status codes?

2.  **Create the OpenAPI Specification:**
    *   Write a valid `openapi.yaml` file that describes the API you designed.
    *   The specification should include:
        *   Basic info (title, version).
        *   At least two paths.
        *   Definitions for the request and response bodies in the `components/schemas` section.
        *   At least one example for each schema.

3.  **Traceability:**
    *   How does your API design fulfill the requirements from Layer 3?
    *   Add a `security` section to your OpenAPI specification that references a JWT-based security scheme, as required by Layer 5.

1.  **تصميم API:**
    *   ما هي أساليب HTTP ومسارات URL التي يجب استخدامها للعمليتين (جلب وتحديث)؟
    *   كيف يجب أن يبدو نص الطلب لعملية التحديث؟
    *   كيف يجب أن يبدو نص الاستجابة لكلتا العمليتين؟
    *   ما هي أكواد حالة HTTP المحتملة للنجاح والخطأ؟

2.  **إنشاء مواصفات OpenAPI:**
    *   اكتب ملف `openapi.yaml` صالحًا يصف واجهة برمجة التطبيقات التي صممتها.
    *   يجب أن تتضمن المواصفات:
        *   معلومات أساسية (العنوان، الإصدار).
        *   مساران على الأقل.
        *   تعريفات لنصوص الطلب والاستجابة في قسم `components/schemas`.
        *   مثال واحد على الأقل لكل مخطط.

3.  **التتبع:**
    *   كيف يلبي تصميم API الخاص بك متطلبات الطبقة الثالثة؟
    *   أضف قسم `security` إلى مواصفات OpenAPI الخاصة بك يشير إلى مخطط أمان قائم على JWT، كما هو مطلوب في الطبقة الخامسة.
