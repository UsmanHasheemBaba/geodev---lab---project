# Data notes

Project: Health facility access analysis — Bosso LGA, Niger State
GeoDev Lab Africa — Month 1, Week 2

---

## GRID3 BOSSO_LGA_BOUNDARY

- Source: GRID3 (data.grid3.org)
- Feature count: [1 features, polygon] filtered from 774 in the source layer
- Geometry type: [Polygon]

## GRID3 BOSSO_WARD

- Source: GRID3 (data.grid3.org)
- Downloaded: [12-9-2026]
- Feature count: [10 wards in LGA, polygon] filtered out of 5,872 in source layer
- Geometry type: [polygon]
- CRS: [fill in]
- Columns: ward_name (text), lga_name (text), state (text)
- Nulls found: No nulls
- Coverage check: Covers my work area fully

## GRID3 BOSSO_HEALTHCARE_FACILITIES

- Source: GRID3 (data.grid3.org)
- Downloaded: [12-9-2026]
- Feature count: [105 features, point] filtered out of 41778 in source layer
- Geometry type: [Point]
- Columns: ward_name (text), lga_name (text), state (text), facility type (text), facility ownership (text), status (text), longitude (decimal/number), latitude (decimal/number) 
- Nulls found: No nulls
- 
- ## Roads, extracted via bbbike (https://extract.bbbike.org/)
- 
- Query: roads within Bosso LGA
- Extracted: [15-09-2026]
- 17,178 features, lines
- Columns: road_name (text), road_type (text), ref_number (text), 
- Coverage check: Covers my work area fully
