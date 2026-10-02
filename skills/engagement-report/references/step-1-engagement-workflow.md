# Step 1 Workflow: Add or select an engagement

## Objective

Create the standard engagement structure or safely select an existing one.

## Required actions

1. Resolve this skill's directory from the location of `SKILL.md`.
2. For a new engagement, run:

   ```bash
   python3 scripts/engagement_report.py add-engagement \
     --repo <report-repository> \
     --name "<engagement name>"
   ```

3. Use the returned slug for subsequent commands.
4. Do not rename or rewrite existing period directories.
5. For a new period, run `generate` with explicit dates:

   ```bash
   python3 scripts/engagement_report.py generate \
     --repo <report-repository> \
     --engagement <engagement-slug> \
     --period-start YYYY-MM-DD \
     --period-end YYYY-MM-DD
   ```

6. Add source material under the generated period's `notes/` directory and rerun `update`.

## Done when

- The engagement has a stable slug and README.
- The selected period path is `<engagement>/<period_start>_<period_end>/`.
- A `notes/` tree exists for source material.
