from __future__ import annotations

import argparse
from pathlib import Path

import whisper
from moviepy.editor import VideoFileClip
from whisper.utils import get_writer


def extract_audio(video_path: Path, audio_path: Path) -> None:
	"""Extract the audio track from the source video so Whisper can transcribe it."""
	audio_path.parent.mkdir(parents=True, exist_ok=True)
	with VideoFileClip(str(video_path)) as video:
		audio_clip = video.audio
		if audio_clip is None:
			raise ValueError(f"No audio track found in {video_path}")
		audio_clip.write_audiofile(str(audio_path))
		audio_clip.close()


def transcribe_audio(audio_path: Path, output_dir: Path, model_name: str, language: str) -> Path:
	model = whisper.load_model(model_name)
	result = model.transcribe(str(audio_path), language=language)

	output_dir.mkdir(parents=True, exist_ok=True)
	writer = get_writer("srt", str(output_dir))
	writer(result, audio_path.stem)
	return output_dir / f"{audio_path.stem}.srt"


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Generate captions from a video file using Whisper.")
	parser.add_argument("--video-path", required=True, help="Path to the source video file.")
	parser.add_argument("--output-dir", default="output", help="Directory to store generated assets.")
	parser.add_argument("--model", default="medium", help="Whisper model size to load (e.g. tiny, base, small, medium, large).")
	parser.add_argument("--language", default="en", help="Language hint for Whisper transcription.")
	parser.add_argument("--keep-audio", action="store_true", help="Keep the intermediate extracted audio file.")
	return parser.parse_args()


def main() -> None:
	args = parse_args()

	video_path = Path(args.video_path).resolve()
	if not video_path.exists():
		raise FileNotFoundError(f"Video file not found: {video_path}")

	output_dir = Path(args.output_dir).resolve()
	audio_path = output_dir / f"{video_path.stem}.mp3"

	extract_audio(video_path, audio_path)
	srt_path = transcribe_audio(audio_path, output_dir, args.model, args.language)

	if not args.keep_audio and audio_path.exists():
		audio_path.unlink()

	print(f"Generated subtitles at {srt_path}")


if __name__ == "__main__":
	main()
