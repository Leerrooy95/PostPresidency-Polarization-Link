# Post-Service Revenue Extension (2009–2025)
### Unwitting Asset Model — Updated November 18, 2025

Observed correlation between rising ANES affective polarization and post-presidency revenue streams (Obama, Trump, Bush, Clinton control, preliminary Biden).

All data public · No intent or malice alleged · Structural observation only

### Full analysis (text + table + new Bush & Biden sections)
![Page 1](page1.png)

### Updated visualization (Bush & Biden added)
![Page 2](page2.png)

*Chart generated November 18, 2025*

Last updated: November 18, 2025
| Clinton – speaking fees (negative control)  | –0.865                    | 2.63 × 10⁻⁶  | Revenue falls as division rises                   |
| Biden – 2025 preliminary (book advance)     | ~ +0.65                   | < 0.01        | Lower than expected despite peak polarization     |

Visualization: see **page2.png** above (generated November 18, 2025).

## Sources
All figures are derived from publicly available disclosures:
- ANES Time Series Cumulative Data File
- OGE Form 278e filings and termination reports
- Publisher advances, Forbes tracking, PolitiFact, ABC News / Center for Public Integrity speaking-fee databases, SEC filings, etc.

## Disclaimer
This repository contains only public financial and survey data with accompanying analysis. Nothing herein asserts wrongdoing or coordination of any kind.

Last updated: November 18, 2025  
Open an issue or submit a pull request if newer public disclosures become available.| Donald Trump – financial rescues & media    | +0.701                                 | 1.05 × 10⁻³   | Rescues track polarization                        | Forbes, Truth Social filings                     |
| George W. Bush – speaking fees & books      | +0.680                                 | < 0.01         | Revenue rises with division (~35% foreign-linked) | PolitiFact, ABC News, CPI database, OGE filings |
| Hillary Clinton – speaking fees (negative control) | –0.865                          | 2.63 × 10⁻⁶   | Revenue falls as division rises                   | CNN Money, OGE filings                           |
| Joe Biden – 2025 preliminary (book advance) | ~ +0.65 (weakens overall set)          | < 0.01         | Lower than expected despite peak polarization     | Hachette announcement, [OGE termination](documents/biden_termination_278e_2025.pdf) (1/20/2025) |

## Key Additions Detail

### George W. Bush (2009–2025)
- ~200 paid speeches (2009–2020) at $100k–$175k each → est. $25–35 M
- “Decision Points” (2010) advance: $7 M
- ~30–40 % of speaking engagements foreign (Canada, UAE, South Korea, etc.)
- Net worth growth: ~$20 M (2009) → ~$50 M+ (2025)
- Polarization context: ANES index rose from ~41 (2008) to ~50+ during peak earning years

**Sources**:
- PolitiFact (2015) – 140 speeches in first two years
- ABC News / Center for Public Integrity speaking fee database
- Bush OGE termination report & subsequent disclosures

### Joe Biden – Preliminary 2025
- Only confirmed revenue to date: ~$10 M Hachette memoir advance (July 2025)
- No major speaking circuit or media deals reported as of November 18, 2025
- Acts as emerging outlier or lag case – monitor 2026 disclosures

## Usage / Reproducibility
```bash
# Install requirements (if any)
pip install -r requirements.txt

# Re-run everything (pulls latest public CSV + ANES data automatically)
python run_correlations.py --include-bush --include-biden-prelim
