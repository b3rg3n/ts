################################################################################
## MUSIC ROOM DECLARATION
################################################################################
init python:
    #################### STEP 1: Set up the music room.
    ## You can make multiple music rooms consisting of different sets of tracks,
    ## if you so desire, or use one music room for all your music. You only need
    ## to pass in the name of the ExtendedMusicRoom object you set up here to
    ## the music room screens below.

    ## You can pass any of the following arguments to ExtendedMusicRoom:
    ## channel: The channel to play the music on. Defaults to 'music'.
    ## fadeout: The time in seconds to fade out the old song when changing
    ##          tracks. Defaults to 0.0 (no fade).
    ## fadein: The time in seconds to fade in the new song when changing tracks.
    ##         Defaults to 0.0 (no fade).
    ## loop: Whether to loop the music when reaching the end of the track list.
    ##       Defaults to True and can be toggled in the music room with a
    ##       button.
    ## single_track: If True, only a single track will loop. Defaults to False
    ##               and can be toggled in the music room with a button.
    ## shuffle: Whether to shuffle the tracks or play them in default order.
    ##          Defaults to False and can be toggled in the music room with a
    ##          button.
    ## stop_action: A screen action to run when the music stops. Defaults to
    ##              None, so no action is run.
    ## alphabetical : If True, the tracks will be sorted alphabetically.
    ##                If False, the default, they will be arranged in the order
    ##                they are added to the music room in.
    music_room = ExtendedMusicRoom(channel='music', fadeout=0.0, fadein=0.0,
        loop=True, single_track=False, shuffle=False, stop_action=None,
        alphabetical=True)

    ## This sets up a default art image for all tracks in this room which aren't
    ## given a more specific one. This default art is 600x600, but several
    ## layouts resize it. It should typically be square.
    music_room.default_art = ts_gui + "music_room/cover_art.webp"

################################################################################
## CONFIGURATION VALUES
################################################################################
## Set this to True if you want to unlock all tracks in the music room during
## development. Set it to False to test the unlock conditions. Tracks will
## automatically obey unlock rules in a distribution regardless of the value
## of this configuration variable.
define myconfig.UNLOCK_TRACKS_FOR_DEVELOPMENT = False

################################################################################
## IMAGES & DEFINITIONS
################################################################################
## These colours are used by the colorize_button transform in the screens below
## to colorize the default music controls. You can change these if you want to
## use the provided images, or simply supply your own and remove the lines
## `at colorize_button` from the screen below.
define MUSIC_ROOM_IDLE_COLOR = "#ffffff"
define MUSIC_ROOM_HOVER_COLOR = "#f93c3e"
define MUSIC_ROOM_SELECTED_IDLE_COLOR = "#ffffff"
define MUSIC_ROOM_SELECTED_HOVER_COLOR = "#f93c3e"
define MUSIC_ROOM_INSENSITIVE_COLOR = "#888"

## Here are the default buttons used for the music controls below. You can
## update these or replace them.
image play_button = ts_gui + "music_room/play.webp"
image pause_button = ts_gui + "music_room/pause.webp"
image next_button = ts_gui + "music_room/next.webp"
image prev_button = Transform(ts_gui + "music_room/next.webp", xzoom=-1.0)
image repeat_all_button = ts_gui + "music_room/repeat all.webp"
## Note that this image is just a foreground on top of the repeat_all button!
image repeat_one_button = ts_gui + "music_room/repeat 1.webp"
image shuffle_button = ts_gui + "music_room/shuffle.webp"
image back_10_button = ts_gui + "music_room/back_10.webp"
image forward_10_button = ts_gui + "music_room/forward_10.webp"

## The "audio level" bars. These are optional to show next to the currently
## playing song. There are four bars that randomly change height.
define AUDIO_BAR_HEIGHT = 30
define AUDIO_BAR_WIDTH = 8
image audio_bar = Transform(MUSIC_ROOM_HOVER_COLOR,
    xysize=(AUDIO_BAR_WIDTH, AUDIO_BAR_HEIGHT))
transform audio_bar_move():
    yzoom renpy.random.random() ## Start at a random height
    block:
        ## Choose a random height to be
        choice:
            ease 0.2 yzoom 1.0
        choice:
            ease 0.2 yzoom 0.2
        choice:
            ease 0.2 yzoom 0.8
        choice:
            ease 0.2 yzoom 0.0
        choice:
            ease 0.2 yzoom 0.5
        repeat
## The final audio bars image, with four bars that randomly change height.
image audio_bars = HBox(
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    yalign=1.0, ysize=AUDIO_BAR_HEIGHT,
)

