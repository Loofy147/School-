# Key Concepts for Service Design & API Contracts
# المفاهيم الأساسية لتصميم الخدمة وعقود API

- **API (Application Programming Interface):** A well-defined set of rules and protocols that allows different software components to communicate with each other.
- **REST (REpresentational State Transfer):** An architectural style for designing networked applications. It's based on a stateless, client-server communication model and the use of standard HTTP methods (GET, POST, PUT, DELETE). It typically uses JSON over HTTP/1.1.
- **OpenAPI Specification (formerly Swagger):** A standard, language-agnostic format for describing RESTful APIs. An OpenAPI file allows both humans and computers to discover and understand the capabilities of a service without access to source code.
- **gRPC (Google Remote Procedure Call):** A high-performance, open-source universal RPC framework. It uses Protocol Buffers as its interface definition language and is often used for high-throughput, low-latency communication between backend services. It operates over HTTP/2.
- **API Gateway:** A single entry point for all clients. The API gateway handles requests by routing them to the appropriate backend service, and can also be used for cross-cutting concerns like authentication, rate limiting, and logging.
- **Mock Server:** A simulated API server that returns predefined data based on an API contract. It allows frontend and backend teams to develop and test in parallel.
- **Consumer-Driven Contract Testing:** A testing pattern where the "consumer" (e.g., a frontend client) defines its expectations of an API in a "contract." The "provider" (the backend service) then runs tests to verify that it continuously meets the terms of that contract.

### REST vs. gRPC / REST مقابل gRPC

| Aspect / الجانب           | REST                                      | gRPC                                      |
| ----------------- | ----------------------------------------- | ----------------------------------------- |
| **Protocol**      | HTTP/1.1                                  | HTTP/2                                    |
| **Data Format**   | JSON (human-readable)                     | Protocol Buffers (binary, smaller, faster) |
| **Browser Support**| Excellent (native support)                | Limited (requires a proxy like gRPC-Web)  |
| **Use Case**      | Public-facing APIs, simple request/response | Internal service-to-service communication |

| الجانب           | REST                                      | gRPC                                      |
| ----------------- | ----------------------------------------- | ----------------------------------------- |
| **البروتوكول**      | HTTP/1.1                                  | HTTP/2                                    |
| **تنسيق البيانات**   | JSON (مقروء للإنسان)                      | Protocol Buffers (ثنائي، أصغر، أسرع)     |
| **دعم المتصفح** | ممتاز (دعم أصلي)                          | محدود (يتطلب وكيلًا مثل gRPC-Web)          |
| **حالة الاستخدام**    | واجهات برمجة التطبيقات العامة، طلب/استجابة بسيط | الاتصال الداخلي بين الخدمات             |

### API Versioning Strategies / استراتيجيات إصدار API

When an API changes, you need a strategy for rolling out the changes without breaking existing clients. Common strategies include:
- **URI Path Versioning:** Include the version number in the URL path (e.g., `/api/v1/users`). This is the most common and straightforward approach.
- **Header Versioning:** Include the version number in a custom request header (e.g., `Accepts-version: v1`).
- **Query Parameter Versioning:** Include the version number as a query parameter (e.g., `/api/users?version=1`).

#### استراتيجيات إصدار API

عندما تتغير واجهة برمجة التطبيقات، فأنت بحاجة إلى استراتيجية لطرح التغييرات دون كسر العملاء الحاليين. تشمل الاستراتيجيات الشائعة ما يلي:
- **إصدار مسار URI:** قم بتضمين رقم الإصدار في مسار URL (على سبيل المثال، `/api/v1/users`). هذا هو النهج الأكثر شيوعًا ومباشرة.
- **إصدار الرأس:** قم بتضمين رقم الإصدار في رأس طلب مخصص (على سبيل المثال، `Accepts-version: v1`).
- **إصدار معلمة الاستعلام:** قم بتضمين رقم الإصدار كمعلمة استعلام (على سبيل المثال، `/api/users?version=1`).
- **API (واجهة برمجة التطبيقات):** مجموعة محددة جيدًا من القواعد والبروتوكولات التي تسمح لمكونات البرامج المختلفة بالتواصل مع بعضها البعض.
- **REST (نقل الحالة التمثيلية):** نمط معماري لتصميم التطبيقات المتصلة بالشبكة. يعتمد على نموذج اتصال عميل-خادم عديم الحالة واستخدام أساليب HTTP القياسية (GET ، POST ، PUT ، DELETE).
- **مواصفات OpenAPI (Swagger سابقًا):** تنسيق قياسي ومستقل عن اللغة لوصف واجهات برمجة التطبيقات RESTful. يسمح ملف OpenAPI لكل من البشر وأجهزة الكمبيوتر باكتشاف وفهم إمكانيات الخدمة دون الوصول إلى الكود المصدري.
- **gRPC (استدعاء الإجراء البعيد من Google):** إطار عمل RPC عالمي عالي الأداء ومفتوح المصدر. يستخدم مخازن البروتوكول المؤقتة كلغة تعريف الواجهة الخاصة به وغالبًا ما يستخدم للاتصال عالي الإنتاجية وزمن الانتقال المنخفض بين خدمات الواجهة الخلفية.
- **بوابة API:** نقطة دخول واحدة لجميع العملاء. تتعامل بوابة API مع الطلبات عن طريق توجيهها إلى خدمة الواجهة الخلفية المناسبة، ويمكن استخدامها أيضًا للاهتمامات الشائعة مثل المصادقة وتحديد المعدل والتسجيل.
- **خادم وهمي:** خادم API محاكى يعيد بيانات محددة مسبقًا بناءً على عقد API. يسمح لفرق الواجهة الأمامية والواجهة الخلفية بالتطوير والاختبار بالتوازي.
- **اختبار العقد الذي يحركه المستهلك:** نمط اختبار يحدد فيه "المستهلك" (على سبيل المثال، عميل الواجهة الأمامية) توقعاته من واجهة برمجة التطبيقات في "عقد". يقوم "الموفر" (خدمة الواجهة الخلفية) بعد ذلك بإجراء اختبارات للتحقق من أنه يفي باستمرار بشروط هذا العقد.
