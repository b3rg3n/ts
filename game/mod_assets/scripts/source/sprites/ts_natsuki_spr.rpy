####НАЦУКИ

image natsuki 11 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 1a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "a.webp") )

image natsuki 1b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "b.webp") )

image natsuki 1c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "c.webp") )

image natsuki 1d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "d.webp") )

image natsuki 1e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "e.webp") )

image natsuki 1f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "f.webp") )

image natsuki 1g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "g.webp") )

image natsuki 1h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "h.webp") )

image natsuki 1i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "i.webp") )

image natsuki 1j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "j.webp") )

image natsuki 1k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "k.webp") )

image natsuki 1l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "l.webp") )

image natsuki 1m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "m.webp") )

image natsuki 1n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "n.webp") )

image natsuki 1o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "o.webp") )

image natsuki 1p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "p.webp") )

image natsuki 1q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "q.webp") )

image natsuki 1r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "r.webp") )

image natsuki 1s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "s.webp") )

image natsuki 1t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "t.webp") )

image natsuki 1u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "u.webp") )

image natsuki 1v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "v.webp") )

image natsuki 1w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "w.webp") )

image natsuki 1x = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "x.webp") )

image natsuki 1y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "y.webp") )

image natsuki 1z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "z.webp") )

image natsuki 1za = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "za.webp") )

image natsuki 1zb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zb.webp") )

image natsuki 1zc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zc.webp") )

image natsuki 21 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 2a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "a.webp") )

image natsuki 2b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "b.webp") )

image natsuki 2c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "c.webp") )

image natsuki 2d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "d.webp") )

image natsuki 2e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "e.webp") )

image natsuki 2f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "f.webp") )

image natsuki 2g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "g.webp") )

image natsuki 2h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "h.webp") )

image natsuki 2i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "i.webp") )

image natsuki 2j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "j.webp") )

image natsuki 2k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "k.webp") )

image natsuki 2l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "l.webp") )

image natsuki 2m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "m.webp") )

image natsuki 2n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "n.webp") )

image natsuki 2o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "o.webp") )

image natsuki 2p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "p.webp") )

image natsuki 2q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "q.webp") )

image natsuki 2r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "r.webp") )

image natsuki 2s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "s.webp") )

image natsuki 2t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "t.webp") )

image natsuki 2u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "u.webp") )

image natsuki 2v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "v.webp") )

image natsuki 2w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "w.webp") )

image natsuki 2x = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "x.webp") )

image natsuki 2y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "y.webp") )

image natsuki 2z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "z.webp") )

image natsuki 2za = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "za.webp") )

image natsuki 2zb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zb.webp") )

image natsuki 2zc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zc.webp") )

image natsuki 31 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 3a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "a.webp") )

image natsuki 3b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "b.webp") )

image natsuki 3c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "c.webp") )

image natsuki 3d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "d.webp") )

image natsuki 3e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "e.webp") )

image natsuki 3f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "f.webp") )

image natsuki 3g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "g.webp") )

image natsuki 3h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "h.webp") )

image natsuki 3i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "i.webp") )

image natsuki 3j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "j.webp") )

image natsuki 3k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "k.webp") )

image natsuki 3l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "l.webp") )

image natsuki 3m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "m.webp") )

image natsuki 3n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "n.webp") )

image natsuki 3o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "o.webp") )

image natsuki 3p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "p.webp") )

image natsuki 3q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "q.webp") )

image natsuki 3r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "r.webp") )

image natsuki 3s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "s.webp") )

image natsuki 3t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "t.webp") )

image natsuki 3u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "u.webp") )

image natsuki 3v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "v.webp") )

image natsuki 3w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "w.webp") )

image natsuki 3x = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "x.webp") )

image natsuki 3y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "y.webp") )

image natsuki 3z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "z.webp") )

image natsuki 3za = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "za.webp") )

image natsuki 3zb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zb.webp") )

