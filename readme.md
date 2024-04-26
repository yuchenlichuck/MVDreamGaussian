# Optimizing Text Prompts for Enhanced 3D Generation with DreamGaussian and MVDream: An Experimental Analysis

This repository is about NLP 804 Project: Optimizing Text Prompts for Enhanced 3D Generation with DreamGaussian and MVDream: An Experimental Analysis

based on the official implementation for [DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation](https://arxiv.org/abs/2309.16653).


## Install

```bash
pip install -r requirements.txt

# a modified gaussian splatting (+ depth, alpha rendering)
git clone --recursive https://github.com/ashawkey/diff-gaussian-rasterization
pip install ./diff-gaussian-rasterization

# simple-knn
pip install ./simple-knn

# nvdiffrast
pip install git+https://github.com/NVlabs/nvdiffrast/

# kiuikit
pip install git+https://github.com/ashawkey/kiuikit
```

Tested on:

- Ubuntu 22 with torch 2.0.1 & CUDA 11.7 on a Nvidia 3090.

## Usage


Text-to-3D DreamGaussian (Baseline):

```bash
### training gaussian stage
python main.py --config configs/text.yaml prompt="a photo of an icecream" save_path=icecream

### training mesh stage
python main2.py --config configs/text.yaml prompt="a photo of an icecream" save_path=icecream
```

Please check `./configs/text.yaml` for more options.

Text-to-3D Multi-view DreamGaussian (Proposed):

```bash
### training gaussian stage
python main.py --config configs/text_mv.yaml prompt="a plush toy of a corgi nurse" save_path=corgi_nurse

### training mesh stage
python main2.py --config configs/text_mv.yaml prompt="a plush toy of a corgi nurse" save_path=corgi_nurse
```

Please check `./configs/text_mv.yaml` for more options.



```bash
# run all image samples (*_rgba.png) in ./data
python scripts/runall.py --dir ./data --gpu 0

# run all text samples (hardcoded in runall_sd.py)
python scripts/runall_sd.py --gpu 0

# export all ./logs/*.obj to mp4 in ./videos
python scripts/convert_obj_to_video.py --dir ./logs
```

## Acknowledgement

This work is built on many amazing research works and open-source projects, thanks a lot:

- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) and [diff-gaussian-rasterization](https://github.com/graphdeco-inria/diff-gaussian-rasterization)
- [threestudio](https://github.com/threestudio-project/threestudio)
- [nvdiffrast](https://github.com/NVlabs/nvdiffrast)
- [dearpygui](https://github.com/hoffstadt/DearPyGui)
