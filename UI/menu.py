

class Menu:
    def __init__(self, menu=["________________________________________________________", "--------------------------------------------------------",[],[""],[],"--------------------------------------------------------"]) -> None:
        self.menu = menu

    def SwitchMenu(self, scene, menu_index, upper_display, lower_display):
        #scene determines the topmost layer of menus, qol for me to navigate in code
        #menu_index uses power of ten values for index, i.e. 10 for menu 1 in products, 11 for a specific product in products, or something like that
        
        pass