# Post-Presidency Revenue & Affective Polarization (2009–2025)
### Unwitting Asset Model – Updated November 18, 2025

This repository examines whether post-presidency revenue streams for recent U.S. presidents correlate with rising affective polarization in American politics, as measured by the American National Election Studies (ANES) feeling-thermometer-based polarization index.

**Core observation**: For most modern ex-presidents, higher societal polarization appears associated with higher post-service earnings (speaking fees, book advances, media deals, financial rescues, etc.). The Clinton era serves as a clear negative control (revenue fell as polarization later rose).

All data are public. All calculations are fully reproducible. No intent or malice is inferred or alleged — this is a structural/market observation only.

## Latest Update – November 18, 2025
- Added George W. Bush (2009–2020 speaking fees, book advance, foreign-linked events)
- Added preliminary 2025 Joe Biden data (Hachette memoir advance; acts as emerging outlier or lag case)
- Updated correlation table and visualization (`final_polarization_overlay_v2.png`)
- New `documents/` folder with supporting files (e.g., OGE termination PDFs)

## Files & Data
- **Core script**: `run_correlations.py` – Re-run for latest calculations (pulls public CSVs + ANES data automatically)
- **Visualization**: `final_polarization_overlay_v2.png` – Polarization overlay chart
- **[documents/ folder](documents/)**: Raw disclosures and attachments
  - `biden_termination_278e_2025.pdf` – Joe Biden's OGE Form 278e termination report (filed January 20, 2025)
- **Other**: `requirements.txt` (if needed), `sources.md` (full source links)

## Correlation Summary (2009–2025)

| President / Revenue Stream                  | Correlation (r) with ANES Polarization | p-value        | Interpretation                                    | Key Sources                                      |
|---------------------------------------------|----------------------------------------|----------------|---------------------------------------------------|--------------------------------------------------|
| Barack Obama – media & book deals           | +0.710                                 | 7.8 × 10⁻⁴    | Revenue rises with division                       | OGE 278e, publisher disclosures                 |
| Donald Trump – financial rescues & media    | +0.701                                 | 1.05 × 10⁻³   | Rescues track polarization                        | Forbes, Truth Social filings                     |
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
