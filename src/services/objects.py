from ...Dependencies import *

class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color('lightskyblue3')
        self.active = False
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.selected_range = (0, 0)
        self.selection_color = pygame.Color('dodgerblue')

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.selected_range = (0, 0)
                text_width = self.font.size(self.text[:self.selected_range[0]])[0]
                self.selection_rect = pygame.Rect(self.rect.x + text_width, self.rect.y + 5, 2, self.font.get_height())
            else:
                self.active = False
                self.selected_range = (0, 0)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)  # You can do something with the entered text here
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    if self.selected_range[0] == self.selected_range[1]:
                        self.text = self.text[:self.selected_range[0] - 1] + self.text[self.selected_range[1]:]
                        self.selected_range = (max(0, self.selected_range[0] - 1), max(0, self.selected_range[0] - 1))
                    else:
                        start, end = sorted(self.selected_range)
                        self.text = self.text[:start] + self.text[end:]
                        self.selected_range = (start, start)
                elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:  # Check for Ctrl+C (copy)
                    copied_text = self.text[self.selected_range[0]:self.selected_range[1]]
                    pyperclip.copy(copied_text)
                elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:  # Check for Ctrl+V (paste)
                    self.text = self.text[:self.selected_range[0]] + pyperclip.paste() + self.text[self.selected_range[1]:]
                    self.selected_range = (self.selected_range[0] + len(pyperclip.paste()), self.selected_range[0] + len(pyperclip.paste()))
                else:
                    char = event.unicode
                    self.text = self.text[:self.selected_range[0]] + char + self.text[self.selected_range[1]:]
                    self.selected_range = (self.selected_range[0] + len(char), self.selected_range[0] + len(char))

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        if text_surface.get_width() > self.rect.width:  # Check if the text is wider than the input box
            scroll_offset = text_surface.get_width() - self.rect.width
            screen.blit(text_surface, (self.rect.x - scroll_offset, self.rect.y + 5))
        else:
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

        if self.active:
            text_width = self.font.size(self.text[:self.selected_range[0]])[0]
            self.selection_rect.x = self.rect.x + text_width
            self.selection_rect.y = self.rect.y + 5
            self.selection_rect.w = 2
            self.selection_rect.h = self.font.get_height()
            pygame.draw.rect(screen, self.selection_color, self.selection_rect)