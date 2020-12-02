#Author: John Miego
#Date: 12/2/2020
#Completed Code for the UI
#Added navigation to the majority of the screen instances
#Added The three different badges screens
#Updated current information for testings and stanislaus COVID response
#Added screen to choose what type of account type you are making
#Edit some UI changes
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)
COVID = """
#:import webbrowser webbrowser
ScreenManager:
    HomeScreen:
    RegisterScreen:
    AccountTypeScreen:
    LoginScreen:
    Question1Screen:
    Question2Screen:
    Question3Screen:
    Question4Screen:
    BadgeScreen:
    GreenBadgeScreen:
    YellowBadgeScreen:
    RedBadgeScreen:
    InfoScreen:

<HomeScreen>:
    name: "home"
    Image:
        source: "covidshield.png"
        size_hint_y: None
        height: 620
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {"center_x":0.5, "center_y":0.30}
        on_press: root.manager.current = "login"

    MDRectangleFlatButton:
        text: 'Register'
        pos_hint: {"center_x":0.5, "center_y":0.21}
        on_press: 
            root.manager.current = "account"
    
        
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Symptom Tracker'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                            text: "Badge"
                            IconLeftWidget:
                                icon: "shield"
                                on_press: root.manager.current = "badge"
                        OneLineIconListItem:
                            text: "Start Survey"
                            IconLeftWidget:
                                icon: "note-text"
                                on_press: root.manager.current = "Question1"
                        OneLineIconListItem:
                            text: "Testing Info"
                            IconLeftWidget:
                                icon: "web"
                                on_press: root.manager.current = "info"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout-variant"
                        
<RegisterScreen>:
    name: "register"
    MDToolbar:
        title: "Register"
        elevation: 10
        pos_hint: {"top":1}
    MDTextField:
        hint_text: "Email"
        helper_text: "Please enter your email address"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.5, "center_y": 0.6}
        size_hint_x: None
        width: 150
    MDTextField:
        hint_text: "Username"
        helper_text: "Please enter your username"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.5, "center_y": 0.5}
        size_hint_x: None
        width: 150
    MDTextField:
        hint_text: "Password"
        helper_text: "Please enter your password"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.5, "center_y": 0.4}
        size_hint_x: None
        width: 150
    MDRectangleFlatButton:
        text: "Create Account"
        pos_hint: {"center_x":0.5, "center_y": 0.2}
        on_release: self.show_data
    MDIconButton:
        icon: "arrow-left"
        on_press: root.manager.current = "home"
    MDTextField:
        hint_text: "Account Type"
        helper_text: "Manager or Employee"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.5, "center_y": 0.3}
        size_hint_x: None
        width: 150

<AccountTypeScreen>:
    name: "account"
    MDRectangleFlatButton:
        text: "Manager"
        pos_hint: {"center_x":0.5, "center_y": 0.5}
        on_press:
            root.manager.current = 'register'
    MDRectangleFlatButton:
        text: "Employee"
        pos_hint: {"center_x":0.5, "center_y": 0.4}
        on_press:
            root.manager.current = 'register'
    
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Account Type'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                                on_press: root.manager.current = "home"
                        OneLineIconListItem:
                            text: "Calendar"
                            IconLeftWidget:
                                icon: "calendar-week"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"
                                
<LoginScreen>:
    name: "login"
    MDToolbar:
        title: "Login"
        elevation: 10
        pos_hint: {"top":1}
    MDTextField:
        hint_text: "Username"
        helper_text: "Forgot Username"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.5, "center_y": 0.5}
        size_hint_x: None
        width: 150
    MDTextField:
        hint_text: "Password"
        helper_text: "Forgot Password"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x":0.5, "center_y": 0.4}
        size_hint_x: None
        width: 150
    MDRectangleFlatButton:
        text: "Login"
        pos_hint: {"center_x":0.5, "center_y": 0.2}
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x":0.1, "center_y": 0.1}
        user_font_size: "25sp"
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'home'
        

<Question1Screen>:
    name: "Question1"
    MDToolbar:
        title: 'Question 1'
        elevation:10
        pos_hint: {"top": 1}
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x":0.1, "center_y":0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'home'
    MDLabel:
        text: "Have you been exposed to COVID-19 in the last 14 days?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question2'
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question2'
    
<Question2Screen>:
    name: "Question2"
    MDToolbar:
        title: 'Question 2'
        elevation:10
        pos_hint: {"top": 1}

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x":0.1, "center_y":0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question1'
    MDLabel:
        text: "Have you had any of the following Symptoms(1): Dry Cough, Sore Throat, or Fever?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question3'
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question3'

<Question3Screen>:
    name: "Question3"
    MDToolbar:
        title: 'Question 3'
        elevation:10
        pos_hint: {"top": 1}
        
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x":0.1, "center_y":0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question2'
    MDLabel:
        text: "Have you had any of the following Symptoms(2): Shortness of breath, trouble breathing, loss sense of smell?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question4'
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question4'


<Question4Screen>:
    name: "Question4"
    MDToolbar:
        title: 'Question 4'
        elevation:10
        pos_hint: {"top": 1}
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_x":0.1, "center_y":0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'Question3'
    MDLabel:
        text: "Have you tested for COVID-19 in the last 14 days?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'info'
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'info'

<BadgeScreen>:
    name: "badge"
    MDLabel:
        text: "For more information please follow the link down below for your corresponding badge"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .7}
           
    MDRectangleFlatButton:
        text: 'Green'
        pos_hint: {"center_x":0.5, "center_y":0.50}
        on_press: 
            root.manager.current = "green"
    MDRectangleFlatButton:
        text: 'Yellow'
        pos_hint: {"center_x":0.5, "center_y":0.40}
        on_press: 
            root.manager.current = "yellow"
    MDRectangleFlatButton:
        text: 'Red'
        pos_hint: {"center_x":0.5, "center_y":0.30}
        on_press: 
            root.manager.current = "red"
            
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Symptom Tracker'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                                on_press: root.manager.current = "home"
                        OneLineIconListItem:
                            text: "Start Survey"
                            IconLeftWidget:
                                icon: "note-text"
                                on_press: root.manager.current = "Question1"
                        OneLineIconListItem:
                            text: "Testing"
                            IconLeftWidget:
                                icon: "web"
                                on_press: root.manager.current = "info"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout-variant"
<GreenBadgeScreen>:
    name: "green"
    MDLabel:
        text: "You are cleared to go back to work"
        pos_hint: {"center_x":0.6, "center_y":0.25}    
    Image:
        source: "greenshield.png"
        size_hint:  (None, None)
        size: (dp(250), dp(250))
        pos_hint: {"center_x":0.5, "center_y":0.54}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x":0.9, "center_y":0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'yellow'
        
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Green Badge'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                                on_press: root.manager.current = "home"
                        OneLineIconListItem:
                            text: "Start Survey"
                            IconLeftWidget:
                                icon: "note-text"
                                on_press: root.manager.current = "Question1"
                        OneLineIconListItem:
                            text: "Testing Info"
                            IconLeftWidget:
                                icon: "web"
                                on_press: root.manager.current = "info"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout-variant"
<YellowBadgeScreen>:
    name: "yellow"
    MDLabel:
        text: "There is a high chance that you were exposed to COVID. Please quarantine for a minimum of 14 days"
        pos_hint: {"center_x":0.5, "center_y":0.2}
        halign: "center"
    Image:
        source: "yellowshield.png"
        size_hint:  (None, None)
        size: (dp(250), dp(250))
        pos_hint: {"center_x":0.5, "center_y":0.54}
    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_x":0.9, "center_y":0.1}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'red'
        
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Yellow Badge'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                                on_press: root.manager.current = "home"
                        OneLineIconListItem:
                            text: "Start Survey"
                            IconLeftWidget:
                                icon: "note-text"
                                on_press: root.manager.current = "Question1"
                        OneLineIconListItem:
                            text: "Testing Info"
                            IconLeftWidget:
                                icon: "web"
                                on_press: root.manager.current = "info"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout-variant"
<RedBadgeScreen>:
    name: "red"
    MDLabel:
        text: "You are showing COVID-19 symptoms. Please get tested and contact your primary care provider immediately."
        pos_hint: {"center_x":0.5, "center_y":0.2}    
        halign: "center"
    Image:
        source: "redshield.png"
        size_hint:  (None, None)
        size: (dp(250), dp(250))
        pos_hint: {"center_x":0.5, "center_y":0.54}
        
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Red Badge'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                                on_press: root.manager.current = "home"
                        OneLineIconListItem:
                            text: "Start Survey"
                            IconLeftWidget:
                                icon: "note-text"
                                on_press: root.manager.current = "Question1"
                        OneLineIconListItem:
                            text: "Testing Info"
                            IconLeftWidget:
                                icon: "web"
                                on_press: root.manager.current = "info"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout-variant"
            
<InfoScreen>:   
    name: "info" 
    Image:
        source: "Medical.png"
        size_hint_y: None
        height: 600
    MDRectangleFlatButton:
        text: "Stanislaus COVID Response"
        pos_hint: {"center_x": .5, "center_y": .25}
        on_release: webbrowser.open("http://schsa.org/coronavirus/")
    MDRectangleFlatButton:
        text: "Set Appointment"
        pos_hint: {"center_x": .5, "center_y": .15}
        on_release: webbrowser.open("https://www.projectbaseline.com/study/covid-19/eligibility/")  
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Testing Info'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
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
                                on_press: root.manager.current = "home"
                        OneLineIconListItem:
                            text: "Start Survey"
                            IconLeftWidget:
                                icon: "note-text"
                                on_press: root.manager.current = "Question1"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"
            
"""


class HomeScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class Question1Screen(Screen):
    pass


class Question2Screen(Screen):
    pass


class Question3Screen(Screen):
    pass


class Question4Screen(Screen):
    pass


class InfoScreen(Screen):
    pass


class BadgeScreen(Screen):
    pass


class GreenBadgeScreen(Screen):
    pass


class YellowBadgeScreen(Screen):
    pass


class RedBadgeScreen(Screen):
    pass


class AccountTypeScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(RegisterScreen(name="register"))
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(Question1Screen(name="Question1"))
sm.add_widget(Question2Screen(name="Question2"))
sm.add_widget(Question3Screen(name="Question3"))
sm.add_widget(Question4Screen(name="Question4"))
sm.add_widget(InfoScreen(name="info"))
sm.add_widget(BadgeScreen(name="badge"))
sm.add_widget(GreenBadgeScreen(name="green"))
sm.add_widget(YellowBadgeScreen(name="yellow"))
sm.add_widget(RedBadgeScreen(name="red"))


class COVIDApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"
        screen = Builder.load_string(COVID)

        return screen


COVIDApp().run()


