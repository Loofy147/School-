# Pact Quickstart - Consumer-Driven Contract Testing
# دليل سريع لـ Pact - اختبارات العقود من جانب المستهلك

## Overview / نظرة عامة
This file contains a minimal consumer test example and provider verification steps using Pact and a Pact Broker.
يحتوي هذا الملف على مثال اختبار مستهلك بسيط وخطوات التحقق على المزود باستخدام Pact وPact Broker.

## Consumer test (JavaScript, using @pact-foundation/pact)
## اختبار المستهلك (جافاسكريبت، باستخدام @pact-foundation/pact)

Install / تثبيت:
```
npm install --save-dev @pact-foundation/pact node-fetch
```

Example consumer test (tests/consumer.pact.test.js) / مثال اختبار المستهلك:
```js
// ... same consumer test as original (English) ...
const path = require('path');
const { Pact } = require('@pact-foundation/pact');
const fetch = require('node-fetch');

const provider = new Pact({
  consumer: 'MyConsumer',
  provider: 'MyProvider',
  port: 1234,
  log: path.resolve(process.cwd(), 'logs', 'pact.log'),
  dir: path.resolve(process.cwd(), 'pacts'),
  logLevel: 'INFO'
});

describe('Pact with MyProvider', () => {
  beforeAll(() => provider.setup());
  afterAll(() => provider.finalize());

  it('returns user details', async () => {
    await provider.addInteraction({
      state: 'user 123 exists',
      uponReceiving: 'a request for user 123',
      withRequest: {
        method: 'GET',
        path: '/users/123',
        headers: { Accept: 'application/json' }
      },
      willRespondWith: {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
        body: { id: 123, name: 'Alice' }
      }
    });

    const res = await fetch('http://localhost:1234/users/123', { headers: { Accept: 'application/json' }});
    const json = await res.json();
    expect(json.id).toBe(123);
    expect(json.name).toBe('Alice');
  });
});
```

Run consumer tests to produce `pacts/*.json`.
شغّل اختبارات المستهلك لإنتاج ملفات `pacts/*.json`.

## Publish to Pact Broker / النشر إلى Pact Broker
Assuming you have a Pact Broker URL and credentials:
```
npx pact-broker publish ./pacts --consumer-app-version $(git rev-parse --short HEAD) --broker-base-url https://your-pact-broker.example --broker-token $PACT_BROKER_TOKEN
```

## Provider verification / تحقق المزود
Provider side can verify published pacts:
```
pact-provider-verifier --provider-base-url=http://localhost:8080 --pact-broker-base-url=https://your-pact-broker.example --pact-broker-token=$PACT_BROKER_TOKEN
```

## Notes & Links / ملاحظات وروابط
- Use semantic versioning for consumer app versions when publishing.
- Consider Pact Broker webhooks for consumer/provider CI orchestration.
- استخدم الترقيم الدلالي لنسخ تطبيق المستهلك عند النشر.
- استخدم webhooks في Pact Broker لأتمتة CI بين المستهلك والمزوّد.
