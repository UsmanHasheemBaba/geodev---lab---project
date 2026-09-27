# Month 1 Summary

## Question

Which settlements in Bosso Local Government Area (Niger State) are more than 5 km from a health facility?

## Operation

Buffered health facility point locations by 5 km (dissolved into a single coverage shape), then overlaid the
result against the population-by-settlement layer to identify settlements or clusters of population falling
outside the 5 km coverage zone.

## Expected

Coverage concentrated around the built-up core of Bosso town, Maikunkele, Bosso 2 Central and Maitumbi, since
that is where facility density is visibly highest. Expected one or two underserved clusters toward the LGA's
western and southern edges (toward Kodo, Beji, Garatu, Katcha), where facility markers are sparser.

## Got

The 5 km buffers overlap heavily in the eastern/central cluster (Bosso, Maikunkele, Bosso 2 Central, Maitumbi,
Chachanga, Shatta), so that side of the LGA has near-total coverage. Coverage thins out moving west and south:

* Settlement clusters around **Kodo** and the southern part of **Beji** sit close to the buffer edge, with
some population patches only partially covered.
* Population pockets near **Garatu** and toward **Katcha** (southern boundary) fall outside any 5 km buffer.
* The northern tip of the LGA (above Shatta, near the Shiroro boundary) has isolated facility coverage with
gaps between buffer circles.

## What surprised me

* Facility placement is heavily clustered around Bosso/Maikunkele rather than spread evenly across the LGA,
so the buffer analysis shows large contiguous "shadow" zones rather than scattered small gaps.
* Some population-by-settlement patches (the olive/yellow shading) sit visibly outside every buffer circle,
particularly toward the south — this is the clearest actionable finding on the map.

## Limitations, stated plainly

* Straight-line (Euclidean) distance, not travel distance. Road access, river crossings, and terrain are not
accounted for, so an area "within 5 km" on the map may still be a long trip in practice.
* No facility-type weighting — a primary health centre and a fully-equipped hospital are treated identically
in the buffer, even though capacity differs.
* Haven't cross-checked facility completeness against local knowledge (per the Week 2/3 quality checklist) —
the facility layer may under- or over-count actual operating health centres.
* 5 km is a fixed, uniform threshold; it doesn't adjust for population density, so a sparsely populated area
just outside the buffer is treated the same as a densely populated one.

## What I still need

* Road network data (https://www.openstreetmap.org/) to move from straight-line to travel-distance access in a later month.
* Population figures per settlement/ward (numeric, not just visual density) to convert "area uncovered" into
"people uncovered," which is the number that actually matters for prioritizing new facilities.
* A facility-type/capacity attribute, to distinguish basic clinics from hospitals in future coverage analysis.
<img width="1449" height="970" alt="HEALTHCARE FACILITES BOSSO LGA" src="https://github.com/user-attachments/assets/fbd3a585-7d45-4893-a64c-ca5e64332338" />


