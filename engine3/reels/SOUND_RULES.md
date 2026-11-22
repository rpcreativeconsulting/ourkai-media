oürkai Reels: defaults, sound and Runway rules

REEL DEFAULTS (approved by Ryan, Nov 18, 2026, Reel 1 "Same sky")
- Format: 9:16, 1080 × 1920, for Instagram and Facebook, unless Ryan asks for another size. Text stays out of the top 280 px and bottom 420 px and 96 px from the sides. (A 4:5 cut-down only for a paid feed ad.)
- Length: 20–30 s. Hook on screen in the first second. Three to five beats, one line each. The on-screen type is the caption (most people watch muted).
- Type: the locked engine3 fonts. Kicker JetBrains Mono caps in the soft grey with a short gold rule; lines in Fraunces italic (light) with Source Serif body; calls to action in gold JetBrains Mono caps with no full stop (SEND THIS TO THEM, COMING SOON TO THE APP STORE).
- Pinyin: always set in Source Serif (italic for emphasis). Fraunces has no third-tone marks (ǎ ǐ ǒ ǔ) and draws them in the wrong place.
- Pictures: slow Runway clips animated from our own approved stills (image first, then 5 s at 9:16), slowed and cross-faded. Metaphor, not illustration, as the visual style doc says. Busy pictures get a soft dark fade at the bottom so the type reads.
- Every beat must show its own line (Ryan, Nov 18). If the words say "Water puts out Fire", the picture shows water putting out fire (rain dimming an ember), not just water. Check each line against its picture before cutting.
- No weekday words in a Reel or its caption (Ryan, Nov 22). "Whose Tuesday never looks like yours?" went out on a Sunday and read as a mistake. Say "day", not a named day, unless the Reel is dated to that day.
- Ending: the question on its own card over a ground that moves or slowly pushes in, then the built end card. Keep moving grounds (ripples, mist) below the text for the whole card.
- Question grounds (Ryan, Nov 18): never the same ground twice in a row, and the ground must carry the Reel's own idea (metaphor, not decoration). One use per Reel; the matrix Assets sheet says where each has been used. The set so far:
  - night sky just after dusk (R01, "Same sky": the same sky, at night)
  - dark hand-troweled plaster (R02, "Light needs shadow": the wall in shadow)
  - dark rammed earth (R03, "Which element is your center?": Earth holds the center)
  - charred cedar, darkened for type (R04 opening: wood that fed fire)
  - two sets of ripples meeting on dark water, animated (R04 Your turn: two charts meeting; the Vibes picture, reuse for Vibes and Pairs pieces)
  - spares: smoked oak (Wood chapter, spring), black linen (winter Reel), water-worn basalt, architectural slate (retired after heavy use; rest it)
  Make new ones with the same recipe: extreme close-up of a real dark material, soft raking light from the upper left, very dark and even, calm, no text.
- End card: built, not generated (AI end clips had rendering issues and are retired). Plain near-black #0e0d0b, the official vertical lockup with tagline (logos/ourkai-lockup-vertical-tagline-gold.svg) fading in, NO glow, and the ask beneath in gold mono caps: COMING SOON TO THE APP STORE (after launch: the post-launch ask). One shared end card for every Reel (the picture only; its sound is new for every Reel, see below). Script: engine3/reels/endcard.py.
- Sound: natural soundscapes, NOT music, generated clean and never processed. See below.
- Build: each Reel has its own folder in the ourkai-media repo, engine3/reels/R##/ with cards.py (type cards) and build.sh (ffmpeg cut); copy the last Reel's folder and change the lines, grounds and timings. Never copy its audio. Drawn diagrams (like the five-element cycle in R04) are rendered frame by frame in the brand fonts and laid over the clips; move a clip's subject out from under a diagram (feathered offset) rather than covering it.
- Names: R##_slug.mp4 (R01_same-sky.mp4), saved in the repo at media/reels/G#/. The Reels sheet of the matrix holds stage, caption, hashtags, file and notes.

THE FEEL IN ONE LINE
Meditation, not movie trailer. Soft, flowing, natural. The sound should feel like breathing slowly in a quiet room with a window open.