image natsuki 3zc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "zc.webp") )

image natsuki 41 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 4a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "a.webp") )

image natsuki 4b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "b.webp") )

image natsuki 4c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "c.webp") )

image natsuki 4d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "d.webp") )

image natsuki 4e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "e.webp") )

image natsuki 4f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "f.webp") )

image natsuki 4g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "g.webp") )

image natsuki 4h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "h.webp") )

image natsuki 4i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "i.webp") )

image natsuki 4j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "j.webp") )

image natsuki 4k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "k.webp") )

image natsuki 4l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "l.webp") )

image natsuki 4m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "m.webp") )

image natsuki 4n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "n.webp") )

image natsuki 4o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "o.webp") )

image natsuki 4p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "p.webp") )

image natsuki 4q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "q.webp") )

image natsuki 4r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "r.webp") )

image natsuki 4s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "s.webp") )

image natsuki 4t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "t.webp") )

image natsuki 4u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "u.webp") )

image natsuki 4v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "v.webp") )

image natsuki 4w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "w.webp") )

image natsuki 4x = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "x.webp") )

image natsuki 4y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "y.webp") )

image natsuki 4z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "z.webp") )

image natsuki 4za = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "za.webp") )

image natsuki 4zb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zb.webp") )

image natsuki 4zc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "zc.webp") )

image natsuki 12 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2t.webp") )

image natsuki 12a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2ta.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2ta.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2ta.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2ta.webp") )

image natsuki 12b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tb.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tb.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tb.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tb.webp") )

image natsuki 12c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tc.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tc.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tc.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tc.webp") )

image natsuki 12d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2td.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2td.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2td.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2td.webp") )

image natsuki 12e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2te.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2te.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2te.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2te.webp") )

image natsuki 12f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tf.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tf.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tf.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tf.webp") )

image natsuki 12g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tg.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tg.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tg.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2tg.webp") )

image natsuki 12h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2th.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2th.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2th.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2th.webp") )

image natsuki 12i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2ti.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2ti.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2ti.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "2ti.webp") )

image natsuki 42 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2t.webp") )

image natsuki 42a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2ta.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2ta.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2ta.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2ta.webp") )

image natsuki 42b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tb.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tb.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tb.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tb.webp") )

image natsuki 42c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tc.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tc.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tc.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tc.webp") )

image natsuki 42d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2td.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2td.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2td.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2td.webp") )

image natsuki 42e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2te.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2te.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2te.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2te.webp") )

image natsuki 42f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tf.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tf.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tf.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tf.webp") )

image natsuki 42g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tg.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tg.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2tg.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "22tg.webp") )

image natsuki 42h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2th.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2th.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2th.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2th.webp") )

image natsuki 42i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2ti.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2ti.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2ti.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "2ti.webp") )

image natsuki 51 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "1t.webp") )

image natsuki 5a = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "a.webp") )

image natsuki 5b = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "b.webp") )

image natsuki 5c = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "c.webp") )

image natsuki 5d = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "d.webp") )

image natsuki 5e = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "e.webp") )

image natsuki 5f = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "f.webp") )

image natsuki 5g = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "g.webp") )

image natsuki 5h = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "h.webp") )

image natsuki 5i = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "i.webp") )

image natsuki 5j = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "j.webp") )

image natsuki 5k = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "k.webp") )

image natsuki 5l = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "l.webp") )

image natsuki 5m = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "m.webp") )

image natsuki 5n = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "n.webp") )

image natsuki 5o = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "o.webp") )

image natsuki 5p = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "p.webp") )

image natsuki 5q = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "q.webp") )

image natsuki 5r = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "r.webp") )

image natsuki 5s = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "s.webp") )

image natsuki 5t = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "t.webp") )

image natsuki 5u = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "u.webp") )

image natsuki 5v = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "v.webp") )

image natsuki 5w = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "w.webp") )

image natsuki 5x = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "x.webp") )

