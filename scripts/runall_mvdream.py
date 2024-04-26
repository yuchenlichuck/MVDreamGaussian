import os
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', default=0, type=int)
args = parser.parse_args()

prompts = [

    ('boy', 'a nendoroid of a chibi cute boy'),
    ('horse', 'a DSLR photo of a horse'),
    ('squirrel_guitar', 'a DSLR photo of a squirrel playing guitar'),
    ('robot', 'a human-like full body robot'),

    ('strawberry', 'a ripe strawberry'),
    ('cactus_pot', 'a small saguaro cactus planted in a clay pot'),
    ('hamburger', 'a delicious hamburger'),
    ('icecream', 'an icecream'),
    ('tulip', 'a blue tulip'),
    ('pineapple', 'a ripe pineapple'),
    ('goblet', 'a golden goblet'),
    ('squitopus', 'a squirrel-octopus hybrid'),
    ('astronaut', 'Michelangelo style statue of an astronaut'),
    ('teddy_bear', 'a teddy bear'),
    ('corgi_nurse', 'a plush toy of a corgi nurse'),
    ('teapot', 'a blue and white porcelain teapot'),
    ('skull', "a human skull"),
    ('penguin', 'a penguin'),
    ('campfire', 'a campfire'),
    ('donut', 'a donut with pink icing'),
    ('cupcake', 'a birthday cupcake'),
    ('pie', 'shepherds pie'),
    ('cone', 'a traffic cone'),
    ('schoolbus', 'a schoolbus'),
    ('avocado_chair', 'a chair that looks like an avocado'),
    ('glasses', 'a pair of sunglasses'),
    ('potion', 'a bottle of green potion'),
    ('chalice', 'a delicate chalice'),
('oak_tree', 'a majestic oak tree'),
('sailboat', 'a small sailboat on a calm lake'),
('chocolate_bar', 'a partially unwrapped chocolate bar'),
('fountain_pen', 'an elegant fountain pen'),
('viking_helmet', 'a Viking helmet with intricate designs'),
('sneakers', 'a pair of brightly colored sneakers'),
('wizard_hat', 'a tall, pointed wizard hat with stars'),
('sphinx_statue', 'a miniature Sphinx statue'),
('robot_dog', 'a futuristic robot dog'),
('diamond_ring', 'a sparkling diamond ring'),
('bookshelf', 'a wooden bookshelf filled with books'),
('saxophone', 'a golden saxophone'),
('lighthouse', 'a lighthouse by the sea at sunset'),
('cherry_blossom_tree', 'a cherry blossom tree in full bloom'),
('treasure_chest', 'an old treasure chest overflowing with jewels'),
('hot_air_balloon', 'a colorful hot air balloon in the sky'),
('moon_lantern', 'a lantern that looks like the full moon'),
('fairy_house', 'a tiny house fit for a fairy'),
('phoenix', 'a mythical phoenix in flames'),
('steampunk_goggles', 'a pair of steampunk goggles'),
('electric_guitar', 'a red electric guitar'),
('magic_carpet', 'a flying magic carpet'),
('vintage_radio', 'a vintage radio'),
('pirate_ship', 'an old pirate ship'),
('dragon_egg', 'a dragon egg with glowing cracks'),
('enchanted_mirror', 'an enchanted mirror with a golden frame'),
('ninja_sword', 'a sharp ninja sword'),
('space_shuttle', 'a space shuttle launching'),
('ice_castle', 'a castle made of ice'),
('unicorn', 'a majestic unicorn'),
('dinosaur_skeleton', 'a dinosaur skeleton in a museum'),
('witches_broom', 'a witch broom'),
('medieval_castle', 'a medieval castle on a hill'),
('cyberpunk_city', 'a cyberpunk city at night'),
('giant_robot', 'a giant robot ready for battle'),
('ancient_scroll', 'an ancient scroll with mysterious writings'),
('nebula_bottle', 'a bottle containing a tiny swirling nebula'),
('crystal_ball', 'a crystal ball on a dark table'),
('samurai_armor', 'a set of traditional samurai armor'),
('floating_island', 'a floating island in the sky'),
('time_machine', 'a time machine with glowing lights'),
('alien_pet', 'a cute alien pet'),
('haunted_house', 'a spooky haunted house'),
('sunflower_field', 'a sunflower field at sunrise'),
('gladiator_sword', 'a gladiator sword with a leather grip'),
('magic_wand', 'a magic wand with a crystal tip'),
('vintage_typewriter', 'a vintage typewriter'),
('giant_panda', 'a giant panda eating bamboo'),
('mystic_orb', 'a mystic orb glowing with power'),
('futuristic_city', 'a futuristic city with flying cars'),
('ancient_pyramid', 'an ancient pyramid under a starry sky'),
('flower_crown', 'a delicate flower crown made of wildflowers'),
('space_station', 'a space station orbiting Earth'),
('underwater_city', 'an underwater city with glowing lights'),
('fire_dragon', 'a fire-breathing dragon atop a mountain'),
('glass_slipper', 'a glass slipper on a red velvet cushion'),
('hoverboard', 'a futuristic hoverboard'),
('jellyfish_lamp', 'a jellyfish-shaped lamp glowing softly'),
('knight_armor', 'a suit of knight s armor standing guard'),
('legendary_sword', 'a legendary sword stuck in stone'),
('mechanical_watch', 'a mechanical watch with visible gears'),
('nordic_runes', 'a stone tablet inscribed with Nordic runes'),
('origami_crane', 'an origami crane made of holographic paper'),
('potion_shop', 'a potion shop with shelves of colorful bottles'),
('quill_and_ink', 'a quill and inkwell on an ancient desk'),
('rainbow_bridge', 'a rainbow bridge leading to a castle'),
('solar_eclipse', 'a solar eclipse with a ring of fire'),
('treehouse_village', 'a treehouse village in an ancient forest'),
('ufo_sighting', 'a UFO sighting over a quiet farm'),
('vampire_castle', 'a vampire castle under a full moon'),
('werewolf_forest', 'a dark forest where werewolves roam'),
('xenon_spaceship', 'a xenon spaceship with sleek design'),
('yarn_ball_planet', 'a planet shaped like a ball of yarn'),
('zeppelin_airship', 'a zeppelin airship flying over the city'),
('abandoned_amusement_park', 'an abandoned amusement park at twilight'),
('bioluminescent_cave', 'a bioluminescent cave with glowing plants'),
('cosmic_gateway', 'a cosmic gateway with swirling galaxies'),
('dwarf_mine', 'a dwarf mine filled with gems'),
('elven_bow', 'an elven bow with intricate carvings'),
('fairy_garden', 'a fairy garden with tiny houses and flowers'),
('ghostly_galleon', 'a ghostly galleon sailing through fog'),
('holographic_globe', 'a holographic globe of Earth'),
('ice_phantom', 'an ice phantom in a blizzard'),
('jungle_temple', 'a jungle temple overrun by vines'),
('kraken_attack', 'a kraken attacking a ship'),
('lost_city_of_atlantis', 'the lost city of Atlantis'),
('mystical_forest', 'a mystical forest with enchanted trees'),
('neon_skatepark', 'a neon skatepark at night'),
('oracle_chamber', 'an oracle chamber with ancient symbols'),
('pirate_treasure_map', 'a pirate treasure map with an X mark'),
('quantum_computer', 'a quantum computer with glowing circuits'),
('robotic_exoskeleton', 'a robotic exoskeleton for enhanced strength'),
('supernova_explosion', 'a supernova explosion in distant space'),
('titanic_underwater', 'the Titanic underwater with marine life'),
('unicorn_forest', 'a forest where unicorns roam freely'),
('viking_longship', 'a Viking longship sailing the northern seas'),
('witches_cauldron', 'a witch s cauldron bubbling with a potion'),
('x-ray_vision_glasses', 'x-ray vision glasses revealing hidden objects'),
('yellow_brick_road', 'the yellow brick road leading to a city'),
('zodiac_constellations', 'zodiac constellations in a starry night sky'),

    # ('butterfly', 'a beautiful, intricate butterfly'),
    # ('boy', 'a nendoroid of a chibi cute boy'),
    # ('axe', 'a viking axe, fantasy, blender'),
    # ('dog_rocket', 'corgi riding a rocket'),
    # ('teapot', 'a chinese teapot'),
    # ('squirrel_guitar', 'a DSLR photo of a squirrel playing guitar'),
    # ('house', 'fisherman house, cute, cartoon, blender, stylized'),
    # ('ship', 'Higly detailed, majestic royal tall ship, realistic painting'),
    # ('einstein', 'Albert Einstein with grey suit is riding a bicycle'),
    # ('angle', 'a statue of an angle'),
    # ('lion', 'A 3D model of Simba, the lion cub from The Lion King, standing majestically on Pride Rock, character'),
    # ('paris', 'mini Paris, highly detailed 3d model'),
    # ('pig_backpack', 'a pig wearing a backpack'),
    # ('pisa_tower', 'Picture of the Leaning Tower of Pisa, featuring its tilted structure and marble facade'),
    # ('robot', 'a human-like full body robot'),
    # ('coin', 'a golden coin'),
    # ('cake', 'a delicious and beautiful cake'),
    # ('horse', 'a DSLR photo of a horse'),
    # ('cat', 'a photo of a cat'),
    # ('cat_hat', 'a photo of a cat wearing a wizard hat'),
    # ('cat_ball', 'a photo of a cat playing with a red ball'),
    # ('nendoroid', 'a nendoroid of a chibi girl'),

]

