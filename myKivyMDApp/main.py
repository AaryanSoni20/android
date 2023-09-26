from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
import ssl
# import pywhatkit as wa
# import webbrowser as wb

KV = '''

MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                id: home
                MDTopAppBar:
                    title: 'Krishna Jewellers'
                    elevation: 4
                    pos_hint: {'top':1}
                    left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                
                MDCard:
                    orientation: 'vertical'
                    size_hint: (None,None)
                    size: (120,120)
                    radius: (100,100,100,100)
                    pos_hint: {'center_x':0.5, 'center_y':0.8}
                    style: 'outlined'
                    line_color: app.theme_cls.primary_color
                    line_width: 1
                    FitImage:
                        source: '../assets/image.png'
                        size_hint: (None, None)
                        size: (120,120)
                        radius: (100,100,100,100)
                
                MDLabel:
                    text: 'KRISHNA JEWELLERS'
                    font_size: 30
                    font_weight: 'bold'
                    font_name: '../fonts/Charter Bold.ttf'
                    pos_hint: {'center_x': 0.675, 'center_y': 0.7}
                
                MDLabel:
                    text: 'Dineshbhai Soni'
                    font_size: 25
                    font_name: '../fonts/Charter Bold Italic.ttf'
                    pos_hint: {'center_x': 0.8, 'center_y': 0.65}
                
                MDLabel:
                    text: 'Proprietor'
                    font_size: 25
                    font_name: '../fonts/Charter Italic.ttf'
                    pos_hint: {'center_x': 0.875, 'center_y': 0.61}

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0,10,10,0)
            size_hint: (None,1)
            drawer_width: dp(300)
            
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title: 'Username'
                    text: 'points'
                    spacing: '4dp'
                    padding: '12dp', 0,0, '56dp'
                
                MDNavigationDrawerItem:
                    icon: 'account'
                    text: 'Account'
                    on_release: nav_drawer.set_state('close')
                
                MDNavigationDrawerItem:
                    icon: 'home'
                    text: 'Home'
                    on_release: nav_drawer.set_state('close')
                
                MDNavigationDrawerItem:
                    icon: 'phone'
                    text: 'Contact'
                    on_release: app.open_dialer()
                
                MDNavigationDrawerItem:
                    icon: 'whatsapp'
                    text: 'WhatsApp'
                    on_release: app.open_whatsapp()

'''

class MD3Card(MDCard):
    text = StringProperty()

class MyApp(MDApp):
    def build(self):
        self.root = Builder.load_string(KV)
        Window.size = (450, 800)
        self.theme_cls.theme_style = "Light"
        return self.root
    
    def open_whatsapp(self):
        # wb.open('https://wa.me/+917043414570?text=Hello%20Krishna%20Jewellers')
        pass
    
    def open_dialer(self):
        # wb.open('tel:+917043414570')
        pass
    
    # def on_start(self):
    #     self.root.ids.home.add_widget(
    #         MD3Card(
    #             line
    #         )
    #     )

if __name__ == '__main__':
    MyApp().run()