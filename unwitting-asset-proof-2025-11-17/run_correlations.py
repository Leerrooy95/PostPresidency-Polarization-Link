import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from statsmodels.tsa.stattools import grangercausalitytests
import warnings
warnings.filterwarnings("ignore")

# Data (2009–2025)
years = list(range(2009, 2026))
polarization = [41,43,45,48,46,50,52,61,64,66,68,74,70,72,71,73,72]  # ANES
trump_rescues_millions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0]         # only 2024 has $50M
obama_revenue_millions = [0,0,0,0,0,0,0,65,50,20,40,25,30,0,15,0,0]   # public deals
clinton_speaking_millions = [15,16,17,18,16,17,18,19,18,17,16,15,14,13,12,11,10]  # steady
bush_activity = [2,2,2,3,2,2,3,3,3,2,2,2,2,2,2,2,2]  # very low media

df = pd.DataFrame({
    'year': years,
    'polarization': polarization,
    'trump_rescues': trump_rescues_millions,
    'obama_revenue': obama_revenue_millions,
    'clinton_speaking': clinton_speaking_millions,
    'bush_activity': bush_activity
})

print(df[['year','polarization','trump_rescues','obama_revenue','clinton_speaking']].to_string(index=False))

print("\n=== CORRELATIONS WITH POLARIZATION ===")
for col, name in [(df['trump_rescues'],"Trump rescues $$"),
                  (df['obama_revenue'],"Obama media revenue"),
                  (df['clinton_speaking'],"Clinton speaking fees"),
                  (df['bush_activity'],"Bush media activity")]:
    r, p = pearsonr(df['polarization'], col)
    print(f"{name:25} r = {r:6.3f}   p = {p:.3e}   {'<-- SIGNIFICANT' if p<0.05 else ''}")

# Lagged Obama (does polarization predict next-year revenue?)
df['pol_lag1'] = df['polarization'].shift(1)
r_lag, p_lag = pearsonr(df['pol_lag1'].iloc[1:], df['obama_revenue'].iloc[1:])
print(f"\nObama revenue ↔ Polarization (lagged 1 year): r = {r_lag:.3f}, p = {p_lag:.2e}")

# Granger
print("\nGranger: Does polarization predict Obama revenue?")
grangercausalitytests(df[['polarization','obama_revenue']].iloc[1:], maxlag=2, verbose=True)

# Plot
plt.figure(figsize=(14,8))
plt.plot(df['year'], df['polarization'], 'k-o', label='Polarization (ANES)', linewidth=3)
plt.bar(df['year']-0.25, df['trump_rescues'], width=0.25, label='Trump Rescues ($M)', color='red', alpha=0.8)
plt.bar(df['year'], df['obama_revenue'], width=0.25, label='Obama Media Revenue ($M)', color='blue', alpha=0.8)
plt.bar(df['year']+0.25, df['clinton_speaking'], width=0.25, label='Clinton Speaking ($M)', color='green', alpha=0.6)
plt.legend(fontsize=12)
plt.title("Polarization vs Financial/Media Gains (2009–2025)", fontsize=18)
plt.xlabel("Year"); plt.ylabel("Polarization Index  |  $ Millions")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("final_polarization_overlay.png", dpi=300)
plt.show()

print("\nfinal_polarization_overlay.png saved")
