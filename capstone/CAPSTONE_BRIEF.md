# Capstone Brief - Top-Down Systems Engineering (Student Capstone)

## Vision (given to student)
Design and deliver a **Privacy-aware Intelligent Service Platform** that accepts user requests, applies a recommendation or classification ML model, and returns results while satisfying security and compliance constraints.

## Acceptance Criteria (minimum)
1. A Vision document (1-2 pages) describing the business goal and KPIs.
2. At least one ADR describing a major architectural decision (ADR-ID).
3. A Traceability Matrix (RTM) showing how Vision requirements map to ADRs, Services, APIs and Tests.
4. OpenAPI spec for the main service with at least 2 endpoints and contract tests (consumer/provider).
5. An implemented service (one container) with:
   - Unit tests (code coverage >= 60%)
   - CI pipeline that runs unit tests and contract verification
   - A basic deployment manifest (Kubernetes manifest or Docker Compose)
6. An ML pipeline stub (train/infer) or simulated model integrated with the service.
7. Monitoring dashboard (basic SLO/SLI) and a runbook for one failure scenario.
8. Final presentation (slides) showing traceability proof: change in Vision -> ADR -> Service -> Test.

## Deliverables (files to submit)
- vision.pdf or vision.md
- ADRs in `adrs/` folder
- RTM CSV
- openapi.yaml
- service source code repo link or zip
- CI config (e.g., .github/workflows/ci.yml)
- pact pacts or pact broker link
- monitoring screenshots or exported dashboard

## Rubric (grading)
- Vision & ADRs completeness: 25%
- RTM & Traceability Proof: 25%
- Implementation quality & tests: 30%
- Monitoring & runbook: 10%
- Presentation & explanations: 10%

## Traceability Proof checklist (for student)
- Each high-level requirement has at least one linked ADR.
- Each ADR lists affected layers and follow-up tasks.
- Each Service in RTM has at least one automated test (unit or contract).
- CI shows successful contract verification or a pact-broker link.
