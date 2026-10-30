# ARENA coastal24 — Sahil tactical coastal map

An isolated one-map beta at /original20/?v=coastal24. The old club manager, battle HUD and compiled CSS are retained. The root 11-map release, root career, production bot and previous APK are unchanged.

## Layout

The former 120×88 grid town is replaced by a 120×120 hand-authored plan guided by the Dust II radar's arrangement: B northwest, A northeast, CT north-centre, T south. A Long follows the east side; Short turns through the raised eastern catwalk; Mid connects the centre; the upper B tunnel and its lower branch sit west. Six explicit tactical waypoint chains use the same metre coordinates as the rendered footprints. This reconstruction approximates the reference's layout; it does not reproduce every source-game detail or its complete layered navigation.

Fifteen irregular main building groups replace the grid. Their concave outlines generate triangulated convex collision pieces, closed exterior walls, return facades, closed polygon roofs, parapets, cornices and rooftop service structures. Fourteen exterior context buildings remain. A/B enclosure walls, wooden double doors at Mid and Long and three covered tunnel floor regions distinguish the areas. Observer cutaways and full/Routes roof inspection remain. Standing floor heights are about A +2.45 m, B +0.65 m, T +1.35 m, with graded approaches and tunnels. No lane enters the sea.

The west quay, palms, rock coast and sea remain outside the playable outline. The water mesh now has actual animated vertex waves, Fresnel sky tint, sun highlights, moving foam and more transparency near the shore. Original white articulated gulls and moving clouds remain. Ground/road batches do not cast self shadows; buildings still cast shadows onto them. Procedural plaster, stone and roof normal maps follow the existing quality controls.

The damped player and auto cameras, analytic operator animation, original VFX/audio and single-held/placed C4 logic are retained. No source-game mesh, texture, sound, animation, nav file or radar image is bundled or requested. Reference imagery was viewed as a layout guide; geometry and materials in this beta are authored in code. This is provenance documentation, not legal clearance.

## Saves and build

The beta continues to use arena-career-original20; root arena-career-rebuilt131 is separate. Because the plan changes, active old20–23 rounds restart at the same round, score and funds. Current24 snapshots, including planted C4, resume in place.

Node: npm install; npm test; npm run build. ARENA_MANAGER_OUT and ARENA_MODULE_RECEIPT optionally select output paths. Serve under /original20/. The shared parent media are the existing original anime portrait atlas at ../ui15/anime-player-portraits.png and 30 authored audio cues at ../audio/<sha256>.(wav|mp3), listed in src/studio-audio.json. The source archive includes all reachable modules, build configuration, public shell and tests; those shared parent media are not duplicated in the archive.

Tests cover all 20 spawn-to-site paths, all six routed chains, blocked islands and map boundaries, actual AI movement, complete attacking A/B rounds, grenade rest heights, C4 placement/resume and old20–23 migration. Optional tests/render-floor24.mjs uses a running dev server (ARENA_TEST_ORIGIN, default http://127.0.0.1:8213), Chromium (ARENA_CHROMIUM) and ARENA_FLOOR_REPORT to compare constructed geometry with navigation heights. Browser checks cover the old UI, map/Routes views, natural movement, player/auto camera, mobile landscape emulation and offline planted-C4 resume. Mobile browser emulation does not establish physical-device performance.
