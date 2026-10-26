# Dust II exterior, missing rear facades and camera presets

The quality review now adds the exterior requested in the annotated screenshots. The supplied map itself remains the source scene: the HD option still renders all 4,541,597 original visible triangles, original UVs and original material bindings.

A continuous source-sand terrain extends underneath the city and into low dunes. Its inner elevation follows the original navigation floors with clearance, rather than burying streets, stairs or changing routes. An irregular east coast blends into shallow animated water. Nine palms are extracted from the supplied source palm geometry and use its textures. Sparse sand wisps and small palm movements provide gentle wind; the city remains unobscured.

Missing exterior facades are reconstructed from actual roof edges and neighboring vertical source surfaces. Panels use the corresponding source plaster/brick/concrete textures, source color factors and measured UV density. Their bases extend into the new terrain. The original west perimeter plane also receives a solid return and a footing down into the terrain, closing its exposed edge and floating base. All new solids remain outside a guard around original playable floors. They close export openings; this does not claim every possible internal export defect is repaired.

Six complete Dust II camera presets cover overview, front, side, rear, the marked exterior facades and a closer oblique street view. Each preset restores its target, zoom and angle, draining pending drag/pan damping first. A/B, spawn, drag/zoom and quarter-turn controls remain. Umumiy returns to the full overview. Other maps keep the four shared views. On narrow phones the camera strip scrolls horizontally. A `view=facades` or `view=streets` link opens the corresponding Dust II view directly.

The large static world is captured at the canvas drawing-buffer resolution with multisample antialiasing, linear HDR color and depth. Gentle exterior animation renders over that depth, avoiding a full source-map redraw every idle frame. Camera, visibility and resize changes recapture the world. Devices lacking multisampled float color use a direct antialiased fallback. This is an optimization, not an increase in the mobile model's source resolution. Actual low-end Android performance still requires device testing.

New source-derived palm bytes are pinned to an immutable media commit and verified before use. Existing verified model caches remain. A network failure is reported with a retry action rather than silently substituting unrelated art.

This update is confined to the standalone quality review. Other ten map entries, the 1.32 game/APK, career saves and production bot are not changed. Source assets remain Valve/their respective owners' property. Source 2's complete renderer and baked lighting are not reproduced.
