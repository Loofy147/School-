# APIs and API Styles
# واجهات برمجة التطبيقات وأنماطها

An API (Application Programming Interface) is a well-defined contract that allows software components to communicate. Choosing the right architectural style for an API is a critical design decision.

- **[REST](./rest/index.md):** A popular, text-based style ideal for public-facing APIs.
- **[gRPC](./grpc/index.md):** A high-performance, binary protocol ideal for internal service-to-service communication.
- **[OpenAPI Specification](./openapi-specification/index.md):** The standard for formally describing RESTful APIs.

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
