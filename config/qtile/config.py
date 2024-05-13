    
#       █████████     ███████    ███████████ █████ █████ ███████████ █████ █████       ██████████
#      ███░░░░░███  ███░░░░░███ ░█░░░░░░███ ░░███ ░░███ ░█░░░███░░░█░░███ ░░███       ░░███░░░░░█
#     ███     ░░░  ███     ░░███░     ███░   ░░███ ███  ░   ░███  ░  ░███  ░███        ░███  █ ░ 
#    ░███         ░███      ░███     ███      ░░█████       ░███     ░███  ░███        ░██████   
#    ░███         ░███      ░███    ███        ░░███        ░███     ░███  ░███        ░███░░█   
#    ░░███     ███░░███     ███   ████     █    ░███        ░███     ░███  ░███      █ ░███ ░   █
#     ░░█████████  ░░░███████░   ███████████    █████       █████    █████ ███████████ ██████████
#      ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░    ░░░░░       ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░ 
#
#                                                                                    - DARKKAL44
  


from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

mod = "mod4"
terminal = "alacritty"

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█




keys = [

#  D E F A U L T

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using a prompt widget"),
    # Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu'),
    # Key([mod], "t", lazy.spawn("sh -c ~/.config/rofi/scripts/themes"), desc='theme_switcher'),
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle Floating on the window'),

# C U S T O M

    Key([mod], "up", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([mod], "down", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([mod, "shift"], "M", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    #Key([mod], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    #Key([mod], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    #Key([mod], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([mod, "shift"], "B", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([mod, "control"], "B", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    #Key([mod],"e", lazy.spawn("thunar"), desc='file manager'),
	#Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
    Key([mod, "shift"], "o", lazy.spawn("picom"), desc='Enable Transparency'),
    Key([mod, "control"], "o", lazy.spawn("killall picom"), desc='Disable Transparency'),
]



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

groups = []
# This function is a helper to keep each group on its own screen for a multi monitor setup
def go_to_group(name):
    def f(qtile):
        if int(name) < 4:
            screen_index = 0
        elif int(name) < 7:
            screen_index = 1
        else:
            screen_index = 2
        qtile.cmd_to_screen(screen_index)
        qtile.groups_map[name].cmd_toscreen()
    return f

# Create groups
for name in map(str, range(1, 9 + 1)):
    # Create a group
    groups.append(Group(
        name=name,
        layout="columns",
        label=name, #"󰏃"
        ))
    # Add keybindings for the group
    keys.extend([
        Key([mod], name, lazy.function(go_to_group(name))),
        Key([mod, 'shift'], name, lazy.window.togroup(name)),
        ])
#groups = [Group(f"{i+1}", label="󰏃") for i in range(8)]
# Default Groups config for qtile cozytile
#for i in groups:
#    keys.extend(
#            [
#                Key(
#                    [mod],
#                    i.name,
#                    lazy.group[i.name].toscreen(),
#                    desc="Switch to group {}".format(i.name),
#                    ),
#                Key(
#                    [mod, "shift"],
#                    i.name,
#                    lazy.window.togroup(i.name, switch_group=True),
#                    desc="Switch to & move focused window to group {}".format(i.name),
#                    ),
#                ]
#            )
#



# L A Y O U T S




layouts = [
    layout.Columns(border_focus="#9ccfd8",
        border_normal="#31748f", 
        border_width=1, 
        margin=8,
    ),

    layout.Max(	border_focus='#9ccfd8',
	    border_normal='#31748f',
	    margin=10,
	    border_width=0,
    ),

    #layout.Floating(	border_focus='#1F1D2E',
	#    border_normal='#1F1D2E',
	#    margin=10,
	#    border_width=0,
	#),
    ## Try more layouts by unleashing below layouts
   ##  layout.Stack(num_stacks=2),
   ##  layout.Bsp(),
    # layout.Matrix(	border_focus='#1F1D2E',
	#    border_normal='#1F1D2E',
	#    margin=10,
	#    border_width=0,
	#),
    # layout.MonadTall(	border_focus='#1F1D2E',
	#    border_normal='#1F1D2E',
    #    margin=10,
	#    border_width=0,
	#),
    #layout.MonadWide(	border_focus='#1F1D2E',
	#    border_normal='#1F1D2E',
	#    margin=10,
	#    border_width=0,
	#),
   ##  layout.RatioTile(),
    # layout.Tile(	border_focus='#1F1D2E',
	#    border_normal='#1F1D2E',
    #),
   ##  layout.TreeTab(),
   ##  layout.VerticalTile(),
   ##  layout.Zoomy(),
]



widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = [ widget_defaults.copy()
        ]



def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")

# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄


def getWidgets(showTray, monitor):
    sysTray = []
    if showTray:
        sysTray = [
                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),
                widget.Systray(
                    background='#282738',
                    fontsize=2,
                ),
                widget.TextBox(
                    text=' ',
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#353446',
                ),
        ]
    
    if monitor == 1:
        visible_groups = ['1', '2', '3']
    elif monitor == 2:
        visible_groups = ['4', '5', '6']
    else:
        visible_groups = ['7', '8', '9']
    return  [
				widget.Spacer(length=15,
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1":power},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),


                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method='block',
                    active='#91B1F0',
                    block_highlight_text_color="#f678ff",
                    highlight_color='#4B427E',
                    inactive='#282738',
                    foreground='#4B427E',
                    background='#353446',
                    this_current_screen_border='#353446',
                    this_screen_border='#353446',
                    other_current_screen_border='#353446',
                    other_screen_border='#353446',
                    urgent_border='#353446',
                    rounded=True,
                    disable_drag=True,
                 ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                ),


                widget.CurrentLayout(
                    background='#353446',
                    foreground='#CAA9E0',
                    fmt='{}',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background='#282738',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground='#CAA9E0',
                    mouse_callbacks={"Button1": search},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),


                widget.WindowName(
                    background = '#353446',
                    format = "{name}",
                    font='JetBrains Mono Bold',
                    foreground='#CAA9E0',
                    empty_group_string = 'Desktop',
                    fontsize=13,

                ),


                *sysTray,
                
                widget.Volume(
                    font='JetBrainsMono Nerd Font',
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background='#353446',
                ),


                widget.Spacer(
                    length=-5,
                    background='#353446',
                    ),


                widget.Volume(
                    font='JetBrains Mono Bold',
                    background='#353446',
                    foreground='#CAA9E0',
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#282738',
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%I:%M %p',
                    background='#282738',
                    foreground='#CAA9E0',
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),


                widget.Spacer(
                    length=18,
                    background='#282738',
                ),



            ],
screens = [

    Screen(
        top=bar.Bar( 
            *getWidgets(True, 1),
            30,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [15,60,6,60],

        ),
    ),
    Screen(
        top=bar.Bar( 
            *getWidgets(False, 2),
            30,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [15,60,6,60],

        ),
    ),
    Screen(
        top=bar.Bar( 
            *getWidgets(False, 3),
            30,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [15,60,6,60],

        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus='#1F1D2E',
	border_normal='#1F1D2E',
	border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)




from libqtile import hook
# some other imports
import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.call([home])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



# E O F
