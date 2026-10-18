import asyncio
import edge_tts
import subprocess
import os
import json
import numpy as np
import scipy.io.wavfile as wavfile
import scipy.signal as signal

VOICE = "en-US-AndrewMultilingualNeural"
SR = 48000
WORK_DIR = r"e:\MubarakTech\motiongraphics\mubaraktech_voice_reel_916"
CLIPS_DIR = os.path.join(WORK_DIR, "audio_clips")
SFX_DIR = r"e:\MubarakTech\motiongraphics\sfx"

os.makedirs(CLIPS_DIR, exist_ok=True)

SCRIPT_SEGMENTS = [
    {
        "id": 1,
        "scene": "s1",
        "text": "Steal the 2-minute voice memo replacing our client's $3,000 assistant.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.40
    },
    {
        "id": 2,
        "scene": "s2",
        "text": "Most agency founders lose two hours every single evening manually transcribing client audio notes and typing them into project management apps.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.35
    },
    {
        "id": 3,
        "scene": "s3",
        "text": "It's completely exhausting.",
        "pitch": "-6Hz",
        "rate": "-1%",
        "pause_after": 0.50
    },
    {
        "id": 4,
        "scene": "s4",
        "text": "You're driving home, a client drops an urgent voice message, and you promise yourself you'll deal with it tomorrow morning.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.30
    },
    {
        "id": 5,
        "scene": "s5",
        "text": "And then you forget.",
        "pitch": "-6Hz",
        "rate": "-2%",
        "pause_after": 0.50
    },
    {
        "id": 6,
        "scene": "s6",
        "text": "Three days later, the client is furious because nobody started the job.",
        "pitch": "-4Hz",
        "rate": "+3%",
        "pause_after": 0.50
    },
    {
        "id": 7,
        "scene": "s7",
        "text": "Here's what our clients at MubarakTech do instead.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.40
    },
    {
        "id": 8,
        "scene": "s8",
        "text": "They forward that 60-second audio note to a private WhatsApp bot.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.35
    },
    {
        "id": 9,
        "scene": "s9",
        "text": "In forty seconds, three things happen automatically.",
        "pitch": "-4Hz",
        "rate": "+3%",
        "pause_after": 0.45
    },
    {
        "id": 10,
        "scene": "s10",
        "text": "First, it extracts the deliverables and assigns them straight to your team with a hard deadline.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.40
    },
    {
        "id": 11,
        "scene": "s11",
        "text": "Second, it drafts a client recap for your one-tap review.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.40
    },
    {
        "id": 12,
        "scene": "s12",
        "text": "Third, it generates the Stripe invoice link automatically.",
        "pitch": "-4Hz",
        "rate": "+4%",
        "pause_after": 0.50
    },
    {
        "id": 13,
        "scene": "s13",
        "text": "Zero manual typing.",
        "pitch": "-5Hz",
        "rate": "+1%",
        "pause_after": 0.30
    },
    {
        "id": 14,
        "scene": "s14",
        "text": "Zero dropped deadlines.",
        "pitch": "-5Hz",
        "rate": "+1%",
        "pause_after": 0.50
    },
    {
        "id": 15,
        "scene": "s15",
        "text": "Stop paying a $3,000 assistant for tasks a smart automation finishes in seconds.",
        "pitch": "-4Hz",
        "rate": "+3%",
        "pause_after": 0.45
    },
    {
        "id": 16,
        "scene": "s16",
        "text": "Comment VOICE and I'll send you our exact template.",
        "pitch": "-4Hz",
        "rate": "+3%",
        "pause_after": 0.40
    },
    {
        "id": 17,
        "scene": "s17",
        "text": "Steal the 2-minute voice memo.",
        "pitch": "-5Hz",
        "rate": "-2%",
        "pause_after": 1.00
    }
]

def trim_silence(data, sr, threshold_db=-40):
    if data.ndim > 1:
        mono = data.mean(axis=1)
    else:
        mono = data
    abs_d = np.abs(mono.astype(float))
    max_v = np.max(abs_d)
    if max_v == 0:
        return data
    thresh = max_v * (10 ** (threshold_db / 20.0))
    above = np.where(abs_d > thresh)[0]
    if len(above) == 0:
        return data
    pad = int(sr * 0.05) # 50ms natural room decay
    start = max(0, above[0] - pad)
    end = min(len(data), above[-1] + pad)
    return data[start:end]

