# THEME SETTINGS

font_family     = "MartianMono Nerd Font"
font_weight     = "Medium"
font_size       = 12
border_size     = 2
inner_gap       = 5
outter_gap      = 4
panel_size      = 24
panel_margin    = [outter_gap, 0, 0, 0]
widget_padding  = 8
widget_margin   = 0

colors = {
        "background": "#080808",
        "foreground": "#bdbdbd",
        "disabled": "#323437",
        "accent": "#cc2850",
        }

borders = {
        "margin" : inner_gap,
        "single_margin" : inner_gap,
        "border_width" : border_size,
        "border_on_single" : True,
        "border_focus" : colors["accent"],
        "border_normal" : colors["disabled"],
        }

widget_defaults = {
        "font" : font_family + " " + font_weight,
        "fontsize" : font_size,
        "padding" : widget_padding,
        "margin" : widget_margin,
        "foreground" : colors["foreground"]
        }

sp_size = {
        "width" : 0.6,
        "height" : 0.6,
        "x" : 0.2,
        "y" : 0.2,
        "opacity" : 1
        }
