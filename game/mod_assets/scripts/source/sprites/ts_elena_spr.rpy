####ЕЛЕНА
image elena a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "A.webp") )

image elena a1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "A1.webp") )

image elena a2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "A2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "A2.webp") )

image elena b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "B.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "B.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "B.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "B.webp") )

image elena b2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "B2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "B2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "B2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "B2.webp") )

image elena c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "C.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "C.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "C.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "A.webp") )

image elena c1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "C1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "C1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "C1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "C1.webp") )

image elena d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "D.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "D.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "D.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "D.webp") )

image elena d1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "D1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "D1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "D1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "D1.webp") )

image elena e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "E.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "E.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "E.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "E.webp") )

image elena e1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "E1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "E1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "E1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "E1.webp") )

image elena f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "F.webp") )

image elena f1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "F1.webp") )

image elena f2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "F2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "F2.webp") )

image elena g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "G.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "G.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "G.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "G.webp") )

image elena g1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "G1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "G1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "G1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "G1.webp") )

image elena h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "H.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "H.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "H.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "H.webp") )

image elena i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "I.webp") )

image elena i1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp") )

image elena i2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "I2.webp") )

image elena j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "J.webp") )

image elena j1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "J1.webp") )

image elena j2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "J2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "J2.webp") )

image elena k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "K.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "K.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "K.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "K.webp") )

image elena k1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "K1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "K1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "K1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "K1.webp") )

image elena m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "M.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "M.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "M.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "M.webp") )

image elena m1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "M1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "M1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "M1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "M1.webp") )

image elena n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "N.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "N.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "N.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "N.webp") )

image elena n1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "N1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "N1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "N1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "N1.webp") )

image elena n2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "I1.webp") )

image elena o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "O.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "O.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "O.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "O.webp") )

image elena o1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "O1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "O1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "O1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "O1.webp") )

image elena p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "P.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "P.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "P.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "P.webp") )

image elena q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "Q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "Q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "Q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "Q.webp") )

image elena r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "R.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "R.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "R.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "R.webp") )

image elena s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "S.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "S.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "S.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "S.webp") )

image elena s1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "S1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "S1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_elena_pt + "S1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_elena_pt + "S1.webp") )
