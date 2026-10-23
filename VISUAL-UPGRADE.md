# ARENA Manager1.27 — CS2 map restoration

The playable map selection returns to the1.25 CS2 reference maps: Dust II,
Mirage, Inferno, Nuke, Train, Ancient, Ancient Night, Anubis, Overpass, Vertigo
and Cache. Ten exported textured GLBs and the existing simplified Ancient Night
view are restored with their source navigation, radar, terrain, water, collision
and surroundings. Map and texture files match the verified1.25 version exactly.
This is a restoration, not a claim that every original CS2 asset is reproduced.

The original ARENA layouts from1.26 are no longer the active maps. That variant
remains preserved separately with its source snapshot and signed APK.

Source-game agents, weapon icons, VFX and the integrated audio set remain.
Static, automatic action and individual-player cameras use the previous angled
overhead views, including the Nuke floor controls. The1.25 original scenery
kits and verified terrain infill are retained around the CS2 base maps.

## Updating from1.26

The Android app keeps the same package and upgrade signer, with versionCode128.
Install over the existing app, without uninstalling, to keep the club.
A saved active1.26 original-map round restarts once on the corresponding restored
CS2 map. Round number, score, player stats, club money and player funds remain.
Already completed rounds/results stay completed. Existing CS2-version saves
resume normally; they are not restarted.

All maps are inside the APK, so the download is approximately384 MB again.
The web version caches maps as they are used; the map library can prepare them
in advance. Original exports and historical public URLs remain preserved.

## Validation and scope

Verification covers132 Node tests, including real1.26 match snapshots from all
11 maps and a real saved club. All ten GLBs, source navigation, terrain and
rendering modules match1.25. Mobile and PC browser checks cover the restored
views, camera controls, actual supplied audio playback and offline reopening.
Native contents, upgrade signer and APK alignment are verified. Physical
Android performance is not measured by those browser checks.

Existing CS2 assets retain their original ownership; reverting the maps does
not make them original ARENA assets or establish distribution rights.
