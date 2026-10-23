# Editing original ARENA maps

`src/original-maps.js` defines independent rectangular districts on a 2-unit
navigation grid. Coordinates are project-authored; do not derive edits from
exported source-game maps. Blocks are solid cover and excluded from walking.
Sites and spawns must remain on open cells. Elevation is a continuous 8-unit
ramp, sampled identically for terrain, nav polygons and agent movement.

`src/original-world.js` builds the geometry and registers wall/floor triangles
for grenade ricochets and line-of-sight. It uses procedural canvas textures and
`src/backdrop-prefabs.js` original architecture. Decorative structures occupy
blocked roofs or the exterior; traversable cells remain clear.

After editing, run `node scripts/bake-original-maps126.mjs`, `npm test`, and
`npm run build`. `scripts/check-original126.mjs` renders all eleven phone views;
`check-cameras126.mjs` checks static/auto/player modes. The selective Vite public
copy excludes preserved `visuals/`, `cs2/`, `terrain/` and old previews from the
active bundle without deleting those source files.

Map names are user-facing. Stable legacy keys only preserve old club records.
Any future layout change must increment the map revision and provide a safe
saved-round migration. Agents/audio/VFX have separate third-party provenance.
