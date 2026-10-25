# ARENA 1.32 — detailed architecture, relief and atmospheric lighting

Eleven existing rebuilt map bases receive twelve original curved and carved assemblies: ventilation with fan blades and louvers, ribbed domes, chimneys, carved stone arches, double-surface parabolic dishes, fluted pillars, detailed balconies, sculpted rocks, ferns, columned canopies, steel trusses and tiered windowed towers. Roof anchors use each model's actual rotation-safe radius; facade heights fit their host buildings. Instancing and static batching keep the additional draw calls bounded.

Six original material families provide 72 albedo, normal and roughness images for plaster, stone, paving and roofs. Colors and height fields are generated mathematically. Surface weathering is restrained so roads remain readable. Existing source agents, icons, original audio, animations, separate auto/player cameras, team silhouettes and base navigation remain.

The former flat apron and artificial foundation are replaced at runtime by an explicitly modeled terrain surface. Hills, dunes, rocks, vegetation, stair nosings and closed handrails follow their map's layout. Vertigo's surrounding city sits 18 world units below the play roof, with a full supporting building, repeated window frames and lower street ground. Existing playable elevations are preserved; no new tactical map floors are claimed here.

Every map receives a procedurally rendered six-face sky: sky and horizon gradients, clouds, a sun or moon, and stars at night. A filtered environment map supplies reflections where supported, including metallic details. Water shading reflects the sky palette and retains moving waves, ripples and splashes. Distant haze starts beyond the play area. Night skylight is balanced separately from the dark sky background to keep players visible.

New solid geometry is added to the exact triangle collision grid before a round can tick. The hidden artificial below-ground foundation faces are omitted for that scene, avoiding invisible floors above the replacement terrain. The same verified collision payload is prepared for 2D and 3D, and stays in the bounded physics cache when the camera mode changes. Scene disposal releases sky textures and visual geometry. Shared geometry/materials and 128-pixel mobile sky capture limit memory use; physical Android performance still needs device testing.

All extra models, themed materials and previews join the verified one-time asset cache and ship inside the APK. The existing career save key, navigation revision, base assets and prior public builds remain. VersionCode133 upgrades 1.31 using the same application ID and signer, without a map migration or current-round reset.

The editable source kit contains reusable detail assemblies with packed textures; the complete base-map Blender scenes remain available in the 1.31 release. This is an authored ARENA interpretation, rather than an exact copy of Valve's art. Existing third-party assets retain their ownership.

Install over the existing ARENA app to keep your club. Do not uninstall first.