image natsuki 5y = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "y.webp") )

image natsuki 5z = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "z.webp") )

image natsuki 5za = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "za.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "za.webp") )

image natsuki 5zb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "zb.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "zb.webp") )

image natsuki 5zc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "zc.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "zc.webp") )

image natsuki 1ba = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "a.webp") )

image natsuki 1bb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "b.webp") )

image natsuki 1bc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "c.webp") )

image natsuki 1bd = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "d.webp") )

image natsuki 1be = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "e.webp") )

image natsuki 1bf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "f.webp") )

image natsuki 1bg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "g.webp") )

image natsuki 1bh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "h.webp") )

image natsuki 1bi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "i.webp") )

image natsuki 1bj = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "j.webp") )

image natsuki 1bk = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "k.webp") )

image natsuki 1bl = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "l.webp") )

image natsuki 1bm = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "m.webp") )

image natsuki 1bn = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "n.webp") )

image natsuki 1bo = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "o.webp") )

image natsuki 1bp = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "p.webp") )

image natsuki 1bq = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "q.webp") )

image natsuki 1br = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "r.webp") )

image natsuki 1bs = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "s.webp") )

image natsuki 1bt = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "t.webp") )

image natsuki 1bu = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "u.webp") )

image natsuki 1bv = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "v.webp") )

image natsuki 1bw = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "w.webp") )

image natsuki 1bx = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "x.webp") )

image natsuki 1by = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "y.webp") )

image natsuki 1bz = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "z.webp") )

image natsuki 2ba = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "a.webp") )

image natsuki 2bb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "b.webp") )

image natsuki 2bc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "c.webp") )

image natsuki 2bd = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "d.webp") )

image natsuki 2be = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "e.webp") )

image natsuki 2bf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "f.webp") )

image natsuki 2bg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "g.webp") )

image natsuki 2bh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "h.webp") )

image natsuki 2bi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "i.webp") )

image natsuki 2bj = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "j.webp") )

image natsuki 2bk = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "k.webp") )

image natsuki 2bl = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "l.webp") )

image natsuki 2bm = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "m.webp") )

image natsuki 2bn = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "n.webp") )

image natsuki 2bo = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "o.webp") )

image natsuki 2bp = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "p.webp") )

image natsuki 2bq = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "q.webp") )

image natsuki 2br = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "r.webp") )

image natsuki 2bs = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "s.webp") )

image natsuki 2bt = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "t.webp") )

image natsuki 2bu = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "u.webp") )

image natsuki 2bv = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "v.webp") )

image natsuki 2bw = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "w.webp") )

image natsuki 2bx = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "x.webp") )

image natsuki 2by = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "y.webp") )

image natsuki 2bz = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1bl.webp",(0,0), ts_natsuki_pt + "2br.webp",(0,0), ts_natsuki_pt + "z.webp") )

image natsuki 3ba = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "a.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "a.webp") )

image natsuki 3bb = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "b.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "b.webp") )

image natsuki 3bc = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "c.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "c.webp") )

image natsuki 3bd = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "d.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "d.webp") )

image natsuki 3be = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "e.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "e.webp") )

image natsuki 3bf = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "f.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "f.webp") )

image natsuki 3bg = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "g.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "g.webp") )

image natsuki 3bh = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "h.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "h.webp") )

image natsuki 3bi = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "i.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "i.webp") )

image natsuki 3bj = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "j.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "j.webp") )

image natsuki 3bk = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "k.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "k.webp") )

image natsuki 3bl = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "l.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "l.webp") )

image natsuki 3bm = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "m.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "m.webp") )

image natsuki 3bn = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "n.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "n.webp") )

image natsuki 3bo = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "o.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "o.webp") )

image natsuki 3bp = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "p.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "p.webp") )

image natsuki 3bq = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "q.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "q.webp") )

image natsuki 3br = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "r.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "r.webp") )

image natsuki 3bs = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "s.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "s.webp") )

