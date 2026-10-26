# Dust II — perimeter shells and unsupported wall bases

The previous roof-edge repair missed some of the supplied castle towers: their export has open shell surfaces and incomplete roof boundaries. Walls that already existed could also stop above the new exterior terrain. Returning only a rear roof edge did not ground those other faces.

This revision derives six tower envelopes from their actual source roof cornices and architectural vertices. It adds 35 missing shell patches (819 triangles), following the source's rotated, chamfered and tapered outlines. Source surfaces are checked before a patch is added; the supplied map mesh is retained. These are repair surfaces, not replacement procedural buildings.

An audit of the lowest exposed structural edges adds 85 wall footings to the exterior terrain. Upper floors, roof antennas and other mounted props are not moved down. Every footing continues the original wall's UV coordinate frame, preserving the source texture phase across the join. The 329 previous returns plus the 85 new footings make 414 rectangular wall panels; tower patches are separate meshes batched by material.

All added footprints are checked outside the original playable-floor guard. Runtime checks cover the full-source HD scene, close north/west views, mobile landscape/portrait, the original triangle count, source normal maps, and the small animated exterior rendering over a stable cached world. This does not establish physical Android performance or claim every intentional opening in the supplied scene is a defect.

Only the standalone map-review page changes. The current game, APK, collision/navigation data and saves are preserved. Full-detail source Dust II retains 4,541,597 visible original triangles. Source 2 lighting remains adapted to the web renderer; supplied art remains its respective owners' property.

Reproduction from the supplied source: run `scripts/locate-perimeter-towers.py`, `scripts/repair-perimeter-shells.py`, and `scripts/continue-footing-uv.py`, then build. The structural audit can be stored as verified gzip to avoid retaining a second large JSON copy. Original source files remain unchanged.
