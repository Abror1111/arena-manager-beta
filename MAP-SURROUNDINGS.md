# Ten map surroundings — review 9

The standalone map review now gives the other ten map entries their own authored exterior collar, continuous ground and architectural finish. The supplied source GLB, source UV and navigation files remain unchanged. Building material bindings are retained; the missing Anubis water shader is restored separately. Dust II craft8 is retained byte for byte in its environment, terrain, facade, water and cache modules.

| Map | Identity | Measured roof-rim closures | Solid rear returns |
| --- | --- | ---: | ---: |
| ancient-night | Same supplied Ancient layout; moonlit palette, lanterns and fireflies | 64 | 0 |
| ancient | Mossy temple masonry, buttress roots, broadleaf jungle, mist | 64 | 0 |
| anubis | Sandstone sanctuary; columns, relief bands, palm/river edge | 5 | 6 |
| cache | Weathered industrial warehouse; louvers, worn metal, birch trees | 120 | 0 |
| inferno | Italian village; shutters, tile ridges, chimneys, cypress | 59 | 7 |
| mirage | North African medina; lattice windows, carved bands, palms, sand drift | 120 | 4 |
| nuke | Power-plant service architecture; flanged tanks, pipework, conifers, steam | 120 | 8 |
| overpass | Urban park; masonry service buildings, bridge piers/railings, river edge | 120 | 2 |
| train | Rail depot; tiled ridges and service gantries, sleepers, steel rails, steam | 120 | 3 |
| vertigo | Existing elevated construction floor; deep city blocks and a trussed crane | 0 | 0 |

Freestanding scenery occupies a collar beyond the measured source-export bounds. The vegetation geometry is checked vertex by vertex against those bounds; trunks are excluded from all reserved building, bridge, rail and tank anchors. Water-edge trees are accepted only on dry ground. Inspection cameras look inward from the selected exterior, so source roofs do not hide the new facade.

Every added building has a closed rear, side returns, a roof and a foundation. Source-derived room returns use measured vertical source planes; roof closures use measured horizontal source rims. Existing roofs and all playable floor levels are protected. New source-rim closure solids and decoration are generated only outside the union of all supplied navigation floors plus a 1.15-unit collar. Independent Shapely validation checks the measurements again against the actual reference nav polygons. Vertigo's supplied elevated base is retained; its street background is far below the match floor rather than filled with ground at player height.

New details include projecting cornices, stone corner courses, individually built shutters and latticework, balcony rails, curved arch blocks, carved friezes, industrial louver blades, pipework, tank collars and ladders, tiled roof ridges, steel rails and sleepers, and branching trees with individually modeled leaves. Color, normal and roughness surfaces are generated locally from each map palette. An active map owns 768 KiB of base atlas pixels (before mipmaps); no new remote texture or model download is added.

The sun shadow camera now spans the measured source and scenery bounds, including the outer buildings and trees. Its direction and intensity are preserved. Independent projection checks place all 80 city-bound corners inside the actual Three.js shadow frustums. Dust II keeps its accepted lighting.

The full source scene is cached at the actual drawing-buffer resolution with HDR color and depth. Small dynamic layers animate vegetation, drifting particles, birds, clouds and, on Anubis/Overpass, transparent reflective water. A camera change refreshes source geometry and water reflections; idle ambient animation does not continually redraw the city. Source and new geometry retain real depth occlusion. Devices without the required HDR multisample support retain the direct antialiased renderer.

Camera framing now accounts for measured source exterior bounds, authored scenery and building height. The new **Fasadlar va muhit** camera inspects the added architecture. The four general views, site/spawn buttons, routes and lower-floor controls remain available. Phone layout, two-finger zoom, map switching/disposal and portrait layout are checked in Chromium touch simulation; this is not a physical-device performance certification.

Anubis's source material 15 contains 519 input triangles and was displayed as an untextured white surface. Its three measured horizontal water levels (approximately 0.3246, 1.0808 and 1.4254 world units) now have animated ripples, transmission, caustic detail and per-level planar reflections. Non-surface volume sides are suppressed. Original GLB data and its vertex/index/UV buffers are preserved; the replacement presentation meshes and temporary material bindings are owned by the environment and released/restored on disposal. The outer Nile continues beyond the rectangular export cut, with no doubled transparent join. Newly authored temples and palms occupy the dry eastern collar instead of the original water footprint.

Ancient Night deliberately shares the supplied Ancient source geometry. It is a separately lit atmosphere variant, not a newly acquired tenth unique CS2 export.

Scope: this is the map-inspection page. The production bot, current playable game entry, game service worker, APK and career saves are outside this change. Source assets remain attributed to Valve and their respective owners.