################################################################################
## TRANSFORMS
################################################################################
## A transform that makes it easier to apply colours to the various buttons.
## The default images are black, so it uses ColorizeMatrix to colorize them.
## The colours are defined at the top of the file.
transform colorize_button(idle=MUSIC_ROOM_IDLE_COLOR,
        hover=MUSIC_ROOM_HOVER_COLOR,
        selected_idle=MUSIC_ROOM_SELECTED_IDLE_COLOR,
        selected_hover=MUSIC_ROOM_SELECTED_HOVER_COLOR,
        insensitive=MUSIC_ROOM_INSENSITIVE_COLOR):
    matrixcolor ColorizeMatrix(insensitive, "#fff")
    on idle:
        matrixcolor ColorizeMatrix(idle, "#fff")
    on hover:
        matrixcolor ColorizeMatrix(hover, "#fff")
    on insensitive:
        matrixcolor ColorizeMatrix(insensitive, "#fff")
    on selected_idle:
        matrixcolor ColorizeMatrix(selected_idle, "#fff")
    on selected_hover:
        matrixcolor ColorizeMatrix(selected_hover, "#fff")

## A simple transform to easily resize buttons. Used by some layouts.
transform zoom_button(z):
    zoom z

################################################################################
## SCREENS - VERSION 1
################################################################################
## Note! This music room gets passed in an ExtendedMusicRoom object as declared
## earlier. If you wanted to have multiple music rooms, you would need to
## declare multiple ExtendedMusicRoom objects, and you would pass those into
## the music_room screen to use.
screen music_room(mr):

    tag menu

    ## Needed to have easy access to information on the currently playing song.
    ## Required for ALL music rooms!
    ## If you'd like to begin the music room without any songs playing, remove
    ## this line and include the following three lines:
    # on 'show' action Stop(mr.channel)
    # on 'replace' action Stop(mr.channel)
    # default current_track = None
    ## Setting current_track to mr.get_current_song() as seen here will make it
    ## pick out whichever song is currently playing (e.g. the main menu track).
    default current_track = mr.get_current_song()

    style_prefix "music_room"

    add ts_images + "anim/zatemnenie.webp"#"#292835" ## The background image

    ## To return to the main menu
    textbutton translation_new["Back"] action Return() activate_sound start_sound_suka hover_sound button_menu align (0.0, 1.0) text_size 40: #_("Return")
        left_margin 17 bottom_margin 17 #25

    ## Buttons to go to the different layouts. Remove once you've decided
    ## on which layout to use.
    #use select_music_room_layout(mr, left_margin=133, align=(0.0, 1.0)) #200

    ## The track list. These are displayed either in the order they were added
    ## to the music room in or in alphabetical order, depending on whether
    ## alphabetical sorting was turned on or not. You can arrange this however
    ## you like, with whichever information you like!
    frame:
        style_prefix 'track_list'
        xsize 500 left_margin 17 top_margin 17 #750, 25
        viewport:
            mousewheel True scrollbars "vertical" draggable True
            has vbox
            label translation_new["ts_menu_mus2"] style "music_room_title"#_("Track List") style "music_room_title"
            ## get_tracklist takes one argument, all_tracks. If all_tracks is
            ## True, it shows all tracks, including locked ones (which will be
            ## shown grayed out). If all_tracks is False, it only shows unlocked
            ## tracks.
            for num, song in enumerate(mr.get_tracklist(all_tracks=True)):
                button:
                    action mr.Play(song.path)
                    activate_sound start_sound_suka
                    hover_sound button_menu
                    has hbox
                    fixed:
                        if song is current_track:
                            ## If the song is currently playing, add a bit of
                            ## flair with some audio bars.
                            add Transform('audio_bars', ysize=20, xalign=0.5, #30
                                yzoom=-1.0, yalign=0.55)
                        else:
                            ## The track number. +1 is because enumerate starts
                            ## at 0 instead of 1.
                            text str(num+1) align (0.5, 0.55)
                    vbox:
                        spacing 3 #
                        ## Track info
                        label song.name
                        text song.artist

    ## This holds the album art, song title, artist, music bar, and music
    ## controls. You may adjust this however you wish! The important part
    ## is generally the actions on the buttons, and the music bar is special
    ## so you can click it to seek in the song.
    frame:
        right_margin 30 background None #45
        xalign 1.0 yalign 0.0
        has vbox
        if current_track:
            add current_track.art xalign 0.5 ysize 293 fit "contain" #440
            text current_track.name
            text current_track.artist
            ## Include more fields if you like e.g.
            # text current_track.description
        else:
            ## To maintain sizing, the default art is shown at alpha 0.0.
            ## You can also just include it without the alpha 0.0 to display
            ## it regardless of whether a track is playing or not.
            add mr.default_art xalign 0.5 alpha 0.0 ysize 293 fit "contain" #440
            text "" # This represents the space taken up by the song title
            text translation_new["ts_menu_mus1"]#_("No song playing")

        hbox:
            spacing 8
            ## This fixed (and the duration one below it) ensure that the
            ## pos and duration text don't change size as the text updates
            ## (which could move the hbox around since it's center-aligned).
            fixed:
                yfit True xsize 100
                add mr.get_pos(style="music_room_pos")
            ## This makes a special music bar which shows the current position
            ## of the song, and also allows you to click the bar to skip around.
            ## It takes the same style properties as a regular bar, and in this
            ## case even gets the style "music_room_bar" because of the style
            ## prefix.
            ## It needs to be passed the music room - in our case, that's
            ## `room mr` because the music room is passed in as "mr".
            music_bar room mr
            ## Again, this fixed helps keep the hbox from changing size.
            fixed:
                yfit True xsize 100
                add mr.get_duration(style="music_room_duration")

        ## This contains the music controls. You can remove whichever ones
        ## you don't need.
        hbox:
            ################## Back 10 seconds button ##################
            #imagebutton:
            #    idle "back_10_button"
                ## This automatically colorizes the button. If you are supplying
                ## your own images, you can remove any `at` ATL transforms to
                ## these buttons.
            #    at colorize_button()
            #    action mr.AdjustTrackPos(-10)
            #    activate_sound start_sound_suka
            #    hover_sound button_menu
            ################## Shuffle button ##################
            imagebutton:
                idle "shuffle_button"
                at colorize_button(MUSIC_ROOM_INSENSITIVE_COLOR, MUSIC_ROOM_IDLE_COLOR)
                action mr.ToggleShuffle()
                activate_sound start_sound_suka
                hover_sound button_menu
            ################## Previous, play/pause, next buttons ##################
            imagebutton:
                idle "prev_button"
                at colorize_button()
                action mr.Previous()
                activate_sound start_sound_suka
                hover_sound button_menu
            imagebutton:
                at colorize_button()
                idle "pause_button" hover "pause_button"
                selected_idle "play_button" selected_hover "play_button"
                action mr.PlayAction()
                activate_sound start_sound_suka
                hover_sound button_menu
            imagebutton:
                idle "next_button"
                at colorize_button()
                action mr.Next()
                activate_sound start_sound_suka
                hover_sound button_menu
            ################## Repeat all, repeat one buttons ##################
            imagebutton:
                at colorize_button(idle=MUSIC_ROOM_INSENSITIVE_COLOR,
                    hover=MUSIC_ROOM_IDLE_COLOR)
                idle "repeat_all_button"
                if mr.single_track:
                    foreground "repeat_one_button"
                action mr.CycleLoop()
                activate_sound start_sound_suka
                hover_sound button_menu
            ################## Forward 10 seconds button ##################
            #imagebutton:
            #    idle "forward_10_button"
            #    at colorize_button()
            #    action mr.AdjustTrackPos(10)
            #    activate_sound start_sound_suka
            #    hover_sound button_menu

