# ARENA Manager 1.30 beta — closed walls and eleven map architecture edits

[Web / PC](https://abror1111.github.io/arena-manager-beta/?v=130) · [Android APK, 400 MB](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.30-beta/ARENA-1.30-beta.apk)

Thin/open observer walls and hidden actors are addressed with actual new 3D geometry: 7,335 closed wall solids, source-derived wall cross-sections, beveled coping and eleven distinct Blender architecture modules. Every map gets its own edited landmark. Existing validated pockets, walkable lanes and source prop exclusions are retained. Supplied base GLBs, navigation and gameplay collision stay byte-identical.

Actual animated occluded bodies show in team color. A stencil veto keeps normally visible skins unchanged, with shared geometry and bones. Portrait pins stay close to actors; a lower-floor indicator, wider framing and separate auto-action/player cameras improve readability. Color and shadow shaders use matching cutaways, including the global lower-floor operation. Hidden ceilings no longer leave the revealed rooms in shadow.

[Map-by-map geometry and visibility](OBSERVER-PIPELINE130.md) · [Changes and scope](VISUAL-UPGRADE.md). New geometry and source textures are cached once and bundled in the APK. The previous architecture, source PBR and original audio remain. Ancient Night still shares the supplied Ancient visual. The new editable Blender source contains eleven modules, not complete source maps. Source-game assets retain their original ownership.

150 Node tests passed, with decoded geometry/UV/footprint checks, source hashes, real cap/bevel normals, skin-sharing and shader regression coverage. Actual WebGL pixels verify four observer angles, occluded-body visibility and unchanged visible colors. All eleven maps were rendered in static/auto/player modes and available lower floors. A final portrait-layout correction was additionally checked on phone/PC at the project prefix, with source recordings and offline reopening. Physical Android performance remains unmeasured.

Install over the existing app without uninstalling; versionCode131 and the same signer preserve saves. Historical public binaries and immutable asset URLs remain preserved. The separate case bot is unchanged.

APK 399893992 bytes; SHA256 `be9935fcaf89537961a0da56cedbda98c5de151ffdd6646b852c718a5e8ef8a5`.
