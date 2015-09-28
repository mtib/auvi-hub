#!/bin/bash
cd $(dirname $0)
ffmpeg -y -f concat -i pr_d.txt output/pr_output.mp4