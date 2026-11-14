# paycore
One payment orchestration service all your apps call, instead of each app integrating
Hubtel, Paystack and other Ghanaian providers on its own. A single API with
idempotency, retries and reconciliation built in

## Why

- **One integration, not one per app.** Payment logic (idempotency, callbacks,
  reconciliation) is hard to get right. paycore gets it right once.
- **One whitelisted server.** Hubtel whitelists each calling server's IP.
  Apps call paycore; only paycore calls Hubtel.
- **COnfigurable provider per payment type.** Hubtel for mobile money, Paystack
  for foreign cards, etc.
- **Provider keys in one place**, not copied into every app.
- **One place to debug.** Every provider call and callback is logged in one
  service.
- **Scales on its own.** A payment spike (results day, a pageant final) scales
  paycore, not every app.


## Where it comes from

Built from running payments in production in Ghana: a pageant voting platform
that took 26,000 paid votes, and a USSD service for WASSCE checker PINs that
served 17,000 users. Both hit the same problems: [duplicate callbacks, and
payments stuck between pending and paid]. paycore is designed around those
failures.

## Trade-offs

- **Single point of failure.** If paycore is down, no app can take payments,
  so it has to be the most reliable service you run.
- **One extra network hop** on every payment.

## Status

Work in progress. v1: Hubtel Online Checkout with idempotency and
reconciliation.
Planned: Paystack; switching new payments to Paystack when Hubtel
payments keep failing.