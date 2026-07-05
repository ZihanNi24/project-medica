# Risk Register

## Data Risks

| Risk ID | Risk Description | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|
| R-001 | Patient data leakage across train, validation, and test sets | High | Medium | Use patient-level split and run split-audit script | Open |
| R-002 | Class imbalance between positive and negative cases | High | High | Track class distribution and compare imbalance strategies | Open |
| R-003 | Inconsistent labels across datasets | High | Medium | Define label mapping rules before model training | Open |
| R-004 | Model may learn shortcuts from text markers, image borders, or devices | High | Medium | Use explainability audit and error analysis | Open |

## System Risks

| Risk ID | Risk Description | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|
| S-001 | Prototype may be interpreted as a diagnostic tool | High | Medium | Add “For research use only” disclaimer | Open |
| S-002 | Unsupported image formats may cause app failure | Medium | Medium | Test empty files, invalid formats, and low-quality images | Open |

## Evaluation Risks

| Risk ID | Risk Description | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|
| E-001 | Threshold may be selected using the test set by mistake | High | Low | Define threshold only on validation set | Open |
| E-002 | Results may vary strongly across random seeds | Medium | Medium | Train with multiple random seeds and report mean ± standard deviation | Open |
