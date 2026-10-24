# ARENA Manager1.28 beta — architectural detail and source PBR

[Web / PC](https://abror1111.github.io/arena-manager-beta/?v=128) · [Android APK, 393 MB](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.28-beta/ARENA-1.28-beta.apk)

All11 selectable maps use a Blender-authored detail library with44 models: curved roof channels, arches, bevelled masonry, window frames, balconies, bent pipes, vents, railcar bogies and multi-storey facades. Original CS2 base geometry, navigation and collision remain. Selected genuine source normal/roughness maps and up-to1024px colors are restored from preserved supplied exports. Source vertex tints are retained when matching the new geometry to map materials.

Ancient Night uses the supplied Ancient visual with identical coordinates, its own night nav/collision/route mask and night lighting. It is a shared-geometry variant, not a separate supplied night visual export. Shared files are cached once; map preparation includes terrain, route masks, detail models and PBR textures. The original1.26 ARENA variant and historical public files remain preserved.

[Changes and scope](VISUAL-UPGRADE.md) · [Blender/source pipeline](DETAIL-PIPELINE128.md). This is an architectural/material pass over source scenes, not eleven newly hand-modeled finished1:1 replicas. Source-game assets retain their original ownership.

Install over the existing app without uninstalling. VersionCode129 and the same signer preserve club and match saves. Verification includes138 Node tests,44 compressed model bounds/UV checks,11 map renders, static/auto/player cameras, source textures, offline cache reopening and exact native assets/signature. Physical Android FPS/memory remains unmeasured. The separate case bot is unchanged.

APK 392136366 bytes; SHA256 `11dd5e8d8beebbfc8ffeaf49ae68078df68cb05d03cd55540f84ddce37cbcf37`.

[Editable Blender detail catalog](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.28-beta/ARENA-Blender-details-1.28.zip) —44 architectural modules.
