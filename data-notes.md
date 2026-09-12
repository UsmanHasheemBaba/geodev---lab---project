# Data notes

Project: Health facility access analysis — Bosso LGA, Niger State
GeoDev Lab Africa — Month 1, Week 2

---

## GRID3 BOSSO_LGA_BOUNDARY

- Source: GRID3 (data.grid3.org)
- Downloaded: [12-9-2026]
- Feature count: [1 features, polyline]
- Geometry type: [Polyline]
- CRS: [fill in — Layer Properties → Information]
- Columns: [fill in — Layer Properties → Fields]
- Nulls found: [yes/no — which column]
- Coverage check: [does it match Bosso LGA as you know it?]

## GRID3 BOSSO_WARD

- Source: GRID3 (data.grid3.org)
- Downloaded: [12-9-2026]
- Feature count: [34 features, polygon]
- Geometry type: [polygon]
- CRS: [fill in]
- Columns: [fill in]
- Nulls found: [yes/no — which column]
- Coverage check: [do the ward boundaries look complete / correctly nested inside the LGA boundary?]

## GRID3 BOSSO_HEALTHCARE_FACILITIES

- Source: GRID3 (data.grid3.org)
- Downloaded: [12-9-2026]
- Feature count: [119 features, point]
- Geometry type: [Point]
- CRS: [fill in]
- Columns: [fill in — check for a facility type/category column]
- Nulls found: [yes/no — which column]

### Completeness check
- Compared against: [a place/facility in Bosso you know personally]
- Result: [e.g. "2 of 3 clinics I know are present" or "all facilities I checked are present"]
- Assumed under/over-count: [your estimate, if any]

### Attribute quality check
- Facility type column has [N] distinct values: [list them]
- Any that look like duplicates/inconsistent labels (e.g. "PHC" vs "Primary Health Centre")? [note here]

---

## CRS and preparation (to complete in Week 3)

- All source layers arrived in: [EPSG code]
- Study area: Bosso LGA
- Target projected CRS for Niger State: [EPSG:32631 or 32632 — check your longitude]
- Layers clipped and reprojected: [not yet done — Week 3]

---

## General notes

- All raw files kept untouched in `data/raw/`
- Working/processed files will go in `data/processed/`
- Three questions asked of every dataset: When was it made? Who made it and why? What does it not cover?
