# Original export visual review

The 1.31/1.32 releases replaced the supplied map buildings with procedural interpretations of the navigation layout. Additional generic details and material families in 1.32 did not restore the source-map identity. A navigation match is not visual fidelity.

This separate review page returns to the supplied, checksummed CS2 visual exports for all eleven map entries. It loads their actual building meshes, elevations, UVs and original colors; the three existing per-map source PBR recordings restore selected higher-resolution surfaces. No rebuilt131 or environment132 buildings, procedural districts, generic material atlases or synthetic landscape replace the original model. The source export is retained byte-for-byte.

Full-model mode keeps roofs intact. Observer mode uses the existing elevation-aware route mask in the color and shadow passes. It does not cut or rewrite source mesh buffers. Opaque faces render from both sides to avoid reversed-face holes; authored foliage coverage is retained. Source compiler brushes remain hidden. Camera controls permit overview, A/B sites, spawns, rotation and zoom.

Lighting is a neutral web preview, not a recreation of the Source 2 renderer or baked game lighting. Mobile exports remain reduced compared with the full source archive. This is a map review, not a completed replacement APK or a claim that all missing export surfaces are fixed. The running game and career storage are unchanged.

The visual reference must drive subsequent fixes: correct silhouettes, routes, stairs/elevations, source-specific facades and palette; no repeated generic buildings to inflate a model count. Dust II is the first detailed comparison target. Integrating a reviewed source map back into the simulator also requires corresponding source collision, prop ranges, water, route visibility and save compatibility; mixing the original visuals with the rebuilt collision is prohibited.

Source assets retain Valve/their respective owners' rights. No claim of original ARENA authorship is made for these CS2 map models or textures.
