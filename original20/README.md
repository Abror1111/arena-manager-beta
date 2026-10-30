# ARENA architecture22 — Sahil tactical old town

An isolated ONE-map original-media beta at /original20/?v=architecture22. The existing club manager, full battle HUD and compiled CSS are retained. Main root game, original 11-map release, legacy saved career, production bot and prior APK are untouched.

Sahil is rebuilt as a 120×88 metre tactical town (10,560 m²), 2.245× the previous 84×56 area. This is new authored architecture and navigation rather than a uniform scale transform or a 1:1 CS2 recreation.

## Architecture and gameplay

38 playfield building masses and 13 exterior context buildings, with modular L-shaped additions, a twin-tower mid gate, fort at raised A, B tower with cupola, arcaded covered market, roofs, parapets, tanks, shutters, satellite dishes, vents and proper stepped foundations. Background blocks, quay, palms and sea connect the town to its surroundings.

Three actual interior floor regions: two connected sections of an L-shaped B tunnel and the covered market. Open doorways, columns, arches, floors and ceilings share the same authored layout as the collision/navigation data. Existing map-view Routes control hides merged roof meshes, so passages can be inspected. Player/auto camera cutaway and original white articulated gulls remain.

A is at +2.45 m and has long/north, short/west and CT/south approaches. B has a +0.65 m yard with three stair entrances; tunnel floor is -0.75 m with entry/exit slopes. Foot navigation rejects retaining cliffs. Six named routes: A LONG, A SHORT, B TUNNEL, B MID, CT A and CT B. Names refer to the tactical sections, not a promise that the entire SHORT path is the globally shortest path.

NPCs choose mapped lanes by role/site and follow waypoint queues; enemy reaction, grenades, cover, spacing, retake and C4 logic continue to take priority. Paths and nearby walls use authored metre coordinates. Grenades bounce off high/low floors and tunnel/market ceilings. C4 single-held/placed fix and analytic terrain-aware operators are preserved. No motion capture or source-game media imports.

The original20 beta save namespace is retained. Active rounds from original20/original21 restart on the new map at the same round, score and funds; new original22 snapshots resume normally. Root career and caches remain separate.

## Build

Node: npm install; npm test; npm run build. ARENA_MANAGER_OUT optionally selects the build directory; ARENA_MODULE_RECEIPT selects the module receipt. Serve under /original20/. Shared parent files remain the original ARENA anime portrait atlas at ../ui15/anime-player-portraits.png and 30 authored cues under ../audio/<sha256>.(wav|mp3), described in src/studio-audio.json. No exported CS2 geometry, texture, nav, VFX, animation, icon or sound is loaded by this beta. This is provenance documentation, not legal clearance.

Scoped shell cache v4 and versioned loading image preserve older root caches. Browser verification covers old UI, rendered full/route views, 3D match, C4 placement, player/auto camera, mobile landscape emulation and offline resume. Node tests check both sites from all ten spawns, all six route chains, height/cliff rules, indoor traversal, grenade floor/ceiling impacts, two 40-second AI scenarios, C4 and old-save migration. Physical-device performance has not been measured.
