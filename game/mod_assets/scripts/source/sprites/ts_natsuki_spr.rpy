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


image natsuki 31 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "1t.webp")
image natsuki 3a = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "a.webp")
image natsuki 3b = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "b.webp")
image natsuki 3c = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "c.webp")
image natsuki 3d = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "d.webp")
image natsuki 3e = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "e.webp")
image natsuki 3f = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "f.webp")
image natsuki 3g = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "g.webp")
image natsuki 3h = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "h.webp")
image natsuki 3i = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "i.webp")
image natsuki 3j = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "j.webp")
image natsuki 3k = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "k.webp")
image natsuki 3l = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "l.webp")
image natsuki 3m = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "m.webp")
image natsuki 3n = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "n.webp")
image natsuki 3o = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "o.webp")
image natsuki 3p = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "p.webp")
image natsuki 3q = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "q.webp")
image natsuki 3r = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "r.webp")
image natsuki 3s = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "s.webp")
image natsuki 3t = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "t.webp")
image natsuki 3u = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "u.webp")
image natsuki 3v = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "v.webp")
image natsuki 3w = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "w.webp")
image natsuki 3x = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "x.webp")
image natsuki 3y = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "y.webp")
image natsuki 3z = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "z.webp")
image natsuki 3za = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "za.webp")
image natsuki 3zb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "zb.webp")
image natsuki 3zc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "zc.webp")

image natsuki 41 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "1t.webp")
image natsuki 4a = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "a.webp")
image natsuki 4b = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "b.webp")
image natsuki 4c = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "c.webp")
image natsuki 4d = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "d.webp")
image natsuki 4e = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "e.webp")
image natsuki 4f = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "f.webp")
image natsuki 4g = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "g.webp")
image natsuki 4h = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "h.webp")
image natsuki 4i = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "i.webp")
image natsuki 4j = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "j.webp")
image natsuki 4k = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "k.webp")
image natsuki 4l = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "l.webp")
image natsuki 4m = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "m.webp")
image natsuki 4n = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "n.webp")
image natsuki 4o = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "o.webp")
image natsuki 4p = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "p.webp")
image natsuki 4q = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "q.webp")
image natsuki 4r = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "r.webp")
image natsuki 4s = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "s.webp")
image natsuki 4t = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "t.webp")
image natsuki 4u = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "u.webp")
image natsuki 4v = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "v.webp")
image natsuki 4w = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "w.webp")
image natsuki 4x = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "x.webp")
image natsuki 4y = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "y.webp")
image natsuki 4z = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "z.webp")
image natsuki 4za = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "za.webp")
image natsuki 4zb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "zb.webp")
image natsuki 4zc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "zc.webp")

image natsuki 12 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2t.webp")
image natsuki 12a = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2ta.webp")
image natsuki 12b = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tb.webp")
image natsuki 12c = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tc.webp")
image natsuki 12d = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2td.webp")
image natsuki 12e = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2te.webp")
image natsuki 12f = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tf.webp")
image natsuki 12g = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2tg.webp")
image natsuki 12h = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2th.webp")
image natsuki 12i = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "2ti.webp")

image natsuki 42 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2t.webp")
image natsuki 42a = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2ta.webp")
image natsuki 42b = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tb.webp")
image natsuki 42c = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tc.webp")
image natsuki 42d = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2td.webp")
image natsuki 42e = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2te.webp")
image natsuki 42f = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tf.webp")
image natsuki 42g = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2tg.webp")
image natsuki 42h = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2th.webp")
image natsuki 42i = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "2ti.webp")

image natsuki 51 = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "1t.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5a = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "a.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5b = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "b.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5c = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "c.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5d = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "d.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5e = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "e.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5f = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "f.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5g = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "g.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5h = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "h.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5i = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "i.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5j = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "j.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5k = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "k.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5l = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "l.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5m = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "m.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5n = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "n.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5o = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "o.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5p = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "p.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5q = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "q.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5r = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "r.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5s = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "s.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5t = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "t.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5u = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "u.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5v = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "v.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5w = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "w.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5x = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "x.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5y = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "y.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5z = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "z.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5za = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "za.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5zb = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "zb.webp", (0, 0), ts_natsuki_pt + "3.webp")
image natsuki 5zc = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "zc.webp", (0, 0), ts_natsuki_pt + "3.webp")

