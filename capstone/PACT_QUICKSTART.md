# Pact Quickstart (Consumer-Driven Contract Testing) - Quick Reference

## Overview
This file contains a minimal consumer test example and provider verification steps using Pact and a Pact Broker.

## Consumer test (JavaScript, using @pact-foundation/pact)
Install:
```
npm install --save-dev @pact-foundation/pact node-fetch
```

Example consumer test (tests/consumer.pact.test.js):
```js
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

## Publish to Pact Broker
Assuming you have a Pact Broker URL and credentials:
```
npx pact-broker publish ./pacts --consumer-app-version $(git rev-parse --short HEAD) --broker-base-url https://your-pact-broker.example --broker-token $PACT_BROKER_TOKEN
```

## Provider verification
Provider side can verify published pacts:
```
pact-provider-verifier --provider-base-url=http://localhost:8080 --pact-broker-base-url=https://your-pact-broker.example --pact-broker-token=$PACT_BROKER_TOKEN
```

Or use a CI job that fetches pacts from the broker and runs provider tests.

## Notes & Links
- Use semantic versioning for consumer app versions when publishing.
- Consider Pact Broker webhooks for consumer/provider CI orchestration.
