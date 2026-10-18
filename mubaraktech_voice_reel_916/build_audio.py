import asyncio
import edge_tts
import json
import subprocess
import os

SCRIPT = """Steal the 2-minute voice memo replacing our client's $3,000 assistant.
Most agency founders lose two hours every single evening manually transcribing client audio notes and typing them into project management apps.
It's completely exhausting.
You're driving home, a client drops an urgent voice message, and you promise yourself you'll deal with it tomorrow morning.
And then you forget.
Three days later, the client is furious because nobody started the job.
Here's what our clients at MubarakTech do instead.
They forward that 60-second audio note to a private WhatsApp bot.
In forty seconds, three things happen automatically.
First, it extracts the deliverables and assigns them straight to your team with a hard deadline.
Second, it drafts a client recap for your one-tap review.
Third, it generates the Stripe invoice link automatically.
Zero manual typing.
Zero dropped deadlines.
Stop paying a $3,000 assistant for tasks a smart automation finishes in seconds.
Comment VOICE and I'll send you our exact template.
Steal the 2-minute voice memo."""

OUT_DIR = r"e:\MubarakTech\motiongraphics\mubaraktech_voice_reel_916"
VOICE_RAW = os.path.join(OUT_DIR, "voice_raw.mp3")
VOICE_WAV = os.path.join(OUT_DIR, "voice.wav")
MUSIC_BED = r"e:\MubarakTech\motiongraphics\pieces\deep-ocean-pulse\renders\stem-music.wav"
AUDIO_MASTER = os.path.join(OUT_DIR, "audio.wav")
TIMINGS_JSON = os.path.join(OUT_DIR, "timings.json")

async def generate_voice():
    print("Generating neural voiceover with en-US-ChristopherNeural...")
    comm = edge_tts.Communicate(SCRIPT, "en-US-ChristopherNeural", rate="+22%", pitch="-1Hz")
    sentences = []
    
    with open(VOICE_RAW, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                t_start = chunk["offset"] / 10000000.0
                dur = chunk["duration"] / 10000000.0
                sentences.append({
                    "start": round(t_start, 2),
                    "end": round(t_start + dur, 2),
                    "duration": round(dur, 2),
                    "text": chunk["text"]
                })
                
    with open(TIMINGS_JSON, "w", encoding="utf-8") as f:
        json.dump(sentences, f, indent=2)
    print(f"Captured {len(sentences)} sentence boundaries.")
    
    # Convert voice to 48kHz WAV
    subprocess.run([
        "ffmpeg", "-y", "-i", VOICE_RAW,
        "-af", "highpass=f=80,lowpass=f=12000,loudnorm=I=-16:TP=-1.5:LRA=9",
        "-ar", "48000", "-ac", "2",
        VOICE_WAV
    ], check=True)
    
    # Get voice duration
    probe = subprocess.check_output([
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
        "-of", "csv=p=0", VOICE_WAV
    ]).decode().strip()
    v_dur = float(probe)
    print(f"Voice duration: {v_dur:.2f}s")
    
    # Master duration target = round to nearest clean frame duration, or v_dur + 1.2s padding
    target_dur = round(v_dur + 1.5, 2)
    print(f"Master target duration: {target_dur:.2f}s")
    
    # Mix voice + stem-music with ducking like deep_ocean_pulse_60s_audio_master
    # Voice at 1.0 vol, Music at 0.18 vol (-15dB), with gentle fade-out at end
    filter_complex = (
        f"[0:a]volume=1.0[voice];"
        f"[1:a]atrim=0:{target_dur},volume=0.20,afade=t=out:st={target_dur-2.0}:d=2.0[music];"
        f"[voice][music]amix=inputs=2:duration=first:dropout_transition=2[out]"
    )
    
    subprocess.run([
        "ffmpeg", "-y",
        "-i", VOICE_WAV,
        "-i", MUSIC_BED,
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-ar", "48000", "-ac", "2",
        AUDIO_MASTER
    ], check=True)
    
    print(f"Master audio generated: {AUDIO_MASTER}")

if __name__ == "__main__":
    asyncio.run(generate_voice())