################################################################################
## Styles for Music Room 1
################################################################################
style music_room_vbox:
    ycenter 0.5 spacing 17 #25
style music_room_frame:
    background "#21212d"
    yalign 0.5 xalign 0.0
    left_margin 17 padding (17, 17) #25
style music_room_text:
    color "#fff"
    xalign 0.5
style music_room_title:
    background None xalign 0.5 bottom_padding 10 #15
style music_room_title_text:
    font cit_font#gui.name_text_font
    size 33 color "#ffffff" xalign 0.5 #50
style music_room_hbox:
    spacing 33 xalign 0.5 yalign 1.0 #50
style music_room_image_button:
    align (0.5, 0.5)
style music_room_bar:
    xsize 467 xalign 0.5 ysize 25 #700, 38
    right_bar "#21212d"
    left_bar "#ffffff"
style music_room_pos:
    color "#fff" xalign 0.5 adjust_spacing False
style music_room_duration:
    color "#fff" xalign 0.5 adjust_spacing False

################################################################################
## Styles for the track list, shared generally by the other rooms.
################################################################################
style track_list_frame:
    background "#21212d00"
    yalign 0.0 xalign 0.0
    padding (25, 25)
style track_list_viewport:
    xfill False yfill False ymaximum config.screen_height-200
style track_list_side:
    spacing 20
style track_list_vbox:
    spacing 0
style track_list_button:
    right_padding 30 #45
    background Transform("#ffffff", ysize=2, yalign=1.0)
    hover_foreground "#fff1"
    ypadding 10 xfill True #15
style track_list_hbox:
    xalign 0.0 spacing 12 #18
style track_list_fixed:
    xsize 45 ysize 45 yalign 0.5 #45
style track_list_text:
    font cit_font
    color "#bfbfb9"
    insensitive_color "#666"
style track_list_label:
    background None padding (2, 0)
style track_list_label_text:
    color "#f7f7ed" hover_color "#f93c3e" selected_color "#ffffff"
    insensitive_color "#666"
style track_list_vscrollbar:
    thumb "#ffffff" base_bar "#292835"
