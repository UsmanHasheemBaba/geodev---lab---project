# My GeoDev Lab Africa project

Health facility access analysis for Bosso Local Government Area, Niger State.

Built over twelve months with GeoDev Lab Africa, Cohort One.

See `project-brief.md` for the full brief and `data-notes.md` for details on
each dataset used.

## Data

- `BOSSO_LGA_BOUNDARY` — GRID3
- `BOSSO_WARD` — GRID3
- `BOSSO_HEALTHCARE_FACILITIES` — GRID3

## Status

- [x] Week 1 — Project brief written
- [x] Week 2 — Data downloaded, opened, described (in progress)
- [x] Week 3 — Reprojected, clipped, quality-checked
- [x] Week 4 — Spatial analysis run


## Month 2: Development Environment and Early Python

-Week 5: Setup Python, VS Code and the terminal hello.py runs
-Week 6: Set up the project with uv and added pandas. check.py prints the pandas version.  
-Week 7: Analyse.py reads wards.csv, coverts each area and classifies each ward.
-Week 8: inspect_data.py summaries latitude and longitude because they only value data/column in my Bosso health facilities data (boss.csv).
- Week 9: summary.py refactors my inspection into small functions and summarises latitude and longitude in my Bosso health facilities data.

### Month 2 reflection
Writing functions that return values, not just print them, finally clicked for me this month. I am still fuzzy on dictionaries and how `report.items()` loops over them. My capstone shows that 105 of the 114 health facilities in my Bosso data have coordinates, so 9 facilities (mostly hospitals in Minna) are missing locations and cannot be mapped yet.
