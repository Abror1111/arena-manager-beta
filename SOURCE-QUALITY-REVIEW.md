# Original export visual review

The 1.31/1.32 releases replaced the supplied map buildings with procedural interpretations of navigation. Additional generic details and material families in 1.32 did not recover the source-map identity. A navigation match is not visual fidelity.

The separate review page returns to the supplied CS2 art for eleven map entries. Its mobile options use existing reduced source-derived geometry and bounded texture copies, with three selected PBR restorations per map. They recover the original layout and architectural identity, but are not a byte-exact or full-resolution copy of the original scene. No rebuilt131/environment132 buildings, generic districts or synthetic material atlases replace the original buildings in this viewer.

Dust II additionally offers **Asl HD**: all 4,541,597 visible source triangles are retained without simplification or quantization, and 556 source texture images retain the original material/PBR bindings at bounded higher resolutions. The source sun's direction and color are used. [Detailed HD scope and limitations](SOURCE-HD-DUST2.md). Other ten entries retain the previous mobile derivations.

Full-model mode keeps roofs intact. Observer mode uses an elevation-aware route mask in both color and shadow passes. Opaque faces render from both sides to avoid reversed-face holes; authored foliage coverage remains. Compiler brushes stay hidden. Camera controls cover overview, A/B sites, spawns, rotation and zoom.

Lighting is a web preview rather than the Source 2 renderer. Baked game lighting, reflection probes, shader-specific layers, the in-game sky and all full-resolution source texture pixels are not reproduced exactly. The supplied original archives are unchanged. This page does not claim every missing export surface is fixed.

This is a visual review. The current 1.32 game, APK and club saves remain unchanged. Integrating a reviewed source scene into the simulator requires matching original collision, prop selections, water and save compatibility; original visuals must not be combined with rebuilt131 collision.

Subsequent work must follow the actual source: silhouettes, routes, stairs/elevations, source-specific facades and palette. Repeating generic buildings does not improve fidelity. Supplied CS2 assets retain Valve/their respective owners' rights; no original ARENA authorship is claimed for them.
