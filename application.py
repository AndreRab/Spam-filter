import pygame
from const import * 
from stringInput import String

class Application:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Spam filter')
        self.screen = pygame.display.set_mode(display_size)

        self.font = pygame.font.Font(None, input_box_height)
        self.start_input_box = pygame.Rect(75, 100, input_box_width, input_box_height)
        self.input_box = self.start_input_box.copy()
        self.input_string = String(visible_lines_count, input_box_height, input_box_width - width_eps)
        
        self.running = True

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if self.input_string.pop():
                            self.input_box.height -= input_box_height

                    elif event.key == pygame.K_RETURN:
                        print(self.input_string.submit())
                        self.input_box = self.start_input_box.copy()

                    elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.input_string.copy()

                    elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.input_box.height += input_box_height * self.input_string.paste(self.input_box.height, self.font)

                    elif event.key == pygame.K_UP:
                        self.input_string.scroll_up()
                    elif event.key == pygame.K_DOWN:
                        self.input_string.scroll_down()

                    else:
                        if self.input_string.add(event.unicode, self.input_box.height, self.font):
                            self.input_box.height += input_box_height

                self.draw_parts()

        pygame.quit()

    def draw_parts(self):
        self.screen.fill(bg_color)
        pygame.draw.rect(self.screen, input_box_color, self.input_box)
        
        self.draw_input_box()
        self.draw_title()
        
        pygame.display.flip()

    def draw_input_box(self):
        for i, line in enumerate(self.input_string.visible_range()):
            line_for_render = line + '|' if self.input_string.lines_len() - 1 == i else line
            text_surface = self.font.render(line_for_render, True, text_color)
            self.screen.blit(text_surface, (self.input_box.x + 10, self.input_box.y + 10 + i * input_box_height))


    def draw_title(self):
        label_surface_first = self.font.render(title_text[0], True, text_color)
        self.screen.blit(label_surface_first, title_text_coordinates[0]) 

        label_surface_second = self.font.render(title_text[1], True, text_color)
        self.screen.blit(label_surface_second, title_text_coordinates[1]) 