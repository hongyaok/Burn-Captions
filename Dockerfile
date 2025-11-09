FROM nvidia/cuda:12.9.0-runtime-ubuntu22.04

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# install ffmpeg and python and pip
RUN apt-get update && apt-get install -y ffmpeg python3 python3-pip

RUN pip3 install --upgrade pip

RUN uv pip install --system --no-cache-dir openai-whisper moviepy==1.0.3