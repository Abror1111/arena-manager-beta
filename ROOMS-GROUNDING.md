# Dust II — complete perimeter rooms and exact ground contact

Some exports are standing facades rather than complete buildings. Adding thickness to a facade did not make a room behind it. Three isolated source facades now receive rear walls, end walls, a stepped roof and a floor. Their profiles follow the source silhouette; their new depth is 3.0–3.6 map units. Existing roof volumes and original playable floors are checked before a room is authored. The existing detailed front face remains in place.

Six source castle structures also receive full masonry bases. Their lowest supplied architectural vertices begin approximately 2.56–5.0 units above the map datum; a small skirt on one edge was insufficient. Each base follows its measured footprint and is clipped away from protected original navigation floors.

Ground contact now comes from the rendered terrain triangles, not interpolation of the analytic height field. An independent Three.js raycast check at 441 points found that the old analytic approximation could differ by 0.3384 map units. The triangle sampler agrees with those raycasts to numerical precision. Foundation bottoms extend below the conservative minimum of actual terrain triangles under their footprint, preventing gaps between sample points.

The decorative source-palm asset has its trunk root offset sideways from its model origin. All nine placements now use the lowest bark vertices as their anchor, rotate around that anchor and plant the root ring into the actual rendered surface. The same correction reaches the cached shadow casters and animated foliage. Main source geometry, rooftop fixtures and original navigation data are not moved.

Validation covers complete room footprints, floor contact, independent rendered-surface raycasts, PC full-source HD, mobile landscape/portrait, palm root gaps, and continued cached-world animation. This is browser testing; physical Android performance has not been measured.

Only the standalone review page changes. The 1.32 game, APK and career saves remain unchanged. Full-source Dust II retains its original 4,541,597 visible triangles. Supplied art remains its respective owners' property; the complete Source 2 renderer is not reproduced.
