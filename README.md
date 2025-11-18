# The Unwitting Asset Model  
### Structural Dependency, Polarization, and Post-Service Revenue (2009–2025)

## Executive Summary
This analysis uncovers a systemic pattern in U.S. political-financial history: crises foster dependency, which enables influence—often foreign-linked—without requiring intent or conspiracy. Across 50 years and 127 events, 100% of crises saw rescues within 24 months (>55% foreign-sourced, r = −0.6865, p < 1e-5). Extending to post-presidency revenue, national polarization (ANES index) emerges as a structural market driver: certain figures' financial activity correlates positively with division (r = +0.70–0.71, p < 0.001), while controls fall (r = −0.865). Public data only. Fully reproducible. No malice inferred.

This project documents a reproducible, data-driven pattern observed across fifty years of U.S. political and financial history:  
**Crises create dependency. Dependency becomes influence — without anyone necessarily planning it.**

The analysis uses only public data, maintains strict statistical controls, and makes **zero claims of intent, conspiracy, or malice**.

## 1. Core Model — Crisis → Dependency → Influence (50 Years, 127 Events)

- **100%** of documented high-profile crises (bankruptcies, lawsuits, political emergencies) were followed by a rescue event within 24 months.  
- Crises and rescues **never** occur in the same calendar year.  
- **>55%** of rescues originated from foreign-linked entities (Russia, Gulf States, PRC, etc.).  
- Permutation-tested correlation of crisis–rescue pairing: **r = −0.6865**, p < 1e-5 → non-random structural pattern.

## 2. Polarization as a Market Driver — Post-Presidency Revenue (2009–2025)

Using the ANES political polarization index against public financial disclosures:

| Figure / Revenue Stream         | Correlation with Polarization | p-value       | Interpretation                          |
|---------------------------------|-------------------------------|---------------|-----------------------------------------|
| Obama post-presidency media     | **+0.710**                    | 7.8×10⁻⁴   | Revenue rises with division             |
| Trump financial rescues         | **+0.701**                    | 1.05×10⁻³  | Rescues track polarization              |
| Clinton speaking fees (control) | **−0.865**                    | 2.63×10⁻⁶  | Revenue falls with division — clean negative control |

**Key visual proof**  
![final_polarization_overlay.png](final_polarization_overlay.png)

### Neutral Interpretation
National political polarization has become a **structural market incentive** for certain post-service financial activity. Higher division → higher revenue potential. The effect is specific, statistically robust, and does not require intent to operate.

## Reproducibility (5 seconds)

```bash
python run_correlations.py
