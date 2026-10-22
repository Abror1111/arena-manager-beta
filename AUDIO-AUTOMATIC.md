# ARENA 1.22 audio

The uploaded 180-file CS2 audio export remains the verified source. The runtime now uses 56 original effects/reload/ambient recordings and two original C4 music cues. The AK uses the current `ak47_01.wav` sample rather than the legacy hyphenated sample. Reload events now route to the verified exported magazine/bolt/add-ammo recordings, where supplied. Ambient excerpts retain source SHA and excerpt duration.

The export does not contain original HE/C4 detonation recordings, seven weapon shots, complete reload sets, or menu/result music. Those gaps use separately attributed ARENA recordings/compositions in `src/studio-audio.json`; they must never be described as CS2 audio. The combined runtime resolves original keys first. Genuine readiness and playback counts exclude authored additions.

The new mix retains original pitch, gives shots priority, reduces score during gunfire, and uses recorded effects for fire tails and ambient sound. Settings lets the player select a weapon and see whether its sample is CS2 or ARENA. Menu, battle and result scores have independent music volume, pause/background handling, fades and bounded streaming memory. The original C4 tracks remain.

Validation includes hashed source assets, real autonomous battles with decoded-buffer source tracing, actual WebAudio output RMS, codec failure/retry, native-like PCM compatibility, project-prefix/offline reopening and packaged APK asset/signature checks. Browser measurement cannot establish the sound heard from a physical Android speaker or prove subjective 1:1 similarity. The user should compare the selected AK/AWP samples in the new build on their phone.
