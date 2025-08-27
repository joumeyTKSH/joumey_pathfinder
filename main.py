import pygame


# === CONSTANTS ===
FPS = 60
RES = WIDTH, HEIGHT = 1000, 600
FW = WIDTH // 5  # FW = Fifth of width
MARGIN = 15
algotyhms = ['A*', 'Dijkstra\'s', 'BFS', 'DFS']

# Colors
GREY = (33, 33, 33)
LIGHT_GREY = (55, 55, 55)
WHITE = (240, 245, 235)


class Pathfinder:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.font_name = None  # default pygame font

    def fit_text(self, text, rect_size):
        """Return a surface with text scaled to fit inside rect_size."""
        max_w, max_h = rect_size
        font_size = 1
        font = pygame.font.Font(self.font_name, font_size)

        # Increase font size until it doesn't fit anymore
        while True:
            next_font = pygame.font.Font(self.font_name, font_size + 1)
            w, h = next_font.size(text)
            if w > max_w or h > max_h:
                break
            font_size += 1
            font = next_font

        return font.render(text, True, WHITE)

    def draw(self):
        self.check_events()
        self.surface.fill(GREY)

        # --- GUI: left to right ---
        h_size = (HEIGHT - MARGIN * 5) // 4
        w_size = FW - MARGIN * 2

        for mult in range(4):
            y = MARGIN + (h_size + MARGIN) * mult

            # outer rectangle
            pygame.draw.rect(
                self.surface, LIGHT_GREY,
                (MARGIN, y, w_size, h_size)
            )

            # inner rectangle
            inner_rect = pygame.Rect(
                MARGIN * 2,
                MARGIN * 2 + (h_size + MARGIN) * mult,
                w_size - MARGIN * 2,
                h_size - MARGIN * 2
            )
            pygame.draw.rect(self.surface, GREY, inner_rect)

            # --- draw text inside ---
            text_surface = self.fit_text(algotyhms[mult], inner_rect.size)
            text_rect = text_surface.get_rect(center=inner_rect.center)
            self.surface.blit(text_surface, text_rect)

        # vertical divider line
        pygame.draw.line(
            self.surface, WHITE,
            (FW, MARGIN), (FW, HEIGHT - MARGIN)
        )

        # update screen
        pygame.display.flip()
        self.clock.tick(FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit


def main():
    pathfinder = Pathfinder()
    while True:
        pathfinder.draw()


if __name__ == "__main__":
    main()
