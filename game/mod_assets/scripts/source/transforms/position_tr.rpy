# TRUE STORY SCREEN TRANSFORMS
# by @b3rg3n & @superrage & @dansalvato
# Since 2024

# небольшое пояснение по анимациям спрайтов на будущее:
# xx - 11, 22, 33, 44, 55, 66 и прочее
# fxx - фокус на персонаже (т.е. из обычного положения он чуть больше становится и остаётся в этом положении)
# sxx - приседает (не юзать два и более раз подряд - он тпхается на исходную и приседает ещё раз (колхоз кароче пиздец) - если нужно дважды сделать анимацию, но шоп она была "грустная" использую между s - d)
# dxx - приседает и возвращается на исходную
# hxx - подпрыгивает и возвращается на исходную
# txx - просто спавнится на позиции с диссолвом и двигает если уже есть спрайт на одном месте
# ixx - тот же самый t, только без диссолва (т.е. мгновенный) и без сдвига

# rightin - влетает справа
# rightout - вылетает вправо
# leftin - влетает слева

# используем так - show sayori 1a at s11 условно

# про цифры:
# 11 - только одна позиция по центру
# 21, 22 - две позиции
# 31, 32, 33 - три позиции
# 41, 42, 43, 44 - четыре позиции
# 51, 52, 53, 54, 55 - пять позиций
# 61, 62, 63, 64, 65, 66 - шесть позиций

# ПОЗИЦИИ T
transform t61:
    tcommon(113)
transform t62:
    tcommon(326)
transform t63:
    tcommon(500)
transform t64:
    tcommon(758)
transform t65:
    tcommon(966)
transform t66:
    tcommon(1200)
transform t51:
    tcommon(100)
transform t52:
    tcommon(380)
transform t53:
    tcommon(640)
transform t54:
    tcommon(940)
transform t55:
    tcommon(1180)
transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)

# ПОЗИЦИИ I

transform i61:
    tinstant(113)
transform i62:
    tinstant(326)
transform i63:
    tinstant(500)
transform i64:
    tinstant(758)
transform i65:
    tinstant(966)
transform i66:
    tinstant(1200)
transform i51:
    tinstant(100)
transform i52:
    tinstant(380)
transform i53:
    tinstant(640)
transform i54:
    tinstant(940)
transform i55:
    tinstant(1180)
transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)

# ПОЗИЦИИ F

transform f61:
    focus(113)
transform f62:
    focus(326)
transform f63:
    focus(500)
transform f64:
    focus(758)
transform f65:
    focus(966)
transform f66:
    focus(1200)
transform f51:
    focus(100)
transform f52:
    focus(380)
transform f53:
    focus(640)
transform f54:
    focus(940)
transform f55:
    focus(1180)
transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)

# ПОЗИЦИИ S

transform s61:
    sink(113)
transform s62:
    sink(326)
transform s63:
    sink(500)
transform s64:
    sink(758)
transform s65:
    sink(966)
transform s66:
    sink(1200)
transform s51:
    sink(100)
transform s52:
    sink(380)
transform s53:
    sink(640)
transform s54:
    sink(940)
transform s55:
    sink(1180)
transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)

# ПОЗИЦИИ H

transform h61:
    hop(113)
transform h62:
    hop(326)
transform h63:
    hop(500)
transform h64:
    hop(758)
transform h65:
    hop(966)
transform h66:
    hop(1200)
transform h51:
    hop(100)
transform h52:
    hop(380)
transform h53:
    hop(640)
transform h54:
    hop(940)
transform h55:
    hop(1180)
transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)

# ПОЗИЦИИ HF
transform hf61:
    hopfocus(113)
transform hf62:
    hopfocus(326)
transform hf63:
    hopfocus(500)
transform hf64:
    hopfocus(758)
transform hf65:
    hopfocus(966)
transform hf66:
    hopfocus(1200)
transform hf51:
    hopfocus(100)
transform hf52:
    hopfocus(380)
transform hf53:
    hopfocus(640)
transform hf54:
    hopfocus(940)
transform hf55:
    hopfocus(1180)
transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)

# ПОЗИЦИИ D
transform d61:
    dip(113)
transform d62:
    dip(326)
transform d63:
    dip(500)
transform d64:
    dip(758)
transform d65:
    dip(966)
transform d66:
    dip(1200)
transform d51:
    dip(100)
transform d52:
    dip(380)
transform d53:
    dip(640)
transform d54:
    dip(940)
transform d55:
    dip(1180)
transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)

# LEFTIN
transform ln41:
    ts_leftin(1.0, 200)
transform ln42:
    ts_leftin(1.0, 493)
transform ln43:
    ts_leftin(1.0, 786)
transform ln44:
    ts_leftin(1.0, 1080)
transform ln31:
    ts_leftin(1.0, 240)
transform ln32:
    ts_leftin(1.0, 640)
transform ln33:
    ts_leftin(1.0, 1040)
