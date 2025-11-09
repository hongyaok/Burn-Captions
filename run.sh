#!/bin/bash
set -euo pipefail

cd /app

# Adjust this single variable to point at a different input video inside the mounted workspace.
SOURCE_VIDEO="video/vid.mov"

OUTPUT_DIR="output"
FONT_SIZE="12"
VIDEO_STEM="$(basename "${SOURCE_VIDEO%.*}")"
CAPTIONS_PATH="${OUTPUT_DIR}/${VIDEO_STEM}.srt"
OUTPUT_VIDEO="${OUTPUT_DIR}/${VIDEO_STEM}_subtitled.mp4"

python3 get_captions.py \
	--video-path "${SOURCE_VIDEO}" \
	--output-dir "${OUTPUT_DIR}"

ffmpeg -y -i "${SOURCE_VIDEO}" -vf "subtitles='${CAPTIONS_PATH}':force_style='Fontsize=${FONT_SIZE}'" -c:a copy "${OUTPUT_VIDEO}"

echo "Final video written to ${OUTPUT_VIDEO}"
