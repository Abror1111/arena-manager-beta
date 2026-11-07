# ARENA Manager 1.46 beta

Playable local career: saved nine-step beginner tutorial, transfers/lineup/training, league and BO3 playoffs, 5v5 simulation on 11 maps, match checkpoint/resume, season advancement and JSON backup.

## Earned economy

Normal progression does not require Play Console or AdMob accounts. Completed official series award 3 stars +1 ticket for a win, 1+1 for a loss. Practice/forfeit do not award these currencies. Once-only goals and participation-scaled season rewards add resources. Fixed coin exchanges, player contracts, cosmetic frames and recovery use earned resources. Club/Pro passes cost earned stars and last 10 completed official series, not calendar days; no automatic renewal or charge. Transactions reconcile to a validated ledger; rewards deduplicate per series.

Legacy commerce45 free TEST stars/tickets are not imported into earned balances. Cosmetic frame ownership is preserved. Settings → Laboratory runs the old purchase/ad demonstrations in a temporary club; closing/reopening resets it and never writes the main save. Existing old saves are preserved and migrated without free power grants.

## Run and build web

Node22+, Python3. Install the exact package.json dependencies. `npm test` runs current and prior regression suites. `ARENA_MANAGER_OUT=/tmp/arena46-web npm run build`, then `python pack-web31.py /tmp/arena46-web`. Serve under `/arena-manager-beta/remix31/` alongside the preserved shared CSS/portrait and map/audio assets. Remote immutable resources are SHA-verified and cached. The source ZIP excludes node_modules and generated builds. See verification46 for build/functional evidence.

## Android preview

See androidGame46/README.md. This is an installable debug-signed preview, separate application ID from older beta. Sandrift 3D, all 11 simulation maps/collisions, covers/portraits/audio are bundled. Other 3D worlds require an initial Internet download. Existing club data can be moved using Settings → export/import backup. No live payment, advertisement, production signing or physical-device FPS claim.

61 Node tests pass. All 11 actual AI simulations reach matchend (229 rounds, 23,497 shots, 117 plants, including overtime). Browser tests exercise legacy migration, earned purchases/pass/rewards, laboratory isolation, four viewport sizes and offline persistence. Extracted APK assets are additionally tested in offline Chromium; this does not substitute for Android device testing.

Map/geometry/audio/portrait art and original core UI are preserved in this version. Original case bot and parent application untouched. Existing source-map licensing questions are not resolved by this release. Prior history and inactive monetization foundation: https://github.com/Abror1111/arena-manager-beta/tree/arena-commerce45-source . Google Play/AdMob accounts and remaining trusted server/lifecycle integration are deferred, as requested.

Reproducible46 source: https://github.com/Abror1111/arena-manager-beta/raw/d3854fe895aaf07f36e06559f1c76580ff98b0ef/ARENA-career46-source.zip
SHA256: c0e6c92f54a17ba9b5f2109b9b5c3b038ede96957e639cb6eb4f0b3d1738b803
Final receipt: arena-career46-source/publication46.json.
Android preview: https://github.com/Abror1111/arena-manager-beta/raw/6163102ead3be38662c2c88b9416fb67b4b71593/ARENA-Manager-1.46-preview.apk