transform ln21:
    ts_leftin(1.0, 400)
transform ln22:
    ts_leftin(1.0, 880)
transform ln11:
    ts_leftin(1.0, 640)

transform lf41:
    ts_leftin(0.5, 200)
transform lf42:
    ts_leftin(0.5, 493)
transform lf43:
    ts_leftin(0.5, 786)
transform lf44:
    ts_leftin(0.5, 1080)
transform lf31:
    ts_leftin(0.5, 240)
transform lf32:
    ts_leftin(0.5, 640)
transform lf33:
    ts_leftin(0.5, 1040)
transform lf21:
    ts_leftin(0.5, 400)
transform lf22:
    ts_leftin(0.5, 880)
transform lf11:
    ts_leftin(0.5, 640)

transform ls41:
    ts_leftin(1.5, 200)
transform ls42:
    ts_leftin(1.5, 493)
transform ls43:
    ts_leftin(1.5, 786)
transform ls44:
    ts_leftin(1.5, 1080)
transform ls31:
    ts_leftin(1.5, 240)
transform ls32:
    ts_leftin(1.5, 640)
transform ls33:
    ts_leftin(1.5, 1040)
transform ls21:
    ts_leftin(1.5, 400)
transform ls22:
    ts_leftin(1.5, 880)
transform ls11:
    ts_leftin(1.5, 640)

transform lss41:
    ts_leftin(2.0, 200)
transform lss42:
    ts_leftin(2.0, 493)
transform lss43:
    ts_leftin(2.0, 786)
transform lss44:
    ts_leftin(2.0, 1080)
transform lss31:
    ts_leftin(2.0, 240)
transform lss32:
    ts_leftin(2.0, 640)
transform lss33:
    ts_leftin(2.0, 1040)
transform lss21:
    ts_leftin(2.0, 400)
transform lss22:
    ts_leftin(2.0, 880)
transform lss11:
    ts_leftin(2.0, 640)

# RIGHTIN
transform rn41:
    ts_rightin(1.0, 200)
transform rn42:
    ts_rightin(1.0, 493)
transform rn43:
    ts_rightin(1.0, 786)
transform rn44:
    ts_rightin(1.0, 1080)
transform rn31:
    ts_rightin(1.0, 240)
transform rn32:
    ts_rightin(1.0, 640)
transform rn33:
    ts_rightin(1.0, 1040)
transform rn21:
    ts_rightin(1.0, 400)
transform rn22:
    ts_rightin(1.0, 880)
transform rn11:
    ts_rightin(1.0, 640)

transform rf41:
    ts_rightin(0.5, 200)
transform rf42:
    ts_rightin(0.5, 493)
transform rf43:
    ts_rightin(0.5, 786)
transform rf44:
    ts_rightin(0.5, 1080)
transform rf31:
    ts_rightin(0.5, 240)
transform rf32:
    ts_rightin(0.5, 640)
transform rf33:
    ts_rightin(0.5, 1040)
transform rf21:
    ts_rightin(0.5, 400)
transform rf22:
    ts_rightin(0.5, 880)
transform rf11:
    ts_rightin(0.5, 640)

transform rs41:
    ts_rightin(1.5, 200)
transform rs42:
    ts_rightin(1.5, 493)
transform rs43:
    ts_rightin(1.5, 786)
transform rs44:
    ts_rightin(1.5, 1080)
transform rs31:
    ts_rightin(1.5, 240)
transform rs32:
    ts_rightin(1.5, 640)
transform rs33:
    ts_rightin(1.5, 1040)
transform rs21:
    ts_rightin(1.5, 400)
transform rs22:
    ts_rightin(1.5, 880)
transform rs11:
    ts_rightin(1.5, 640)
transform rs51:
    ts_rightin(1.5, 216)
transform rs52:
    ts_rightin(1.5, 432)
transform rs53:
    ts_rightin(1.5, 648)
transform rs54:
    ts_rightin(1.5, 864)
transform rs55:
    ts_rightin(1.5, 1080)

transform rss41:
    ts_rightin(2.0, 200)
transform rss42:
    ts_rightin(2.0, 493)
transform rss43:
    ts_rightin(2.0, 786)
transform rss44:
    ts_rightin(2.0, 1080)
transform rss31:
    ts_rightin(2.0, 240)
transform rss32:
    ts_rightin(2.0, 640)
transform rss33:
    ts_rightin(2.0, 1040)
transform rss21:
    ts_rightin(2.0, 400)
transform rss22:
    ts_rightin(2.0, 880)
transform rss11:
    ts_rightin(2.0, 640)

# RIGHTOUT
transform ron41:
    ts_rightout(1.0, 200)
transform ron42:
    ts_rightout(1.0, 493)
transform ron43:
    ts_rightout(1.0, 786)
transform ron44:
    ts_rightout(1.0, 1080)
transform ron31:
    ts_rightout(1.0, 240)
