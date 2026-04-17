import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs('exports', exist_ok=True)
case_results = pd.read_csv('processed/case_level_results.csv')
mode_metrics = pd.read_csv('processed/mode_metrics.csv')
case_results['execution_time_ms'] = pd.to_numeric(case_results['execution_time_ms'], errors='coerce')
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()
mode_metrics.plot(x='mode', y='total_sessions', kind='bar', ax=ax1, position=1, width=0.4, color='blue', label='Sessions')
mode_metrics.plot(x='mode', y='total_case_rows', kind='bar', ax=ax2, position=0, width=0.4, color='orange', label='Case Rows')
ax1.set_ylabel('Sessions'); ax2.set_ylabel('Case Rows')
plt.title('Sessions and Case Rows by Mode'); plt.savefig('exports/mode_sessions_vs_rows.png'); plt.close()
if 'status' in case_results.columns:
    outcomes = case_results.groupby('mode')['status'].value_counts(normalize=True).unstack().fillna(0)
    for col in ['success', 'crash', 'escape_detected']:
        if col not in outcomes.columns: outcomes[col] = 0
    outcomes[['success', 'crash', 'escape_detected']].plot(kind='bar', figsize=(10, 6))
    plt.title('Outcome Rates by Mode'); plt.ylabel('Rate'); plt.savefig('exports/outcome_rates_by_mode.png'); plt.close()
case_results.dropna(subset=['execution_time_ms']).boxplot(column='execution_time_ms', by='mode', figsize=(10,6))
plt.title('Execution Time by Mode'); plt.suptitle(''); plt.ylabel('ms'); plt.savefig('exports/execution_time_by_mode.png'); plt.close()
