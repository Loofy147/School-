# Level 2: Container Diagram
# المستوى الثاني: مخطط الحاوية

The Container diagram zooms into the system from the Context diagram. It shows the high-level technical building blocks (containers) of your system and their interactions. A "container" is a separately deployable or runnable unit, such as a web application, an API service, a database, or a file system.

يقوم مخطط الحاوية بتكبير النظام من مخطط السياق. يُظهر اللبنات الفنية عالية المستوى (الحاويات) لنظامك وتفاعلاتها. "الحاوية" هي وحدة قابلة للنشر أو التشغيل بشكل منفصل، مثل تطبيق ويب أو خدمة API أو قاعدة بيانات أو نظام ملفات.

## Key Elements / العناصر الرئيسية

- **Containers:** The major technical building blocks of your system. Each container should have a clear responsibility.
- **Relationships:** The communication pathways between containers. It's important to label these with the technology and protocol being used (e.g., "Sends REST API requests to").
- **Actors & External Systems:** The same actors and external systems from the Context diagram, showing how they interact with your containers.

- **الحاويات:** اللبنات الفنية الرئيسية لنظامك. يجب أن تكون لكل حاوية مسؤولية واضحة.
- **العلاقات:** مسارات الاتصال بين الحاويات. من المهم تسميتها بالتكنولوجيا والبروتوكول المستخدم (على سبيل المثال، "يرسل طلبات REST API إلى").
- **الفاعلون والأنظمة الخارجية:** نفس الفاعلين والأنظمة الخارجية من مخطط السياق، مما يوضح كيفية تفاعلهم مع حاوياتك.

## Best Practices / أفضل الممارسات

- **Show Technology Choices:** This is the first level where you start to introduce specific technology choices (e.g., "PostgreSQL Database," "React Web App").
- **Group by Deployment:** A container should represent a unit of deployment. If you deploy your API and your database together, they might be a single container. If you deploy them separately, they should be separate containers.
- **Don't Over-Detail:** Avoid showing internal components or implementation details. Focus on the high-level structure and communication.

- **إظهار الخيارات التقنية:** هذا هو المستوى الأول الذي تبدأ فيه في تقديم خيارات تقنية محددة (على سبيل المثال، "قاعدة بيانات PostgreSQL"، "تطبيق ويب React").
- **المجموعة حسب النشر:** يجب أن تمثل الحاوية وحدة نشر. إذا قمت بنشر واجهة برمجة التطبيقات وقاعدة البيانات معًا، فقد تكونان حاوية واحدة. إذا قمت بنشرهما بشكل منفصل، فيجب أن تكونا حاويات منفصلة.
- **لا تفرط في التفاصيل:** تجنب إظهار المكونات الداخلية أو تفاصيل التنفيذ. ركز على الهيكل عالي المستوى والاتصال.

## PlantUML Example / مثال PlantUML

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND()

Person(user, "User", "A user of the platform.")
System_Ext(data_provider, "External Data Provider", "Provides anonymized data for analysis.")

System_Boundary(platform, "Privacy-aware Intelligent Service Platform") {
    Container(web_app, "Web Application", "React", "Provides the user interface.")
    Container(api, "API Service", "Python (FastAPI)", "Handles business logic and data processing.")
    ContainerDb(db, "Database", "PostgreSQL", "Stores user data and anonymized analytics.")
    Container(anonymizer, "Anonymization Service", "Python", "Anonymizes data from external providers.")
}

Rel(user, web_app, "Uses", "HTTPS")
Rel(web_app, api, "Makes API calls to", "JSON/HTTPS")
Rel(api, db, "Reads from and writes to", "SQL")
Rel(api, anonymizer, "Processes data from")
Rel(anonymizer, data_provider, "Pulls data from", "HTTPS")
@enduml
```
