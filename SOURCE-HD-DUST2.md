# Dust II source HD — visual fidelity work

The previous visual review used a mobile derivation with simplified geometry, mostly reduced albedo textures and three selected PBR restorations. It preserved the source layout and identity, but was not the full source geometry.

Dust II now has a separate full-detail option derived from the supplied 321 MiB source GLB. It retains 4,541,597 rendered source triangles. Only invisible compiler brushes and Source 2 engine-effect cards are removed. No mesh simplification or quantization transform runs. Batching retains the triangle count; every geometry attribute is compared byte-for-byte after writing and reading the compressed GLB, and triangle indices are compared with equivalent cyclic rotations accepted. Source archives remain unchanged.

The HD scene retains original material factors, UV sets, tangent data and source normal/roughness/metallic/AO texture bindings. Its 556 runtime texture images are derived from the supplied art: four dominant surface textures can reach 2048 pixels, the next 48 albedos 1024, other albedos 512, with bounded normal/ORM copies. Images are not enlarged beyond their source resolution. WebP conversion and downsampling mean runtime pixels are not identical to every full-resolution original image.

The directional sun's orientation and color come from the source export. Light intensity is adapted to the web renderer; baked Source 2 lighting, reflection probes, shader-specific material layers and the in-game sky are not reproduced exactly. A fixed-camera check exposed shadow self-interference; calibrated shadow offsets remove the observed stripes while retaining cast shadows. Authored overlay materials receive a small depth offset rather than fighting the underlying surface.

HD downloads 159,397,686 bytes in two individually SHA256-verified parts and caches them once. Desktop Dust II defaults to HD; touch devices default to the existing mobile model, with explicit HD selection available. Quality switches recreate the graphics canvas and release the old scene. Idle views stop drawing. Low-memory device performance has not been measured on physical hardware.

This update concerns the separate map-review page. Other map entries still use their previous source-based mobile assets, and the running 1.32 game/APK and career saves remain unchanged. Full-detail Dust II must subsequently be integrated with its corresponding original collision, prop selections and navigation rather than the rebuilt131 collision.

Reproducible derivation: `scripts/build-hd-dust2.mjs`, with the original supplied export and the separately installed glTF Transform/meshoptimizer/sharp tools. Public immutable asset commit and checksums are recorded alongside the validation receipts. All supplied CS2 assets remain the property of Valve and their respective owners.