image natsuki 3bt = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "t.webp") )

image natsuki 3bu = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "u.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "u.webp") )

image natsuki 3bv = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "v.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "v.webp") )

image natsuki 3bw = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "w.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "w.webp") )

image natsuki 3bx = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "x.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "x.webp") )

image natsuki 3by = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "y.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "y.webp") )

image natsuki 3bz = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "z.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2bl.webp",(0,0), ts_natsuki_pt + "1br.webp",(0,0), ts_natsuki_pt + "z.webp") )



image natsuki 4ba = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "a.webp")
image natsuki 4bb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "b.webp")
image natsuki 4bc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "c.webp")
image natsuki 4bd = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "d.webp")
image natsuki 4be = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "e.webp")
image natsuki 4bf = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "f.webp")
image natsuki 4bg = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "g.webp")
image natsuki 4bh = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "h.webp")
image natsuki 4bi = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "i.webp")
image natsuki 4bj = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "j.webp")
image natsuki 4bk = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "k.webp")
image natsuki 4bl = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "l.webp")
image natsuki 4bm = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "m.webp")
image natsuki 4bn = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "n.webp")
image natsuki 4bo = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "o.webp")
image natsuki 4bp = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "p.webp")
image natsuki 4bq = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "q.webp")
image natsuki 4br = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "r.webp")
image natsuki 4bs = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "s.webp")
image natsuki 4bt = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "t.webp")
image natsuki 4bu = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "u.webp")
image natsuki 4bv = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "v.webp")
image natsuki 4bw = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "w.webp")
image natsuki 4bx = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "x.webp")
image natsuki 4by = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "y.webp")
image natsuki 4bz = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "z.webp")

image natsuki 12ba = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2bta.webp")
image natsuki 12bb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2btb.webp")
image natsuki 12bc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2btc.webp")
image natsuki 12bd = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2btd.webp")
image natsuki 12be = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2bte.webp")
image natsuki 12bf = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2btf.webp")
image natsuki 12bg = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2btg.webp")
image natsuki 12bh = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2bth.webp")
image natsuki 12bi = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "2bti.webp")

image natsuki 42ba = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2bta.webp")
image natsuki 42bb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2btb.webp")
image natsuki 42bc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2btc.webp")
image natsuki 42bd = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2btd.webp")
image natsuki 42be = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2bte.webp")
image natsuki 42bf = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2btf.webp")
image natsuki 42bg = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2btg.webp")
image natsuki 42bh = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2bth.webp")
image natsuki 42bi = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "2bti.webp")

image natsuki 5ba = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "a.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bb = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "b.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bc = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "c.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bd = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "d.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5be = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "e.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bf = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "f.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bg = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "g.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bh = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "h.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bi = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "i.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bj = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "j.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bk = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "k.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bl = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "l.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bm = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "m.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bn = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "n.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bo = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "o.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bp = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "p.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bq = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "q.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5br = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "r.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bs = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "s.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bt = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "t.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bu = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "u.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bv = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "v.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bw = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "w.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bx = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "x.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5by = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "y.webp", (0, 0), ts_natsuki_pt + "3b.webp")
image natsuki 5bz = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "z.webp", (0, 0), ts_natsuki_pt + "3b.webp")

image natsuki 1 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 2 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "1l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 3 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "1r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 4 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "2l.webp",(0,0), ts_natsuki_pt + "2r.webp",(0,0), ts_natsuki_pt + "1t.webp") )

image natsuki 5 = ConditionSwitch(
"persistent.sprite_time=='cloudly'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.63, 0.78, 0.85) ),
"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18, 22), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.94, 0.82, 1.0) ),
"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "1t.webp"), im.matrix.tint(0.5, 0.5, 0.6) ),
True,im.Composite((960,960), (0,0), ts_natsuki_pt + "3.webp",(18,22), ts_natsuki_pt + "1t.webp") )
