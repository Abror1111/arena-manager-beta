# ARENA Manager 1.26 beta — Original Maps

[Play on web / PC](https://abror1111.github.io/arena-manager-beta/?v=126) · [Android APK, 28 MB](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.26-beta/ARENA-1.26-beta.apk)

Eleven ARENA-authored beta maps replace the source-game map dependency: independent layouts, navigation, terrain, collision, architecture, texture patterns, water and surroundings. The app generates these maps locally. Original map downloads, radar images, terrain rasters and GLBs from CS2 are excluded from the active bundle. Historical public asset URLs and original exports remain preserved.

[Map details and scope](VISUAL-UPGRADE.md) · [Authoring](ORIGINAL-MAPS.md) · [Provenance](arena-maps/PROVENANCE.json)

Existing source-game agents, weapon icons, VFX textures and audio remain third-party assets. Map originality does not establish rights for the rest of the game. These new layouts need further playtesting and balance work.

Old active rounds restart once on new geometry, retaining score, round number, club money and player stats; current-version saves resume normally. Back up the club before updating, then install over the old app without uninstalling. VersionCode127; same upgrade signer. APK 27876351 bytes; SHA256 `a0efc02e38ec160bae1158db34da15d44b25acde7203b589229d7d7d5dfbd99e`.

Verification covers132 Node tests, all11 rendered phone views, static/auto/player cameras, actual audio playback and offline reopening on phone and PC emulation, plus native assets, signature and alignment. Physical Android performance has not been measured. The separate case bot is unchanged.
