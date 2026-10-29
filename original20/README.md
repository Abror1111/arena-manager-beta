# ARENA manager original20 — old interface, original media test

Full existing club manager and old match HUD, with identical compiled CSS SHA256 2953bdfcbc0385d887037eb3871bd4685e45e95faf775e844f0065d8e547111a. Manager menus, anime portraits, careers, tactical Match engine, round rules and economy remain. UI asset references and audio/map labels differ to fit original content.

This isolated beta includes ONE author-designed Sahil map (15 architecture masses, asymmetric paths, raised A terrace with steps). It is not the rebuilt 11-map release and does not claim to reproduce CS2. The existing root game and 11 source maps are untouched. Separate arena-career-original20 save and audio upload DB prevent loading or overwriting the legacy career or CS2 audio pack.

Operators are original detailed rigid articulated models, 20 transform joints and analytic limb IK. World-anchored stance feet, longer step cadence, smooth yaw, acceleration weight shift, low-ready walk/run, aim, reload, objective, grenade follow-through, pistol, sniper and knife handling. Not skeletal mocap or CS2-equivalent animation.

No CS2 exported model/texture/audio/VFX/icon media is loaded. Geometry, textures, effects and nav are authored programmatically. Shared ../ui15/anime-player-portraits.png and ../audio/<sha256>.(wav|mp3) are existing original ARENA files and remain required. The 30-clip bank includes 26 effects/ambience and four music cues. Browser caching validates shared audio by size/hash. This is an asset-provenance statement, not legal clearance.

## Build

Install Node dependencies with npm install. npm test runs operator constraints and planted-foot slip tests. npm run build outputs dist; set ARENA_MANAGER_OUT to override. Serve this directory under /original20/ with original ARENA portrait and audio files in the parent paths above; their source metadata is in src/studio-audio.json. Source media/nav loaders are disabled for this map.

Service worker caches only this beta shell and shared portrait, preserves root caches, and audio uses a validated shared cache. Reload offline then use the existing Resume match action.

## Verification

Browser engine tests cover full old UI → 3D match, player/auto camera, independent saved career, audio readiness, cache isolation and offline match resume. Layout tested in 23 viewports across 10 manager screens. No physical-device performance certification. See validation.json. Third-party license texts: public/THIRD_PARTY_NOTICES.txt.
