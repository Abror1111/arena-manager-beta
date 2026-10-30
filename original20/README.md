# ARENA motion21 — expanded Sahil, gulls, roofs and C4 fix

The full old club-manager UI and battle HUD are preserved. Compiled CSS is byte-identical to the main game: 2953bdfcbc0385d887037eb3871bd4685e45e95faf775e844f0065d8e547111a. This is an isolated ONE-map original-media beta at /original20/?v=motion21. Main root game, existing 11 source maps, root saved career and previous APK are untouched.

## Changed behavior

Sahil expands from 60×40 to 84×56 metres: 1.4× each axis, 1.96× area. Same authored footprints drive geometry and navigation; a covered connector, additional houses, street lanes, barriers and stepped A site shape the routes. All ten spawns can reach both sites. 21 building masses including the tower, not eleven remade maps or a 1:1 CS2 map.

Roofs have real perimeter parapet/coping, access hatches, tanks, ventilation, satellite dishes or gable tiles, ridge caps and gutters. Removed the extra solid cap that covered the parapets and the old overlapping pyramid roof. Focused camera cutaway still reveals the selected player. Nine original white gulls now have bodies, necks, heads, eyes, yellow bills, forked tails and independently hinged wings with flap/glide phases.

Movement adds acceleration/braking, target-aware body rotation, pelvis weight transfer, gaze anticipation, terrain-aware foot IK, equipment draw/recovery and authored cubic hand-pose tracks for throwing and planting. Still a detailed rigid 20-joint analytic rig, not mocap, not a CS2 animation import, and not a claim of AAA parity.

C4 plant completion clears the carrier and plant animation timer in both AI paths. The renderer shows held equipment only during actual live planting by the current carrier. A stale plant timer cannot display another bomb after planting, death or save restore. Only the placed bomb remains.

Existing original20 beta career namespace is retained. A saved active round from the smaller map restarts at the same round number, with score and funds retained, so players cannot resume inside a new building. Original21 snapshots resume normally including planted C4. Root legacy career and caches remain isolated.

## Build and assets

Node: npm install, npm test, npm run build. Optional ARENA_MANAGER_OUT sets output folder; ARENA_MODULE_RECEIPT sets module receipt. Serve the build at /original20/. Original ARENA ../ui15/anime-player-portraits.png and the 30 author-created ../audio/<hash>.(wav|mp3) cues remain shared parent dependencies (src/studio-audio.json). No source-game exported geometry, texture, animation, navigation, VFX, sound or icon files are loaded. This is provenance information, not legal clearance.

The scoped service worker preserves root caches. A versioned preview and new shell cache avoid loading the old district artwork. Archive contains all build-reachable sources, worker sources and tests; third-party license texts are in public/THIRD_PARTY_NOTICES.txt.

Verification includes path reachability, rig constraints/foot contact, six roof variants, gull anatomy/pose, actual tactical-AI C4 completion and render visibility, earlier beta snapshot migration, mobile landscape emulation and offline resume. Physical-device performance has not been measured. See validation.json and verification/.
