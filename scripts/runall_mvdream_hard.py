import os
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', default=0, type=int)
args = parser.parse_args()

prompts = [
('book', 'A detailed image of an antique hardcover book with ornate golden embossing on the spine and a slightly worn cover, lying open to reveal crisp, aged pages filled with classic typeface, literature'),
('pen', 'An elegantly crafted fountain pen with a glossy ebony barrel and a fine gold nib, depicted in the act of writing flowing script on a piece of parchment, writing instrument'),
('apple', 'A hyper-realistic image of a shiny red apple, complete with a perfectly detailed stem and a single leaf, the surface reflecting a subtle light, fruit'),
('keyboard', 'A mechanical keyboard with individual RGB lighting under each key, designed for precision typing and gaming, shown in a dimly lit room enhancing the colorful backlighting, technology'),
('mouse', 'An ergonomic optical computer mouse tailored for gaming, featuring customizable side buttons and a glowing RGB light strip, technology'),
('chair', 'A modern office chair with high-tech mesh fabric for breathability, adjustable armrests, and lumbar support, designed for comfort and efficiency in a stylish office setting, furniture'),
('desk', 'A spacious wooden desk with a smooth finish and minimalist design, equipped with compartments for organizing, set up in a well-lit study room, furniture'),
('lamp', 'A sleek desk lamp with an LED light, articulated arm, and touch-sensitive control panel that provides adjustable brightness for a home office environment, lighting'),
('backpack', 'A durable hiking backpack made from high-strength, water-resistant material, featuring multiple compartments, hydration pack access, and reflective safety strips, ideal for outdoor adventures, equipment'),
('bicycle', 'A rugged mountain bicycle with a lightweight aluminum frame, hydraulic disc brakes, and aggressive tread on tires, captured on a rocky trail with a backdrop of mountains, vehicle'),
('helmet', 'A high-performance cycling helmet with aerodynamic design, integrated ventilation holes, and a visor for sun protection, essential for road safety, protective gear'),
('glove', 'A pair of premium leather gloves, intricately stitched and lined with soft fleece for warmth, shown gripping a wooden walking stick, apparel'),
('boot', 'A pair of robust hiking boots crafted from waterproof leather with reinforced soles for superior traction on uneven terrain, essential for mountain trekking, footwear'),
('scarf', 'A luxurious woolen scarf in a deep burgundy color, woven with a subtle herringbone pattern, draped elegantly over a coat in a wintery scene, accessory'),
('hat', 'A classic baseball cap made from durable fabric, featuring a curved brim and an adjustable strap at the back, embroidered with a popular sports team logo, headwear'),
('ball', 'A professional soccer ball designed with pentagonal and hexagonal panels, stitched together to ensure optimal performance and durability on a grassy field, sports equipment'),
('bat', 'A handcrafted wooden baseball bat, polished to a high sheen, shown in mid-swing hitting a baseball in an action-packed game scenario, sports equipment'),
('guitar', 'An acoustic guitar with a mahogany body and spruce top, strung with high-quality nylon strings, resting on a wooden stand in a cozy room filled with musical memorabilia, musical instrument'),
('piano', 'A majestic grand piano finished in glossy black lacquer, with the lid open to show its intricate internal strings and hammers, set on a concert stage under a spotlight, musical instrument'),
('drum', 'A professional bass drum as part of a larger drum set, featuring a high-gloss finish and chrome hardware, captured with sticks mid-air, ready to strike in a rhythmic beat, musical instrument'),
('violin', 'A classic violin crafted from aged wood, with a polished finish and fine strings, accompanied by a bow, resting on a velvet-lined case, highlighting its elegance and readiness for a performance, musical instrument'),
('trumpet', 'A brass trumpet with a polished, reflective surface, showcasing the intricate valves and mouthpiece, set against a backdrop of sheet music, ready for a jazz performance, musical instrument'),
('saxophone', 'An alto saxophone with a golden finish, detailed engraving on the bell, and leather pads, displayed in a music room setting with soft lighting, emphasizing its sleek design, musical instrument'),
('microphone', 'A high-end studio microphone with a large diaphragm and pop filter, mounted on a boom stand in a soundproof recording studio, essential for capturing clear and detailed vocal performances, audio equipment'),
('speaker', 'A portable Bluetooth speaker with a durable, waterproof exterior and powerful audio drivers, shown playing music on a sandy beach at sunset, audio equipment'),
('laptop', 'A sleek modern laptop with a high-resolution display and a thin, lightweight design, featuring cutting-edge hardware optimized for professional software applications, shown on a clean, minimalist desk, technology'),
('tablet', 'A state-of-the-art digital tablet with a large, vibrant screen, displaying a creative drawing app, held by an artist in a studio filled with natural light, technology'),
('smartphone', 'A latest model smartphone featuring an edge-to-edge display with no bezels, a triple-camera system on the back, and facial recognition technology, shown in a hand against a cityscape, technology'),
('camera', 'A professional digital camera with a large sensor and a telephoto lens, mounted on a tripod overlooking a scenic landscape at golden hour, capturing stunning details, technology'),
('telescope', 'An astronomical telescope set against the backdrop of a starry night sky, with a detailed viewfinder and precision adjustment knobs, aimed at uncovering the mysteries of distant galaxies, scientific instrument'),
('clock', 'A vintage wall clock with Roman numerals and ornate hands, housed in a dark wooden frame, hanging on a pastel-colored wall in a classic living room setting, home decor'),
('watch', 'A luxury wristwatch with a stainless steel band, sapphire crystal face, and a sophisticated chronograph display, shown close-up on a wrist dressed in a fine suit, accessory'),
('bracelet', 'An elegant silver bracelet with intricate links and a delicate clasp, adorned with small diamonds that catch the light beautifully, displayed on a velvet cushion, jewelry'),
('necklace', 'A stunning gold necklace featuring a fine chain and a pendant with an elaborate design, showcased on a mannequin with an evening gown, jewelry'),
('ring', 'A close-up image of a diamond ring with a large, radiant-cut stone set in a platinum band, surrounded by smaller pavé diamonds, presented in an open jewelry box, luxury item'),
('earring', 'A pair of hoop earrings made from polished gold, each adorned with tiny, sparkling gemstones, displayed against a dark, textured background to highlight their elegance, jewelry'),
('sunglasses', 'A pair of aviator sunglasses with polarized lenses and a metal frame, resting on a rocky surface under bright sunlight, fashion accessory'),
('binoculars', 'A pair of high-performance binoculars with adjustable zoom and focus, used for bird watching, shown in a natural setting with a clear view of distant mountains, outdoor equipment'),
('map', 'A detailed world map with colorful political boundaries and major cities marked, spread out on a table with a magnifying glass and other travel essentials, educational tool'),
('compass', 'An old-fashioned orienteering compass with a brass casing and a floating needle, lying next to a map on a wooden table in a forest setting, navigation tool'),
('flashlight', 'A robust LED flashlight emitting a powerful beam of light, designed for durability and long battery life, shown illuminating a dark path at night, safety equipment'),
('tent', 'A high-quality camping tent set up in a serene forest location, with a waterproof canopy and room for two, shown at dusk with a cozy interior glow, outdoor shelter'),
('sleeping bag', 'A mummy sleeping bag designed for extreme temperatures, shown partially unzipped and inviting, laid out inside a tent with a view of the starry sky, camping gear'),
('fireplace', 'A rustic stone fireplace with a roaring fire, providing warmth and light in a cozy cabin setting, the mantelpiece decorated with family photos and vintage ornaments, home comfort'),
('grill', 'A charcoal grill in action, with smoky flavors rising from cooking steaks, depicted in a summer backyard setting with friends gathered around, cooking equipment'),
('kettle', 'A stainless steel kettle with a sleek, modern design, boiling water with visible steam, placed on an induction cooktop in a contemporary kitchen, kitchen appliance'),
('mug', 'A ceramic coffee mug filled with steaming hot coffee, the surface adorned with a quaint café logo, positioned on a rustic wooden table alongside a croissant, beverage container'),
('plate', 'A porcelain plate with a delicate floral pattern, set on a dining table with silver cutlery and crystal glasses, ready for an elegant meal, tableware'),
('bowl', 'A ceramic soup bowl filled with homemade vegetable soup, steam rising, accompanied by a spoon and fresh bread on a kitchen counter, kitchenware'),
('spoon', 'A stainless steel spoon with a polished finish, designed with an ergonomic handle, resting beside a bowl of cereal with milk, captured in the morning light, kitchen utensil')
]

for name, prompt in prompts:
    hard_name=name+"_hard"
    print(f'======== processing {hard_name} ========')
    # first stage
    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} python main.py --config configs/text_mv.yaml prompt="{prompt}" save_path={hard_name}')
    # second stage
    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} python main2.py --config configs/text_mv.yaml  prompt="{prompt}" save_path={hard_name}')
    # export video
    mesh_path = os.path.join('logs', f'{hard_name}.obj')
    os.makedirs('videos_hard', exist_ok=True)
    os.system(f'python -m kiui.render {mesh_path} --save_video videos_hard/{hard_name}.mp4 --wogui')