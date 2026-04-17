# Data Schema (Initial)

## sessions_manifest.csv

| Column | Description |
| --- | --- |
| session_id | Graphene session id (e.g., session_20260324_214501_a17f) |
| run_date | Date of execution (YYYY-MM-DD) |
| language | Target language (python/java/javascript/go/rust/multi) |
| mode | static/dynamic/both/fused |
| notes | Optional notes on environment or caveats |

Raw folder path is derived from manifest fields as:

- raw/<run_date>_<mode>_<session_id>

## processed tables (planned)

- processed/mode_metrics.csv: per-mode aggregate metrics
- processed/language_metrics.csv: per-language aggregate metrics
- processed/case_level_results.csv: case-level normalized rows
