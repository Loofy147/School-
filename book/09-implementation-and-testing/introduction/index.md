# Layer 9: Code, Languages, Frameworks, Testing
# الطبقة التاسعة: الكود واللغات والأطر والاختبار

## Introduction / مقدمة

This is the final layer, where the architectural designs and service contracts are turned into working, tested software. It's the most concrete part of the system, but it's important to remember that all the code written here should be directly traceable to the decisions made in the layers above it. Clean code and a robust testing strategy are essential for building a system that is not only functional but also maintainable and reliable.

هذه هي الطبقة الأخيرة، حيث يتم تحويل التصميمات المعمارية وعقود الخدمة إلى برامج عاملة ومختبرة. إنه الجزء الأكثر واقعية في النظام، ولكن من المهم أن نتذكر أن كل الكود المكتوب هنا يجب أن يكون قابلاً للتتبع مباشرة إلى القرارات المتخذة في الطبقات فوقه. يعد الكود النظيف واستراتيجية الاختبار القوية ضروريين لبناء نظام ليس وظيفيًا فحسب، بل يمكن صيانته وموثوقيته أيضًا.

In this layer, you will learn about:
- The principles of writing clean, maintainable code.
- The different types of software testing and how they fit together (the Testing Pyramid).
- The importance of choosing the right languages and frameworks for the job.

في هذه الطبقة، ستتعلم عن:
- مبادئ كتابة كود نظيف وقابل للصيانة.
- الأنواع المختلفة لاختبار البرامج وكيفية تناسبها معًا (هرم الاختبار).
- أهمية اختيار اللغات والأطر المناسبة للوظيفة.

### Code Review Best Practices / أفضل ممارسات مراجعة الكود

Code reviews are a critical part of the development process. They help to catch bugs, improve code quality, and share knowledge among the team. Some best practices for code reviews include:
- **Be kind:** Remember that you are reviewing the code, not the person.
- **Be specific:** Provide specific examples of what you think could be improved.
- **Automate what you can:** Use linters and formatters to catch simple style issues so you can focus on the important stuff.
- **Keep it small:** Small, focused pull requests are easier to review than large, sprawling ones.

#### أفضل ممارسات مراجعة الكود

تعد مراجعات الكود جزءًا مهمًا من عملية التطوير. فهي تساعد في اكتشاف الأخطاء وتحسين جودة الكود ومشاركة المعرفة بين الفريق. تتضمن بعض أفضل الممارسات لمراجعات الكود ما يلي:
- **كن لطيفًا:** تذكر أنك تراجع الكود وليس الشخص.
- **كن محددًا:** قدم أمثلة محددة لما تعتقد أنه يمكن تحسينه.
- **أتمتة ما يمكنك:** استخدم أدوات التدقيق والتنسيق لاكتشاف مشكلات النمط البسيطة حتى تتمكن من التركيز على الأشياء المهمة.
- **اجعلها صغيرة:** من الأسهل مراجعة طلبات السحب الصغيرة والمركزة من الطلبات الكبيرة والمترامية الأطراف.
