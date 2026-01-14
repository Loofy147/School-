# Level 1: System Context Diagram
# المستوى الأول: مخطط سياق النظام

The System Context diagram is the highest level of abstraction in the C4 model. It provides a bird's-eye view of your system and its interactions with the outside world. It is the most important diagram for communicating the scope and key relationships of your system to a non-technical audience.

مخطط سياق النظام هو أعلى مستوى من التجريد في نموذج C4. إنه يوفر نظرة عامة على نظامك وتفاعلاته مع العالم الخارجي. وهو أهم مخطط لتوصيل نطاق النظام وعلاقاته الرئيسية لجمهور غير تقني.

## Key Elements / العناصر الرئيسية

- **Your System:** Represented as a single, central box. This is the "black box" that you are describing.
- **Actors:** The users or roles that interact directly with your system (e.g., "Customer," "Administrator").
- **External Systems:** Other software systems that your system interacts with (e.g., "Stripe Payment Gateway," "Google Maps API").

- **نظامك:** يتم تمثيله كمربع مركزي واحد. هذا هو "الصندوق الأسود" الذي تصفه.
- **الفاعلون (Actors):** المستخدمون أو الأدوار التي تتفاعل مباشرة مع نظامك (على سبيل المثال، "العميل"، "المسؤول").
- **الأنظمة الخارجية:** أنظمة البرامج الأخرى التي يتفاعل معها نظامك (على سبيل المثال، "بوابة الدفع Stripe"، "واجهة برمجة تطبيقات خرائط Google").

## Best Practices / أفضل الممارسات

- **Keep it Simple:** Avoid technical details. Focus on people and systems, not technologies or protocols.
- **Clear Naming:** Use clear and understandable names for your system, actors, and external systems.
- **Focus on Scope:** The primary goal is to show what is *inside* your system's scope and what is *outside*.

- **اجعلها بسيطة:** تجنب التفاصيل الفنية. ركز على الأشخاص والأنظمة، وليس التقنيات أو البروتوكولات.
- **تسمية واضحة:** استخدم أسماء واضحة ومفهومة لنظامك والفاعلين والأنظمة الخارجية.
- **التركيز على النطاق:** الهدف الأساسي هو إظهار ما هو *داخل* نطاق نظامك وما هو *خارج*.

## PlantUML Example / مثال PlantUML

Here is a simple PlantUML example for a "Privacy-aware Intelligent Service Platform."

فيما يلي مثال بسيط لـ PlantUML لـ "منصة خدمات ذكية واعية بالخصوصية".

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

LAYOUT_WITH_LEGEND()

Person(user, "User", "A user of the platform.")
System_Ext(data_provider, "External Data Provider", "Provides anonymized data for analysis.")
System_Ext(regulator, "Regulatory Body", "Audits the system for privacy compliance.")

System(platform, "Privacy-aware Intelligent Service Platform", "Our system that provides intelligent services while protecting user privacy.")

Rel(user, platform, "Uses services")
Rel(platform, data_provider, "Pulls data from")
Rel(regulator, platform, "Audits")
@enduml
```
