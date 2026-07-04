# main.py

import pygame
from config import *
from synth_engine import SynthEngine

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mac Instrument Studio")
clock = pygame.time.Clock()

engine = SynthEngine(volume=INITIAL_VOLUME)
engine.load_instrument("harmonium")

pressed_keys = set()
increase_volume = False
decrease_volume = False

font_title = pygame.font.SysFont("Arial", 48, bold=True)
font_ui = pygame.font.SysFont("Arial", 26)
font_small = pygame.font.SysFont("Arial", 18)

current_instrument = "harmonium"

running = True


def draw_gradient():
    for y in range(WINDOW_HEIGHT):
        color = (20, 20 + y // 20, 35 + y // 15)
        pygame.draw.line(screen, color, (0, y), (WINDOW_WIDTH, y))


def draw_ui():
    draw_gradient()

    title = font_title.render("Instrument Studio", True, (255, 255, 255))
    screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 30))

    inst_text = font_ui.render(f"Instrument: {current_instrument.title()}", True, (0, 255, 200))
    screen.blit(inst_text, (50, 120))

    # Volume bar
    bar_width = 500
    bar_height = 18
    bar_x = WINDOW_WIDTH // 2 - bar_width // 2
    bar_y = 200

    pygame.draw.rect(screen, (50, 50, 50),
                     (bar_x, bar_y, bar_width, bar_height), border_radius=12)

    pygame.draw.rect(screen, (0, 180, 255),
                     (bar_x, bar_y,
                      bar_width * engine.volume, bar_height), border_radius=12)

    vol_text = font_ui.render(f"Volume: {int(engine.volume * 100)}%", True, (220, 220, 220))
    screen.blit(vol_text, (WINDOW_WIDTH // 2 - vol_text.get_width() // 2, 230))

    keys_text = font_ui.render(
        f"Pressed Keys: {' '.join(sorted(pressed_keys)).upper()}",
        True,
        (200, 200, 200)
    )
    screen.blit(keys_text, (50, 300))

    notes_text = font_ui.render(
        f"Playing Notes: {' '.join(engine.active_notes.keys())}",
        True,
        (0, 255, 150)
    )
    screen.blit(notes_text, (50, 340))

    footer = font_small.render(
        "TAB Switch Instrument | HOLD ↑ ↓ Volume | ESC Quit",
        True,
        (180, 180, 180)
    )
    screen.blit(footer, (WINDOW_WIDTH // 2 - footer.get_width() // 2, 550))

    pygame.display.flip()


while running:
    clock.tick(FPS)

    if increase_volume:
        engine.set_volume(engine.volume + VOLUME_STEP / 100)

    if decrease_volume:
        engine.set_volume(engine.volume - VOLUME_STEP / 100)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_TAB:
                current_instrument = "guitar" if current_instrument == "harmonium" else "harmonium"
                engine.load_instrument(current_instrument)

            elif event.key == pygame.K_UP:
                increase_volume = True

            elif event.key == pygame.K_DOWN:
                decrease_volume = True

            else:
                key_char = event.unicode.lower()
                if key_char in ALL_KEYS:
                    pressed_keys.add(key_char)
                    engine.play_note(ALL_KEYS[key_char])

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                increase_volume = False

            elif event.key == pygame.K_DOWN:
                decrease_volume = False

            else:
                key_char = event.unicode.lower()
                if key_char in ALL_KEYS:
                    pressed_keys.discard(key_char)
                    engine.stop_note(ALL_KEYS[key_char])

    draw_ui()

pygame.quit()
