# Runtime Resolution

Use one skill-local resolver for every shell-facing Python invocation.

## Standard shell contract

```bash
PYTHON_CMD="$(scripts/resolve_python.sh)"
"$PYTHON_CMD" scripts/<helper>.py ...
```

## Rules

- Do not hardcode `python3` in workflow docs, quality gates, or test harnesses.
- Do not probe for `python` versus `python3` in multiple places.
- Once the runtime is resolved, use that same interpreter for every shell-facing helper invocation in the current run.

## Helper path

- Resolver script: [../scripts/resolve_python.sh](../scripts/resolve_python.sh)
