# ARENA original11 remix31 data

User-supplied CS2 map exports and their navigation/collision metadata remain source-game material. Relocating A/B and replacing rendered textures does not provide legal clearance. This branch supplies the compressed runtime metadata for a test remix; original models are reused from existing site assets. Ancient Night shares Ancient geometry and is a lighting variant:11 selectable entries,10 distinct source geometries.

sites31.json records old/new bomb sites, source-nav area IDs, distances and route metrics. New points were selected on reachable source navigation with room around the standing point and checked before use. Further gameplay balance testing is still needed.

ARENA-harbour30-preserved-source.zip preserves the separate authored port layout interrupted when the user changed direction; it is not the selected published runtime.

Final sites31.json includes the replacement Vertigo A point after collision-floor validation. validated-sites31.json records220 reachable spawn/site paths and all22 physical-floor checks. The earlier1328 metadata pack is byte-identical and remains pinned by the runtime; it does not carry the plant-zone overrides, which are compiled from the final src/sites31.json in the source archive.
