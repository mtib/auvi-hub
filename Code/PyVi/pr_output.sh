#!/bin/bash
cd $(dirname $0)
ffmpeg -y -f concat -i pr_o.txt output/pr_output.mp4
#ffmpeg -y -f concat -i pr_o_f.txt -c copy output/pr_output_funktion.mp4
#ffmpeg -y -r 0.25 -f concat -i pr_o_final.txt output/pr_output_funktion.mp4