The sound follows the picture. If the video is still water at dawn, the sound is still water at dawn. Nothing in the sound should be bigger, faster or darker than what is on screen.

SOUND RULES (Ryan, Nov 22; replaces the Nov 18 mixing rules and the clean_audio.py step)

1. Clean from the start. No cleanup.
- Processing a generated bed breaks it. No notch filters, no EQ, no high-pass, no denoise, no loudness normalisation, no compression, no fades, no trims, no cross-fades, no layering or mixing two beds together, no speed or pitch change. engine3/reels/clean_audio.py is retired.
- Every quality the sound needs (how loud, how soft, how it starts and ends, what it contains) is written into the prompt and fixed at generation.
- If a bed is wrong in any way (hum, too loud, a sudden sound, the wrong mood, the wrong length), it is regenerated with a better prompt. It is never repaired.

2. New sound for every piece of content. No reuse.
- Every Reel, Story and video gets its own new sound, generated for it. No bed is used twice: not in another Reel, not in a Story, not in a re-cut or ad version of a different piece.
- A re-cut of the same Reel (v2, v3) may keep its own beds only if the picture timing is unchanged; if the timing changes, generate new beds at the new lengths.
- Every bed is logged once in the matrix Assets sheet (task or generation id, Reel, scene, length). The log is checked before any build so nothing is used twice.
- Runway video clips come back with their own generated audio: never use it (generateAudio false).

3. Where sound is made (Ryan, Nov 22): Runway only. ElevenLabs is not used for Reels or social.
- Default: Runway Mirelo SFX 2 (mirelo-sfx-2) scores the finished, silent picture and returns one sound track for the whole Reel, matched to it scene by scene. Output format wav. About 2 credits per second (a 27 s Reel is about 54 credits).
- The silent picture is a stream copy of the cut (video copied, no re-encode), committed to the Reel's folder in ourkai-media at engine3/reels/R##/picture/R##_picture_silent.mp4, and given to Runway by its public CDN link: https://cdn.jsdelivr.net/gh/rpcreativeconsulting/ourkai-media@<branch>/engine3/reels/R##/picture/R##_picture_silent.mp4
- The finished track is committed to engine3/reels/R##/snd/ as delivered, with its prompt and task id in engine3/reels/R##/sound.md. Git is the record of every Reel's sound, so reuse is easy to spot.
- Fallback: Runway sound effects (sound-effects), one bed per scene at its exact length. Their beds have carried an electrical hum; a bed with hum is regenerated, never filtered.


4. How sound is placed (the only thing done to it).
- With Mirelo: the one track sits under the whole Reel from frame 1, as delivered.
- With the fallback: one bed per scene, generated at the scene's exact length, with its own fade in and fade out written into the prompt. Beds are placed end to end on the timeline under their scenes. Where two scenes share a sound, generate one bed for both at their combined length.
- The question card and end card share one bed of their own (near-silence, see the templates), generated at their combined length, fading to silence by the last frame.
- Beds are put into the video as generated. If the file format has to change for Instagram (AAC in the mp4), that is one straight encode at 48 kHz, 256 kbps, with no filters. Nothing else touches the audio.

5. Check, don't fix. Measurement only; the file is never changed by the check.
- Loudness: integrated −26 to −18 LUFS, true peak no higher than −1 dBTP (ffmpeg ebur128, measure only).
- Hum: no steady tone at 50, 60, 100, 120 Hz or their multiples, no sub-bass drone (spectrum check, measure only).
- Length: within 0.1 s of the scene it sits under.
- Fails any check: regenerate with the prompt adjusted (quieter, softer, more distant, fewer sources), never filter.

SOUND PROMPT TEMPLATE (Runway Mirelo SFX 2, scoring the silent picture)

Settings: model mirelo-sfx-2 · video = the silent picture's CDN link · duration = the Reel's exact length · format wav · one task (never re-run the same request).

