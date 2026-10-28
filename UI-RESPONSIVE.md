# Responsive map explorer — UI 12

The standalone `quality.html` map explorer now has a responsive dark interface with warm gold accents. This update changes the map inspection interface; the main game and Android package are separate releases.

## Layout and controls

- Phones use a five-action bottom dock and dismissible sheets. Landscape phones use compact horizontal controls to preserve map height.
- Tablets and desktop screens use wider panels and additional point shortcuts. The same controls remain available on narrow screens through the dock.
- A searchable map library shows the eleven supplied navigation silhouettes, A/B markers, active selection and first-download size.
- Camera, point selection, model/routes, floors and quality have separate labelled panels. Focus mode hides the interface without recreating the map. Fullscreen is offered when the browser supports it.
- Notches and system gesture areas use all four safe-area insets. Dialogs follow the visual viewport when the keyboard opens; their content scrolls independently.
- Where the browser exposes viewport segments, a book fold puts the map in one segment and controls in the other; tabletop mode places controls below the hinge. A keyboard covering the lower segment moves the open panel into the available region. Browsers without the segment API use the ordinary responsive layout.
- Dialogs support touch dismissal, Escape, keyboard focus containment and restoration. Interactive targets are at least 44 CSS pixels. Motion and transparency preferences have CSS fallbacks. Browser pinch zoom is not disabled.

## Validation

`tests/responsive-ui.mjs` runs component integration checks with an explicitly injected lightweight renderer. It covers 29 portrait/landscape viewports from 280 CSS pixels wide through tablet and desktop sizes, panel bounds, search, map/quality lifecycle, floors, focus, safe areas, reduced motion and keyboard-sized visual viewports. It checks that changing the viewport does not create another map world.

`tests/foldable-ui.mjs` uses Chromium display-feature emulation for a 54-pixel vertical hinge and a 40-pixel horizontal hinge. It checks both map/control segment placement and dialog bounds, then unfolds into a narrow phone without recreating the world.

`tests/real-explorer.mjs` separately checks the production build with the actual Mirage source GLB and WebGL renderer. Phone touch pinch, camera and A-point commands, model/routes switching, landscape, tablet, book fold and focus mode passed with one source-model request and the same canvas throughout. Its phone renderer pixel ratio was 1.75. The existing map/world engine source files and model assets are unchanged.

These are browser simulations, not physical Android, iPhone or iPad certification. Older engines without native dialog or WebGL support may require a newer browser. No fixture entry or test-only URL flag is included in the production build.

## Reproduce

Install the pinned dependencies with `npm ci`, then run `npm run build`. For UI integration tests, run the Vite dev server on port 5180 and execute `node tests/responsive-ui.mjs` and `node tests/foldable-ui.mjs`. The real-renderer test expects the built site, including its existing map assets, at `http://127.0.0.1:8184/arena-manager-beta/`.
