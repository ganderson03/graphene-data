import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

try:
    df = pd.read_csv('processed/case_level_results.csv')
    mm = pd.read_csv('processed/mode_metrics.csv')
except Exception as e:
    print(f"Error loading CSVs: {e}")
    exit(1)

# mode_sessions_vs_rows
fig, ax1 = plt.subplots(figsize=(10, 6))
x = np.arange(len(mm['mode']))
width = 0.35
ax1.bar(x - width/2, mm['total_sessions'], width, label='Sessions', color='skyblue')
ax2 = ax1.twinx()
ax2.bar(x + width/2, mm['total_case_rows'], width, label='Case Rows', color='salmon')
ax1.set_xticks(x)
ax1.set_xticklabels(mm['mode'])
ax1.set_ylabel('Sessions')
ax2.set_ylabel('Case Rows')
plt.title('Sessions vs Case Rows by Mode')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.savefig('exports/mode_sessions_vs_rows.png')
plt.close()

# outcome_rates_by_mode
modes = mm['mode'].unique()
rates = []
for m in modes:
    m_df = df[df['mode'] == m]
    if len(m_df) == 0:
        rates.append({'mode': m, 'success': 0, 'crash': 0, 'escape': 0})
    else:
        # Assuming status column exists and has values like 'success', 'crash', 'escape_detected'
        # Or similar. If not, we'll try to infer from success/error columns if they exist.
        # Based on typical results: status or similar.
        total = len(m_df)
        success = (m_df['status'] == 'success').sum() / total * 100 if 'status' in m_df.columns else 0
        crash = (m_df['status'] == 'crash').sum() / total * 100 if 'status' in m_df.columns else 0
        escape = (m_df['status'] == 'escape_detected').sum() / total * 100 if 'status' in m_df.columns else 0
        rates.append({'mode': m, 'success': success, 'crash': crash, 'escape': escape})

rdf = pd.DataFrame(rates)
rdf.set_index('mode').plot(kind='bar', figsize=(10, 6))
plt.title('Outcome Rates by Mode (%)')
plt.ylabel('Rate (%)')
plt.ylim(0, 100)
plt.savefig('exports/outcome_rates_by_mode.png')
plt.close()

# execution_time_by_mode
data_to_plot = []
labels = []
for m in modes:
    m_df = df[df['mode'] == m]
    if 'execution_time_ms' in m_df.columns and not m_df['execution_time_ms'].dropna().empty:
        data_to_plot.append(m_df['execution_time_ms'].dropna())
        labels.append(m)

plt.figure(figsize=(10, 6))
if data_to_plot:
    plt.boxplot(data_to_plot, labels=labels)
    plt.title('Execution Time by Mode (ms)')
else:
    plt.title('Execution Time by Mode (No data found)')
plt.ylabel('Time (ms)')
plt.savefig('exports/execution_time_by_mode.png')
plt.close()
