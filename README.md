# ARENA Manager 1.29 beta — scenery completion pass

[Web / PC](https://abror1111.github.io/arena-manager-beta/?v=129) · [Android APK, 393 MB](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.29-beta/ARENA-1.29-beta.apk)

The supplied CS2 base scenes and 1.28 architectural/PBR pass remain. Four shared Blender scenery meshes add branched trees, curved palms, eroded rock clusters and slatted pallet crates. The new catalog has 44 objects (four types in eleven palettes) sharing four mesh datablocks. All eleven maps actually place the new scenery inside previously validated non-walkable pockets, preserving their position, height, rotation and footprints.

Outer ground now derives its transition tone from the actual source paving. Selected masked materials retain their original color/alpha and regain their genuine source normal/roughness maps. Both detail libraries are cached once and bundled in the APK; whole-instance floor switching remains. Original source map geometry, navigation, collision and audio remain unchanged. Ancient Night still shares Ancient geometry with its own night navigation and lighting.

[Scope and limits](VISUAL-UPGRADE.md) · [New Blender pipeline](SCENERY-PIPELINE129.md) · [Previous architecture pipeline](DETAIL-PIPELINE128.md).

This completes a bounded scenery pass, not every production task or a handmade 1:1 rebuild of every CS2 object. Source-game assets retain their original ownership. Physical Android performance remains unmeasured. Install over the existing app without uninstalling; versionCode130 and the same signer preserve saves. Historical public binaries and asset URLs remain preserved. The separate case bot is unchanged.

APK 392311592 bytes; SHA256 `0ad1116f1ebf894d5fae146e816c2363220963ea50b4e0e75498a3baca521437`.
