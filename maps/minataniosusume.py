from maps.AbstractGakushoku import AbstractGakushoku

class minataniosusume(AbstractGakushoku):

    def get_menu(self):
        return "100円朝食"
    
    def get_summary(self):
        return "トーストとゆで卵がついてきて１００円は安い！！"
    
    def get_author(self):
        return"南谷悠真"