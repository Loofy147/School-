# Layer 6: SRE / DevOps / Observability at System Level
# الطبقة السادسة: SRE / DevOps / المراقبة على مستوى النظام

Welcome to Layer 6. This layer is the engine room of our system. It's about how we build, deploy, run, and monitor our services in a reliable, automated, and scalable way. DevOps is the culture and practice of collaboration between development and operations teams, while Site Reliability Engineering (SRE) is a prescriptive implementation of DevOps with a strong focus on data and automation.

مرحبًا بك في الطبقة السادسة. هذه الطبقة هي غرفة محرك نظامنا. يتعلق الأمر بكيفية بناء خدماتنا ونشرها وتشغيلها ومراقبتها بطريقة موثوقة ومؤتمتة وقابلة للتطوير. DevOps هي ثقافة وممارسة التعاون بين فرق التطوير والعمليات، في حين أن هندسة موثوقية الموقع (SRE) هي تطبيق إلزامي لـ DevOps مع التركيز القوي على البيانات والأتمتة.

At the system level, this isn't just about a single service. It's about managing the entire ecosystem of services, ensuring they can be deployed independently, communicate reliably, and be monitored from a single pane of glass. The goal is to deliver value to users quickly and reliably, while also maintaining a healthy and sustainable operational posture.

على مستوى النظام، لا يقتصر الأمر على خدمة واحدة. يتعلق الأمر بإدارة النظام البيئي الكامل للخدمات، والتأكد من إمكانية نشرها بشكل مستقل، والتواصل بشكل موثوق، ومراقبتها من لوحة معلومات واحدة. الهدف هو تقديم قيمة للمستخدمين بسرعة وموثوقية، مع الحفاظ أيضًا على وضع تشغيلي صحي ومستدام.

### The Role of the SRE / دور مهندس موثوقية الموقع

The SRE is a software engineer who specializes in reliability. They have two main goals: to ensure that the system is reliable and to make the system more reliable over time. They do this by:
- **Setting and monitoring SLOs:** SREs are responsible for defining the SLOs for the system and for monitoring the system's performance against those SLOs.
- **Automating everything:** SREs are always looking for ways to automate manual tasks, from deploying code to responding to incidents.
- **Building for reliability:** SREs work with developers to design and build systems that are reliable from the ground up.

#### دور مهندس موثوقية الموقع

مهندس موثوقية الموقع هو مهندس برمجيات متخصص في الموثوقية. لديهم هدفان رئيسيان: التأكد من أن النظام موثوق به وجعل النظام أكثر موثوقية بمرور الوقت. يفعلون ذلك عن طريق:
- **إعداد ومراقبة أهداف مستوى الخدمة:** يتحمل مهندسو موثوقية الموقع مسؤولية تحديد أهداف مستوى الخدمة للنظام ومراقبة أداء النظام مقابل تلك الأهداف.
- **أتمتة كل شيء:** يبحث مهندسو موثوقية الموقع دائمًا عن طرق لأتمتة المهام اليدوية، من نشر التعليمات البرمجية إلى الاستجابة للحوادث.
- **البناء من أجل الموثوقية:** يعمل مهندسو موثوقية الموقع مع المطورين لتصميم وبناء أنظمة موثوقة من الألف إلى الياء.
