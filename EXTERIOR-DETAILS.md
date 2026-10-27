# Dust II: shoreward surf and detailed exterior architecture

This is the next standalone `quality.html` review after the coastal-life update.
The main source scene remains unchanged: all 4,541,597 visible HD source triangles,
UV/material bindings, routes, nine room parts, nine support parts and the repaired
tower bases are retained. The changes are confined to exterior dressing and water.

## Shore motion

The old crossing ripples are replaced by a shared analytic surface-height and
gradient function in the vertex and fragment shaders. The main crest travels
toward the actual curving coast, with a shorter crossing wave and a broad swell.
The geometry has finer sampling in the visible near-coast region. Analytic
gradients keep highlights/reflection distortion aligned with the surface motion.

The shore wash advances and recedes with surface height. Broken, advected foam
forms in a shallow-water band and trails behind the incoming crests. Low-amplitude
ribbon caustics replace the conspicuous dot pattern. Transparent shallows,
depth tint, sun highlights and the real cached planar coast reflection remain.
This is an authored coastal water effect, not a fluid simulation or gameplay
buoyancy model. The underlying authored seabed remains unchanged.

## Architecture and layered materials

There are now **25 dressed facade/side-return spans**, with **46,801 additional
static detail triangles** in eight material batches. Four prior compositions
are retained, eleven longer spans attach to the accepted source-derived roof
wall panels, eight short side returns attach to exact closed-room edges, and two audited source faces receive details aligned to their actual visible plane.
Normal orientation for room returns is derived from the room polygon, not a
guessed camera direction. These are details on existing volumes, not new generic
gameplay buildings.

Three architectural treatments give the edge a coherent variety:

- Residences: stone arch reveals and sills, louvered timber shutters, stepped
  cornices and corbels, balcony railings, scalloped fabric awnings and planted
  turned terracotta pots.
- Workshops: deep rectangular louver frames, corrugated sheet canopies, service
  panels and rounded bent drainpipes with wall clamps.
- Kasbah walls: tapered, stepped stone buttresses, recessed narrow ventilation
  openings and layered coping courses.

Only newly authored exterior materials receive the layered PBR finish. Existing
source maps still supply their original plaster/brick/concrete texture and UVs;
world-scaled grain, chipped plaster with masonry joints, softened weather stains,
faded lower paint bands, timber fibers, fabric variation and metal patina add
surface variation. The effect also perturbs normals and roughness, so light
responds to the finish rather than merely tinting it one solid color. Original
source materials are never passed to this modifier. No new model/image downloads
are needed. The procedural finish is a web rendering addition, not extracted
Source 2 baked lighting.

The full-resolution, antialiased static-world cache and camera-settled reflection
cache remain. Extra detail geometry is static and batched; only water, wind,
birds and clouds animate during idle. Physical Android performance still needs
a device check; browser tests exercise mobile layouts and rendering fallbacks.

## Verification and publication

`check-detail.mjs` checks mobile/HD views, exact source geometry counts, preserved
ground repairs, all 25 facade spans, layered material state and stable idle
capture counts. The HD run also inspects the closer `Fasadlar` camera.
`check-detail-water.mjs` compares actual rendered reflection versus sky-only
pixels at a fixed time, checks live wave pixels, camera-follow reflection and the
direct non-float fallback. `check-detail-cache.mjs` compares cached/direct source
city pixels at fixed animation time. Independent rendered-terrain raycasts and
all camera frusta remain part of validation.

The previous generated rooms-review bundle `quality-DBIxgZs5.js`, if retired to
fit the Pages limit, is first scanned for live references, archived and verified
byte-for-byte. It remains recoverable from Git history. Current/previous main
review bundles, raw source exports, maps, current game, APK and production bot are
retained. The published update is only this standalone Dust II review.

Two original blank source facade planes (nodes 2525/2528, material 49) are overlaid using copies of their exact 4/29 indexed triangles, original UVs and a 0.016-unit outward offset. This preserves any original openings; a guessed rectangular cover is not used. A roof-derived decorative span that was hidden behind the actual source facade has been replaced. Original source meshes/materials are retained.
