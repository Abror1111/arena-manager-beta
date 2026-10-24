# Blender/source-material pipeline

1. Run Blender4.3.2 with `--background --python scripts/build-detail-kit128.py`.
   The output catalog has11 columns and four model types per setting; it saves
   an editable `.blend` source and the runtime GLB.
2. Run `node scripts/compress-detail128.mjs` using the existing pinned glTF tool
   workspace. Keep unused UV attributes: materials are deliberately assigned
   source textures at runtime. Dropping these UVs produces flat sampled colors.
3. Run `node scripts/check-detail-geometry128.mjs`. It verifies all44 compressed
   model bounds and UVs against the validated placement envelopes.
4. `scripts/extract-pbr128.py` reads preserved export archives and emits bounded
   runtime WebP copies. Do not overwrite the source archives or original GLBs.
5. `scripts/bake-ground128.py` derives a ground transition from the existing
   source coverage raster; it does not edit nav, collision or terrain heights.
6. Build/test the app. Inspect both close-up material assignment and all11 map
   views, including night foliage and Vertigo. Geometry-only tests cannot detect
   missing UVs or incorrect source material tints in the final renderer.

Runtime matching uses actual source texture names and baked vertex tint samples.
`source-pbr.js` restores selected genuine source recordings; it preserves alpha
coverage and releases newly decoded images when a loading operation is aborted.
Ancient Night shares Ancient's supplied visual only because the coordinate
transform is identical; its nav, collision and route mask remain distinct.
