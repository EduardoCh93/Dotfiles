from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

fuente = 'VictorMono'
fuenteWidget = 'Hack Nerd Font'
tamanioFuente = 12
backgroundColor = "#0f101a"
interface = 'wlan0'

def separator():
    return widget.Sep(foreground = backgroundColor,
                        background = backgroundColor,
                        linewidth = 0,
                        padding = 3)


def icon(bg, fontsize=16, text="?"):
    return widget.TextBox(
        background = bg,
        foreground = '#000000',
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(color1, color2):
    return widget.TextBox(
        background = color2,
        foreground = color1,
        font = fuenteWidget,
        text="", # Icon: nf-oct-triangle_left
        fontsize=43,
        padding=-6,
    )


def workspaces(): 
    return [
        widget.GroupBox(
            font='Victor Mono',
            highlight_method='line',
            border_width = 2,
            active = colors['active'],
            inactive = colors['inactive'],
            disable_drag = False,
            fontsize = 19,
            background = backgroundColor,
            this_current_screen_border = '#bd93f9'
        ),
        separator(),
        widget.WindowName(
            background = backgroundColor,
            fontsize = 12
        ),
        separator(),
]


primary_widgets = [
    *workspaces(),
    #Updates
    powerline(colors['color4'], backgroundColor),
    icon(bg=colors['color4'], text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        distro='Arch',
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
        padding = 10,
    ),

    #Wifi
    powerline(colors['color3'],colors['color4']),
    icon(bg=colors['color3'], text=' '),  # Icon: nf-fa-feed
    widget.Net(
        interface='wlp1s0',
        background=colors['color3'], 
        foreground='#000000',
        format='{up} - {down}', #  nf-cod-arrow_up,  nf-cod-arrow_down
        use_bits='true',
        padding = 10,
    ),
    
    # Ventanas
    powerline(colors['color2'], colors['color3']),
    widget.CurrentLayoutIcon(
        background = colors['color2'],
        scale = 0.5,
        padding = 2,
    ),
    widget.CurrentLayout(
        background=colors['color2'], 
        foreground = '#000000',
        padding = 10,
    ),
    # Fecha
    powerline(colors['color1'], colors['color2']),
    icon(bg=colors['color1'], fontsize=20, text=''), # Icon: nf-mdi-calendar_clock
    widget.Clock(
        background = colors['color1'],
        foreground ='#000000',
        format ='%d/%m/%Y %A %H:%M ',
        padding = 10,
    ),
    #Volume
    powerline(colors['color0'], colors['color1']),
    widget.Volume(
        background = colors['color0'],
        foreground = '#000000',
        check_mute_string = '[ﱝ]',
        limit_max_volume = True,
        fmt = 'Vol: {}'
    ),
    widget.Systray(
        background=colors['color0'],
        padding=5),
    separator(),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    # powerline('color1', 'dark'),
    # widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    # widget.CurrentLayout(**base(bg='color1'), padding=5),
    # powerline('color2', 'color1'),
    # widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
    # powerline('dark', 'color2'),
]

widget_defaults = {
    'font': fuente,
    'fontsize': tamanioFuente,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()
