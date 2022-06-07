import pygame


class Shop:

    def __init__(self, game):
        self.game = game
        self.opened_shop_window = False

    def shop_management(self):
        if self.opened_shop_window:
            shop_window_x = 100
            shop_window_y = 100
            shop_window = pygame.Rect(shop_window_x, shop_window_y, self.game.screen.get_width() - 200,
                                      self.game.screen.get_height() - 200)
            pygame.draw.rect(self.game.screen, (125, 15, 55), shop_window)
            text = self.game.font.render("Shop", True, (0, 0, 0))
            self.game.screen.blit(text, (self.game.screen.get_width() / 2 - 30, shop_window_x + 10))
            player_items = self.game.player.get_equipment()
            shopkeeper_items = self.game.map.shopkeeper.get_equipment()
            my_font = pygame.font.SysFont('Arial', 14)
            gold = self.game.player.get_gold()

            sell_rects = []
            buy_rects = []

            for index, item in enumerate(player_items):
                pos_x = shop_window_x + index * 3 * self.game.settings.tile_size + 30
                pos_y = shop_window_y + self.game.settings.tile_size * 3
                if index == 0:
                    text = self.game.font.render("Sell", True, (0, 0, 0))
                    self.game.screen.blit(text, (pos_x, pos_y - 30))
                item.render_graphics(pygame.display.get_surface(), (pos_x, pos_y))
                text = my_font.render(f"Price: {item.get_price()}", True, (255, 215, 0))
                self.game.screen.blit(text, (pos_x, pos_y + 2 * self.game.settings.tile_size + 5))
                text = my_font.render(f"Power: {item.get_power()}", True, (0, 0, 0))
                self.game.screen.blit(text, (pos_x, pos_y + 2 * self.game.settings.tile_size + 20))
                sell_rects.append(pygame.Rect(pos_x, pos_y, self.game.settings.tile_size * 2, self.game.settings.tile_size * 2))

            for index, item in enumerate(shopkeeper_items):
                pos_x = shop_window_x + index * 3 * self.game.settings.tile_size + 30
                pos_y = shop_window_y + 8 * self.game.settings.tile_size
                if index == 0:
                    text = self.game.font.render("Buy", True, (0, 0, 0))
                    self.game.screen.blit(text, (pos_x, pos_y - 30))
                item.render_graphics(pygame.display.get_surface(), (pos_x, pos_y))
                text = my_font.render(f"Price: {item.get_price() * 2}", True,
                                      (255, 0, 0) if item.get_price() * 2 > gold else (0, 255, 0))
                self.game.screen.blit(text, (pos_x, pos_y + 2 * self.game.settings.tile_size + 5))
                text = my_font.render(f"Power: {item.get_power()}", True, (0, 0, 0))
                self.game.screen.blit(text, (pos_x, pos_y + 2 * self.game.settings.tile_size + 20))
                buy_rects.append(pygame.Rect(pos_x, pos_y, self.game.settings.tile_size * 2, self.game.settings.tile_size * 2))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.game.double_click:
                for index, item in enumerate(sell_rects):
                    if item.collidepoint((mouse_x, mouse_y)):
                        transaction_gold = self.game.player.sell_item(index)
                        self.game.player.change_gold(transaction_gold)
                for index, item in enumerate(buy_rects):
                    if item.collidepoint((mouse_x, mouse_y)):
                        if self.game.player.get_gold() >= shopkeeper_items[
                            index].get_price() * 2 and self.game.player.equipment.items_limit > len(
                                self.game.player.equipment.items):
                            new_item = self.game.map.shopkeeper.sell_item(index)
                            self.game.player.equipment.attach_sword(new_item)
                            self.game.player.change_gold(- 2 * new_item.get_price())
                self.game.double_click = False
