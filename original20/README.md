# ARENA design29 — authored Sahil geometry and C4 blast

One-map engineering update. Old manager and battle UI/CSS preserved. Offline reference analysis used the original Dust II collision surface for scalar elevation ranges and circulation issues: 77,976 grid probes at 1m, 5,022 walkable-layer samples and 3,940 route probes at 0.1m. This is sampled analysis, not an every-centimetre survey. No source mesh, nav, texture, agent or audio files are included or requested by this beta.

Geometry remains our own ARENA mesh generation, proportions, materials and route decisions. A 6.1m, B 3.8m, T 6.6m and CT 0.4m; three stair flights with 58 treads, rises <=17cm and runs >=28cm. The lower tunnel returns to Mid through a separate supported gallery. Long has an offset chamfered vestibule and two true arched double-door openings. Rendered floors/arches, projectile solids, route grid and foot contact use shared definitions. Closed terrain skirts and grounded building bases join the coast. New roof observatories and stair handrails add silhouette detail.

Game C4: 48m damage radius, 62m visible ground-conforming pressure/dust wave, body exposure rays and lower damage through cover. Damage is immediate, not a physical fluid-pressure simulation. Wider automatic blast framing; selected-player camera remains independent. Five-second explosion outro. Twelve actual map crates react with mass-weighted impulses, wall/ceiling collision, settling, burnt planks and removal from tactical cover. Not arbitrary destruction of buildings.

Old active snapshots migrate by restarting the current round, retaining round, score, funds and statistics. Current29 snapshots resume, including crate states. Root career and root caches remain separate. The root 11-map game, production bot and old APK are unchanged.

This is not a source-map clone, a completed 11-map remake or a legal clearance. A reference-inspired route plan can still require independent design and rights review. Old archives and other demos are not purged.

Build: npm install, npm test, npm run build. ARENA_MANAGER_OUT and ARENA_MODULE_RECEIPT choose output paths. Serve under /original20/. The original anime atlas is shared at ../ui15/anime-player-portraits.png; authored audio samples are bundled. The archive contains reachable runtime modules, tests and provenance. Private source-analysis grid/meshes are excluded.

Verified source archive: https://github.com/Abror1111/arena-manager-beta/raw/68bbe1a602f72cf3b7cdcfda4bce2a7ca6e95b7f/ARENA-manager-design29-source.zip
SHA256: 129cbe3192ce7d153aa725a3170d4a62b352284b026d83fc658e0df0aa2a608a
