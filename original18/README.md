# ARENA Originals — Sahil 01

A separate original coastal 3D visual sample. Does not replace the existing manager or production bot.

The scene, facade elements, canvas materials, palm geometry, water/flame/particle shaders, articulated characters, grid navigation and synthesized audio were authored for this sample. No CS2 model, texture, sound, icon, animation clip or navigation asset is imported. Three.js 0.180.0 is used under MIT; the complete notice accompanies the web build and is embedded in the downloadable HTML.

Controls: drag to orbit the overview; wheel/pinch to zoom. Separate Auto-action and Agent cameras. Click a visible agent label or choose a roster entry in Agent mode. Effects menu: grenade, smoke, incendiary, flash, C4. Sound requires a user click. Pause, HD/ECO and fullscreen controls included.

This is an 85-second looping demonstration with independently navigating agents and staged events, not a finished competitive AI or integrated career match. The characters and sound design are original procedural prototypes; no claim of scanned/captured studio assets, final AAA quality or legal certification is made.

Build from this directory with `node build.mjs`; dependencies resolve to the existing pinned Three.js/esbuild installation. Default output is `/dev/shm/arena-original18-build` to avoid modifying the large manager build or filling the workspace disk. `ARENA_SHOWCASE_OUT` can override the output directory. The output HTML embeds its code/material generation; no CDN assets are needed. The optional subdirectory service worker is restricted to `/original18/` and uses its own cache namespace.

The downloadable HTML can be opened by a WebGL-capable browser. The managed test browser blocks `file:` navigation; a no-network browser context rendering the exact HTML is used to verify self-containment instead. Physical Android/iOS devices have not been certified. Relative links to the separate notice document require the accompanying file or the hosted version; its full notice is also embedded in the HTML itself.

Source legality of the main manager's legacy CS2 materials is a separate unresolved matter; this sample does not clear those distributions.
