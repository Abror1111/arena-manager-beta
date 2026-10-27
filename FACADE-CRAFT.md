# Dust II: crafted exterior facade ornaments

This update refines the existing **25 exterior facade and side-return spans**.
It adds 7 portals, 27 lattice screens, 569 mosaic tiles, 84 scrollwork panels and
98 carved reliefs. The facade detail mesh totals 101,791 triangles in nine
material batches. It does not change the main source map, navigation, enclosed room plan, terrain,
camera presets or coastal water. The prior water function and those source files
are checked byte-for-byte against the previous review source archive.

## Architectural detail

- Segmented stone portal arches, molded jamb bases/capitals, paneled double timber
  doors, iron ring knockers and carved star reliefs. Entrances are placed only
  where height below the existing balcony and the ground slope permit them.
- Projecting timber lattice screens on selected upper windows, diamond grille
  geometry, ledges and stepped support brackets. Windows are deliberately varied
  instead of placing a screen on every opening.
- Paired curved iron scrolls between balcony pickets and rounded handrails.
- Glazed geometric tile friezes, small carved rosettes, alternating corner stone
  blocks and additional molding edges. Residences, service buildings and kasbah
  walls retain their different treatments.

These ornaments have actual depth: tube geometry for curved ironwork and door
knockers, separated arch stones, projecting frames, inset panels and cut-out
lattice rods. They are merged into static material batches with the previous
facade geometry. The glazed-tile material adds one batch (nine in total), rather
than a draw call per tile or ornament. Decorative doors are facade dressing on
existing closed volumes, not new gameplay entrances.

Entrance thresholds follow the actual rendered terrain sampler. Their lower
vertices overlap the terrain slightly. Door height adapts to leave clearance
under the existing balcony slab, and kasbah gates sit between the existing
buttresses. No portal is placed on the two copied source-plane overlays. Corner
stonework on those overlays starts at the actual source face's bottom elevation.

## Ceramic finish

A locally generated atlas contains four coordinated cream/teal, blue, terracotta
and sage geometric motifs. It includes separate 512×512 color and relief-normal
maps, plus a 256×256 roughness map. The uncompressed base-level RGBA image budget
is 2,359,296 bytes (about 3 MiB including mipmaps). Tile UVs use inset atlas cells
to reduce neighbor bleeding. The glaze responds to light; it is not a solid
paint stripe. No additional remote image/model downloads are required.

The main map still uses its original geometry/material bindings. The small new
ornaments do not animate. The full-resolution antialiased static-world cache and
the camera-settled planar reflection remain; idle frames animate the existing
water, clouds, birds and wind only. Physical Android performance remains a device
check; browser validation covers mobile layouts and rendering behavior.

## Inspection and verification

`Kamera → Fasadlar` shows the exterior row. Zoom in to inspect the lattice, glazed
frieze and door details. `Umumiy` restores the normal overview.

`check-craft.mjs --phone` and `--hd` inspect facade, close-zoom, marked perimeter
and coast views, portrait layout, source geometry counts, repair/ground contact
telemetry and stable idle scene/reflection capture counts. A cached/direct pixel
comparison checks that the added materials preserve main-map rendering clarity.
The scope receipt verifies that the water function, camera, terrain sampler,
closed-room plan and static-world cache implementation did not change.

Publication is confined to this standalone `quality.html` review. The current
game/APK, saved club progress and production bot remain unchanged. An obsolete,
unreferenced generated review bundle may be retired only after byte-exact archival
and a live-reference scan; source exports and current review bundles are retained.
