# Design Options

- Created: 2026-03-24
- Last updated: 2026-03-24T09:12:00Z

## Candidate Options

| Option | Summary | Tradeoffs | Status |
| ------ | ------- | --------- | ------ |
| Option A | keep one continuous skill prompt and improve instructions only | simpler docs, weak enforcement | rejected |
| Option B | use a deterministic controller plus fresh runner phases | stronger separation, more helper scripts | chosen |

## Chosen Direction

- Selected option: Option B
- Why it fits the goal: it enforces hard phase separation while preserving the current final handoff package.

## Rejected Alternatives

- Rejected option: Option A
- Rejection reason: prompt-only discipline is not a strong enough control boundary for the required separation.

## Open Decisions

- D1: none for the example fixture
