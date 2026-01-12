# Pact Quickstart - Consumer-Driven Contract Testing (Python)
# دليل سريع لـ Pact - اختبارات العقود من جانب المستهلك (بايثون)

## Overview / نظرة عامة
This file contains a minimal consumer test example and provider verification steps using `pact-python`.
يحتوي هذا الملف على مثال اختبار مستهلك بسيط وخطوات التحقق على المزود باستخدام `pact-python`.

## Consumer test (Python, using pact-python)
## اختبار المستهلك (بايثون، باستخدام pact-python)

Install / تثبيت:
```
pip install pact-python pytest requests
```

Example consumer test (`capstone/tests/test_consumer.py`) / مثال اختبار المستهلك:
```python
import pytest
import requests
from pact import Consumer, Provider, Like

# Define the Pact consumer and provider
pact = Consumer('WebFrontend').has_pact_with(Provider('IntelligentService'))

pact.start_service()

@pytest.fixture
def pact_mock_service_url():
    return pact.uri

def test_get_recommendations_consumer(pact_mock_service_url):
    expected_request = {
        'method': 'POST',
        'path': '/recommendations',
        'body': {'user_id': 'user-consumer-test', 'context': {}},
        'headers': {'Content-Type': 'application/json'}
    }
    expected_response = {
        'status': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {
            'user_id': Like('user-consumer-test'),
            'recommendations': Like(['item_1', 'item_2']),
            'confidence': Like(0.85)
        }
    }

    (pact
     .given('a user exists and has recommendations')
     .upon_receiving('a request for recommendations')
     .with_request(**expected_request)
     .will_respond_with(**expected_response))

    with pact:
        response = requests.post(
            f"{pact_mock_service_url}/recommendations",
            json={'user_id': 'user-consumer-test', 'context': {}},
            headers={'Content-Type': 'application/json'}
        )
        assert response.status_code == 200

def pytest_sessionfinish(session, exitstatus):
    pact.stop_service()
```

Run consumer tests to produce `pacts/*.json`.
شغّل اختبارات المستهلك لإنتاج ملفات `pacts/*.json`.

## Provider verification / تحقق المزود
The provider (FastAPI service) can verify the published pacts.

Install the verifier / تثبيت أداة التحقق:
```bash
pip install pact-python
```

Run verification / تشغيل التحقق:
```bash
pact-verifier \\
  --provider-base-url=http://localhost:8000 \\
  --pact-file=./capstone/pacts/webfrontend-intelligentservice.json \\
  --provider-app-version=$(git rev-parse --short HEAD) \\
  --publish-verification-results
```
*Note: You may need to provide Pact Broker details if you are publishing the pacts.*
*ملاحظة: قد تحتاج إلى توفير تفاصيل Pact Broker إذا كنت تنشر العقود.*
