#Author: Miranda Humphreys
#Pair Reviewed by: John Clarke Miego
#Welcome, Login, Register Page
#Initial code was written by Miranda, but after the demo we decided it was time to do pair programming since we didn't
#have everything we wanted implemented and we were able to come up with more functionality for the welcome screen
#2nd Draft
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window

Window.size = (300, 500)

navigation_toolbar = """
Screen:    
    Image:
        source: "covidshield.png"
        size_hint_y: None
        height: 620
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {"center_x":0.5, "center_y":0.30}

    MDRectangleFlatButton:
        text: 'Register'
        pos_hint: {"center_x":0.5, "center_y":0.21}

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Symptom Tracker'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Home"
                            IconLeftWidget:
                                icon: "home"
                        OneLineIconListItem:
                            text: "Calendar"
                            IconLeftWidget:
                                icon: "calendar-week"
                        OneLineIconListItem:
                            text: "Survey"
                            IconLeftWidget:
                                icon: "note-text"
                        OneLineIconListItem:
                            text: "Testing"
                            IconLeftWidget:
                                icon: "web"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout-variant"


"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"
        screen = Builder.load_string(navigation_toolbar)

        return screen


DemoApp().run()
