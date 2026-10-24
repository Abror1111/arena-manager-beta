# Scenery completion pass 1.29

The supplied CS2 base scenes and navigation remain unchanged. The 1.28
architecture/PBR work is retained. This pass replaces the remaining primitive
vegetation, rocks and static decorative cargo with four authored Blender meshes:

- A tapered, branched tree with root buttresses and curved, veined leaves.
- A bent palm with trunk scars, frond stems, leaflets and hanging fruit.
- A cluster of irregular eroded rocks with individual chips.
- A pallet crate assembled from separate planks, braces, steel bands and handles.

The catalog has 44 objects (four types in each of 11 map palettes), sharing four
mesh datablocks. This is intentional reuse, not 44 independently unique models.
The previous 44 architectural modules remain separate. Runtime source bark,
wood, metal and stone textures are matched where available. Leaf pigmentation
and geometry are ARENA authored; no claim is made that these are CS2 tree assets.

`sceneryPlacements` changes only selected validated non-walkable pocket records,
without changing their position, height, rotation or original footprint. Every
map has an actual new placement; this is checked against the decoded mesh bounds.
Source navigation, collision, prop physics, original exports and source audio
remain untouched. Whole-instance floor switching applies to both detail sets.

The terrain transition now samples a low-frequency tone from its actual source
paving rather than imposing a fixed outer soil color. Selected alpha-tested
source surfaces retain their original base color/coverage while receiving their
genuine normal and roughness recordings. Transparent surfaces remain unchanged.

## Rebuild

1. `ARENA_BLEND_OUTPUT=/path/to/catalog.blend blender -b --python scripts/build-scenery129.py`
2. `node scripts/compress-scenery129.mjs`
3. `node --test tests/scenery129.test.js`
4. Build and inspect the 11 maps and static/auto/player/lower-floor cameras.

Keep UV and vertex color attributes during compression. Files in `detail129`
are supplementary to `detail128`; do not overwrite the 1.28 library or its URLs.
Prepare-all includes both libraries once, so an unseen map also opens offline.

## Scope still requiring separate production work

The base scenes are the supplied CS2 exports. This work does not manually remake
every landmark or restore every source PBR material. Ancient Night is still a
night variant of the supplied Ancient visual with its own navigation/collision.
Physical Android frame rate, thermal load and memory need device measurements.
These limitations are explicit; completing this scenery pass does not turn the
beta into a finished commercial game or eleven independently hand-modeled maps.