image natsuki 1ba = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "a.webp")
image natsuki 1bb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "b.webp")
image natsuki 1bc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "c.webp")
image natsuki 1bd = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "d.webp")
image natsuki 1be = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "e.webp")
image natsuki 1bf = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "f.webp")
image natsuki 1bg = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "g.webp")
image natsuki 1bh = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "h.webp")
image natsuki 1bi = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "i.webp")
image natsuki 1bj = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "j.webp")
image natsuki 1bk = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "k.webp")
image natsuki 1bl = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "l.webp")
image natsuki 1bm = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "m.webp")
image natsuki 1bn = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "n.webp")
image natsuki 1bo = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "o.webp")
image natsuki 1bp = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "p.webp")
image natsuki 1bq = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "q.webp")
image natsuki 1br = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "r.webp")
image natsuki 1bs = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "s.webp")
image natsuki 1bt = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "t.webp")
image natsuki 1bu = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "u.webp")
image natsuki 1bv = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "v.webp")
image natsuki 1bw = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "w.webp")
image natsuki 1bx = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "x.webp")
image natsuki 1by = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "y.webp")
image natsuki 1bz = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "z.webp")

image natsuki 2ba = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "a.webp")
image natsuki 2bb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "b.webp")
image natsuki 2bc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "c.webp")
image natsuki 2bd = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "d.webp")
image natsuki 2be = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "e.webp")
image natsuki 2bf = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "f.webp")
image natsuki 2bg = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "g.webp")
image natsuki 2bh = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "h.webp")
image natsuki 2bi = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "i.webp")
image natsuki 2bj = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "j.webp")
image natsuki 2bk = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "k.webp")
image natsuki 2bl = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "l.webp")
image natsuki 2bm = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "m.webp")
image natsuki 2bn = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "n.webp")
image natsuki 2bo = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "o.webp")
image natsuki 2bp = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "p.webp")
image natsuki 2bq = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "q.webp")
image natsuki 2br = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "r.webp")
image natsuki 2bs = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "s.webp")
image natsuki 2bt = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "t.webp")
image natsuki 2bu = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "u.webp")
image natsuki 2bv = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "v.webp")
image natsuki 2bw = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "w.webp")
image natsuki 2bx = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "x.webp")
image natsuki 2by = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "y.webp")
image natsuki 2bz = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1bl.webp", (0, 0), ts_natsuki_pt + "2br.webp", (0, 0), ts_natsuki_pt + "z.webp")

image natsuki 3ba = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "a.webp")
image natsuki 3bb = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "b.webp")
image natsuki 3bc = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "c.webp")
image natsuki 3bd = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "d.webp")
image natsuki 3be = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "e.webp")
image natsuki 3bf = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "f.webp")
image natsuki 3bg = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "g.webp")
image natsuki 3bh = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "h.webp")
image natsuki 3bi = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "i.webp")
image natsuki 3bj = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "j.webp")
image natsuki 3bk = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "k.webp")
image natsuki 3bl = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "l.webp")
image natsuki 3bm = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "m.webp")
image natsuki 3bn = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "n.webp")
image natsuki 3bo = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "o.webp")
image natsuki 3bp = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "p.webp")
image natsuki 3bq = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "q.webp")
image natsuki 3br = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "r.webp")
image natsuki 3bs = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "s.webp")
image natsuki 3bt = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "t.webp")
image natsuki 3bu = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "u.webp")
image natsuki 3bv = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "v.webp")
image natsuki 3bw = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "w.webp")
image natsuki 3bx = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "x.webp")
image natsuki 3by = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "y.webp")
image natsuki 3bz = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2bl.webp", (0, 0), ts_natsuki_pt + "1br.webp", (0, 0), ts_natsuki_pt + "z.webp")

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

image natsuki 1 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "1t.webp")
image natsuki 2 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "1l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "1t.webp")
image natsuki 3 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "1r.webp", (0, 0), ts_natsuki_pt + "1t.webp")
image natsuki 4 = im.Composite((960, 960), (0, 0), ts_natsuki_pt + "2l.webp", (0, 0), ts_natsuki_pt + "2r.webp", (0, 0), ts_natsuki_pt + "1t.webp")
image natsuki 5 = im.Composite((960, 960), (18, 22), ts_natsuki_pt + "1t.webp", (0, 0), ts_natsuki_pt + "3.webp")
