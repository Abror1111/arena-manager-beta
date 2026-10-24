# 1.30 observer map reconstruction

Every selectable map receives actual new 3D geometry. Base supplied CS2 GLBs,
source navigation and gameplay collision stay byte-identical. The render adds
closed, source-textured low walls and distinct Blender architecture. This is a
visual adaptation for a tactical observer, not an entire handmade CS2 replica.

## Closed walls across the playable map

`scripts/bake-observer-walls130.py` takes horizontal cross-sections through real
vertical collision triangles near the navigation network. Fragments are merged
before extruding irregular wall footprints. Walkable polygons and source prop
bounds are excluded, preserving doorways and movable/destructible original props.
Each solid has sides, a bottom, real beveled coping and an upward cap. Nested
holes remain holes. Every footprint has zero intersection area with navigation;
source nav/collision hashes and solid counts are recorded in `observer130`.
The bounded binary sets contain two material groups, source-matched at runtime.
The original source triangles/UVs and gameplay collision are not rewritten.

Route cutaways lower nearby rendered walls to reveal the roughly 0.9-unit agent
bodies. Exterior buildings and roofs outside routes remain. A fixed lower-floor
plane is applied for multi-level maps, with additional closed section caps. The
same route/floor cutaway applies to shadow depth materials so hidden ceilings do
not leave the revealed rooms in shadow. Shadow depth shaders have a different
vertex layout from the color shader; both use the shared project-vertex anchor.

## Eleven distinct architecture edits

`scripts/build-landmarks130.py` creates eleven distinct Blender meshes using the
maintained geometry helpers in `build-detail-kit128.py`:

| Map | Added architecture |
| --- | --- |
| Dust II | Octagonal masonry arcade with curved dome and carved supports |
| Mirage | Riad arcade, cedar pergola and polygonal fountain |
| Inferno | Terracotta campanile, real roof channels and arched bell openings |
| Nuke | Domed pressure vessel, flanged pipes and maintenance ladder |
| Train | Braced signal gantry, lights, ladder and rail profiles |
| Ancient | Stepped carved altar, fluted columns and overgrowth |
| Ancient Night | Stone observatory pavilion and sculpted stele |
| Anubis | Lotus columns, curved pylon and fountain basin |
| Overpass | Twin brick/stone arches, balustrade and bent utility pipe |
| Vertigo | Lattice crane hub, winch, ladder, counterweight and hook |
| Cache | Sawtooth workshop roof, clerestory glazing and ribbed shutter |

These replace generic pocket modules at the exact existing validated positions.
All eleven edited modules fit the existing 3.6 x 3.2 pocket envelope. They are
ARENA-authored geometry matched to source textures; they are not newly extracted
CS2 landmarks. The prior detailed buildings, vegetation and source PBR remain.
The editable Blender source contains these eleven modules, not the complete
source scenes. Ancient Night still shares the supplied Ancient visual.

## Actor visibility at different angles

The occluded overlay renders each actor's actual animated geometry and bones in
its team color only where world depth hides it. Visible actor pixels write a
stencil veto after opaque map geometry, preventing rear faces from painting over
the normal visible skin. Ghosts share geometry/skeleton buffers and restore
shared material state when disposed. There is no second full scene depth render.
Screen-space portrait pins and a lower-floor indicator make crowded positions
readable; auto action and selected-player cameras remain separate. Overview
framing includes additional portrait margin and markers avoid the playback bar.
Gameplay tactics, line of sight, hit detection and source wall heights stay intact.

## Rebuild and verify

1. Run the wall baker using the installed Python/shapely/numpy/scipy environment.
2. Run Blender 4.3 with `--background --python scripts/build-landmarks130.py`.
3. Run `node scripts/compress-landmarks130.mjs` in the pinned glTF tool workspace.
4. Run Node tests, including actual decoded UV/bounds, source-hash, nav-exclusion,
   cap/bevel, skin-sharing, shared-material lifetime and depth-shader checks.
5. The WebGL pixel check covers four camera azimuths with/without an occluder,
   verifying normal visible colors and genuinely revealed occluded body pixels.
6. Inspect all eleven static/auto/player views, lower floors, source recordings,
   project-prefix links, first-time offline map opening and the signed APK assets.

The model/texture additions are cached once and included in the APK. Physical
Android frame rate and thermal/memory behavior still need device measurements.