# SFX Synthesis functions for custom whooshes
def make_whoosh(dur=0.55, rise=True, pitch_low=300, pitch_high=2600):
    n = int(dur * SR)
    t = np.linspace(0, dur, n, endpoint=False)
    noise = np.random.rand(n) * 2 - 1
    if rise:
        f_center = pitch_low + (pitch_high - pitch_low) * (t / dur)**1.8
    else:
        f_center = pitch_high - (pitch_high - pitch_low) * (t / dur)**1.4
    env = np.sin(np.pi * (t / dur))**1.6
    q = 3.5
    filtered = np.zeros(n)
    block = 512
    for i in range(0, n, block):
        end = min(n, i + block)
        fc = f_center[i]
        b_low = max(60, fc / q)
        b_high = min(SR/2 - 100, fc * q)
        sos = signal.butter(2, [b_low, b_high], 'bandpass', fs=SR, output='sos')
        filtered[i:end] = signal.sosfilt(sos, noise[i:end])
    left = filtered * env * 0.7
    right = filtered * env * 0.7
    return np.stack([left, right], axis=1)

def load_wav_sample(path):
    if not os.path.exists(path):
        return None
    sr, data = wavfile.read(path)
    float_data = data.astype(np.float32)
    if float_data.max() > 1.0 or float_data.min() < -1.0:
        float_data = float_data / 32768.0
    if float_data.ndim == 1:
        float_data = np.column_stack([float_data, float_data])
    return float_data

async def generate_voice_clips():
    print("Generating voice clips with en-US-AndrewMultilingualNeural...")
    for seg in SCRIPT_SEGMENTS:
        raw_mp3 = os.path.join(CLIPS_DIR, f"clip_{seg['id']:02d}.mp3")
        comm = edge_tts.Communicate(seg["text"], VOICE, pitch=seg["pitch"], rate=seg["rate"])
        await comm.save(raw_mp3)

        raw_wav = os.path.join(CLIPS_DIR, f"clip_{seg['id']:02d}_raw.wav")
        subprocess.run(["ffmpeg", "-y", "-i", raw_mp3, "-ar", str(SR), "-ac", "1", raw_wav], capture_output=True, check=True)

        sr, data = wavfile.read(raw_wav)
        trimmed = trim_silence(data, sr)
        trim_wav = os.path.join(CLIPS_DIR, f"clip_{seg['id']:02d}.wav")
        wavfile.write(trim_wav, sr, trimmed)
        seg["dur"] = len(trimmed) / sr
        print(f"[{seg['id']:02d}] {seg['dur']:.2f}s | {seg['text'][:40]}...")

