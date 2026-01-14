# Level 3: Component Diagram
# المستوى الثالث: مخطط المكونات

The Component diagram zooms into an individual container to show its internal components. A component is a logical grouping of related code that represents a major functional area of the container. This diagram is typically used by developers to understand the internal structure of a service or application.

يقوم مخطط المكونات بتكبير حاوية فردية لإظهار مكوناتها الداخلية. المكون هو تجميع منطقي للكود ذي الصلة يمثل منطقة وظيفية رئيسية للحاوية. يستخدم هذا المخطط عادةً من قبل المطورين لفهم الهيكل الداخلي لخدمة أو تطبيق.

## Key Elements / العناصر الرئيسية

- **Components:** The logical building blocks of a container. Each component should have a well-defined responsibility and interface (e.g., "User Management Component," "Report Generation Component").
- **Relationships:** The interactions between components within the container.
- **Other Containers:** It's often useful to show key external dependencies on other containers (e.g., the database).

- **المكونات:** اللبنات المنطقية للحاوية. يجب أن يكون لكل مكون مسؤولية وواجهة محددة جيدًا (على سبيل المثال، "مكون إدارة المستخدم"، "مكون إنشاء التقارير").
- **العلاقات:** التفاعلات بين المكونات داخل الحاوية.
- **الحاويات الأخرى:** غالبًا ما يكون من المفيد إظهار التبعيات الخارجية الرئيسية على الحاويات الأخرى (مثل قاعدة البيانات).

## Best Practices / أفضل الممارسات

- **Focus on One Container at a Time:** Don't try to show the components of all your containers in one diagram.
- **Technology Agnostic (Mostly):** Components are about logical structure, so you don't need to specify every technology. However, it can be useful to show the technology of the component's interface (e.g., "REST API").
- **Clear Interfaces:** Define the public interface of each component. What services does it provide to other components?

- **التركيز على حاوية واحدة في كل مرة:** لا تحاول إظهار مكونات جميع حاوياتك في مخطط واحد.
- **محايد تقنيًا (في الغالب):** تتعلق المكونات بالهيكل المنطقي، لذلك لا تحتاج إلى تحديد كل تقنية. ومع ذلك، قد يكون من المفيد إظهار تقنية واجهة المكون (على سبيل
المثال، "REST API").
- **واجهات واضحة:** حدد الواجهة العامة لكل مكون. ما هي الخدمات التي يقدمها للمكونات الأخرى؟

## PlantUML Example / مثال PlantUML

This example zooms into the "API Service" container.

هذا المثال يقوم بتكبير حاوية "خدمة API".

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUM/master/C4_Component.puml

LAYOUT_WITH_LEGEND()

Container(web_app, "Web Application", "React", "Provides the user interface.")
ContainerDb(db, "Database", "PostgreSQL", "Stores user data and anonymized analytics.")
Container(anonymizer, "Anonymization Service", "Python", "Anonymizes data from external providers.")

System_Boundary(api, "API Service") {
    Component(auth, "Authentication Component", "Handles user sign-in and permissions.")
    Component(user_service, "User Service", "Manages user profiles and settings.")
    Component(analytics_service, "Analytics Service", "Processes and exposes anonymized analytics.")
    Component(data_ingestion, "Data Ingestion Component", "Receives data from the Anonymization Service.")

    Rel(auth, user_service, "Uses")
    Rel(analytics_service, db, "Reads anonymized data from", "SQL")
    Rel(user_service, db, "Reads/writes user data to", "SQL")
    Rel(data_ingestion, analytics_service, "Forwards data to")
}

Rel(web_app, auth, "Authenticates via", "JSON/HTTPS")
Rel(web_app, user_service, "Manages user profile via", "JSON/HTTPS")
Rel(web_app, analytics_service, "Views analytics via", "JSON/HTTPS")
Rel(anonymizer, data_ingestion, "Sends anonymized data to", "AMQP")
@enduml
```