promptText, in this order:
1. One line for the whole piece: "A calm natural soundscape that follows the picture from <start> into <end>."
2. One line per scene, with its times: "<from> to <to> seconds, <what is on screen>: <its sound source, the space, how far away>." Sources from SOUND FOR EACH SCENE below.
3. The question card and end card: "<from> to <end> seconds, a still dark card with words, then a logo on black: almost silent <air or room tone that fits the Reel's idea>, fading to complete silence by the last second." Change the detail for each Reel; never reuse the wording.
4. Level, every time: "Very quiet throughout, soft and sparse, gentle and even, like a clean natural field recording. Begins softly from silence."

negativePrompt, every time: "music, melody, tones, hum, buzz, electrical drone, low rumble, sub-bass, voices, speech, footsteps, impacts, whooshes, risers, sudden or loud sounds, wind gusts, thunder"

Fallback (Runway sound-effects, one bed per scene): source first, then the space, then "very quiet, soft and sparse, natural field recording, fades in from silence and fades out to silence". Short, one sound per bed; duration = the scene's exact length.

SOUND FOR EACH SCENE (sources for line 1 of the template)
- Water (ocean, rain, mist): soft rain, slow waves, a stream.
- Wood (trees, vines, forest): wind in leaves, birds at dawn.
- Fire (sun, candle, ember): a candle or fire crackling quietly; rain on embers is a soft hiss.
- Earth (mountain, soil, garden): open air, a soft breeze over grass, drips after rain.
- Metal (ore, jewel, steel, stone): still air, a faint cool wind, stone room tone.
- Sky and light: morning birds at a distance, a light breeze.
- Rooms and doorways: a light breeze, birds faint outside, a curtain moving.
- Night: quiet night air, crickets very faint.

NEVER
- No music beds, no trending audio, no songs.
- No epic or trailer sound: no booms, impacts, risers or whooshes.
- No voices or words. No gongs, no clichéd "oriental" sound.
- No sound that moves faster or louder than the picture.
- No hum, buzz or drone. A bed with any is regenerated, never filtered.
- No processing of any kind after generation (rule 1).
- No bed used in more than one piece of content (rule 2).

CHECK BEFORE A REEL GOES OUT
1. Close your eyes. Does it feel calm, like a walk in nature?
2. Does each sound match what is on screen, scene by scene?
3. Any music, beat, impact, voice or sudden sound? If yes, it does not go out.
4. Was the sound generated new for this Reel, committed with its sound.md, logged once in Assets, and left unprocessed? Do the loudness, hum and length measurements pass? Listen on a phone at full volume, especially on the quiet question card and end card.
5. Is the question ground new for this Reel and true to its idea?
6. Does every picture show the line written over it?
7. Does any line or caption name a weekday? If so, change it to "day".

oürkai working rules for Runway: save credits, no duplicates

BEFORE ANYTHING IS GENERATED
1. Show the plan first: what, how long, the estimated credits. Wait for approval for anything beyond small sound effects and still grounds.
2. Check existing assets first (the matrix Assets sheet, Runway recent assets) for pictures. Never make the same picture twice. Sound is the exception: it is always new (sound rule 2).
3. Ask one question if the request is unclear.

HOW MANY
4. One output per request. No variations unless the request says how many.
5. One shot at a time.
6. Never repeat a generation that was already approved, rejected or still running.

ORDER OF WORK (cheapest first)
7. Make the still image first. Check it (and its fit with the type) before animating.
8. Only then animate it: 5 seconds, 9:16, 720p for drafts, with generated audio off.
9. Upscale only the clip that is approved as final.
10. Use the cheaper model for tests.
11. Sound last: once the cut and its timings are locked, commit the silent picture and score it with Mirelo.

WHEN SOMETHING GOES WRONG
12. A result with text, letters, logos, people, faces or hands, or anything off-brand: say so and stop.
13. Stop after two failed tries on the same shot or bed and suggest one prompt change.
14. A small picture fix (light, speed, crop) is an edit, not a new generation. A sound fix is always a new generation with a changed prompt, never an edit.

NAMING AND TRACKING
15. Name every asset by its shot: R1-A-v1 (Reel 1, Shot A, first version); beds R1-snd-A-v1. Log every Runway task id in the matrix Assets sheet and in the Reel's sound.md in git.
