# Dust II: coastal water, exterior life and four dressed facades

This update applies to the standalone `quality.html` review. It preserves the
supplied Dust II geometry, UV/material bindings, all nine enclosed perimeter room
parts, all nine source plinth parts and the previously repaired tower bases.
The other ten maps, current game, Android APK, saves and production bot are unchanged.

## Water and animation

The eastern coast has a denser shoreline-following water mesh. Two wave scales
displace the surface; smaller ripples perturb its normals. Shallow water blends
over the original sand, with increasing absorption and a deeper turquoise tint
away from the beach. The shader adds a moving wash/foam edge, subdued caustics,
sun highlights and view-angle-dependent reflection. Shore depth is an approximation
of this scene's authored seabed, not a general-purpose depth/refraction simulation.

A clipped, mirrored orthographic camera captures the actual static coast/city.
Reflection color is stored in linear space with an alpha mask; unoccupied areas
receive a procedural sky reflection. The water itself never enters this pass.
The initial capture is refreshed after the main shadow map is ready. Subsequent
captures wait for 160 ms of camera/visibility/resize inactivity, rather than
drawing the whole map on every drag or animation frame. The longest target side
is limited to 384 pixels on mobile layouts and 640 on desktop. This affects only
the intentionally rippled reflection; the main map remains at full canvas
resolution with its existing antialiasing. Static reflected foliage updates with
the camera, not on every individual leaf movement.

Nine instanced, wing-flapping/gliding coastal birds and six drifting, soft cloud
billboards animate outside the city. Four extra source-derived palms bring the
exterior total to thirteen. Their roots use the actual rendered terrain sampler.
The existing 120 sand wisps now travel with a directional wind and fade near water
and the playable city. Palm fronds share a gentle wind animation. The additions
use shader animation, instancing and small material batches; no new texture or
model downloads are needed for this update.

## Four exterior facade compositions

The west residence, radio-building return, northeast workshop and curved bay
receive original, locally authored detailing: thick stone arches/reveals/sills,
split timber shutters with louver geometry and a small generated weathered paint
texture, cornices, balcony rails, shaped fabric sunshades with scalloped hems,
turned open-rim terracotta planters and curved foliage. They attach to the new
perimeter closures and leave the original source fronts intact. Their geometry
is batched into seven material groups. These are four facade compositions, not
four new gameplay buildings.

`Kamera → Suv va sohil` (`view=water`) opens a closer oblique inspection view.
`Sohil tomoni` retains the whole coastal side; `Umumiy` restores the full map.

## Build and verification

The Three vendor implementation did not change. The post-build step verifies its
entire executable-body SHA and export set, then maps Vite's reordered export
aliases back to the already published, byte-identical vendor. It fails closed if
the implementation or export set changes. The app receives a new SHA-derived
filename. This avoids downloading a duplicate vendor or exceeding the Pages
artifact limit solely because export aliases moved.

`check-coast.mjs --phone` and `--hd` exercise the marked/coast/water cameras,
landscape/portrait layouts, preserved geometry/contact repairs, live ambient
frames and stable idle scene/reflection capture counts. `check-water.mjs`
compares frozen-time real-reflection versus sky-only rendered pixels, checks
moving water pixels without static recaptures, camera-follow reflection refresh,
and the direct non-float fallback. Ground contact and all nine camera frusta
are checked independently. These are Chromium desktop/mobile-layout tests;
physical low-end Android performance remains a device check.
