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