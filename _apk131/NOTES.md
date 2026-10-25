# ARENA 1.31 — complete base-map reconstruction

Eleven complete, editable Blender scenes are generated independently: Dust II, Mirage, Inferno, Nuke, Train, Ancient, Ancient Night, Anubis, Overpass, Vertigo and Cache. The old 1.30 source project and public assets are retained.

This is a procedural architectural reconstruction using the CS2 navigation layout and elevations as a guide. It is not an exact reconstruction of Valve's buildings, and it is not a hand-modeled copy of every original object. No source GLB, VPK model, source collision mesh, radar image or source texture is imported into these new map scenes. Original agent, icon and audio assets in the game remain third-party assets; rebuilding maps does not change their ownership or determine licensing for a public/commercial game.

The new scene includes closed floor prisms, ramps, an irregular foundation, sealed building backs and roofs, modeled windows/cornices, complete authored civil/industrial/temple buildings, a map-specific landmark, branched vegetation, physical prop assemblies and authored basins on selected maps. PBR colors, normal maps and roughness maps come from mathematical height fields. Every core solid is checked for manifold edges before export. Collision is exported from the exact new scene solids, rather than a legacy source collision mesh. Reference navigation is preserved for recognizable A/B routes; precise visibility and grenade impacts use the new collision.

Runtime meshes are batched and Meshopt-compressed; editable Blender files keep their separate objects and packed texture data. Auto-action and individual-player cameras remain separate. Team silhouettes preserve animated players' visibility behind scenery.

The new web career key is separate from 1.30. Existing validated careers can be copied into it; an active round using an old map is restarted once, preserving the club, scores and economy. Existing save storage is retained for the classic edition. The Android upgrade uses the same application ID and signer.

Rebuild tools: `scripts/plan-rebuilt-maps131.py`, `scripts/make-rebuilt-textures131.py`, `scripts/build-rebuilt-maps131.py`, `scripts/finish-rebuilt131.mjs`. Architectural function definitions come from ARENA's own detail128/landmarks130/scenery129 generators; no source models are loaded by those calls. The complete scene files, rather than just a decoration kit, are supplied separately.

Install over the existing ARENA app to keep your club. Do not uninstall first.
