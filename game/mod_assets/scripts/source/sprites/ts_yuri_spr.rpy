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





image yuri 1a = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "a.webp")
image yuri 1b = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "b.webp")
image yuri 1c = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "c.webp")
image yuri 1d = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "d.webp")
image yuri 1e = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "e.webp")
image yuri 1f = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "f.webp")
image yuri 1g = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "g.webp")
image yuri 1h = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "h.webp")
image yuri 1i = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "i.webp")
image yuri 1j = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "j.webp")
image yuri 1k = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "k.webp")
image yuri 1l = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "l.webp")
image yuri 1m = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "m.webp")
image yuri 1n = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "n.webp")
image yuri 1o = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "o.webp")
image yuri 1p = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "p.webp")
image yuri 1q = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "q.webp")
image yuri 1r = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "r.webp")
image yuri 1s = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "s.webp")
image yuri 1t = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "t.webp")
image yuri 1u = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "u.webp")
image yuri 1v = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "v.webp")
image yuri 1w = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "w.webp")

image yuri 1y1 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y1.webp")
image yuri 1y2 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y2.webp")
image yuri 1y3 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y3.webp")
image yuri 1y4 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y4.webp")
image yuri 1y5 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y5.webp")
image yuri 1y6 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y6.webp")
image yuri 1y7 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "1r.webp", (0, 0), ts_yuri_pt + "y7.webp")

image yuri 2a = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "a.webp")
image yuri 2b = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "b.webp")
image yuri 2c = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "c.webp")
image yuri 2d = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "d.webp")
image yuri 2e = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "e.webp")
image yuri 2f = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "f.webp")
image yuri 2g = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "g.webp")
image yuri 2h = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "h.webp")
image yuri 2i = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "i.webp")
image yuri 2j = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "j.webp")
image yuri 2k = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "k.webp")
image yuri 2l = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "l.webp")
image yuri 2m = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "m.webp")
image yuri 2n = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "n.webp")
image yuri 2o = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "o.webp")
image yuri 2p = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "p.webp")
image yuri 2q = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "q.webp")
image yuri 2r = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "r.webp")
image yuri 2s = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "s.webp")
image yuri 2t = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "t.webp")
image yuri 2u = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "u.webp")
image yuri 2v = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "v.webp")
image yuri 2w = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "w.webp")

image yuri 2y1 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y1.webp")
image yuri 2y2 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y2.webp")
image yuri 2y3 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y3.webp")
image yuri 2y4 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y4.webp")
image yuri 2y5 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y5.webp")
image yuri 2y6 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y6.webp")
image yuri 2y7 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "1l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y7.webp")

image yuri 3a = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "a.webp")
image yuri 3b = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "b.webp")
image yuri 3c = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "c.webp")
image yuri 3d = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "d.webp")
image yuri 3e = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "e.webp")
image yuri 3f = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "f.webp")
image yuri 3g = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "g.webp")
image yuri 3h = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "h.webp")
image yuri 3i = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "i.webp")
image yuri 3j = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "j.webp")
image yuri 3k = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "k.webp")
image yuri 3l = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "l.webp")
image yuri 3m = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "m.webp")
image yuri 3n = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "n.webp")
image yuri 3o = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "o.webp")
image yuri 3p = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "p.webp")
image yuri 3q = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "q.webp")
image yuri 3r = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "r.webp")
image yuri 3s = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "s.webp")
image yuri 3t = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "t.webp")
image yuri 3u = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "u.webp")
image yuri 3v = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "v.webp")
image yuri 3w = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "w.webp")

image yuri 3y1 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y1.webp")
image yuri 3y2 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y2.webp")
image yuri 3y3 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y3.webp")
image yuri 3y4 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y4.webp")
image yuri 3y5 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y5.webp")
image yuri 3y6 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y6.webp")
image yuri 3y7 = im.Composite((960, 960), (0, 0), ts_yuri_pt + "2l.webp", (0, 0), ts_yuri_pt + "2r.webp", (0, 0), ts_yuri_pt + "y7.webp")

