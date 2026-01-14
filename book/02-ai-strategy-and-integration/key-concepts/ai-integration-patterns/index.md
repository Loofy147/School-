# AI Integration Patterns
# أنماط تكامل الذ 수요 الاصطناعي

Choosing the right pattern to integrate AI into a system is a critical architectural decision. It depends on the problem you are trying to solve, the data you have, and your budget. This section explores the most common and effective patterns.

- **[Retrieval-Augmented Generation (RAG)](./rag/index.md):** For grounding models in factual, real-time data.
- **[Agentic Systems](./agentic-systems/index.md):** For creating autonomous agents that can perform complex tasks.
- **[Fine-Tuning](./fine-tuning/index.md):** For adapting a model to a specific domain or style.

---

### Trade-offs: RAG vs. Fine-Tuning / المفاضلات: RAG مقابل الضبط الدقيق

| Aspect / الجانب      | RAG                                       | Fine-Tuning                               |
| ----------------- | ----------------------------------------- | ----------------------------------------- |
| **Knowledge Update** | Easy to update (just update the data source) | Requires retraining the model             |
| **Cost**          | Generally cheaper (training is expensive) | Can be very expensive and time-consuming  |
| **Explainability**| High (you can see the retrieved context) | Low (it's hard to know why the model says what it does) |
| **Task-specific Skills** | Less effective for teaching new skills | More effective for teaching a specific style or tone |

| الجانب           | RAG                                       | الضبط الدقيق                              |
| ----------------- | ----------------------------------------- | ----------------------------------------- |
| **تحديث المعرفة**  | سهل التحديث (فقط قم بتحديث مصدر البيانات)  | يتطلب إعادة تدريب النموذج                 |
| **التكلفة**         | أرخص بشكل عام (التدريب مكلف)             | يمكن أن يكون مكلفًا للغاية ويستغرق وقتًا طويلاً |
| **قابلية الشرح** | عالية (يمكنك رؤية السياق المسترد)         | منخفضة (من الصعب معرفة سبب قول النموذج لما يقوله) |
| **المهارات الخاصة بالمهمة** | أقل فعالية لتعليم مهارات جديدة        | أكثر فعالية لتعليم نمط أو نبرة معينة        |
