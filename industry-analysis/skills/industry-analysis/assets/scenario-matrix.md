# Scenario Matrix Template

> Use during the scenario building step of industry-analysis.
> Build a 2x2 matrix from 2 key variables.

## Key Variables

| Variable | ON | OFF | Why Critical |
|----------|----|-----|--------------|
| **V1: [name]** | [desc] | [desc] | [divergence + uncertainty + timing] |
| **V2: [name]** | [desc] | [desc] | [divergence + uncertainty + timing] |

## Four Scenarios

```
                    V2=OFF                    V2=ON
                  ┌──────────────────┐    ┌──────────────────┐
  V1=OFF          │ Scenario A:      │    │ Scenario B:      │
                  │ Probability: ~XX%│    │ Probability: ~XX%│
                  ├──────────────────┤    ├──────────────────┤
  V1=ON           │ Scenario C:      │    │ Scenario D:      │
                  │ Probability: ~XX%│    │ Probability: ~XX%│
                  └──────────────────┘    └──────────────────┘
```

## Signals to Track

- [ ] Signal for scenario A
- [ ] Signal for scenario B
- [ ] Signal for scenario C
- [ ] Signal for scenario D
