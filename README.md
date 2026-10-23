# ARENA Manager 1.24 beta

[Web / PC](https://abror1111.github.io/arena-manager-beta/?v=124) · [Android APK](https://github.com/Abror1111/arena-manager-beta/releases/download/arena-1.24-beta/ARENA-1.24-beta.apk) · [Download page](download.html)

The new user CS2 export is integrated: 75 original effects/reload/ambient cues and four original Valve music cues. Original C4/HE, molotov, flash, smoke, planting, four additional weapon shots and nine reload cues replace/extend the previous set. Original menu and MVP music are wired; the menu uses a documented 119.5-second excerpt. Settings can audition weapon and utility recordings. [Audio provenance and remaining ARENA cues](AUDIO-AUTOMATIC.md).

Effects decode at 32kHz with a 24MiB buffer budget (about 16.2MiB in browser measurements); new effects have PCM compatibility copies. Critical explosions win a voice under saturated gunfire. Legacy personal radio/physics misclassifications cannot override correctly bundled explosion cues. Music is streamed separately. Existing source recordings and public asset URLs are retained.

The 1.23 map ground and route-cutaway fixes remain, with unchanged source map/career/terrain data. Eleven layouts, ten authentic source mobile GLBs and simplified Ancient Night remain. Terrain/scenery additions are ARENA reconstructions. [Details](VISUAL-UPGRADE.md).

Validation includes 128 Node tests, actual decoded source hashes and measured audio output, original utility event routing, menu/MVP/C4 music, PCM codec compatibility, project-prefix/offline reopening, and exact APK assets/signature checks. Physical Android output/performance is not established by emulation.

Install over the old app without uninstalling. App ID `uz.arena.tactics.beta`, versionCode125, same upgrade signer. APK 383459041 bytes, SHA256 `f53c136d58f9bba45e05d6755b680d6ca4009e63fd281dfefa954de9475bfa35`. Original assets belong to Valve/respective owners; authored recordings have separate provenance. The separate case bot remains untouched.
