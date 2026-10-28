# Source-map structural repairs — review 10

This update repairs the source cities in the standalone map-inspection page. It replaces the previous roof-rim strips and detached generic scenery with measured, closed source-wall volumes, actual floor-edge foundations, and ground heights fitted to the supplied source and navigation floors. The playable game, APK, service worker, production bot and career saves are outside this change.

| Map | Closed source volumes | Floor-edge supports | Exterior identity |
| --- | ---: | ---: | --- |
| Mirage | 136 | 855 | Source medina masonry, lattice details, native palms, sand collar and wind |
| Vertigo | 1 tower base | — | A closed tower below the lowest match floor, glazed facades, skyline and moving clouds |
| Nuke | 76 | 2,159 | Concrete and industrial siding, source asphalt, native beech, pipework and steam |
| Anubis | 136 | 1,725 | Sandstone, palm bank, source sand and reflective water |
| Ancient | 112 | 1,178 | Source stone and mud, native jungle foliage, carved bands and mist |
| Inferno | 153 | 1,217 | Source plaster, tile roofs, shutters, native trees and drifting pollen |
| Overpass | 94 | 1,597 | Park/service masonry, native broadleaf trees, earth and water edge |
| Cache | 63 | 871 | Source brick, corrugated roofs, asphalt and native poplar vegetation |
| Train | 116 | 1,911 | Source depot masonry, metal roofing, native trees, rails and steam |
| Ancient Night | 112 | 1,178 | The same supplied Ancient layout with moonlight, lanterns and fireflies |

Each reconstructed room has physical side and rear faces, a bottom and a roof. Its footprint follows measured source wall planes and is clipped away from all supplied navigation floors. Concave roof boundaries use constrained triangulation rather than a bounding rectangle. Source tree roots and measured water surfaces are kept clear; courtyard holes have physical inner walls as well as correctly cut roof faces. The new walls retain measured source texture coordinates and use the active map's own materials; projecting trim, windows, shutters, carved bands or service details are added only where there is adequate clearance.

A 121 × 121 source-fitted ground grid replaces the previous single global floor height. The rendered terrain remains below every navigation level. Floor-edge supports extend down to the actual rendered terrain triangles; where their horizontal footprint crosses a route, the top stays at or below that route's floor. Vertigo retains its height above the street instead of raising terrain into the playable building. Anubis also has a separate, below-water bed for the western Nile extension, so unrelated land relief cannot appear as isolated humps through the river. The source model files, indices, UVs and navigation files are not rewritten.

Added vegetation reuses bounded triangle subsets and alpha/PBR textures from the active source map, not the earlier generic triangular leaves. Source 2 foliage wind weights are excluded from the runtime color multiplier so affected vegetation no longer becomes a black silhouette. Root positions are measured against the rendered ground, with a small buried overlap. Wind animation is applied to the foliage layer. The supplied source contains vegetation cards on some maps; these remain source cards rather than newly acquired high-detail tree assets.

Structural plans are content-addressed gzip assets (approximately 543 KiB across all ten entries). The existing verified asset store checks each download and caches it for reuse. Only the selected map's plan and runtime geometry are decoded. Geometry, materials, owned texture wrappers and vegetation instances are disposed on map switching. The source city is cached at drawing-buffer resolution; idle birds, clouds, particles, foliage and water animate over its depth buffer without repeatedly rendering the entire city.

Use **Fasadlar va muhit** to inspect a reconstructed source room. **Old tomondan**, **Yon tomondan** and **Orqa tomondan** show the city-ground joins. The route cutaway and lower-floor controls remain available. Source 2 lighting is adapted to this web renderer; identical Source 2 output is not claimed.

Validation covers original source hashes, navigation clearance, concave roof coverage, physical ray intersections with room sides/roofs, ground raycasts and all supplied navigation vertices. Desktop and Chromium phone-touch simulation cover all ten entries, camera presets, route/lower-floor controls, map switching, portrait layout, pinch zoom and idle cache behavior. This is not a physical Android performance certification. Accepted Dust II environment/material/terrain/water/cache modules and its nine camera poses are preserved and regression-checked separately.

Ancient Night deliberately shares the supplied Ancient source geometry. Source exports remain attributed to Valve and their respective owners; the new closure/foundation geometry is authored from the supplied measurements. These structural repairs do not certify that every decorative opening in the source exports has been rebuilt.
