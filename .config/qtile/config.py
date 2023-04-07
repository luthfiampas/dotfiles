# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key(
        [mod],
        "left",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key(
        [mod],
        "right",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key(
        [mod],
        "down",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key(
        [mod],
        "up",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    Key(
        [mod],
        "space",
        lazy.group.next_window(),
        desc="Move window focus to other window",
    ),
    Key(
        [mod, "control"],
        "space",
        lazy.window.bring_to_front(),
        desc="Bring floating window to front",
    ),
    Key(
        [mod, "shift"],
        "left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key(
        [mod, "shift"],
        "down",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key(
        [mod, "shift"],
        "up",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),
    Key(
        [mod, "control"],
        "up",
        lazy.layout.grow(),
        desc="Grow MonadTall window"
    ),
    Key(
        [mod, "control"],
        "down",
        lazy.layout.shrink(),
        desc="Shrink MonadTall window"
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
    ),
    Key(
        [mod],
        "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),
    Key(
        [mod],
        "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    Key(
        [mod],
        "x",
        lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key(
        [mod, "control"],
        "r",
        lazy.reload_config(),
        desc="Reload the config"
    ),
    Key(
        [mod, "control"],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),
    Key(
        [mod],
        "p",
        lazy.spawn("dmenu_run"),
        desc="Run suckless dmenu"
    ),
    Key(
        [],
        "Print",
        lazy.spawn("flameshot gui"),
        desc="Take a screenshot using flameshot"
    ),
    Key(
        [mod],
        "f",
        lazy.window.toggle_floating(),
        desc="Toggle floating window",
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_props = dict(
    border_normal="#282a36",
    border_focus="#50fa7b",
    border_width=2,
    margin=4
)

layouts = [
    layout.MonadTall(**layout_props),
    layout.MonadWide(**layout_props),
    layout.Max(**layout_props),
    # layout.Floating(**layout_props),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(**layout_props),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=12,
    padding=4,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(scale=0.6),
                widget.GroupBox(
                    disable_drag=True,
                    highlight_method='line',
                    highlight_color=["#6272a4", "#44475a"]
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(icon_size=14, padding=10),
                widget.Spacer(length=10),
                widget.Memory(
                    format=" Mem:{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} ",
                    #background="#bd93f9",
                    #foreground="#bd93f9"
                ),
                widget.PulseVolume(
                    #background="#ff79c6",
                    #foreground="#bd93f9",
                    fmt=" Vol: {} "
                ),
                widget.Clock(
                    format=" %Y-%m-%d %a %H:%M ",
                    #background="#bd93f9",
                    #foreground="#bd93f9"
                ),
            ],
            20,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click(
        [mod],
        "Button2",
        lazy.window.bring_to_front()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **layout_props,
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