for name, prompt in prompts:
    print(f'======== processing {name} ========')
    # first stage
    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} python main.py --config configs/text_mv.yaml prompt="{prompt}" save_path={name}')
    # second stage
    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} python main2.py --config configs/text_mv.yaml  prompt="{prompt}" save_path={name}')
    # export video
    mesh_path = os.path.join('logs', f'{name}.obj')
    os.makedirs('videos', exist_ok=True)
    os.system(f'python -m kiui.render {mesh_path} --save_video videos/{name}.mp4 --wogui')

    book & a
    hardcover
    book & A
    detailed
    image
    of
    an
    antique
    hardcover
    book
    with ornate golden embossing on the spine and a slightly worn cover, lying open to reveal crisp, aged pages filled with classic typeface, literature \ \
            pen & a fountain pen & An elegantly crafted fountain pen with a glossy ebony barrel and a fine gold nib, depicted in the act of writing flowing script on a piece of parchment, writing instrument \ \
            apple & a shiny red apple & A hyper-realistic image of a shiny red apple, complete with a perfectly detailed stem and a single leaf, the surface reflecting a subtle light, fruit \ \
            keyboard & a mechanical keyboard & A mechanical keyboard with individual RGB lighting under each key, designed for precision typing and gaming, shown in a dimly lit room enhancing the colorful backlighting, technology \ \
            mouse & an optical computer mouse & An ergonomic optical computer mouse tailored for gaming, featuring customizable side buttons and a glowing RGB light strip, technology \ \
            chair & a modern office chair & A modern office chair with high-tech mesh fabric for breathability, adjustable armrests, and lumbar support, designed for comfort and efficiency in a stylish office setting, furniture \ \
            desk & a wooden desk & A spacious wooden desk with a smooth finish and minimalist design, equipped with compartments for organizing, set up in a well-lit study room, furniture \ \
            lamp & a desk lamp & A sleek desk lamp with an LED light, articulated arm, and touch-sensitive control panel that provides adjustable brightness for a home office environment, lighting \ \
            backpack & a hiking backpack & A durable hiking backpack made from high-strength, water-resistant material, featuring multiple compartments, hydration pack access, and reflective safety strips, ideal for outdoor adventures, equipment \ \
            bicycle & a mountain bicycle & A rugged mountain bicycle with a lightweight aluminum frame, hydraulic disc brakes, and aggressive tread on tires, captured on a rocky trail with a backdrop of mountains, vehicle \ \
            helmet & a cycling helmet & A high-performance cycling helmet with aerodynamic design, integrated ventilation holes, and a visor for sun protection, essential for road safety, protective gear \ \
            glove & a pair of leather gloves & A pair of premium leather gloves, intricately stitched and lined with soft fleece for warmth, shown gripping a wooden walking stick, apparel \ \
            boot & a pair of hiking boots & A pair of robust hiking boots crafted from waterproof leather with reinforced soles for superior traction on uneven terrain, essential for mountain trekking, footwear \ \
            scarf & a woolen scarf & A luxurious woolen scarf in a deep burgundy color, woven with a subtle herringbone pattern, draped elegantly over a coat in a wintery scene, accessory \ \
            hat & a baseball cap & A classic baseball cap made from durable fabric, featuring a curved brim and an adjustable strap at the back, embroidered with a popular sports team logo, headwear \ \
            ball & a soccer ball & A professional soccer ball designed with pentagonal and hexagonal panels, stitched together to ensure optimal performance and durability on a grassy field, sports equipment \ \
            bat & a baseball bat & A handcrafted wooden baseball bat, polished to a high sheen, shown in mid-swing hitting a baseball in an action-packed game scenario, sports equipment \ \
            guitar & an acoustic guitar & An acoustic guitar with a mahogany body and spruce top, strung with high-quality nylon strings, resting on a wooden stand in a cozy room filled with musical memorabilia, musical instrument \ \
            piano & a grand piano & A majestic grand piano finished in glossy black lacquer, with the lid open to show its intricate internal strings and hammers, set on a concert stage under a spotlight, musical instrument \ \
            drum & a bass drum & A professional bass drum as part of a larger drum set, featuring a high-gloss finish and chrome hardware, captured with sticks mid-air, ready to strike in a rhythmic beat, musical instrument \ \
            violin & a classic violin & A classic violin crafted from aged wood, with a polished finish and fine strings, accompanied by a bow, resting on a velvet-lined case, highlighting its elegance and readiness for a performance, musical instrument \ \
            trumpet & a brass trumpet & A brass trumpet with a polished, reflective surface, showcasing the intricate valves and mouthpiece, set against a backdrop of sheet music, ready for a jazz performance, musical instrument \ \
            saxophone & an alto saxophone & An alto saxophone with a golden finish, detailed engraving on the bell, and leather pads, displayed in a music room setting with soft lighting, emphasizing its sleek design, musical instrument \ \
            microphone & a studio microphone & A high-end studio microphone with a large diaphragm and pop filter, mounted on a boom stand in a soundproof recording studio, essential for capturing clear and detailed vocal performances, audio equipment \ \
            speaker & a portable speaker & A portable Bluetooth speaker with a durable, waterproof exterior and powerful audio drivers, shown playing music on a sandy beach at sunset, audio equipment \ \
            laptop & a modern laptop & A sleek modern laptop with a high-resolution display and a thin, lightweight design, featuring cutting-edge hardware optimized for professional software applications, shown on a clean, minimalist desk, technology \ \
            tablet & a digital tablet & A state-of-the-art digital tablet with a large, vibrant screen, displaying a creative drawing app, held by an artist in a studio filled with natural light, technology \ \
            smartphone & a latest model smartphone & A latest model smartphone featuring an edge-to-edge display with no bezels, a triple-camera system on the back, and facial recognition technology, shown in a hand against a cityscape, technology \ \
            camera & a digital camera & A professional digital camera with a large sensor and a telephoto lens, mounted on a tripod overlooking a scenic landscape at golden hour, capturing stunning details, technology \ \
            telescope & an astronomical telescope & An astronomical telescope set against the backdrop of a starry night sky, with a detailed viewfinder and precision adjustment knobs, aimed at uncovering the mysteries of distant galaxies, scientific instrument \ \
            clock & a wall clock & A vintage wall clock with Roman numerals and ornate hands, housed in a dark wooden frame, hanging on a pastel-colored wall in a classic living room setting, home decor \ \
            watch & a wristwatch & A luxury wristwatch with a stainless steel band, sapphire crystal face, and a sophisticated chronograph display, shown close-up on a wrist dressed in a fine suit, accessory \ \
            bracelet & a silver bracelet & An elegant silver bracelet with intricate links and a delicate clasp, adorned with small diamonds that catch the light beautifully, displayed on a velvet cushion, jewelry \ \
            necklace & a gold necklace & A stunning gold necklace featuring a fine chain and a pendant with an elaborate design, showcased on a mannequin with an evening gown, jewelry \ \
            ring & a diamond ring & A close-up image of a diamond ring with a large, radiant-cut stone set in a platinum band, surrounded by smaller pavé diamonds, presented in an open jewelry box, luxury item \ \
            earring & a pair of hoop earrings & A pair of hoop earrings made from polished gold, each adorned with tiny, sparkling gemstones, displayed against a dark, textured background to highlight their elegance, jewelry \ \
            sunglasses & a pair of aviator sunglasses & A pair of aviator sunglasses with polarized lenses and a metal frame, resting on a rocky surface under bright sunlight, fashion accessory \ \
            binoculars & a pair of binoculars & A pair of high-performance binoculars with adjustable zoom and focus, used for bird watching, shown in a natural setting with a clear view of distant mountains, outdoor equipment \ \
            map & a world map & A detailed world map with colorful political boundaries and major cities marked, spread out on a table with a magnifying glass and other travel essentials, educational tool \ \
            compass & an orienteering compass & An old-fashioned orienteering compass with a brass casing and a floating needle, lying next to a map on a wooden table in a forest setting, navigation tool \ \
            flashlight & a LED flashlight & A robust LED flashlight emitting a powerful beam of light, designed for durability and long battery life, shown illuminating a dark path at night, safety equipment \ \
            tent & a camping tent & A high-quality camping tent set up in a serene forest location, with a waterproof canopy and room for two, shown at dusk with a cozy interior glow, outdoor shelter \ \
            sleeping bag & a mummy sleeping bag & A mummy sleeping bag designed for extreme temperatures, shown partially unzipped and inviting, laid out inside a tent with a view of the starry sky, camping gear\ \
            fireplace & a stone fireplace & A rustic stone fireplace with a roaring fire, providing warmth and light in a cozy cabin setting, the mantelpiece decorated with family photos and vintage ornaments, home comfort \ \
            grill & a charcoal grill & A charcoal grill in action, with smoky flavors rising from cooking steaks, depicted in a summer backyard setting with friends gathered around, cooking equipment \ \
            kettle & a stainless steel kettle & A stainless steel kettle with a sleek, modern design, boiling water with visible steam, placed on an induction cooktop in a contemporary kitchen, kitchen appliance \ \
            mug & a ceramic coffee mug & A ceramic coffee mug filled with steaming hot coffee, the surface adorned with a quaint café logo, positioned on a rustic wooden table alongside a croissant, beverage container \ \
            plate & a porcelain plate & A porcelain plate with a delicate floral pattern, set on a dining table with silver cutlery and crystal glasses, ready for an elegant meal, tableware \ \
            bowl & a ceramic soup bowl & A ceramic soup bowl filled with homemade vegetable soup, steam rising, accompanied by a spoon and fresh bread on a kitchen counter, kitchenware \ \
            spoon & a stainless steel spoon & A stainless steel spoon with a polished finish, designed with an ergonomic handle, resting beside a bowl of cereal with milk, captured in the morning light, kitchen utensil \\