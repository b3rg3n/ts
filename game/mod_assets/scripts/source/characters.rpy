# TRUE STORY CHARACTERS
# by @b3rg3n
# Since 2024

init:
    define brg = DynamicCharacter('razrab_name', what_prefix='"', what_suffix='"')
    define teacher = DynamicCharacter('teacher_name', image='yuri', what_prefix='"', what_suffix='"')
    define ts_ft = DynamicCharacter('ts_ft_name', image='hiroto', what_prefix='"', what_suffix='"')
    define mc = DynamicCharacter('user', what_prefix='"', what_suffix='"')
    define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"')
    define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"')
    define em = DynamicCharacter('em_name', image='monika', what_prefix='"', what_suffix='"')
    define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"')
    define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"')
    define ny = DynamicCharacter('natandyuriname', what_prefix='"', what_suffix='"')
    define ts_unk = DynamicCharacter('unk_name', what_prefix='"', what_suffix='"')
    define pod1 = DynamicCharacter('pod1_name', image='himari', what_prefix='"', what_suffix='"')
    define pod2 = DynamicCharacter('pod2_name', image='elena', what_prefix='"', what_suffix='"')
    define cm = DynamicCharacter('cm_name', image='monika', what_prefix='"', what_suffix='"')
    define ts_mt = DynamicCharacter('ts_mt_name', image='monika', what_prefix='"', what_suffix='"')
    define stud = DynamicCharacter('stud_name', what_prefix='"', what_suffix='"')
    define k = DynamicCharacter('k_name', image='kuninobu', what_prefix='"', what_suffix='"')
    define misc = DynamicCharacter('misc_name', image='harumi', what_prefix='"', what_suffix='"')
    define ts_director = DynamicCharacter('ts_director_name', image='daisuke', what_prefix='"', what_suffix='"')
    define doc = DynamicCharacter('doc_name', what_prefix='"', what_suffix='"')


###NVL ПАЦАНТРЕ
    define nvlbazar = Character (u' ', kind=nvl, color = "#dd9933", what_color="FFFFFF",)

### ИМЕНА
    if _preferences.language == "english":
        $ teacher_name = "Teacher"
        $ ts_ft_name = "Dad"
        $ s_name = "Sayori"
        $ m_name = "Monika"
        $ y_name = "Yuri"
        $ n_name = "Natsuki"
        $ pod1_name = "Girlfriend"
        $ pod2_name = "Girlfriend"
        $ ts_mt_name = "Minami"
        $ natandyuriname = "Natsuki and Yuri"
        $ stud_name = "Classmate"
        $ k_name = "Mira"
        $ misc_name = "Administrator"
        $ ts_director_name = "Director"
        $ doc_name = "Dr. Bergen"
    else:
        $ teacher_name = "Учитель"
        $ ts_ft_name = "Папа"
        $ s_name = "Сайори"
        $ m_name = "Моника"
        $ y_name = "Юри"
        $ n_name = "Нацуки"
        $ pod1_name = "Подруга"
        $ pod2_name = "Подруга"
        $ ts_mt_name = "Минами"
        $ natandyuriname = "Нацуки и Юри"
        $ stud_name = "Одноклассник"
        $ k_name = "Мира"
        $ misc_name = "Администратор"
        $ ts_director_name = "Директор"
        $ doc_name = "Д-р Берген"

    $ unk_name = "???"
    $ em_name = glitchtext(12)
    $ player = "[user]"
    $ razrab_name = "BERGEN"
    $ cm_name = "???"