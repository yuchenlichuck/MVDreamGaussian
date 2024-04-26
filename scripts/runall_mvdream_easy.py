import os
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', default=0, type=int)
args = parser.parse_args()

prompts = [
('book', 'a hardcover book'),
('pen', 'a fountain pen'),
('apple', 'a shiny red apple'),
('keyboard', 'a mechanical keyboard'),
('mouse', 'an optical computer mouse'),
('chair', 'a modern office chair'),
('desk', 'a wooden desk'),
('lamp', 'a desk lamp'),
('backpack', 'a hiking backpack'),
('bicycle', 'a mountain bicycle'),
('helmet', 'a cycling helmet'),
('glove', 'a pair of leather gloves'),
('boot', 'a pair of hiking boots'),
('scarf', 'a woolen scarf'),
('hat', 'a baseball cap'),
('ball', 'a soccer ball'),
('bat', 'a baseball bat'),
('guitar', 'an acoustic guitar'),
('piano', 'a grand piano'),
('drum', 'a bass drum'),
('violin', 'a classic violin'),
('trumpet', 'a brass trumpet'),
('saxophone', 'an alto saxophone'),
('microphone', 'a studio microphone'),
('speaker', 'a portable speaker'),
('laptop', 'a modern laptop'),
('tablet', 'a digital tablet'),
('smartphone', 'a latest model smartphone'),
('camera', 'a digital camera'),
('telescope', 'an astronomical telescope'),
('clock', 'a wall clock'),
('watch', 'a wristwatch'),
('bracelet', 'a silver bracelet'),
('necklace', 'a gold necklace'),
('ring', 'a diamond ring'),
('earring', 'a pair of hoop earrings'),
('sunglasses', 'a pair of aviator sunglasses'),
('binoculars', 'a pair of binoculars'),
('map', 'a world map'),
('compass', 'an orienteering compass'),
('flashlight', 'a LED flashlight'),
('tent', 'a camping tent'),
('sleeping bag', 'a mummy sleeping bag'),
('fireplace', 'a stone fireplace'),
('grill', 'a charcoal grill'),
('kettle', 'a stainless steel kettle'),
('mug', 'a ceramic coffee mug'),
('plate', 'a porcelain plate'),
('bowl', 'a ceramic soup bowl'),
('spoon', 'a stainless steel spoon'),

]

for name, prompt in prompts:
    easy_name=name+"_easy"
    print(f'======== processing {easy_name} ========')
    # first stage

    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} python main.py --config configs/text_mv.yaml prompt="{prompt}" save_path={easy_name}')
    # second stage
    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} python main2.py --config configs/text_mv.yaml  prompt="{prompt}" save_path={easy_name}')
    # export video
    mesh_path = os.path.join('logs', f'{easy_name}.obj')
    os.makedirs('videos_easy', exist_ok=True)
    os.system(f'python -m kiui.render {mesh_path} --save_video videos_easy/{easy_name}.mp4 --wogui')