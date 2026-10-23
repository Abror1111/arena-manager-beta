# ARENA Originals — 1.26 beta

The eleven playable maps now use ARENA-authored layouts, navigation, collision,
terrain, buildings, procedural texture patterns, water and surrounding scenery.
No exported CS2 map model, radar, material, terrain raster or navigation dataset
is loaded by this version. Existing exports and historical releases are retained
separately; they are excluded from the new APK and active map download list.

- Dune Courtyard: warm courtyard district and shaded architecture.
- Azure Arcade: pale plaster, blue accents and rooftop arcades.
- Amber Terraces: terracotta buildings and pergolas.
- Tidal Works: a compact energy campus with solar structures.
- Copper Depot: copper and timber service buildings.
- Fern Sanctuary: planted stone courtyards in a green setting.
- Moonlit Sanctuary: an independent night layout with illuminated garden details.
- Reed Quarter: sandstone river architecture and a shallow rill.
- Linden Promenade: green urban blocks and a water garden.
- Skyline Gardens: a grounded urban test arena with solar garden structures.
- Foundry Courtyard: workshop architecture and equipment.

Each layout has two bombsites, ten valid spawns, connected routes, cover,
continuous ramps and its own arrangements. These are original beta arenas,
not reproductions of the CS2 maps or finished competitive balance designs.
Buildings have closed backs and foundations. Continuous terrain reaches beyond
the perimeter, with sparse trees, rocks and matching architecture. Instancing
keeps repeated scenery in shared draw calls. Static, automatic action and
individual player cameras retain their existing angled overhead controls.

Original maps are generated locally from the app code, rather than downloading
large source-game map GLBs. Maps, radar previews and provenance are under
`arena-maps/`; `PROVENANCE.json` records each independent layout hash.
Legacy internal keys are retained only for club save compatibility; they do not
identify the old layouts. A saved active round from an old layout restarts once
on the new geometry, retaining its round number, score, club funds and player
stats. New-version matches resume normally. Back up the club before updating.

## Scope of originality

This change covers maps only. Existing exported CS2 agents, weapon UI icons,
VFX textures and audio are still third-party assets. They have not been made
original or licensed by changing the maps. Full independent commercial release
requires replacing or separately securing rights for those assets as well.
Original exports and prior signed APKs remain preserved.

## Verification

Route, collision, movement, C4, economy, deterministic save, migration, audio,
map provenance and rendering checks cover the new maps. Mobile browser
emulation and PC browser tests do not substitute for physical Android
performance measurements. Install the APK over the existing app without
uninstalling to retain the club.
