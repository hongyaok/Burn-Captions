# Burn Captions

Generate subtitles and burn them into a video using whisper.

## Use case
- Input frame:
   ![Input video frame](images/input.png)
- Output frame with burned captions:
   ![Output video frame with subtitles](images/output.png)

## Prerequisites
- Docker 24+ with `docker compose` plugin
- NVIDIA GPU drivers and NVIDIA Container Toolkit

## Quick Start
1. Clone the repository and change into it:
   ```bash
   git clone https://github.com/hongyaok/Burn-Captions.git
   cd Burn-Captions
   ```
2. Place your source video inside the `video/` directory (create it if it does not exist). Example: `video/my_clip.mov`.
3. Open `run.sh` and update the `SOURCE_VIDEO` variable so it points to your file, e.g.
   ```bash
   SOURCE_VIDEO="video/my_clip.mov"
   ```
4. Start the pipeline:
   ```bash
   docker compose up --build
   ```

## Outputs
- Subtitles: `output/<video-name>.srt`
- Final video with burned captions: `output/<video-name>_subtitled.mp4`

Repeat the steps above for additional videos—only change the `SOURCE_VIDEO` value in `run.sh`.