def assemble_master_audio():
    print("\nCalculating timeline offsets...")
    current_time = 0.20 # Start 0.2s in for smooth hook intro
    timeline = []
    
    for seg in SCRIPT_SEGMENTS:
        start_t = round(current_time, 2)
        end_t = round(start_t + seg["dur"], 2)
        timeline.append({
            "id": seg["id"],
            "scene": seg["scene"],
            "text": seg["text"],
            "start": start_t,
            "end": end_t,
            "duration": round(seg["dur"], 2)
        })
        current_time = end_t + seg["pause_after"]

    total_duration = round(current_time + 0.5, 2)
    print(f"Total Composition Duration: {total_duration}s")

    # Save timings.json
    timings_path = os.path.join(WORK_DIR, "timings.json")
    with open(timings_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_duration": total_duration,
            "voice": VOICE,
            "segments": timeline
        }, f, indent=2)
    print(f"Saved precise timings to: {timings_path}")

    # Assemble voice buffer
    total_samples = int(np.ceil(total_duration * SR))
    voice_track = np.zeros(total_samples, dtype=np.float32)

    for seg, item in zip(SCRIPT_SEGMENTS, timeline):
        trim_wav = os.path.join(CLIPS_DIR, f"clip_{seg['id']:02d}.wav")
        sr, data = wavfile.read(trim_wav)
        float_data = data.astype(np.float32) / 32768.0

        start_idx = int(round(item["start"] * SR))
        end_idx = min(total_samples, start_idx + len(float_data))
        chunk_len = end_idx - start_idx

        if chunk_len > 0 and start_idx < total_samples:
            # Gentle 15ms de-click fade
            fade_len = min(int(SR * 0.015), chunk_len // 4)
            if fade_len > 0:
                float_data[:fade_len] *= np.linspace(0, 1, fade_len)
                float_data[-fade_len:] *= np.linspace(1, 0, fade_len)
            voice_track[start_idx:end_idx] += float_data[:chunk_len]

    raw_voice_wav = os.path.join(CLIPS_DIR, "voice_assembled_raw.wav")
    wavfile.write(raw_voice_wav, SR, (voice_track * 32767).astype(np.int16))

    # Master voice with broadcast DSP chain:
    # 80Hz highpass rumble cut, warm chest body at 180Hz, de-box cut at 480Hz, clarity presence boost at 3.5kHz, smooth broadcast opto compression
    voice_master_wav = os.path.join(CLIPS_DIR, "voice_mastered.wav")
    dsp_chain = (
        "highpass=f=80,"
        "equalizer=f=180:t=q:w=1.2:g=2.2,"
        "equalizer=f=480:t=q:w=1.8:g=-1.8,"
        "equalizer=f=3500:t=q:w=1.2:g=2.4,"
        "equalizer=f=11000:t=q:w=1.0:g=1.2,"
        "acompressor=threshold=-16dB:ratio=2.6:attack=15:release=120:makeup=2.2"
    )
    subprocess.run([
        "ffmpeg", "-y", "-i", raw_voice_wav,
        "-af", dsp_chain,
        "-ar", str(SR), "-ac", "2",
        voice_master_wav
    ], check=True, capture_output=True)

    # Assemble Sound Effects (SFX) Track
    sfx_track = np.zeros((total_samples, 2), dtype=np.float32)

    def place_sfx(sound, t_sec, vol=1.0):
        if sound is None:
            return
        idx = int(round(t_sec * SR))
        end = min(total_samples, idx + len(sound))
        ln = end - idx
        if ln > 0 and idx < total_samples:
            sfx_track[idx:end] += sound[:ln] * vol

    # Load SFX files
    pop = load_wav_sample(os.path.join(SFX_DIR, "pop.wav"))
    snap = load_wav_sample(os.path.join(SFX_DIR, "snap.wav"))
    success = load_wav_sample(os.path.join(SFX_DIR, "success.wav"))
    chime = load_wav_sample(os.path.join(SFX_DIR, "chime.wav"))
    switch = load_wav_sample(os.path.join(SFX_DIR, "switch.wav"))
    tick = load_wav_sample(os.path.join(SFX_DIR, "tick.wav"))
    fill = load_wav_sample(os.path.join(SFX_DIR, "fill.wav"))

    # Place crisp SFX synchronized with visual keyframes:
    # 0.15s: Intro Whoosh
    place_sfx(make_whoosh(0.5, rise=False, pitch_low=200, pitch_high=1600), 0.15, 0.45)
    place_sfx(pop, 0.25, 0.5)

    for it in timeline:
        t = it["start"]
        sid = it["id"]

        # Scene transitions and card entrances
        if sid == 2: # Scene 2 Founder grind
            place_sfx(make_whoosh(0.45, rise=True, pitch_low=300, pitch_high=2000), t - 0.2, 0.4)
            place_sfx(switch, t + 0.1, 0.5)
        elif sid == 3: # Scene 3 Exhausting
            place_sfx(make_whoosh(0.5, rise=False, pitch_low=180, pitch_high=1400), t - 0.15, 0.4)
        elif sid == 4: # Scene 4 Driving home
            place_sfx(make_whoosh(0.4, rise=True, pitch_low=250, pitch_high=1800), t - 0.15, 0.35)
            place_sfx(pop, t + 0.2, 0.5)
        elif sid == 5: # Scene 5 And then you forget
            place_sfx(switch, t - 0.1, 0.5)
        elif sid == 6: # Scene 6 Three days later & Alerts
            place_sfx(make_whoosh(0.45, rise=False, pitch_low=400, pitch_high=2400), t - 0.2, 0.4)
            place_sfx(pop, t + 0.3, 0.6)
            place_sfx(pop, t + 0.7, 0.6)
            place_sfx(pop, t + 1.1, 0.6)
            place_sfx(pop, t + 1.5, 0.6)
        elif sid == 7: # Scene 7 Here's what MubarakTech does instead
            place_sfx(snap, t - 0.15, 0.7)
            place_sfx(make_whoosh(0.6, rise=True, pitch_low=300, pitch_high=2600), t - 0.1, 0.5)
            place_sfx(chime, t + 0.4, 0.5)
        elif sid == 8: # Scene 8 Forward to WhatsApp bot
            place_sfx(make_whoosh(0.45, rise=False, pitch_low=250, pitch_high=2000), t - 0.15, 0.4)
            place_sfx(switch, t + 0.3, 0.6) # Voice note sent
            place_sfx(tick, t + 0.9, 0.6)   # Typing indicator
            place_sfx(pop, t + 1.6, 0.7)    # Bot response pop
        elif sid == 9: # Scene 9 In forty seconds 3 things happen
            place_sfx(make_whoosh(0.4, rise=True, pitch_low=300, pitch_high=2200), t - 0.1, 0.4)
            place_sfx(chime, t + 0.3, 0.5)
        elif sid == 10: # Scene 10 Pillar 1 Extract
            place_sfx(make_whoosh(0.45, rise=True, pitch_low=350, pitch_high=2400), t - 0.15, 0.4)
            place_sfx(tick, t + 0.6, 0.6)
            place_sfx(tick, t + 1.1, 0.6)
            place_sfx(success, t + 1.6, 0.5)
        elif sid == 11: # Scene 11 Pillar 2 Recap
            place_sfx(make_whoosh(0.45, rise=True, pitch_low=350, pitch_high=2400), t - 0.15, 0.4)
            place_sfx(switch, t + 0.8, 0.5) # Cursor glide
            place_sfx(snap, t + 1.5, 0.7)   # 1-Tap button press
        elif sid == 12: # Scene 12 Pillar 3 Stripe invoice
            place_sfx(make_whoosh(0.45, rise=True, pitch_low=350, pitch_high=2400), t - 0.15, 0.4)
            place_sfx(chime, t + 0.5, 0.6)
            place_sfx(success, t + 1.2, 0.55)
        elif sid == 13: # Scene 13 Zero manual typing
            place_sfx(snap, t - 0.05, 0.8)
            place_sfx(fill, t + 0.1, 0.5)
        elif sid == 14: # Scene 14 Zero dropped deadlines
            place_sfx(snap, t - 0.05, 0.8)
            place_sfx(fill, t + 0.1, 0.5)
        elif sid == 15: # Scene 15 Stop paying $3K assistant
            place_sfx(make_whoosh(0.5, rise=False, pitch_low=200, pitch_high=1800), t - 0.15, 0.4)
        elif sid == 16: # Scene 16 Comment VOICE
            place_sfx(pop, t + 0.2, 0.7)
            place_sfx(chime, t + 0.4, 0.6)
        elif sid == 17: # Scene 17 Outro brand lockup
            place_sfx(make_whoosh(0.7, rise=True, pitch_low=250, pitch_high=2600), t - 0.1, 0.5)
            place_sfx(success, t + 0.5, 0.65)

    # Master mix: Mastered Voice + Mastered SFX (NO BGM, NO LOUD NOISE)
    sr_v, voice_master = wavfile.read(voice_master_wav)
    v_float = voice_master.astype(np.float32) / 32768.0

    min_len = min(len(v_float), len(sfx_track))
    final_mix = v_float[:min_len] * 1.05 + sfx_track[:min_len] * 0.75

    # Master soft peak limiter to prevent clipping
    peak = np.max(np.abs(final_mix))
    if peak > 0.95:
        final_mix = final_mix * (0.95 / peak)

    final_premaster = os.path.join(CLIPS_DIR, "final_premaster.wav")
    wavfile.write(final_premaster, SR, (final_mix * 32767).astype(np.int16))

    # Loudnorm master audio to broadcast standard -16 LUFS
    final_audio_master = os.path.join(WORK_DIR, "audio.wav")
    subprocess.run([
        "ffmpeg", "-y", "-i", final_premaster,
        "-af", "loudnorm=I=-16:LRA=7:tp=-1.0",
        "-ar", str(SR), "-ac", "2",
        final_audio_master
    ], check=True, capture_output=True)

    print(f"\n==========================================")
    print(f"SUCCESS: Master Audio built at:")
    print(f"{final_audio_master}")
    print(f"Duration: {total_duration}s")
    print(f"BGM: NONE (Clean Voice + Tailored SFX)")
    print(f"Voice: {VOICE} (Perfect English Cadence)")
    print(f"==========================================")

if __name__ == "__main__":
    asyncio.run(generate_voice_clips())
    assemble_master_audio()
