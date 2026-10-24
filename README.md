# TikTok: Die beliebtesten Flaggen der Welt

Kurzes, cleanes TikTok-Video (**ca. 20 Sekunden**, 9:16 Hochformat, 1080×1920).

## Inhalt der Animation
1. **Intro**: Saubere Weltkugel, um die ein weißes Flugzeug kreist
2. **Voiceover** (klare, clean Stimme):
   > „Die beliebtesten Flaggen der Welt, kennst du sie und ihre Länder?“
3. **Vier Flaggen** nacheinander mit cleanem weißem Punkt und Ländername darunter:
   - **Japan**
   - **Kanada**
   - **Frankreich**
   - **Deutschland**

   Der Ländername wird jeweils vorgelesen.

## Fertiges Video
Das gerenderte Video liegt hier im Repo unter `video/flags_tiktok.mp4` (siehe Releases oder Dateien).

## Selbst generieren
```bash
# Manim + ffmpeg benötigt
python -m manim -ql --resolution 1080,1920 tiktok_flags.py FlagsTikTok
# Audio (mit Voice-TTS erzeugt) + Video muxen
ffmpeg -i media/.../flags_silent.mp4 -i full_audio.mp3 -c:v libx264 -c:a aac -shortest flags_tiktok.mp4
```

## Quellen
- Flaggen: Public Domain (flagcdn / Wikimedia)
- Animation: Manim Community
- Stimme: Multilingual TTS (clean Female Voice „Ara“)

Viel Spaß beim Posten auf TikTok! 🌍✈️
