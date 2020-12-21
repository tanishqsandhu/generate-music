"""Visualization tools."""
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shutil
import math
import os
from PIL import Image, ImageDraw

def save_video(foldername, songpath, songlen, num_steps, output):
    """Make video from given frames. Add audio appropriately."""
    num_steps_by_len = num_steps / songlen
    p = subprocess.Popen(['ffmpeg', '-f', 'image2', '-r', str(num_steps_by_len), '-i', '%d.png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2', 'movie.mp4'], cwd=foldername)
    p.wait()

    p = subprocess.Popen(['ffmpeg', '-i', '.'+ songpath, '-i', 'movie.mp4','-c', 'copy', '-map', '0:a', '-map', '1:v', output], cwd=foldername)
    p.wait()


def save_dance(states, songpath, duration, num_steps):
    """Save dance."""
    # Make folder if not already exists
    if not os.path.exists('./plots/'):
        os.makedirs('plots/')

    # Delete old items
    print("Starting file deletions")
    for item in os.listdir('./plots/'):
        delfile = os.path.join('./plots/', item)
        os.remove(delfile)
    print("File deletions complete")

    # Create dance video
    print("Creating dance video frames")
    for j in range(1, 20):
        # ****************** stick figure agent ******************
        shutil.copy("imgs/" + str(j) + '.png', 'plots/' + str(j) + '.png')

    # Save video
    save_video('./plots', songpath, duration, num_steps, 'song.mov')
