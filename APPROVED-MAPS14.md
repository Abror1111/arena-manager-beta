# Accepted maps connected to the game — maps 14

The full-game UI 13 release had retained the older simplified 1.31/1.32 map renderer. The accepted source models and completed surroundings were only available in the separate inspection page. This update connects those accepted scenes to the main game's free-map viewer and live 5v5 renderer.

The entries are Dust II, Mirage, Vertigo, Nuke, Anubis, Ancient, Inferno, Overpass, Cache, Train and Ancient Night. They use the exact checksummed mobile-balanced visual assets from the accepted review. Ancient Night retains the accepted shared Ancient geometry with its separate night atmosphere and navigation. The geometry, source textures, completed facade/room repairs, supporting ground, themed districts, palms/vegetation, water and atmospheric effects come from the reviewed scene modules. The separate review page is retained.

## Gameplay alignment

The reviewed source transform is applied directly; models are not recentered by their bounding boxes. Navigation polygons, spawn/site coordinates and player scale remain unchanged. Source visibility data and the matching CS2 collision meshes replace the simplified map collision. Physics preparation completes before a match advances, and it is shared by 2D and 3D. Source-source objects use the existing mesh-part promotion system for grenade and fire responses; the old rectangular substitute objects are not used in the new scenes.

Battle views cut only geometry above the actual playable routes. Upper/lower floor selection remains available. Free-map viewing starts with the complete accepted model and offers a separate routes view. Actors, weapons, C4, particles and water interaction effects render over the source scene's preserved color/depth. A stable-camera HDR cache avoids redrawing the complete static source model for every actor frame; it invalidates for camera, floor, route visibility and source-object changes. The reviewed dynamic exterior remains animated.

The library and loading screens use new previews captured from the connected scenes. Bulk downloads and readiness checks now list the accepted models, matching collision, route masks, source PBR media and supporting structures, sharing the existing verified asset cache. Previously cached accepted assets can be reused. They no longer prepare the old simplified model pack.

## Saved clubs

The career storage key and schema remain unchanged. Current matches use `arena-reviewed-14`. A previously deployed `arena-rebuilt-131` snapshot is validated against its original object definitions, then retains its score, round, timer, actors, funds, gear, tactics and random state while moving to the accepted scene. Only obsolete old-model object damage states are cleared, because their IDs describe different geometry. Club funds, roster, season, history and BO3 progress remain intact. The signed previous Android package is unchanged; this deployment updates the web game.

## Checks

The current test command covers the accepted-map integration, source collision, gameplay movement, old-save migration, career progression, asset validation, audio and effects. The previous `tests/rebuilt` and `tests/environment132` scene-specific assertions describe the superseded scene pack and are kept as historical material rather than the current map contract.

Browser checks load every accepted scene both in free-map viewing and an actual 5v5 match, verify its source hash and physics revision, and check that inspection-to-match reuse requests the visual model only once. They also exercise route/lower-floor views, camera modes, mobile rotation and match checkpointing. A fixture from the actual previously deployed UI 13 app checks migration without losing score or player positions. The production project prefix, offline cached launch/resume, and protected review-page files are checked separately before publication. Browser transport fixtures serve exact local copies of the pinned media, retaining normal game hash validation.

Chromium touch/WebGL checks are browser simulations. Physical phone/iPad performance and Safari-specific behavior have not been certified here. Source geometry and recordings retain their original attribution and ownership.
