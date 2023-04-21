import pygame
class ComboBox():
    def __init__(self, screen, options, rect, background_color, font_type, font_size, border_radius, text_options_color, text_selected_option_color, gap_value, initial_selected_value):
        self.screen = screen
        self.options = options
        self.rect = rect
        self.x = self.rect.x
        self.y = self.rect.y
        self.background_color = background_color
        self.font_type = font_type
        self.font_size = font_size
        self.border_radius = border_radius
        self.text_options_color = text_options_color
        self.text_selected_option_color = text_selected_option_color
        self.gap_value = gap_value
        self.width = self.rect.width
        self.height = self.rect.height + (self.gap_value * len(options))
        self.combo_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.combo_open = False
        self.select_dict = {}
        self.selected_index = -1
        self.selected_option = initial_selected_value
    
    def draw(self):
        self.clickOnInitialRect()
        self.clickOutOfCombo()
        self.drawSelectedOption()
        if self.combo_open:
            pygame.draw.rect(self.screen, self.background_color, self.combo_rect, 0, self.border_radius)
            gap = 0
            for option in self.options:
                font = pygame.font.SysFont(self.font_type, self.font_size)
                render_text = font.render(option, True, self.text_options_color, None)
                self.screen.blit(render_text, (self.rect.x + 5, self.rect.y + self.rect.height + gap + (self.gap_value/2 - render_text.get_height()/2)))
                pygame.draw.line(self.screen, self.text_options_color, (self.rect.x, self.rect.y + self.rect.height + gap), (self.rect.x + self.rect.width, self.rect.y + self.rect.height + gap), 3) 
                self.select_dict[option] = pygame.Rect(self.rect.x, self.rect.y + self.rect.height + gap, self.rect.width, 31)
                gap += self.gap_value
            self.setSelectedIndex()
    
    def clickOnInitialRect(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == True:
            self.combo_open = True
    
    def clickOutOfCombo(self):
        if not self.combo_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == True:
            self.combo_open = False
    
    def setSelectedIndex(self):
        if self.combo_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == True:
            dict_values = list(self.select_dict.values())
            dict_keys = list(self.select_dict.keys())
            for rect in self.select_dict.values():
                if rect.collidepoint(pygame.mouse.get_pos()):
                    self.selected_index = list(self.select_dict.values()).index(rect) + 1
                    self.selected_option = dict_keys[dict_values.index(rect)]
                    self.combo_open = False
    
    def getIndex(self):
        return self.selected_index
    
    def getValue(self):
        return self.selected_option

    def drawSelectedOption(self):
        font = pygame.font.SysFont(self.font_type, self.font_size, True)
        render_text = font.render(self.selected_option, True, self.text_selected_option_color, None)
        self.screen.blit(render_text, (self.rect.x + 10, self.rect.y + (self.rect.height - render_text.get_height())/2))
    

