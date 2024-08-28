####ЮРЕЦ
image yuri 4f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "f2.webp") )

image yuri 1z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "z.webp") )

image yuri 1f2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "f2.webp") )

image yuri 1y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y.webp") )

image yuri 1zx = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zx.webp") )

image yuri 1ze = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "ze.webp") )

image yuri 1zf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zf.webp") )

image yuri 1zg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zg.webp") )

image yuri 1zh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zh.webp") )

image yuri 1zi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "zi.webp") )

image yuri 2z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "z.webp") )

image yuri 2f2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f2.webp") )

image yuri 2y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y.webp") )

image yuri 2zx = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zx.webp") )

image yuri 2ze = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "ze.webp") )

image yuri 2zf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zf.webp") )

image yuri 2zg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zg.webp") )

image yuri 2zh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zh.webp") )

image yuri 2zi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zi.webp") )

image yuri 3z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "z.webp") )

image yuri 3f2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f2.webp") )

image yuri 3y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y.webp") )

image yuri 3zx = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zx.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zx.webp") )

image yuri 3ze = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "ze.webp") )

image yuri 3zf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zf.webp") )

image yuri 3zg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zg.webp") )

image yuri 3zh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zh.webp") )

image yuri 3zi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "zi.webp") )

image yuri 9a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 9b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "b.webp") )

image yuri 9c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "c.webp") )

image yuri 9d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "d.webp") )

image yuri 9e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "e.webp") )

image yuri 9f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "f.webp") )

image yuri 9g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "g.webp") )

image yuri 9h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "h.webp") )

image yuri 9i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "i.webp") )

image yuri 9j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "j.webp") )

image yuri 9k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "k.webp") )

image yuri 9l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "l.webp") )

image yuri 9m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "m.webp") )

image yuri 9n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "n.webp") )

image yuri 9o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "o.webp") )

image yuri 9p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "p.webp") )

image yuri 9q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "q.webp") )

image yuri 9r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "r.webp") )

image yuri 9s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "s.webp") )

image yuri 9t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "t.webp") )

image yuri 9u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "u.webp") )

image yuri 9v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "v.webp") )

image yuri 9w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "w.webp") )

image yuri 9f2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "f2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "f2.webp") )

image yuri 9x = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "x.webp") )


image yuri 9y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "y.webp") )


image yuri 9z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "z.webp") )


image yuri 9ze = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "ze.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "ze.webp") )


image yuri 9zf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zf.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zf.webp") )


image yuri 9zg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zg.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zg.webp") )


image yuri 9zh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zh.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zh.webp") )

image yuri 9zi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp", (0, 0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zi.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "4.webp",(0,0), ts_yuri_pt + "zi.webp") )

image yuri 1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 3 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 4 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "a2.webp") )

image yuri 1a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 1b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "b.webp") )

image yuri 1c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "c.webp") )

image yuri 1d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "d.webp") )

image yuri 1e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "e.webp") )

image yuri 1f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "f.webp") )

image yuri 1g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "g.webp") )

image yuri 1h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "h.webp") )

image yuri 1i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "i.webp") )

image yuri 1j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "j.webp") )

image yuri 1k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "k.webp") )

image yuri 1l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "l.webp") )

image yuri 1m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "m.webp") )

image yuri 1n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "n.webp") )

image yuri 1o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "o.webp") )

image yuri 1p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "p.webp") )

image yuri 1q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "q.webp") )

image yuri 1r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "r.webp") )

image yuri 1s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "s.webp") )

image yuri 1t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "t.webp") )

image yuri 1u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "u.webp") )

image yuri 1v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "v.webp") )

image yuri 1w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "w.webp") )

image yuri 1y1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y1.webp") )

image yuri 1y2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y2.webp") )

image yuri 1y3 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y3.webp") )

image yuri 1y4 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y4.webp") )

image yuri 1y5 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y5.webp") )

image yuri 1y6 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y6.webp") )

image yuri 1y7 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "y7.webp") )

image yuri 1x = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "1r.webp",(0,0), ts_yuri_pt + "x.webp") )


image yuri 2a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 2b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "b.webp") )

image yuri 2c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "c.webp") )

image yuri 2d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "d.webp") )

image yuri 2e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "e.webp") )

image yuri 2f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f.webp") )

image yuri 2g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "g.webp") )

image yuri 2h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "h.webp") )

image yuri 2i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "i.webp") )

image yuri 2j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "j.webp") )

image yuri 2k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "k.webp") )

image yuri 2l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "l.webp") )

image yuri 2m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "m.webp") )

image yuri 2n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "n.webp") )

image yuri 2o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "o.webp") )

image yuri 2p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "p.webp") )

image yuri 2q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "q.webp") )

image yuri 2r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "r.webp") )

image yuri 2s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "s.webp") )

image yuri 2t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "t.webp") )

image yuri 2u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "u.webp") )

image yuri 2v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "v.webp") )

image yuri 2w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "w.webp") )

image yuri 2y1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y1.webp") )

image yuri 2y2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y2.webp") )

image yuri 2y3 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y3.webp") )

image yuri 2y4 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y4.webp") )

image yuri 2y5 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y5.webp") )

image yuri 2y6 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y6.webp") )

image yuri 2y7 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y7.webp") )

image yuri 3a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 3b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "b.webp") )

image yuri 3c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "c.webp") )

image yuri 3d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "d.webp") )

image yuri 3e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "e.webp") )

