# АХУЕННЫЙ ШЕЙДЕР
# ВЗЯТО ОТСЮДА https://www.shadertoy.com/view/wsdBWM
# ADAPTED BY BERGENCHEEEK SUKA
init 10 python:
    renpy.register_shader(

        "ts_shader_chromaticAbberation",

        variables="""
            uniform float u_lod_bias;
            uniform sampler2D tex0;

            uniform float u_distortionAmount;
            uniform float u_redShift;
            uniform float u_greenShift;
            uniform float u_blueShift;

            attribute vec2 a_tex_coord;

            varying vec2 v_tex_coord;
        """,

        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,

        fragment_300="""
            float child_alpha = texture2D(tex0, v_tex_coord, u_lod_bias).a;         

            float rChannel = texture2D(tex0, distortion(v_tex_coord, u_redShift * u_distortionAmount), u_lod_bias).r;
            float gChannel = texture2D(tex0, distortion(v_tex_coord, u_greenShift * u_distortionAmount), u_lod_bias).g;
            float bChannel = texture2D(tex0, distortion(v_tex_coord, u_blueShift * u_distortionAmount), u_lod_bias).b;
            
            gl_FragColor = vec4(rChannel, gChannel, bChannel, child_alpha);
        """,

        fragment_functions="""
            vec2 distortion(in vec2 uv, float strength) {
                vec2 st = uv - 0.5;
                float uvA = atan(st.x, st.y);
                float uvD = dot(st, st);
                return 0.5 + vec2(sin(uvA), cos(uvA)) * sqrt(uvD) * (1.0 - strength * uvD);
            }
        """
    )

init 15 python:
    from renpy.uguu import GL_REPEAT

init 15:
    transform ts_trns_chromAbber(update_delay=0.016, red_shift=0.3, green_shift=0.15, blue_shift=0.075, distortion_amount=0.75):# БОЛЕЕ ЛАЙТОВЫЙ ОРИГ БЕЗ ЗАТЕМНЕНИЯ И ОБЕСЦВЕТА
        mesh True
        shader "ts_shader_chromaticAbberation"

        u_distortionAmount distortion_amount
        u_redShift red_shift
        u_greenShift green_shift
        u_blueShift blue_shift
        gl_texture_wrap (GL_REPEAT, GL_REPEAT)

    transform ts_trns_dream:# СТАТИК БЕЗ ОБЕСЦВЕТА С БЛУМОМ
        ts_trns_chromAbber(0.016, 0.3, 0.15, 0.075, 0.75)
        matrixcolor SaturationMatrix(2.) * BrightnessMatrix(.15)
    transform ts_trns_baddream:# СТАТИЧЕСКИЙ ЭФФЕКТ + ОБЕСЦВЕТ
        ts_trns_chromAbber(0.016, 0.3, 0.15, 0.075, 0.75)
        matrixcolor SaturationMatrix(.1) * BrightnessMatrix(-.15)