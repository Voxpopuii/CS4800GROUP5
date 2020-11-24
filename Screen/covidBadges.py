#Author: Miranda Humphreys
#Pair Reviewed with: John Clarke Miego

#Badge Screens
#Green badge screen
<GreenBadgeScreen>:
    name: "green"
    MDToolbar:
        title: "Green Badge"
        pos_hint: {"top": 1}
    MDLabel:
        text: "Cleared to go back to work"
    Image:
        source: ""
        size_hint_y: None
        height: 620

#Yellow badge screen
<YellowBadgeScreen>:
    name: "yellow"
    MDToolbar:
        title: "Yellow Badge"
        pos_hint: {"top": 1}
    MDLabel:
        text: "Please quarantine for 14 days"
    Image:
        source: ""
        size_hint_y: None
        height: 620

#Red badge screen 
<RedBadgeScreen>:
    name: "red"
    MDToolbar:
        title: "Yellow Badge"
        pos_hint: {"top": 1}
    MDLabel:
        text: "Get tested immediately and follow cdc guidelines since you're showing symptoms"
    Image:
        source: ""
        size_hint_y: None
        height: 620
"""