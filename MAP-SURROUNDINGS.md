# Connected surroundings — review 11

The other ten map entries now have a visible surrounding district, rather than a small source city centered on an oversized empty ground plane. The overview frames the playable area and its near surroundings. It no longer zooms out to include obsolete, distant scenery anchors. Navigation remains inside the frame in desktop, phone landscape and phone portrait checks. The observer camera stays tilted; this update does not introduce a vertical overhead camera.

| Map entry | Surrounding buildings | Additional trees | Environment |
| --- | ---: | ---: | --- |
| Mirage | 13 | 52 | Medina blocks, fabric awnings, palm clusters, outcrops and sand |
| Vertigo | 144 | — | A dense city skyline below the match floor, glazed facades and rooftop equipment |
| Nuke | 8 | 82 | Service campus, access roads, tanks, pipework, tree belt and roof-level steam |
| Anubis | 5 | 64 | Sandstone colonnades, palm groves, desert banks and the western Nile |
| Ancient | 6 | 125 | Dense native jungle canopy, stepped ruins, mossy outcrops and ground mist |
| Inferno | 17 | 72 | Tiled village roofs, shutters, projecting balconies, cypress/olive trees, paths and vineyard rows |
| Overpass | 10 | 110 | Urban park, service buildings, paths/benches and a bounded reflective canal |
| Cache | 14 | 78 | Brick industrial blocks, loading doors, roof vents and poplar-shaped tree belts |
| Train | 9 | 70 | Depot blocks, extra rails/sleepers, service roads and a broadleaf tree belt |
| Ancient Night | 6 | 125 | The same Ancient layout with moonlight, lanterns and fireflies |

The new structures have closed walls and roofs, physical foundations, and projecting architectural detail. They reuse active-map material recordings where suitable, including roof, masonry, bark and paving textures. Trees use measured source geometry where a usable canopy exists. The village, campus, park, warehouse and rail districts use authored volumetric branch/crown clusters where a supplied billboard or sparse canopy does not read well from above. Inferno also has low, supported vineyard rows on its open Tuscan side. Terrain color transitions into each district's sand, grass or forest floor, preserving the source material near the playable streets.

The district layout is generated against the supplied navigation polygons and measured source roofs/wall faces, not arbitrary remote anchors. New building volumes, canopy/root clearances and rocks stay outside the protected navigation area. The background city on Vertigo is checked vertically: its highest rooftop equipment remains below the lowest navigation floor. Foundations sample the actual rendered terrain. Border roads and rails follow that terrain instead of floating above a flat reference height.

Anubis no longer has an extra ocean on its eastern side; the restored source canals and western Nile remain. Overpass has a finite-width canal with retaining walls and railings, rather than an ocean plane. Its ripples and planar reflections use owned presentation resources and are disposed when changing maps. The supplied source model files and their UV/index buffers remain unchanged.

An Inferno vegetation classification error was also corrected: the substring `fern` in the name `inferno` had incorrectly included some house/metalwork triangles in a tree prototype. The classifier now requires a botanical name boundary. The corrected tree subset is verified and packaged separately, and the district source occupancy is regenerated with the corrected classifier.

Use **Umumiy** for the closer match-area overview. **Atrof-muhit** inspects the new surrounding district. The original side/back views, source-room detail view, route cutaway and lower-floor selector remain available. Panning can reach the surrounding district without enlarging the initial camera frame.

Background trees and architectural detail are batched and cached with the source city. Small wind/particle/cloud/bird layers animate separately. Idle atmosphere does not repeatedly redraw the complete city. Mobile drawing-buffer resolution remains capped at 1.75 device pixels per CSS pixel; no source texture is downscaled by this change. The active map owns and releases the added GPU geometry, materials and texture wrappers.

Validation includes the ten generated districts against actual navigation, all 30 map/viewport overview projections, rendered-ground raycasts/all navigation vertices, complete source-room geometry regression, expanded shadow-frustum bounds, unchanged accepted Dust II modules/camera poses, and Chromium desktop plus phone-touch simulation for every map entry. Camera navigation, map switching, route/lower-floor controls, idle cache, portrait layout and pinch zoom are checked. Browser simulation is not a physical Android performance certification.

This is the standalone map-inspection page. The production bot, playable game entry, game service worker, APK and career saves remain unchanged. Ancient Night deliberately shares the supplied Ancient source. Original exports remain attributed to Valve and their respective owners. Existing source-export decorative openings are not claimed to be fully rebuilt by this surrounding-environment update.
