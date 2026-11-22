# R01 "Same sky": sound

Rules: engine3/reels/SOUND_RULES.md (Nov 22). New sound for this Reel only, Runway Mirelo SFX 2 scoring the silent picture, never processed.

Picture: picture/R01_picture_silent.mp4 (stream copy of media/reels/G1/R01_same-sky.mp4, the "Whose day never looks like yours?" cut, 26.9 s). Scenes: clouds 0-8.7, leaf shadows on paper 8.7-16.9, night sky question 16.9-21.7, end card 21.7-26.9.

| File | Runway task | Checks |
|---|---|---|
| snd/R01_snd_scored_v1.wav | 3c5251fa-c49e-4e44-9472-dac347e221a7 | Rejected: hum 9-21 s (+21 to +25 dB), -39.0 LUFS |
| snd/R01_snd_scored_v2.wav | 387f8320-a895-4e24-b723-654d7bffc7c8 | Rejected: hum 9-27 s, worst +37 dB under the night sky, -33.8 LUFS |
| snd/R01_snd_text_v1.wav | 7443472d-9b3c-496a-8f85-e299277be83a | Passed. Text only (no picture). -22.3 LUFS, true peak -1.0 dBTP, hum tones at most -42 dB below the bed (R02's approved track: -26 dB). In preview |
| snd/R01_snd_scored_v3.wav | 584407d2-8f0e-419c-a495-f04045225af6 | Rejected: asked for a full continuous bed, but the leaf-shadow scene came back near-silent (-55.5 dBFS) with hum (+18.5 dB); -40.0 LUFS |

Pattern so far (R01, R02, R03): the hum turns up in the sparse, quiet passages (leaf shadows, night, question cards) and not where the bed is full (breeze, waves). Next try: a continuous full natural bed in every scene, no near-silent passage until the final fade.

After v3: scoring from the picture overrides the level asked for. The paper-and-shadow scene reads as a quiet indoor shot, so Mirelo makes it near-silent, and the hum lives in that near-silence. Next step needs a source that follows the prompt, not the picture.

Text-only v1 prompt: full continuous meadow soundscape, steady wind through leaves under the whole piece; 0-9 s morning birds nearby; 9-17 s fuller leaf rustle, a bird now and then; 17-24 s evening, full cricket chorus; 24-26.9 s fade to silence; starts softly from silence. Same negative prompt as v3.

Question card (Ryan, Nov 22): "Whose day never looks like yours?" / SEND THIS TO THEM replaced by "How is today meeting you?" / COMMENT ONE WORD. Only the card's words changed: same night-sky ground (Runway 2c5a0542), same timings, so the text-only sound fits unchanged. New picture: picture/R01_picture_silent_v6.mp4.

Preview: preview/R01_same-sky_v6_preview.mp4 (new card + text-only sound; not approved, not in Vista).

| snd/R01_snd_text_v2.wav | 4f97cd29-ff40-48c8-af6a-bae4e3be3814 | Ryan: text v1 had no audible birds or breeze (measured: steady hiss, over half its energy at 3-8 kHz) and should be softer. v2 asks for breeze swells and distinct birdsong. Result: birds and breeze present, but -22.6 LUFS (no softer: text mode lands near -22 LUFS whatever the prompt says), peak -0.7 dBTP, a bird burst at 25.5 s under the end card. Preview: preview/R01_same-sky_v7_preview.mp4 |

| snd/R01_music_v1.mp3 | 09b02eca-578a-429f-a589-92bfc7c8525a | Ryan, Nov 22: try soft house, instrumental, smooth transitions, a little more fun (the breeze sounded static and like water). Soft deep house, 118 BPM, Rhodes, gentle bass. Asked for 27 s; came back 37 s at -15 LUFS, quiet intro to 8 s, full groove from 8 s, its own fade only at 32-34 s. In the preview it is cut off at 26.9 s under the end card. Preview: preview/R01_same-sky_v8_music-preview.mp4 |