transform ron32:
    ts_rightout(1.0, 640)
transform ron33:
    ts_rightout(1.0, 1040)
transform ron21:
    ts_rightout(1.0, 400)
transform ron22:
    ts_rightout(1.0, 880)
transform ron11:
    ts_rightout(1.0, 640)

transform rof41:
    ts_rightout(0.5, 200)
transform rof42:
    ts_rightout(0.5, 493)
transform rof43:
    ts_rightout(0.5, 786)
transform rof44:
    ts_rightout(0.5, 1080)
transform rof31:
    ts_rightout(0.5, 240)
transform rof32:
    ts_rightout(0.5, 640)
transform rof33:
    ts_rightout(0.5, 1040)
transform rof21:
    ts_rightout(0.5, 400)
transform rof22:
    ts_rightout(0.5, 880)
transform rof11:
    ts_rightout(0.5, 640)

transform ros41:
    ts_rightout(1.5, 200)
transform ros42:
    ts_rightout(1.5, 493)
transform ros43:
    ts_rightout(1.5, 786)
transform ros44:
    ts_rightout(1.5, 1080)
transform ros31:
    ts_rightout(1.5, 240)
transform ros32:
    ts_rightout(1.5, 640)
transform ros33:
    ts_rightout(1.5, 1040)
transform ros21:
    ts_rightout(1.5, 400)
transform ros22:
    ts_rightout(1.5, 880)
transform ros11:
    ts_rightout(1.5, 640)
transform ros51:
    ts_rightout(1.5, 216)
transform ros52:
    ts_rightout(1.5, 432)
transform ros53:
    ts_rightout(1.5, 648)
transform ros54:
    ts_rightout(1.5, 864)
transform ros55:
    ts_rightout(1.5, 1080)

transform ross41:
    ts_rightout(2.0, 200)
transform ross42:
    ts_rightout(2.0, 493)
transform ross43:
    ts_rightout(2.0, 786)
transform ross44:
    ts_rightout(2.0, 1080)
transform ross31:
    ts_rightout(2.0, 240)
transform ross32:
    ts_rightout(2.0, 640)
transform ross33:
    ts_rightout(2.0, 1040)
transform ross21:
    ts_rightout(2.0, 400)
transform ross22:
    ts_rightout(2.0, 880)
transform ross11:
    ts_rightout(2.0, 640)

# LEFTOUT
transform lon41:
    ts_leftout(1.0, 200)
transform lon42:
    ts_leftout(1.0, 493)
transform lon43:
    ts_leftout(1.0, 786)
transform lon44:
    ts_leftout(1.0, 1080)
transform lon31:
    ts_leftout(1.0, 240)
transform lon32:
    ts_leftout(1.0, 640)
transform lon33:
    ts_leftout(1.0, 1040)
transform lon21:
    ts_leftout(1.0, 400)
transform lon22:
    ts_leftout(1.0, 880)
transform lon11:
    ts_leftout(1.0, 640)

transform lof41:
    ts_leftout(0.5, 200)
transform lof42:
    ts_leftout(0.5, 493)
transform lof43:
    ts_leftout(0.5, 786)
transform lof44:
    ts_leftout(0.5, 1080)
transform lof31:
    ts_leftout(0.5, 240)
transform lof32:
    ts_leftout(0.5, 640)
transform lof33:
    ts_leftout(0.5, 1040)
transform lof21:
    ts_leftout(0.5, 400)
transform lof22:
    ts_leftout(0.5, 880)
transform lof11:
    ts_leftout(0.5, 640)

transform los41:
    ts_leftout(1.5, 200)
transform los42:
    ts_leftout(1.5, 493)
transform los43:
    ts_leftout(1.5, 786)
transform los44:
    ts_leftout(1.5, 1080)
transform los31:
    ts_leftout(1.5, 240)
transform los32:
    ts_leftout(1.5, 640)
transform los33:
    ts_leftout(1.5, 1040)
transform los21:
    ts_leftout(1.5, 400)
transform los22:
    ts_leftout(1.5, 880)
transform los11:
    ts_leftout(1.5, 640)
transform los51:
    ts_leftout(1.5, 216)
transform los52:
    ts_leftout(1.5, 432)
transform los53:
    ts_leftout(1.5, 648)
transform los54:
    ts_leftout(1.5, 864)
transform los55:
    ts_leftout(1.5, 1080)

transform loss41:
    ts_leftout(2.0, 200)
transform loss42:
    ts_leftout(2.0, 493)
transform loss43:
    ts_leftout(2.0, 786)
transform loss44:
    ts_leftout(2.0, 1080)
transform loss31:
    ts_leftout(2.0, 240)
transform loss32:
    ts_leftout(2.0, 640)
transform loss33:
    ts_leftout(2.0, 1040)
transform loss21:
    ts_leftout(2.0, 400)
transform loss22:
    ts_leftout(2.0, 880)
transform loss11:
    ts_leftout(2.0, 640)
