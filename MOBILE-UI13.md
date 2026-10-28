# Full manager interface — UI 13

This web update applies the navy and gold visual system to the complete game: startup, the club dashboard, squad, training, transfers, season, tactics, maps, settings and the live match. The separate `quality.html` inspection page remains available with its UI 12 design.

## Opening and navigation

The opening screen reads the existing club save and offers entry to the club or direct continuation of a saved match. It never resets a career. Maps and settings can also be opened here. The initial HTML loading state uses the same colors, without a blank white screen while JavaScript loads.

Phones have a five-action bottom dock: Club, Squad, Tactics, Season and Menu. The menu exposes all eight sections in a labelled panel. Tablets use a compact side rail; desktop screens use a full rail with club information. Player cards scroll horizontally on a small dashboard instead of shrinking five portraits into unreadable columns. Training and transfer cards, league tables and the pre-match plan use layouts appropriate to their available space.

## Live match and map viewing

The match has separate Camera, Players and Commands panels. Static, automatic action and individual-player cameras remain distinct. The player roster exposes all ten agents, weapons, ammunition, health and armor; selecting an agent switches to their camera. Small screens keep this roster in a panel so it does not cover the map. Commands retain strategy, economy, graphics, audio and grenade controls. The arsenal opens separately, restores the prior pause state on closing, and has independently scrollable category tabs.

Round and match results use the shared dialog. A dismissed round result can be reopened with the Result action; round auto-advance retains its previous behavior. The existing C4 outro and simulation are unchanged. The game's free-map viewer also groups camera, quality and floor controls in a panel.

## Device handling

All four safe-area insets, portrait and landscape, dynamic viewport height, and the visual viewport when a keyboard opens are handled. Dialogs have independent scrolling, Escape/outside dismissal, touch dismissal, focus containment and focus restoration. Main controls have minimum 44 CSS pixel targets. Reduced-motion and reduced-transparency preferences are respected.

Where supported by the browser, book folds place club navigation in the first segment and content in the second. Live matches place the battlefield in the first segment and the roster/controls in the second. Tabletop folds split these regions above and below the hinge. Dialogs remain in the control segment. Browsers without viewport-segment support use the normal responsive layout. Rotation and fold changes do not replace a running game or renderer.

## Save and release compatibility

The career key `arena-career-rebuilt131`, schema, import/export format, match engine, navigation, simulation, source agents, maps, textures and audio are retained. The service-worker shell cache is versioned as `arena-shell-1.32-ui13` so offline openings use the updated interface; verified binary map caches are preserved. This is a web-interface release. Previously signed Android APKs are unchanged.

## Verification

- The existing 56 Node tests passed, including careers, asset integrity and environment physics.
- `tests/ui13-responsive.mjs`: the actual manager's eight sections across 29 simulated viewports, with target sizes, overflow, dialog focus, safe-area, visual-viewport and reduced-motion checks.
- `tests/ui13-foldable.mjs`: actual manager startup, navigation and dialogs in book and tabletop hinge emulation, then normal narrow-phone navigation.
- `tests/ui13-game-flow.mjs`: actual training, rest, transfer confirmation, naming and save/reload; practice start, pause, camera selection, roster, buy policy, arsenal, round transition, checkpoint/resume and free-map inspection. It renders actual hashed media with WebGL and checks that rotation/UI actions retain the canvas. A round result is triggered via the existing engine method for integration coverage.
- `tests/ui13-battle-layout.mjs`: actual paused BO3/Nuke match UI across the same 29 viewport sizes, its panels and lower-floor controls, plus both hinge configurations and result dismissal/return.
- The production prefix and service-worker offline behavior are checked separately against the built files.

Viewport and hinge checks use Chromium emulation. Physical Android, iPhone and iPad hardware, and Safari-specific rendering, have not been certified here. The existing GPU and WebGL requirements still apply.
