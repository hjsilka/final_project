import pygame

# box for all the dialogue - with a picture of the person speaking next to it
def draw_dialogue_box(speaker, text):
    box_pos = (20, HEIGHT - 80, WIDTH - 40,70)
    pygame.draw.rect(screen, (230, 230, 250), box_pos)
    pygame.draw.rect(screen, BLACK, box_pos, 2)

    if speaker in character_images:
        screen.blit(character_images[speaker], (30, HEIGHT - 75))

    speaker_text = dialogue_font.render(speaker + ":", True, BLACK)
    screen.blit(speaker_text, (90, HEIGHT - 75))

    text_lines = [text]
    for i, line in enumerate(text_lines):
        screen.blit(dialogue_font.render(line, True, BLACK), (90, HEIGHT - 45 + i * 25))

