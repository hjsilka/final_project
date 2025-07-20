import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.bg_color = (255, 224, 230)
        self.button_color = (255, 150, 135)
        self.button_hover = (255, 120, 110)

        self.title_font = pygame.font.Font('media/fonts/Atma-SemiBold.ttf', 48)
        self.text_font = pygame.font.Font('media/fonts/Atma-SemiBold.ttf', 28)
        self.button_font = pygame.font.Font('media/fonts/Atma-SemiBold.ttf', 24)

        self.clock_img = pygame.image.load('media/backgrounds/clock.png')
        self.clock_img = pygame.transform.scale(self.clock_img, (150, 150))

        self.start_button = pygame.Rect(self.width//2 - 75, 400, 150, 50)

    def handle(self, event):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)

        title = self.title_font.render('TECHBASICS CHAOS: MORNING RUSH', True, (210, 50, 50))
        self.screen.blit(title, title.get_rect(center=(self.width // 2, 80)))

        self.screen.blit(self.clock_img, self.clock_img.get_rect(center=(self.width // 2, 200)))

        subtitle = self.text_font.render('Can you beat the clock and make it to class on time?', True, (0, 0, 0))
        self.screen.blit(subtitle, subtitle.get_rect(center=(self.width // 2, 350)))

        self.draw_button("START", self.start_button)

    def draw_button(self, text, rect):
        mouse_pos = pygame.mouse.get_pos()
        hovering = rect.collidepoint(mouse_pos)
        color = self.button_hover if hovering else self.button_color
        pygame.draw.rect(self.screen, color, rect, border_radius=20)

        label = self.button_font.render(text, True, (255, 255, 255))
        self.screen.blit(label, label.get_rect(center=rect.center))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.collidepoint(pygame.mouse.get_pos()):
                return "start"
        return None






