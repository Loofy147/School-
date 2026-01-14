# SLIs, SLOs, and SLAs
# مؤشرات مستوى الخدمة، وأهداف مستوى الخدمة، واتفاقيات مستوى الخدمة

This framework is essential for defining and managing the reliability of a service.

- **Service Level Indicator (SLI):** A quantitative measure of some aspect of the level of service being provided (e.g., the percentage of requests that complete in under 100ms).
- **Service Level Objective (SLO):** A target value or range of values for an SLI. This is an internal goal for the team (e.g., 99.9% of requests will be faster than 100ms).
- **Service Level Agreement (SLA):** An explicit, legally-binding contract with a customer that defines the consequences of not meeting the SLOs.

## How to define them:
1.  **Choose what to measure:** Start by identifying what matters to your users. Is it speed? Availability? Something else?
2.  **Define the SLI:** Create a specific, measurable metric for the user-centric property you chose.
3.  **Set the SLO:** Set a realistic target for your SLI based on user expectations and business needs.
4.  **Establish the SLA:** If necessary, create a formal agreement with your users that defines the consequences of missing the SLO.

---

هذا الإطار ضروري لتحديد وإدارة موثوقية الخدمة.

- **مؤشر مستوى الخدمة (SLI):** مقياس كمي لبعض جوانب مستوى الخدمة المقدمة (على سبيل المثال، النسبة المئوية للطلبات التي تكتمل في أقل من 100 مللي ثانية).
- **هدف مستوى الخدمة (SLO):** قيمة مستهدفة أو نطاق من القيم لـ SLI. هذا هدف داخلي للفريق (على سبيل المثال، 99.9٪ من الطلبات ستكون أسرع من 100 مللي ثانية).
- **اتفاقية مستوى الخدمة (SLA):** عقد صريح وملزم قانونًا مع العميل يحدد عواقب عدم تحقيق أهداف مستوى الخدمة.

## كيفية تحديدها:
1.  **اختر ما تريد قياسه:** ابدأ بتحديد ما يهم المستخدمين. هل هي السرعة؟ التوفر؟ شيء آخر؟
2.  **حدد SLI:** أنشئ مقياسًا محددًا وقابلًا للقياس للخاصية التي تركز على المستخدم والتي اخترتها.
3.  **حدد SLO:** حدد هدفًا واقعيًا لـ SLI الخاص بك بناءً على توقعات المستخدم واحتياجات العمل.
4.  **أنشئ SLA:** إذا لزم الأمر، قم بإنشاء اتفاقية رسمية مع المستخدمين تحدد عواقب عدم تحقيق SLO.
