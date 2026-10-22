# ARENA 1.20 beta — map surfaces and interactive water

Opaque original map surfaces now render from both sides, so a reverse camera view no longer looks through a one-sided wall. Authored foliage/glass transparency stays intact. Lower-floor cuts receive geometry caps only from closed source-mesh intersection contours; nested courtyard holes and open paths remain open. This does not reconstruct entire buildings absent from the exported map.

The source textures remain unchanged. A modest render-only saturation and midtone lift, high roughness and softer fill lighting give a brighter, smoother illustrated look while preserving readable shadows and detail.

Original water triangles on Anubis, Ancient, Inferno, Nuke and Train use a transparent animated Fresnel surface. Coplanar untextured exported water skins are hidden in memory without removing beds, banks or bridges. Moving agents make ripples and small splashes; water-entry grenades and HE/C4 explosions create larger ballistic droplets. Height checks prevent bridge traffic and blasts on another level from disturbing the water. Foam is clipped to source water polygons; spray depth-tests against the map and respects lower-floor cuts. Droplets are bounded to 96 on mobile, 160 on PC, 48 with reduced motion, with one instanced draw call. No screen-space refraction or fluid simulation is claimed.

Existing detailed recreated C4/utility models, 43 pinned original CS2 SVG icons, original exported map/agent geometry, 31 original effects and two original C4 music cues remain. Missing source effects use procedural fallback; absent menu/result music stays silent. Ancient Night remains simplified. Navigation, physics, career save schema and Android upgrade signer are preserved.

Phone and PC browser testing does not measure performance on physical Android devices. Install over the existing app to keep your club. Source map, icon and audio ownership remains with Valve and respective owners; included provenance and license files describe the sources.
