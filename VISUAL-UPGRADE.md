# ARENA Manager1.28 — CS2 architectural detail pass

This version keeps the supplied CS2 map layouts, navigation, collision and base
geometry. It rebuilds the previous simple surrounding architecture as a compact
Blender-modeled detail library, and restores selected genuine PBR material data
that the mobile conversion previously removed. This is a visual reconstruction
pass over the existing source scenes, not a claim of eleven newly hand-modeled,
finished1:1 replicas of every CS2 object.

## Geometry

All11 selectable maps use the new library. Its44 modules cover buildings,
courtyards, planters and roof equipment, with separate designs for sandstone
quarters, terracotta streets, industry, rail, jungle masonry and a city skyline.
Details include curved overlapping roof channels, voussoir arches, bevelled
stone courses, window frames, balcony rails, bent pipes, ventilator slats, wagon
bogies/wheels and multi-storey glazed facades. Blender source is editable.

The library is meshopt-compressed with real tiled UVs retained. Runtime batches
repeated geometry into instanced meshes and binds it to materials from the
loaded CS2 map, including baked source vertex tints. Existing validated
footprints keep added architecture off navigation; the playable geometry and
AI paths are unchanged. Because these modules stay outside all walkable footprints, their exterior silhouettes remain intact in lower-floor cameras. Interior modules belonging to a hidden upper floor are hidden as whole instances, rather than sliced. Matching source materials are also used on Vertigo's
support body, and its skyline retains tall background buildings.

## Materials and surroundings

A source-derived pack restores selected original color, normal and roughness
recordings from the preserved supplied exports. Color copies are at most1024px;
normal and roughness copies are bounded to256px for mobile. Roughness uses the
original packed green channel. Runtime source material UVs and alpha coverage
are preserved; transparent/masked surfaces retain their original treatment.
These are sourced PBR recordings, not synthetic normals inferred from color.
Source image hashes, original sizes and runtime adaptations are recorded in
`detail128/pbr/PROVENANCE.json`.

Outside the source geometry, a source-coverage distance blend transitions paving
into a setting-appropriate terrain tone. Geometry heights remain unchanged.
The maximum additional decoded PBR texture allocation is bounded and checked;
physical-device memory use and FPS have not been measured.

## Ancient Night

Ancient Night now uses the supplied textured Ancient scene, with the same
coordinate transform, its own original navigation, a dedicated route mask and
night lighting. Its water, material corrections and map props are enabled.
This is an explicit shared-geometry night variant, not a separately supplied
`de_ancient_night` visual export. No second Ancient GLB is downloaded or bundled.

## Downloads and saves

The cache preparation list includes each map's visual, collision, radar, terrain,
route mask, the common detail library and its PBR recordings. Shared files are
counted/downloaded once. APK assets are available offline; web assets can be
prepared in advance or saved as maps are used. Existing club and match saves
remain compatible, with the1.27 migration for1.26 original-layout saves retained.
Install over the previous app without uninstalling. VersionCode129, same signer.

Original exports, prior signed APKs, published asset URLs and the1.26 original
ARENA variant are preserved. The separate case bot is untouched. Existing CS2
assets retain their ownership; the new detail geometry does not establish rights
for source-game maps or textures.
