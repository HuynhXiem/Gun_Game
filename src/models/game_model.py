class GameModel:
    def __init__(self):
        self.current_screen = 'intro'  # Trạng thái màn hình hiện tại, ban đầu là 'intro'
        self.pve_selected = False  # Biến để xác định liệu PvE đã được chọn hay không
        self.pvp_selected = False  # Biến để xác định liệu PvP đã được chọn hay không
        self.start_button_clicked = False  # Biến để xác định liệu nút Start đã được nhấn hay không
        self.character_alive = True

    def select_pve(self):
        """Chọn chế độ PvE"""
        self.pve_selected = True
        self.pvp_selected = False

    def select_pvp(self):
        """Chọn chế độ PvP"""
        self.pve_selected = False
        self.pvp_selected = True

    def click_start_button(self):
        """Xử lý sự kiện khi nút Start được nhấn"""
        if self.pve_selected:
            self.start_button_clicked = 1
        elif self.pvp_selected:
            self.start_button_clicked = 2
