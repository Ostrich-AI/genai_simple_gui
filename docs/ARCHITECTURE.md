# genai_simple_gui architecture

## Source map

This diagram maps source folders/files actually present in the reviewed commit. It describes code organisation, not a verified live network topology.

```mermaid
flowchart TD
  R["genai_simple_gui"]
  N0["__pycache__"]
  R --> N0
```

## Entry points

- [Dockerfile](https://github.com/Ostrich-AI/genai_simple_gui/blob/124c2aba8cadb528c2b6e201d3abe3dd023f17f1/Dockerfile)

## Integration and deployment context

For internal users, the wider system context is maintained in the Ostrich system-blueprints engineering hub. Public demo/installer repositories expose their own source/release context only.

Runtime calls, trust boundaries, exposed URLs, identity controls, data storage and residency must be checked against the chosen release's actual code and environment configuration before drawing security conclusions. Repository/source dependencies do not establish an enabled integration.

## Reviewed source

- [Dockerfile](https://github.com/Ostrich-AI/genai_simple_gui/blob/124c2aba8cadb528c2b6e201d3abe3dd023f17f1/Dockerfile)
- [requirements.txt](https://github.com/Ostrich-AI/genai_simple_gui/blob/124c2aba8cadb528c2b6e201d3abe3dd023f17f1/requirements.txt)
- [inference.py](https://github.com/Ostrich-AI/genai_simple_gui/blob/124c2aba8cadb528c2b6e201d3abe3dd023f17f1/inference.py)

Review date: 2026-11-15. Missing topology/configuration evidence is requested through the central agency handover draft rather than separate forms.
