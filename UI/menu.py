

class Menu:
    def __init__(self, menu=["________________________________________________________", "--------------------------------------------------------",[],[""],[],"--------------------------------------------------------"]) -> None:
        self.menu = menu


    def DrawMenu(self):
        for item in self.menu:
            if type(item) == list:
                for sub_item in item:
                    print(sub_item)
            else:
                print(item)
        pass

    def SwitchMenu(self, upper_display=[""], lower_display=[""], alternate_display=False):

        if alternate_display:
            f_upper_display = self.FormatOptions(upper_display)

            self.menu[2] = f_upper_display

            f_lower_display = self.FormatOptions(lower_display, upper_display.__len__()+1)

            self.menu[4] = f_lower_display
        else:

            self.menu[2] = upper_display

            f_lower_display = self.FormatOptions(lower_display)

            self.menu[4] = f_lower_display

    def FormatOptions(self, options, i=1):
        all_options = []
        current_row = ""
        j = 1

        for opt in options:
            opt += f" [{i}] | "
            
            if current_row == "":
                opt = "| " + opt
            
            current_row += opt
            if j%3 == 0:
                all_options.append(current_row)
                current_row = ""
            
            j+=1
            i+=1
        all_options.append(current_row)
        return all_options
        
        
