# Adding a New Harness Example

Snapshot example derived from the analyzed Raidar docs pattern. This shows how a short workflow doc can cover one contributor task without polluting the README.

## 1. Extend the Harness Registry

1. Add enum entry in `orchestrator/src/raidar/agents/config.py`.
2. Implement adapter in `orchestrator/src/raidar/agents/adapters/`.
3. Register the adapter in `orchestrator/src/raidar/agents/adapters/registry.py`.

Harness adapter responsibilities:

- validate provider or model prefix compatibility
- validate required CLI binaries and environment prerequisites
- emit Harbor harness name, model argument, and extra Harbor args

## 2. Wire CLI and Rules Mapping

1. Ensure CLI choices include the new harness where relevant.
2. Add rule filename mapping in `orchestrator/src/raidar/agents/rules.py`.

## 3. Ensure Scenario Rules Compatibility

For each active scenario revision, add the harness-specific rules file under `scenarios/<scenario>/v###/rules/`.

## 4. Trace Parsing Coverage

If log format differs, extend the trace parser and add tests so process metrics and trace events are extracted consistently.

## 5. Validate End-to-End

```bash
make harness-validate HARNESS=<harness> MODEL=<provider/model>
make experiment-run \
  SCENARIO=scenarios/hello-world-smoke/v001/scenario.yaml \
  HARNESS=<harness> \
  MODEL=<provider/model>
```
