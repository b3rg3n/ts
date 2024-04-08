init python:
 
    renpy.register_shader("shadertoy.rainonwindow", variables="""
        uniform float u_time;
        uniform vec2 u_model_size;
        uniform float u_rain_amount;
        uniform sampler2D tex0;
    """,
        fragment_functions="""
        vec3 N13(float p)
        {
           vec3 p3 = fract(vec3(p) * vec3(.1031,.11369,.13787));
           p3 += dot(p3, p3.yzx + 19.19);
           return fract(vec3((p3.x + p3.y)*p3.z, (p3.x+p3.z)*p3.y, (p3.y+p3.z)*p3.x));
        }
        vec4 N14(float t)
        {
            return fract(sin(t*vec4(123., 1024., 1456., 264.))*vec4(6547., 345., 8799., 1564.));
        }
 
        float N(float t)
        {
            return fract(sin(t*12345.564)*7658.76);
        }
 
        float Saw(float b, float t)
        {
            return smoothstep(0., b, t) * smoothstep(1., b, t);
        }
 
        vec2 DropLayer2(vec2 uv, float t)
        {
            vec2 UV = uv;
 
            uv.y += t*0.75;
            vec2 a = vec2(6., 1.);
            vec2 grid = a*2.;
            vec2 id = floor(uv*grid);
 
            float colShift = N(id.x);
            uv.y += colShift;
 
            id = floor(uv*grid);
            vec3 n = N13(id.x*35.2+id.y*2376.1);
            vec2 st = fract(uv*grid)-vec2(.5, 0);
 
            float x = n.x-.5;
 
            float y = UV.y*20.;
            float wiggle = sin(y+sin(y));
            x += wiggle*(.5-abs(x))*(n.z-.5);
            x *= .7;
            float ti = fract(t+n.z);
            y = (Saw(.85, ti)-.5)*.9+.5;
            vec2 p = vec2(x, y);
 
            float d = length((st-p)*a.yx);
 
            float mainDrop = smoothstep(.4, .0, d);
 
            float r = sqrt(smoothstep(1., y, st.y));
            float cd = abs(st.x-x);
            float trail = smoothstep(.23*r, .15*r*r, cd);
            float trailFront = smoothstep(-.02, .02, st.y-y);
            trail *= trailFront*r*r;
 
            y = UV.y;
            float trail2 = smoothstep(.2*r, .0, cd);
            float droplets = max(0., (sin(y*(1.-y)*120.)-st.y))*trail2*trailFront*n.z;
            y = fract(y*10.)+(st.y-.5);
            float dd = length(st-vec2(x, y));
            droplets = smoothstep(.3, 0., dd);
            float m = mainDrop+droplets*r*trailFront;
 
            return vec2(m, trail);
        }
 
        float StaticDrops(vec2 uv, float t)
        {
            uv *= 40.;
 
            vec2 id = floor(uv);
            uv = fract(uv)-.5;
            vec3 n = N13(id.x*107.45+id.y*3543.654);
            vec2 p = (n.xy-.5)*.7;
            float d = length(uv-p);
 
            float fade = Saw(.025, fract(t+n.z));
            float c = smoothstep(.3, 0., d)*fract(n.z*10.)*fade;
            return c;
        }
 
        vec2 Drops(vec2 uv, float t, float l0, float l1, float l2)
        {
            float s = StaticDrops(uv, t)*l0;
            vec2 m1 = DropLayer2(uv, t)*l1;
            vec2 m2 = DropLayer2(uv*1.85, t)*l2;
 
            float c = s+m1.x+m2.x;
            c = smoothstep(.3, 1., c);
 
            return vec2(c, max(m1.y*l0, m2.y*l1));
        }
    """,
        vertex_300="""
        v_tex_coord = a_tex_coord;
    """,
 
        fragment_300="""
        vec2 uv = (gl_FragCoord.xy - u_model_size.xy*.5) / u_model_size.y;
        vec2 UV = gl_FragCoord.xy/u_model_size.xy;
        float T = u_time + 2.;
 
        float t = T*.2;
 
        float rainAmount = u_rain_amount;
 
        float maxBlur = mix(3., 6., rainAmount);
        float minBlur = 2.;
 
        float story = 0.;
        float heart = 0.;
 
 
        float zoom = 1.0;
        uv *= .7+zoom*.3;
 
        UV = (UV-.5)*(.9+zoom*.1)+.5;
 
        float staticDrops = smoothstep(-.5, 1., rainAmount)*2.;
        float layer1 = smoothstep(.25, .75, rainAmount);
        float layer2 = smoothstep(.0, .5, rainAmount);
 
 
        vec2 c = Drops(uv, t, staticDrops, layer1, layer2);
 
        vec2 e = vec2(.001, 0.);
        float cx = Drops(uv+e, t, staticDrops, layer1, layer2).x;
        float cy = Drops(uv+e.yx, t, staticDrops, layer1, layer2).x;
        vec2 n = vec2(cx-c.x, cy-c.x);
 
 
        float focus = mix(maxBlur-c.y, minBlur, smoothstep(.1, .2, c.x));
        vec3 col = texture2DLod(tex0, UV+n, focus).rgb;
 
        gl_FragColor = vec4(col, 1.);
    """)
 
init python:
 
    class RainOnWindow(renpy.Displayable):
 
        def __init__(self, child, width, height, rainamount=1.0, **kwargs):
            super(RainOnWindow, self).__init__(**kwargs)
 
            self.child = renpy.displayable(child)
            self.width = width
            self.height = height
            self.rainamount = rainamount;
 
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.place(self.child)
            render.add_shader("shadertoy.rainonwindow")
            render.add_uniform("u_time", st)
            render.add_uniform("u_model_size", (self.width, self.height))
            render.add_uniform("u_rain_amount", self.rainamount)
            renpy.redraw(self, 0)
            return render