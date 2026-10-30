# ARENA measured27 — Dust II source-aligned Sahil beta

The beta keeps the old club manager, match HUD, anime portraits, analytic ARENA operators, equipment, audio and VFX. The root eleven-map release, root career, production bot and previous APK are unchanged. This update replaces the approximate authored core map with the user-supplied Dust II visual, measured collision and navigation.

## Measurements and geometry

The previous town used hand-drawn percentage footprints, invented height regions and separately placed arches. Those core buildings, floors, bridge rectangles, route chains and choke walls are no longer used by the measured27 map. The native optimized source visual derived from ../visuals/dust2/mobile.glb supplies the actual architecture, doors, stairs, ramps, props and textures. Its native metre scale is preserved. It receives only the Source2Viewer axis rotation and documented origin translation; it is not stretched to fit the former 120 m square. The mobile geometry LOD is 1,010,490 triangles, with source texture image resolution preserved. It is verified by hash and served from an immutable GitHub source-asset commit; the previous visual remains unchanged. The source radar coordinate square is 114.44224 m wide. The shared conversion is exactly 0.0254 metres per Source unit; nav/collision coordinates previously expressed at 80 Source units per game unit are multiplied by 2.032, with a common vertical datum shift.

Physics uses all 229,653 triangles from ../cs2/dust2.cmesh, uniformly transformed into the same space as the visual. Navigation uses 2,242 source polygons and their directed links. The source metadata's approximate CT marker sits on a raised surface, so CT starts are selected from the actual adjacent street polygons; the selected central street polygon is source area 1258. The code preserves that street's real elevation instead of levelling the whole north side or putting a fabricated tunnel beneath it. Spawn locations are chosen from source walkable surfaces, not claimed to be exact info_player entity coordinates.

Visible terrain heights and operator foot placement are refined with downward rays against the actual collision surface, because nav polygons can sit several centimetres above the physical ground. Large vertical nav links are excluded from ordinary walking, so actors use stairs and ramps instead of abrupt falls. Path smoothing processes the complete route before limiting queued points. The former A/Long archways and flanking wall patches are removed; the source model provides their true openings. A live movement test passes through five native Long-corridor polygons to A without crossing a collision wall.

The previous coastal water, gulls, clouds and exterior context houses remain outside the core. The old player/auto camera separation and minimum fields remain: 22 m player and 28 m automatic vertical field in landscape, wider on narrow screens. Targeted material reveal remains for actors under roofs. The native source material fixes suppress compiler-only surfaces and foliage animation colours. This beta now uses source-game map assets; it is not an entirely original ARENA map and does not claim legal clearance.

## Storage and verification

Both native map assets are verified by SHA-256 and retained in an independent arena-measured27-assets cache. Reopening a cached map does not require redownloading it. The beta shell has its own updated service worker. Root career/cache namespaces are preserved. Old20–26 active rounds restart on the new plan preserving round, score and funds; measured27 saves resume normally.

Use npm install, npm test, npm run build. The source archive includes reachable modules, public shell, native collision test fixture and tests. Production dependencies: ../cs2/dust2.cmesh, the immutable mobile visual URL recorded in src/measured27-plan.json, the original anime atlas and authored audio cues. For the optional Vite dev test, expose the parent cs2 folder through a public-directory symlink; the build intentionally emits public files only. ARENA_MANAGER_OUT and ARENA_MODULE_RECEIPT select optional output locations.

Verification covers uniform source-coordinate conversion, twenty spawn-to-site paths, actual T/CT walks to A/B, the Long door corridor and wall-crossing checks, two completed AI rounds, nav/physical floors, actual source visual/physical floor raycasts, previous-save migration, separate cameras, mobile landscape fit, native asset caching, C4 single held/placed state and offline resume. Browser emulation is not a physical-device performance certification. No new APK is built in this update.

Source download: https://github.com/Abror1111/arena-manager-beta/raw/5de2c0f90743059cf9176aed0faf4bf2df4f1fae/source-archives/ARENA-manager-measured27-source.zip

CT street view proof: https://github.com/Abror1111/arena-manager-beta/raw/5de2c0f90743059cf9176aed0faf4bf2df4f1fae/source-assets/ct-street27.jpg
