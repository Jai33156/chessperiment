import pygame

"Thanks to DevilsWork.shop for setting the artwork online!"


class Stuk:
    def __init__(self, soort, sprite, kleur):
        self.soort = soort
        self.sprite = sprite


class Bord:
    def __init__(self, pos):
        self.pos = pos
        self.stukken = []


    def setup_bord(self):
        for x in range(8):
            self.stukken.append([])
            for y in range(8):
                stuk = None
                stuk_kleur = None
                if y == 1 or y == 6:
                    stuk = "pawn"
                if y == 0 or y == 7:
                    if x == 0 or x == 7:
                        stuk = "rook"
                    if x == 1 or x == 6:
                        stuk = "knight"
                    if x == 2 or x == 5:
                        stuk = "bishop"
                    if x == 3:
                        stuk = "queen"
                    if x == 4:
                        stuk = "king"
                if y >= 4:
                    stuk_kleur = "white"
                else:
                    stuk_kleur = "black"
                if stuk is not None:
                    self.stukken[x].append(Stuk(stuk, image(f"chess_asset_pack/{stuk_kleur}_{stuk}.png"),stuk_kleur))
                else:
                    self.stukken[x].append(None)
def image(img, grootte=1):
    return pygame.transform.scale_by(pygame.image.load(img), grootte)


pygame.init()
factor = 2
background_img = pygame.transform.scale_by(image("chess_asset_pack/board.png"), 2)
klok_grootte = 50 * factor
background_grootte = [background_img.get_width(), background_img.get_height()+klok_grootte]
grootte_vakje = [22*factor, 22*factor]
stukken = ["pawn", "knight", "bishop", "rook", "queen", "king"]
stukken_img = []
for i in stukken:
    kleuren = ["white", "black"]
    stukken_img.append([
        image(f"chess_asset_pack/{kleuren[0]}_{i}.png", factor),
        image(f"chess_asset_pack/{kleuren[1]}_{i}.png", factor)
    ])

screen = pygame.display.set_mode(background_grootte)

pygame.display.set_caption('Chess game')

running = True
bord = Bord([0, klok_grootte/2])
bord.setup_bord()

def blit_en_centreer(pos, sprite, rect):
    # Kopieer de pos in een nieuwe lijst
    new_pos = list(pos)  # Maak een lijst van pos om te muteren
    grootte_sprite = [sprite.get_width(), sprite.get_height()]

    # Centreer het sprite in de gegeven rect
    new_pos[0] += (rect[0] - grootte_sprite[0]) / 2  # X-as
    new_pos[1] += (rect[1] - grootte_sprite[1]) / 2  # Y-as

    # Blit het sprite op de nieuwe positie
    screen.blit(sprite, new_pos)


def draw_game():
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, klok_grootte/2))
    for x in range(len(bord.stukken)):
        for y, waarde in enumerate(bord.stukken[x]):
            if waarde is not None:
                blit_en_centreer([x*grootte_vakje[0], y*grootte_vakje[1]+int(klok_grootte/2)], pygame.transform.scale_by(waarde.sprite, factor), grootte_vakje)

    pygame.display.update()


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    draw_game()
