# ARENA Manager 1.47 — Supply market

The club shop now opens on a coherent Supply market: original SVG product illustrations, three-currency wallet, grouped catalog, responsive product cards, clear checkout/ownership states and saved transaction history. All changes are scoped to the shop; existing club/battle UI and 11 maps are retained.

15 market offers:3 fixed one-time bundles,3 coin→star exchanges,8 permanent portrait frames and roster recovery. Bundles show guaranteed stars/tickets/frame/energy before checkout, debit club coins atomically and cannot be bought again after export/import. Existing46 balances/ownership migrate without grants. Frames are cosmetics. Recovery caps at100. No random loot or real-money charges.

Player contracts retain level/8player restrictions and now show consistent original anime portraits, OVR,3 skill bars, role, potential, salary and prices. Name search, role/open-only filters and price/rating sorting work. Club/Pro passes still last10completedofficialseries and use earned stars. Six reward goals and existing themes/emblems remain available. TEST laboratory stays temporary and isolated.

65Node tests pass including4new bundle/migration/atomicity/frame tests and61existing, plus preserved custom regression scripts. Browser checks cancellation, fixed bundle ownership/ledger, mobile checkout,8frames/exchange, player filters/unlocks/contracts, pass/goal/old theme purchases, five viewport sizes280–1024px and offline persistence. No frame-rate claim. Source ZIP web rebuild is byte-identical.

Node22+/Python3: install exact package.json dependencies, `npm test`; build with `ARENA_MANAGER_OUT=/tmp/arena47-web npm run build` then `python pack-web31.py /tmp/arena47-web`. Serve at /arena-manager-beta/remix31/ with existing shared root assets. No new heavyweight art downloads: product graphics are inline SVG and portraits reuse verified original atlases.

Android Preview1.47 uses the same application ID/signing certificate as1.46 and can update it. Sandrift3D/all11simulation/collisions/audio/portraits bundled; other3D worlds require first Internet download. See androidGame47/README.md. Generated assets/private signing keys/build caches are excluded from source. Native build/signature/89asset hashes and extracted-APK browser smoke are checked; no physical Android installation claim.

PlayConsole/AdMob are deferred by user. No real payment/ad activation, commercial-release readiness or source-map rights clearance claim. Case bot and parent sources remain untouched. Prior46 source and receipt: https://github.com/Abror1111/arena-manager-beta/tree/arena-career46-source .

Source: https://github.com/Abror1111/arena-manager-beta/raw/0fe7b07357db89bc9eaf8a630527af34cc40df27/ARENA-market47-source.zip
SHA256: c2e6ea08b0642ab1cfae82ec45154714c55a68b57cadc29263fa254a3aae5f27
Receipt: arena-market47-source/publication47.json
APK: https://github.com/Abror1111/arena-manager-beta/raw/51469bdbf10603d531d16ae1a9608feaafd3c1b4/ARENA-Manager-1.47-preview.apk