image yuri 4a = im.Composite((960, 960), (0, 0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "a2.webp")
image yuri 4b = im.Composite((960, 960), (0, 0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "b2.webp")
image yuri 4c = im.Composite((960, 960), (0, 0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "c2.webp")
image yuri 4d = im.Composite((960, 960), (0, 0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "d2.webp")
image yuri 4e = im.Composite((960, 960), (0, 0), ts_yuri_pt + "3.webp", (0, 0), ts_yuri_pt + "e2.webp")

image yuri 1ba = im.Composite((960, 960), (0, 0), ts_yuri_pt + "a.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bb = im.Composite((960, 960), (0, 0), ts_yuri_pt + "b.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bc = im.Composite((960, 960), (0, 0), ts_yuri_pt + "c.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bd = im.Composite((960, 960), (0, 0), ts_yuri_pt + "d.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1be = im.Composite((960, 960), (0, 0), ts_yuri_pt + "e.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bf = im.Composite((960, 960), (0, 0), ts_yuri_pt + "f.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bg = im.Composite((960, 960), (0, 0), ts_yuri_pt + "g.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bh = im.Composite((960, 960), (0, 0), ts_yuri_pt + "h.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bi = im.Composite((960, 960), (0, 0), ts_yuri_pt + "i.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bj = im.Composite((960, 960), (0, 0), ts_yuri_pt + "j.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bk = im.Composite((960, 960), (0, 0), ts_yuri_pt + "k.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bl = im.Composite((960, 960), (0, 0), ts_yuri_pt + "l.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bm = im.Composite((960, 960), (0, 0), ts_yuri_pt + "m.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bn = im.Composite((960, 960), (0, 0), ts_yuri_pt + "n.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bo = im.Composite((960, 960), (0, 0), ts_yuri_pt + "o.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bp = im.Composite((960, 960), (0, 0), ts_yuri_pt + "p.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bq = im.Composite((960, 960), (0, 0), ts_yuri_pt + "q.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1br = im.Composite((960, 960), (0, 0), ts_yuri_pt + "r.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bs = im.Composite((960, 960), (0, 0), ts_yuri_pt + "s.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bt = im.Composite((960, 960), (0, 0), ts_yuri_pt + "t.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bu = im.Composite((960, 960), (0, 0), ts_yuri_pt + "u.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bv = im.Composite((960, 960), (0, 0), ts_yuri_pt + "v.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")
image yuri 1bw = im.Composite((960, 960), (0, 0), ts_yuri_pt + "w.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "1br.webp")

image yuri 2ba = im.Composite((960, 960), (0, 0), ts_yuri_pt + "a.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bb = im.Composite((960, 960), (0, 0), ts_yuri_pt + "b.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bc = im.Composite((960, 960), (0, 0), ts_yuri_pt + "c.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bd = im.Composite((960, 960), (0, 0), ts_yuri_pt + "d.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2be = im.Composite((960, 960), (0, 0), ts_yuri_pt + "e.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bf = im.Composite((960, 960), (0, 0), ts_yuri_pt + "f.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bg = im.Composite((960, 960), (0, 0), ts_yuri_pt + "g.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bh = im.Composite((960, 960), (0, 0), ts_yuri_pt + "h.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bi = im.Composite((960, 960), (0, 0), ts_yuri_pt + "i.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bj = im.Composite((960, 960), (0, 0), ts_yuri_pt + "j.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bk = im.Composite((960, 960), (0, 0), ts_yuri_pt + "k.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bl = im.Composite((960, 960), (0, 0), ts_yuri_pt + "l.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bm = im.Composite((960, 960), (0, 0), ts_yuri_pt + "m.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bn = im.Composite((960, 960), (0, 0), ts_yuri_pt + "n.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bo = im.Composite((960, 960), (0, 0), ts_yuri_pt + "o.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bp = im.Composite((960, 960), (0, 0), ts_yuri_pt + "p.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bq = im.Composite((960, 960), (0, 0), ts_yuri_pt + "q.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2br = im.Composite((960, 960), (0, 0), ts_yuri_pt + "r.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bs = im.Composite((960, 960), (0, 0), ts_yuri_pt + "s.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bt = im.Composite((960, 960), (0, 0), ts_yuri_pt + "t.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bu = im.Composite((960, 960), (0, 0), ts_yuri_pt + "u.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bv = im.Composite((960, 960), (0, 0), ts_yuri_pt + "v.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 2bw = im.Composite((960, 960), (0, 0), ts_yuri_pt + "w.webp", (0, 0), ts_yuri_pt + "1bl.webp", (0, 0), ts_yuri_pt + "2br.webp")

image yuri 3ba = im.Composite((960, 960), (0, 0), ts_yuri_pt + "a.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bb = im.Composite((960, 960), (0, 0), ts_yuri_pt + "b.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bc = im.Composite((960, 960), (0, 0), ts_yuri_pt + "c.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bd = im.Composite((960, 960), (0, 0), ts_yuri_pt + "d.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3be = im.Composite((960, 960), (0, 0), ts_yuri_pt + "e.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bf = im.Composite((960, 960), (0, 0), ts_yuri_pt + "f.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bg = im.Composite((960, 960), (0, 0), ts_yuri_pt + "g.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bh = im.Composite((960, 960), (0, 0), ts_yuri_pt + "h.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bi = im.Composite((960, 960), (0, 0), ts_yuri_pt + "i.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bj = im.Composite((960, 960), (0, 0), ts_yuri_pt + "j.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bk = im.Composite((960, 960), (0, 0), ts_yuri_pt + "k.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bl = im.Composite((960, 960), (0, 0), ts_yuri_pt + "l.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bm = im.Composite((960, 960), (0, 0), ts_yuri_pt + "m.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bn = im.Composite((960, 960), (0, 0), ts_yuri_pt + "n.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bo = im.Composite((960, 960), (0, 0), ts_yuri_pt + "o.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bp = im.Composite((960, 960), (0, 0), ts_yuri_pt + "p.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bq = im.Composite((960, 960), (0, 0), ts_yuri_pt + "q.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3br = im.Composite((960, 960), (0, 0), ts_yuri_pt + "r.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bs = im.Composite((960, 960), (0, 0), ts_yuri_pt + "s.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bt = im.Composite((960, 960), (0, 0), ts_yuri_pt + "t.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bu = im.Composite((960, 960), (0, 0), ts_yuri_pt + "u.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bv = im.Composite((960, 960), (0, 0), ts_yuri_pt + "v.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")
image yuri 3bw = im.Composite((960, 960), (0, 0), ts_yuri_pt + "w.webp", (0, 0), ts_yuri_pt + "2bl.webp", (0, 0), ts_yuri_pt + "2br.webp")

image yuri 4ba = im.Composite((960, 960), (0, 0), ts_yuri_pt + "a2.webp", (0, 0), ts_yuri_pt + "3b.webp")
image yuri 4bb = im.Composite((960, 960), (0, 0), ts_yuri_pt + "b2.webp", (0, 0), ts_yuri_pt + "3b.webp")
image yuri 4bc = im.Composite((960, 960), (0, 0), ts_yuri_pt + "c2.webp", (0, 0), ts_yuri_pt + "3b.webp")
image yuri 4bd = im.Composite((960, 960), (0, 0), ts_yuri_pt + "d2.webp", (0, 0), ts_yuri_pt + "3b.webp")
image yuri 4be = im.Composite((960, 960), (0, 0), ts_yuri_pt + "e2.webp", (0, 0), ts_yuri_pt + "3b.webp")
