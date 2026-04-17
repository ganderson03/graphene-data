# Graphene Data Repository

This repository stores data artifacts produced by Graphene-HA experiments.

## Directory Layout

- raw/: Original, unmodified data drops from runs.
- processed/: Cleaned and normalized data tables.
- exports/: Figures, dashboards, and publication-ready outputs.
- metadata/: Manifests and run-level metadata.
- docs/: Data definitions and ingestion notes.

## Recommended Ingestion Flow

1. Copy a new run output bundle into raw/ with a dated folder name.
2. Register the run in metadata/sessions_manifest.csv.
3. Transform raw data into normalized tables in processed/.
4. Export aggregate tables/plots to exports/ for report use.

## Naming Convention

Use manifest-derived folder names:

- raw/YYYY-MM-DD_mode_session_id/

Example:

- raw/2026-04-16_dynamic_session_20260416_120000_a17f/
