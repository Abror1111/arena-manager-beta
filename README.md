# ARENA Manager 1.23 beta

[Web / PC](https://abror1111.github.io/arena-manager-beta/?v=123) · [Android APK](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.23-beta/ARENA-1.23-beta.apk) · [Download page](download.html)

The render terrain now fills the map interior as well as the perimeter. Exact source navigation faces receive backing 0.09 units lower; polygon-clipped terrain fills non-playable gaps. Ground uses local grades and appropriate original paving textures. The distant plane has a central opening so it cannot cover low routes. Inferno uses its source stone and terracotta materials; irregular source-empty placements replace perimeter rows. Vertigo has an underlying building support and lower city ground. Route-height cutaways preserve full original exterior roofs while keeping lower streets visible; lower-floor selection is retained.

All eleven layouts have verified compact terrain payloads. Source geometry, navigation, agents and career data are preserved. Original ten mobile GLBs remain unchanged; Ancient Night is simplified. Terrain/scenery additions are ARENA reconstructions. [Details and limits](VISUAL-UPGRADE.md).

125 Node tests, compressed-mesh coverage/nav-safety checks, eleven rendered phone views, static/auto/player cameras and native package verification. Physical Android performance is not measured in browser emulation.

Audio is unchanged from 1.22: 56 original effects/reload/ambient clips, two original C4 cues, and separately attributed ARENA additions. The new 20261022 source archive has not been integrated because its downloadable URL is still needed. [Audio provenance](AUDIO-AUTOMATIC.md).

Install over the previous app, without uninstalling, to retain the club. App ID `uz.arena.tactics.beta`, versionCode 124, same upgrade signer as 1.10. APK 377620423 bytes, SHA256 `dfbfbc0ea8d7fb710c8d8e02c20adc4b782e0accfd98f53f55ce2dffe2757591`. Source assets belong to Valve/respective owners. The case bot is unchanged.
