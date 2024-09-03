####ГЛИТЧИ БЛЯ ИЗ ОРИГА

####МОНИКА
image monika g1:
    ts_monika_pt + "g1.webp"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g1loop:
    ts_monika_pt + "g1.webp"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat


image monika g2:
    block:
        choice:
            ts_monika_pt + "g2.webp"
        choice:
            ts_monika_pt + "g3.webp"
        choice:
            ts_monika_pt + "g4.webp"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

####ЮРЕЦ
image y_glitch_head:
    ts_yuri_pt + "za.webp"
    0.15
    ts_yuri_pt + "zb.webp"
    0.15
    ts_yuri_pt + "zc.webp"
    0.15
    ts_yuri_pt + "zd.webp"
    0.15
    repeat

image yuri stab_1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "stab/1.webp") )

image yuri stab_2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "stab/2.webp") )

image yuri stab_3 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/3.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/3.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/3.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "stab/3.webp") )

image yuri stab_4 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/4.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/4.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/4.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "stab/4.webp") )

image yuri stab_5 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/5.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/5.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "stab/5.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "stab/5.webp") )


image yuri stab_6 = LiveComposite((960,960), (0, 0), ts_yuri_pt + "stab/6-mask.webp", (0, 0), "yuri stab_6_eyes", (0, 0), ts_yuri_pt + "stab/6.webp")

image yuri stab_6_eyes:
    ts_yuri_pt + "stab/6-eyes.webp"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "oneeye.webp", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    ts_yuri_pt + "oneeye2.webp"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    ts_yuri_pt + "glitch1.webp"
    pause 0.1
    ts_yuri_pt + "glitch2.webp"
    pause 0.1
    ts_yuri_pt + "glitch3.webp"
    pause 0.1
    ts_yuri_pt + "glitch4.webp"
    pause 0.1
    ts_yuri_pt + "glitch5.webp"
    pause 0.1
    repeat
image yuri glitch2:
    ts_yuri_pt + "0a.webp"
    pause 0.1
    ts_yuri_pt + "0b.webp"
    pause 0.5
    ts_yuri_pt + "0a.webp"
    pause 0.3
    ts_yuri_pt + "0b.webp"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), ts_yuri_pt + "eyes1.webp", (0, 0), "yuripupils")

image yuri eyes_base = ts_yuri_pt + "eyes1.webp"

image yuripupils:
    ts_yuri_pt + "eyes2.webp"
    yuripupils_move

image yuri cuts = ts_yuri_pt + "cuts.webp"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        ts_yuri_pt + "dragon1.webp"
        0.01
        ts_yuri_pt + "dragon2.webp"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

####НАЦУКИ
image natsuki mouth = LiveComposite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "0.webp", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image ts_glaza_yrec = LiveComposite((960, 960), (403, 390), "n_rects_mouth", (470, 389), "n_rects_mouth")
image ts_glaza = LiveComposite((960, 960), (420, 420), "n_rects_mouth", (500, 414), "n_rects_mouth")
image ts_glaza_k = LiveComposite((960, 960), (420, 470), "n_rects_mouth", (500, 464), "n_rects_mouth")


image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    ts_natsuki_pt + "mouth.webp"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    ts_natsuki_pt + "ghost_blood.webp" with ImageDissolve("mod_assets/source/images/anim/transit/wipedown.webp", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    ts_natsuki_pt + "ghost1.webp"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image(ts_natsuki_pt + "ghost2.webp")
image natsuki ghost3 = Image(ts_natsuki_pt + "ghost3.webp")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    ts_natsuki_pt + "glitch1.webp"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "scream.webp")

image natsuki screamnohead = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l1.webp", (0, 0), ts_natsuki_pt + "1r.webp")
image natscreamhead = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "scream1.webp")

image natsuki vomit = ts_natsuki_pt + "vomit.webp"

image n_blackeyes = "images/natsuki/blackeyes.webp"
image n_eye = "images/natsuki/eye.webp"

####САЁРИ
image sayori glitch:
    ts_sayori_pt + "glitch1.webp"
    pause 0.01666
    ts_sayori_pt + "glitch2.webp"
    pause 0.01666
    repeat

image sayori glazkam_pizda = im.Composite((960, 960), (0, 0), ts_sayori_pt + "s_glazkam_pizda.webp")
image sayori glazkam_pizda1 = im.Composite((960, 960), (0, 0), ts_sayori_pt + "s_glazkam_pizda1.webp")