# ARENA Manager 1.31 beta — eleven complete rebuilt base maps

[Web / PC](https://abror1111.github.io/arena-manager-beta/?v=131) · [Android APK, 96 MB](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.31-beta/ARENA-1.31-beta.apk) · [All 11 editable Blender scenes](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.31-beta/ARENA-11-complete-maps-1.31.zip) · [Classic 1.30](https://abror1111.github.io/arena-manager-beta/classic-1.30.html)

Eleven complete procedural architectural scenes use the CS2 navigation layout and elevations as a reference. New floors, foundation, closed building backs, shaped roofs, windows, full architectural assemblies, landmarks, vegetation, props and mathematical PBR replace the previous source base meshes in this edition. These are authored layout interpretations, not an exact copy of every Valve building or a claim of manual modeling. Old 1.30 assets and its separate project remain unchanged.

Collision comes from the exact new solids. Gameplay waits for it before the first tick. Runtime meshes are batched and compressed; the downloadable Blender scenes retain individual geometry, packed own PBR, lighting and a camera. Source agents, icons and audio retain their original ownership. [Scope and reproducible tools](REBUILT-131.md).

47 Node checks passed in the final validation set. All eleven maps were rendered with source agents and static/auto/player cameras, including existing lower floors. Closed-solid topology, route/floor correspondence, prop collision, career migration, deterministic restore, economy and source audio were checked. A project-prefix browser test downloaded the full set, removed its network fixture, reopened a never-visited Ancient Night offline and played an original CS2 audio clip; phone and PC layouts passed. Every pinned public media file was SHA256-verified separately. Android APK signing, alignment and every packaged asset were checked; physical Android performance is not measured here.

Install over 1.30 without uninstalling. Application ID and signer are retained, with versionCode132. Validated careers copy to a separate new save key; old save storage remains. An active source-map round restarts once while club, series, scores and funds remain.

APK: 95012684 bytes; SHA256 `73da3ada24f5ac26055d3f7d5fcb90248e869335343793a3dd2da903280bfc4f`.