image yuri 3f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "f.webp") )

image yuri 3g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "g.webp") )

image yuri 3h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "h.webp") )

image yuri 3i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "i.webp") )

image yuri 3j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "j.webp") )

image yuri 3k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "k.webp") )

image yuri 3l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "l.webp") )

image yuri 3m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "m.webp") )

image yuri 3n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "n.webp") )

image yuri 3o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "o.webp") )

image yuri 3p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "p.webp") )

image yuri 3q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "q.webp") )

image yuri 3r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "r.webp") )

image yuri 3s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "s.webp") )

image yuri 3t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "t.webp") )

image yuri 3u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "u.webp") )

image yuri 3v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "v.webp") )

image yuri 3w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "w.webp") )

image yuri 3y1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y1.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y1.webp") )

image yuri 3y2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y2.webp") )

image yuri 3y3 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y3.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y3.webp") )

image yuri 3y4 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y4.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y4.webp") )

image yuri 3y5 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y5.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y5.webp") )

image yuri 3y6 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y6.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y6.webp") )

image yuri 3y7 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y7.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2l.webp",(0,0), ts_yuri_pt + "2r.webp",(0,0), ts_yuri_pt + "y7.webp") )

image yuri 4a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "a2.webp") )

image yuri 4b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "b2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "b2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "b2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "b2.webp") )

image yuri 4c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "c2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "c2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "c2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "c2.webp") )

image yuri 4d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "d2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "d2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "d2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "d2.webp") )

image yuri 4e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "e2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "e2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "e2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3.webp",(0,0), ts_yuri_pt + "e2.webp") )

image yuri 1ba = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 1bb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "b.webp") )

image yuri 1bc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "c.webp") )

image yuri 1bd = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "d.webp") )

image yuri 1be = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "e.webp") )

image yuri 1bf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "f.webp") )

image yuri 1bg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "g.webp") )

image yuri 1bh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "h.webp") )

image yuri 1bi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "i.webp") )

image yuri 1bj = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "j.webp") )

image yuri 1bk = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "k.webp") )

image yuri 1bl = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "l.webp") )

image yuri 1bm = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "m.webp") )

image yuri 1bn = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "n.webp") )

image yuri 1bo = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "o.webp") )

image yuri 1bp = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "p.webp") )

image yuri 1bq = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "q.webp") )

image yuri 1br = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "r.webp") )

image yuri 1bs = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "s.webp") )

image yuri 1bt = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "t.webp") )

image yuri 1bu = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "u.webp") )

image yuri 1bv = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "v.webp") )

image yuri 1bw = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp", (0, 0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "1br.webp",(0,0), ts_yuri_pt + "w.webp") )

image yuri 2ba = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 2bb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "b.webp") )

image yuri 2bc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "c.webp") )

image yuri 2bd = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "d.webp") )

image yuri 2be = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "e.webp") )

image yuri 2bf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "f.webp") )

image yuri 2bg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "g.webp") )

image yuri 2bh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "h.webp") )

image yuri 2bi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "i.webp") )

image yuri 2bj = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "j.webp") )

image yuri 2bk = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "k.webp") )

image yuri 2bl = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "l.webp") )

image yuri 2bm = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "m.webp") )

image yuri 2bn = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "n.webp") )

image yuri 2bo = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "o.webp") )

image yuri 2bp = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "p.webp") )

image yuri 2bq = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "q.webp") )

image yuri 2br = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "r.webp") )

image yuri 2bs = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "s.webp") )

image yuri 2bt = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "t.webp") )

image yuri 2bu = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "u.webp") )

image yuri 2bv = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "v.webp") )

image yuri 2bw = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "1bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "w.webp") )

image yuri 3ba = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "a.webp") )

image yuri 3bb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "b.webp") )

image yuri 3bc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "c.webp") )

image yuri 3bd = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "d.webp") )

image yuri 3be = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "e.webp") )

image yuri 3bf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "f.webp") )

image yuri 3bg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "g.webp") )

image yuri 3bh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "h.webp") )

image yuri 3bi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "i.webp") )

image yuri 3bj = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "j.webp") )

image yuri 3bk = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "k.webp") )

image yuri 3bl = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "l.webp") )

image yuri 3bm = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "m.webp") )

image yuri 3bn = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "n.webp") )

image yuri 3bo = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "o.webp") )

image yuri 3bp = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "p.webp") )

image yuri 3bq = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "q.webp") )

image yuri 3br = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "r.webp") )

image yuri 3bs = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "s.webp") )

image yuri 3bt = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "t.webp") )

image yuri 3bu = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "u.webp") )

image yuri 3bv = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "v.webp") )

image yuri 3bw = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp", (0, 0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "2bl.webp",(0,0), ts_yuri_pt + "2br.webp",(0,0), ts_yuri_pt + "w.webp") )

image yuri 4ba = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp", (0, 0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "a2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "a2.webp") )

image yuri 4bb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "b2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp", (0, 0), ts_yuri_pt + "b2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "b2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "b2.webp") )

image yuri 4bc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "c2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp", (0, 0), ts_yuri_pt + "c2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "c2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "c2.webp") )

image yuri 4bd = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "d2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp", (0, 0), ts_yuri_pt + "d2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "d2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "d2.webp") )

image yuri 4be = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "e2.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp", (0, 0), ts_yuri_pt + "e2.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "e2.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_yuri_pt + "3b.webp",(0,0), ts_yuri_pt + "e2.webp") )