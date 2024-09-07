# TRUE STORY POEMS
# written by @Maddie, The Mad & @Dan Salvato
# ported from ddlc by @b3rg3n
# original style by @Dan Salvato

init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

    poem_y1 = Poem(
    author = "yuri",
    title = "Призрак на свету",
    text = """\
Локоны мои блестят в янтарном свете,
В нём купаясь.
Я нашла:
Всего один фонарь прошёл сквозь время, сквозь года,
Лишь для того, чтоб будущего тени раскрасили больным зелёно-синим его жар.
Я им омыта. Я спокойна; вдыхаю воздух настоящего, из прошлого глядя.
Мерцает свет.
В ответ мерцаю я."""
    )

    poem_y1_eng = Poem(
    author = "yuri",
    title = "Ghost Under the Light",
    text = """\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
It must be this one.
The last remaining streetlight to have withstood the test of time.
the last yet to be replaced by the sickening blue-green hue of the future.
I bathe. Calm; breathing air of the present but living in the past.
The light flickers.
I flicker back."""
    )


    poem_farewell_aki = Poem(
    author = "monika",
    title = "",
    text = """\
Привет, бездарность. Думаю, кое-что всё-таки нужно прояснить.

В общем, помнишь, как я говорила, что {b}всё{/b}, с момента твоей отключки после пьянки, и до судьбоносной встречи с Мирой, было сном?

Ну так вот, я... слегка тебе наврала. Ну, неправду сказала. Приукрасила, так сказать.

Первый цикл на самом деле сном не был. Сны начались уже со второго цикла. Поэтому-то за тебя никто и не беспокоился о тебе, потому что ты на самом деле жила эту жизнь.

А все эти кошмары второго цикла и так далее - это уже было... моё видение всей этой недели, так сказать.

Но не об этом - тебе был дан второй шанс. Не потрать его впустую, как первый.

Всегда твоя (а какая же ещё?),

Аки."""
    )

    poem_farewell_aki_eng = Poem(
    author = "monika",
    title = "",
    text = """\
Hi there, mediocrity. I think it's time to set the record straight.

Soooooo, you know how I said that {b}everything{/b}, ever since the moment of passing out from a drink event and up until fatal meeting with Mira, was a dream?

Weeeell, I... lied to you. Just a little bit. I said untruth. I, uh, overexaggerated it all a little.

First cycle wasn't actually a dream. Dreams began since the second one. And that's why no one ever bothered about where you've been, because you actually lived a real life.

And all those nightmares and such - that was... my envision of the week, so to speak.

But I digress - you've been given a second chance. Don't waste it like the first one.

Always yours (and no one else's),

Aki."""
    )

    poem_farewell = Poem(
    author = "lemaman",
    title = "Прости. Прощай.",
    text = """\
Привет, Моника. Если ты это читаешь, то меня уже давно нет. Но не в том смысле, что я умерла, а что меня просто нет.

Когда папа рассказал про твою кому, у меня буквально сердце в пятки ушло. Я отправилась домой первым же рейсом и как можно быстрее примчалась к тебе. И твоё состояние было... явно не из лучших.

Мы с папой и ещё с парой девочек, которые, как я понимаю, состояли с тобой в одном клубе, дежурили и подменяли друг друга. Но, естественно, у них у всех была ещё и школа, и работа, и прочие прелести жизни.

Поэтому с тобой часто оставалась одна только я.

Спустя где-то недели три папа не справился с горем и начал пить. Так сильно, как никогда в жизни. Утром он шёл на работу, а домой он всегда возвращался минимум с двумя бутылками водки.

Естественно, я оставалась с ним, и даже уволилась с работы. В начале нового года мы должны были разрабатывать новый проект, однако я сказала, что не оставлю мужа одного, иначе он бы просто спился.

Но... Ещё спустя где-то месяц даже моё нахождение рядом с ним дало сбой, и он начал спиваться, даже когда я была рядом. И это не говоря о том, что мы до сих пор продолжали ездить к тебе. Правда, девочек уже что-то не было видно...

Клянусь, я была с ним до последнего, но однажды ему продали некачественную водку, плюс в тот вечер он напился сильнее обычного, и в общем... К утру его уже не стало.

Не справившись с потерей двух моих самых близких и дорогих людей, которые у меня только были, я от злости и горя пишу тебе эту записку, а сама уезжаю в аэропорт и возьму билет на первый попавшийся рейс, лишь бы куда подальше от этого проклятого города.

Я не знаю, прочтёшь ли ты это вообще, или же нет, но я в любом случае хочу... попросить у тебя прощения.

Прости меня за то, что была не настолько хорошей матерью все эти годы... И что если бы не я, то этого бы в принципе не произошло.

Прости меня, Моника. Прости. Прощай.

Мама."""
    )

    poem_farewell_eng = Poem(
    author = "lemaman",
    title = "Monika,",
    text = """\
If you're reading this, then I'm long gone. Not in a sense that I died, I'm just gone.

When dad told me about your coma, my heart literally sank to my feet. I came back as soon as possible and leaped to you as quickly as it got. Your condition was... not the best of all.

Me, my dad and a couple of girls who I guess were your clubmates were keeping up the watch and changing one another. But of course, they've all got either school or work or something else.

So I was frequently left alone with you.

After three weeks or so dad didn't cope with grief and started drinking. So hard like never in my life. Every morning he left for work, coming back with at least two bottles of vodka.

Naturally, I stayed with him, and even quit my job. Initially we planned to develop a new project at the start of next year, but I said that I won't leave my husband alone, otherwise he'd just drink himself to death.

But... After about a month after that even me being with him malfunctioned, and he started getting hungout even with me on his side. And that's not even talking about that we still kept coming to you. However, the girls went missing...

I swear, I was with him until the very end, but one night he bought a low-quality vodka, plus that night he drank even more than usual, and so... By morning he had already passed away.

Having not coped with the loss of two of the closest people who I ever had, out of anger and frustration I'm writing to you this note, and then I'll come to the airport and buy a ticket at the first available flight, as further from this cursed town as possible.

I don't even know if you read this or not, but I still want you to... forgive me.

Forgive me for I haven't been a good mother all these years... And if it isn't for me, then that would've never happened in the first place.

Forgive me, Monika. And farewell.

Mom."""
    )

    poem_test = Poem(
    author = "monika",
    title = "С другой стороны",
    text = """\
Вдоль дороги\n
я вижу\n
девочку одну\n\n
И вижу,\n
как копает она\n
к центру Земли\n\n\n
Копает всё дальше, копает сильнее
Бурит она сквозь почву и магму
Чтоб Солнце увидеть с другой стороны\n\n

У дороги\n
говорю я\n
с девочкой одной\n\n
Она даёт мне\n
лопату\n
чтобы с ней я вместе копала\n\n
Не смею я задавать ей вопросы
О намерениях её и обо всём остальном
Лишь жестом показала\n
копать вместе с ней\n\n

У дороги\n
копаем мы\n
свой собственный путь\n\n
До земли\n
где можем мы\n
Солнце увидеть\n
с другой стороны\n\n\n
После тысячи лет темноты
Она мне наконец предоставила
Возможность солнце увидеть\n\n\n\n\n\n\n\n\n
с другой стороны"""
    )

    poem_test_eng = Poem(
    author = "monika",
    title = "Dig for the Sun",
    text = """\
Off the road\n
I see\n
A young girl\n
I see her\n
Digging her way\n\n
Working harder, going deeper\n
She will walk through Earth innards\n
Just to see the sun\n\n\n

Off the road\n
I talk\n
To young girl\n
She gives a shovel\n
To dig with her\n\n
I don't dare to ask a question\n
Only made a single gesture\n
To dig for the sun\n\n

Off the road\n
we dig\n
Our own way\n
To the land we can\n
See the sun\n\n
After thousand years of midnight\n
The option that I'm given\n
I'm glad to see the sun"""
    )

    poem_m1 = Poem(
    author = "monika",
    title = "Дыра в стене",
    text = """\
Запутанная, я отчаянно оглядываюсь вокруг себя.
Но мои обожжённые глаза не могут больше различать цвета.
Есть ли другие в этой комнате? Они ведь тоже говорят, да?
Или это просто стихи на плоских бумаги листах,
Чьи звуки безумного скрипа творят какофонию у меня в ушах?
Комната начинает сужаться.
Всё меньше пространства оставляя.
Воздух, не доходя до лёгких, рассеивается, удушая.
Я в панике мечусь. Выход найти хочу.
Он прямо здесь. Под рукой.

Подавив страхи все, я перо беру и пишу стих свой."""
    )

    poem_m1_eng = Poem(
    author = "monika",
    title = "Hole in Wall",
    text = """\
Confused, I frantically glance at my surroundings.
But my burned eyes can no longer see color.
Are there others in this room? Are they talking?
Or are they simply poems on flat sheets of paper,
The sound of frantic scrawling playing tricks on my ears?
The room begins to crinkle.
Closing in on me.
The air I breathe dissipates before it reaches my lungs.
I panic. There must be a way out.
It's right there. He's right there.

Swallowing my fears, I brandish my pen."""
    )

    poem_s1 = Poem(
    author = "sayori",
    title = "Дорогие солнца лучики",
    text = """\
То, как ваш свет через жалюзи утром проходит,
Даёт мне понять, что вы скучали по мне.
Вы целуете меня в лобик, помогая с постели подняться скорей.
И глаза открыть, если сонливость с них долго не сходит
                
Вы просите меня выйти поиграть вместе с вами?
Верите, что дождливый день прогнать я смогу?
Я гляжу наверх: гладь да синева под небесами.
Вам я тоже верю, по секрету скажу.

Если б не вы, я бы спала дни и ночи.
Но я не сержусь,

Только вот кушать хочется очень."""
    )

    poem_s1_eng = Poem(
    author = "sayori",
    title = "Dear Sunshine",
    text = """\
The way you glow through my blinds in the morning
It makes me feel like you missed me.
Kissing my forehead to help me out of bed.
Making me rub the sleepy from my eyes.

Are you asking me to come out and play?
Are you trusting me to wish away a rainy day?
I look above. The sky is blue.
It's a secret, but I trust you too.

If it wasn't for you, I could sleep forever.
But I'm not mad.

I want breakfast."""
    )

    poem_n1 = Poem(
    author = "natsuki",
    title = "Орлы могут летать",
    text = """\
Обезьянки могут лазать,
Сверчки же - ловко прыгать,
Лошадки - скакать грациозно,
Совы - зыркать серьёзно,
Гепарды - быстро бегать,
Орлы - летать под облаками,
А люди могут попытаться,
Но на этом всё."""
    )

    poem_n1_eng = Poem(
    author = "natsuki",
    title = "Eagles Can Fly",
    text = """\
Monkeys can climb
Crickets can leap
Horses can race
Owls can seek
Cheetahs can run
Eagles can fly
People can try
But that's about it."""
    )

    poem_y1 = Poem(
    author = "yuri",
    title = "Призрак в тусклом свете",
    text = """\
Пряди моих волос злато отражают, в янтарном свете ниспадающем
Купаясь.
А вот его источник, стоящий одиноко.
Последний уличный фонарь, временем испытанный жестоко.
Неоном будущего сине-изумрудным он вскоре будет заменён.
И всё же продолжаю плыть я в нём.
В тиши вдыхаю воздух настоящего, но в прошлом существую.
Мерцает свет.
Мерцаю я ему в ответ."""
    )

    poem_y1_eng = Poem(
    author = "yuri",
    title = "Ghost Under the Light",
    text = """\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
It must be this one.
The last remaining streetlight to have withstood the test of time.
the last yet to be replaced by the sickening blue-green hue of the future.
I bathe. Calm; breathing air of the present but living in the past.
The light flickers.
I flicker back."""
    )

    poem_m3 = Poem(
    author = "monika",
    title = "Леди Которая Знает Всё",
    text = """\
Есть одна повесть, что как мир стара.
То сказ о странствующей леди, передающийся из уст в уста.
Леди, которой всё известно.
Леди, которая нашла ответы на вопросы повсеместные,
Весь смысл бытия,
Всю жизни суть,
Всё, что когда-то отыскать пытались.

И вот он я,


              перо


Потерянная жертва беззащитная, гонимая потоками ветров.

День за днём я ищу её без отдыха и снов.
Ищу, почти надежду потеряв, зная, что верою в легенды я не прав.
Но, когда прахом обратились все мои попытки,
Когда у остальных я наблюдал лишь спины да затылки,
Легенда - моя единственная надежда не растаявшая, - последняя тусклая звезда, в чёрном небе мерцающая.

И вот однажды ветер перестал.
Я опускаться быстро стал.
Я падал неизвестности навстречу, как мне казалось, целую вечность.
Как писчее перо по бумаге плывя.
Сухо выводящее безликие слова.

Тут меня двумя пальцами поймала чья-то рука.
Прекрасной леди принадлежала она.
Я взглянул в глаза деве и утонул в её взгляда бездне.

Леди Которая Знает Всё догадалась о моих мыслях.
Прежде чем я спросил, она прошептала пусто и близко:
«Я нашла все ответы, но цена им ничто.
Нет в мире смысла.
И цели давно.
Мы лишь невозможное пытаемся найти.
Я не легенда,
Её не существует, и нам не по пути».

Лёгким дыханием она меня обратно в полёт отправила, а там порыв ветра меня подобрал, унося в далёкие дали."""
    )

    poem_m3_eng = Poem(
    author = "monika",
    title = "The Lady who Knows Everything",
    text = """\
An old tale tells of a lady who wanders Earth.
The Lady who Knows Everything.
A beautiful lady who has found every answer,
All meaning,
All purpose,
And all that was ever sought.

And here I am,


              a feather


Lost adrift the sky, victim of the currents of the wind.

Day after day, I search.
I search with little hope, knowing legends don't exist.
But when all else has failed me,
When all others have turned away,
The legend is all that remains - the last dim star glimmering in the twilit sky.

Until one day, the wind ceases to blow.
I fall.
And I fall and fall, and fall even more.
Gentle as a feather.
A dry quill, expressionless.

But a hand catches me between the thumb and forefinger.
The hand of a beautiful lady.
I look at her eyes and find no end to her gaze.

The Lady who Knows Everything knows what I am thinking.
Before I can speak, she responds in a hollow voice.
"I have found every answer, all of which amount to nothing.
There is no meaning.
There is no purpose.
And we seek only the impossible.
I am not your legend.
Your legend does not exist."

And with a breath, she blows me back afloat, and I pick up a gust of wind."""
    )

    poem_m21 = Poem(
    author = "monika",
    title = "Дыра в стене",
    text = """\
Запутанная, я отчаянно оглядываюсь вокруг себя.
Но мои обожжённые глаза не могут больше различать цвета.
Есть ли другие в этой комнате? Они ведь тоже говорят, да?
Или это просто стихи на плоских бумаги листах,
Чьи звуки безумного скрипа творят какофонию у меня в ушах?
Комната начинает сужаться.
Всё меньше пространства оставляя.
Воздух, не доходя до лёгких, рассеивается, удушая.
Я в панике мечусь. Выход найти хочу.
Он прямо здесь. Под рукой.

Подавив страхи все, я перо беру и пишу стих свой."""
    )

    poem_m21_eng = Poem(
    author = "monika",
    title = "Hole in Wall",
    text = """\
Confused, I frantically glance at my surroundings.
But my burned eyes can no longer see color.
Are there others in this room? Are they talking?
Or are they simply poems on flat sheets of paper,
The sound of frantic scrawling playing tricks on my ears?
The room begins to crinkle.
Closing in on me.
The air I breathe dissipates before it reaches my lungs.
I panic. There must be a way out.
It's right there. He's right there.

Swallowing my fears, I brandish my pen."""
    )


    poem_m22a = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не
"""
   )

    poem_m22a_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
"""
   )

    poem_m22b = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не
Яркие, прекрасные цвета
Мерцают, взрываются, пронзают
"""
    )

    poem_m22b_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, beautiful colors
Flashing, expanding, piercing
"""
    )

    poem_m22c = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не 
Яркие, пре расные цвет 
М рцают, взрыва тся, пр нзают
Красный, зелёный, синий
Бесконечная
"""
    )

    poem_m22c_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, pi rcing
Red, green, blue
An  ndless
"""
    )

    poem_m22d = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не 
Яркие, пре расные цвет 
М рцают, взрыва тся, пр нзают
Красный, зелёный, синий
Бесконечная
КАКОФОНИЯ
БЕССМЫСЛЕННОГО
ШУМА
"""
    )

    poem_m22d_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, pi rcing
Red, green, blue
An endless
CACOPHONY
OF MEANINGLESS
NOISE
"""
    )

    poem_m22e = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не 
Яркие, пре расные цвет 
М рцают, вз ыва тся, пр нз ют
К асный, з лёный, синий
Бесконечная
КАКОФОНИЯ
БЕССМЫСЛЕННОГО
ШУМА

ШУМ, ОН НЕ ПРЕКРАЩАЕТСЯ.
"""
    )

    poem_m22e_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, pi r ing
R d, g een, blue
An endless
CACOPHONY
OF MEANINGLESS
NOISE

THE NOISE, IT WON'T STOP
"""
    )

    poem_m22f = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не 
Яркие, пре расные цвет 
М рцают, вз ыва тся, пр нз ют
К асный, з лёный, с   й
Беск н чная
КАК ФО ИЯ
БЕС М  Л   ОГО
  МА

ШУМ, ОН НЕ ПРЕКРАЩАЕТСЯ.
Безумные, грохочущие волны
"""
    )

    poem_m22f_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, pi r ing
R d, g een, b  e
An en l ss
CAC PHO Y
OF  E  IN   ESS
N  SE

THE NOISE, IT WON'T STOP
Violent, grating waveforms
"""
    )

    poem_m22fuck = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не 
Яркие, пре расные цвет 
М рцают, вз ыва тся, пр нз ют
К асный, з л  ый, с   й
Б  к н ч ая
К К  О ИЯ
БЕ  М  Л   ОГО
  МА

ШУМ, ОН НЕ ПРЕКРАЩАЕТСЯ.
Безу ные, грох чу ие во ны
Пищат, визжат, пронзают
"""
    )

    poem_m22fuck_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, pi r ing
R d, g een, b  e
An en l ss
CAC PHO Y
OF  E  IN   ESS
N  SE

THE NOISE, IT WON'T STOP
Viol nt, grating w vef rms
Squeaking, screeching, piercing
"""
    )

    poem_m22g = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не 
Яркие, пре расные цвет 
М рцают, вз ыва тся, пр нз ют
К асный, з л  ый, с   й
Б  к н ч ая
К К  О ИЯ
Б   М  Л    ГО
  МА

ШУМ, ОН НЕ ПРЕКРАЩАЕТСЯ.
Безу ные, грох чу ие во ны
Пи ат, в зжат, пр нза т
СИНУС, КОСИНУС, ТАНГЕНС
"""
    )

    poem_m22g_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
F a h ng, exp nd ng, pi r ing
R d, g   n, b  e
An  n l  s
CAC P O Y
OF  E  IN   ESS
N   E

THE NOISE, IT WON'T STOP
Viol nt, grating w vef rms
Sq e king, screech ng, piercing
SINE, COSINE, TANGENT
"""
    )

    poem_m22h = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цв та, они не 
 рк е, пре р с ые цв т 
М рцают, вз ыва тся, пр нз ют
К асный, з л  ый, с   й
Б  к н ч ая
К К  О ИЯ
Б   М  Л    ГО
  МА

Ш М, ОН НЕ ПР  РАЩ ЕТСЯ.
Безу ные, грох чу ие во ны
Пи ат, в зжат, пр нза т
С НУ , ОС Н С, Т  ГЕ С
    Как играть с пластинкой на диджей-вертушке
        КАК ИГРАТЬ С НОЖОМ НА ДЫШАЩЕЙ ГРУДИ
Бесконечный
стих
Бессмыслицы
"""
    )

    poem_m22h_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The c lors, they won't
B i  t, be  t f l c l  s
F a h ng, exp nd ng, pi r ing
R d, g   n, b  e
An  n l  s
CAC P O Y
OF  E  IN   ESS
N   E

THE N  SE, IT W N'T S  P
Viol nt, grating w vef rms
Sq e king, scr ech ng, pi rc ng
S N ,  OS N , T  GE T
    Like playing a chalkboard on a turntable
        LIKE PLAYING A KNIFE ON A BREATHING RIBCAGE
An endless
poem
Of meaningless
"""
    )

    poem_m22i = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цв та, они не
 рк е, пре р с ые цв т 
М рцают, вз ыва тся, пр нз ют
К а  ый, з л  ый, с   й
Б  к н ч ая
К К  О ИЯ
Б   М  Л    Г 
  М 

Ш М, ОН НЕ ПР К Р  Щ Е СЯ.
Б  у ные, г ох чу ие в  ны
Пи ат, в зж т, пр   а т
С НУ , ОС Н С, Т  ГЕ С
    Как игр ть с пл сти кой на д дже ве туш е
        КАК ИГР  Ь С Н  ОМ НА Д  АЩ Й ГР ДИ
ес он чн й
с и
Б с мы ли ы
"""
    )

    poem_m22i_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The c lors, they won't
B i  t, be  t f l c l  s
F a h ng, exp nd ng, pi r ing
R d, g   n, b  e
An  n l  s
C C P O Y
OF  E  IN   E
N   

THE N  SE, IT W   T S  P
V  l nt, g  t n  w v f  ms
Sq e king, scr ech ng, pi rc ng
S N ,  OS N , T  GE T
    Like p aying a ch lkb  rd on a t rnt ble
        LIKE P   I G A K  FE ON A B   TH NG R BCA E
 n  n l  s
p  m
O e  in l  s
"""
    )

    poem_act3_s = Poem(
    author = "sayori",
    title = "Квест",               
    text = """\
Но почему
Весь мир ко мне настолько жесток
Я застряла навеки
Должна пройти этот квест, чтобы я смогла жить

Все одинаковы, и все равны
Деньги, связи - это всё безразлично
Не важен статус и твои достижения
Я как другие, должна ждать вечно

Никто не знает, сколько должно
Пройти, чтобы я сделала всё
Но мне лишь кажется, что я в вечной борьбе
Этот вечный квест...

Моя жизнь - это квест, я вечно жду
Одного лишь решения мелочного
Я устала ждать, я устала жить
Я не хочу...
"""
    )

    poem_act3_s_eng = Poem(
    author = "sayori",
    title = "My Life's a Quest",               
    text = """\
I wonder why
The world's so hateful to me now
I'm stuck forever
I must pass a quest to have a life

We're all equal to this process
No matter do you have money or not
No status matters, nor your achievements
You stand in line, you take your spot

And no one knows how much time
Will it take for you to proceed
You wait forever to complete
Your lifetime quest...

My life is a quest, I wait forever
For resolving of my request
I'm tired of waiting, tired of living
I just don't want
"""
    )

    poem_act3_n = Poem(
    author = "natsuki",
    title = "Целый мир",               
    text = """

Время идёт, он живёт день за днём
Всё, что он умеет - ненавидеть всех вокруг
Он не может объяснить свой нездоровый эгоизм
И ненависть к миру, который его и породил

Он просто глупый ребёнок-эгоист
В его глазах другие - это просто мясные куски
Мне жаль его семью за то, что он такой родился
Никто не знает, за что он им приключился

Целый мир
\nненавидим тобой
Целый мир
\nне сделал и единой вещи плохой
Целый мир
\nизбавиться от тебя хочет
Целый мир
\nежедневно говорит «да пошёл ты»

Время идёт, он живёт день за днём
Всё, что он умеет - ненавидеть всех вокруг
Мне жаль его семью за то, что он такой родился
Никто не знает, за что он им приключился"""
)

    poem_act3_n_eng = Poem(
    author = "natsuki",
    title = "Whole World",               
    text = """

Time flows away, as he lives day by day 
The only thing he knows is how to hate 
He can't explain his selfish attitude 
To the world that he just abused

He's only a stupid and selfish kid 
For the others he is just walking meat 
I'm sorry to his family for him
Everyone now doesn't know what to do! 

Whole world 
\nIs hated by him
Whole world
\nDidn't do a thing for him 
Whole world
\nWants to get rid of him
Whole world
\nEveryday says 'screw him' 

Time flows away, as he lives day by day 
The only thing he knows is how to hate 
I'm sorry to his family for him
Everyone now doesn't know what to do!"""
)

    poem_act3_y = Poem(
    author = "yuri",
    title = "На глубине дна морского",               
    text = """

Барды слагают легенды
О печально известной королеве
Чьё царство растворилось
На глубине дна морского
Никогда не видел никто
Ни царство, ни саму королеву
Одна лишь расщелина
На глубине дна морского

Там есть древний дворец
В городе забытом
Внутри одной расщелины
На глубине дна морского
Одни лишь мифы да легенды
Со скоростью света плодятся
О царстве, которое
На глубине дна морского

Барды слагают легенды
О тени, которой века
Живущей во дворце
На глубине дна морского
Поговаривают, что тень
Это сама королева и есть
Но никаких доказательств
О царстве на глубине дна морского"""
)

    poem_act3_y_eng = Poem(
    author = "yuri",
    title = "На глубине дна морского",               
    text = """

Bards sing epics
Of infamous queen
Whose kingdom was banished
In the depths of the sea
No one has seen
Neither kingdom or queen
Only a deep trench
In the bottom of the sea

There's an ancient palace
In forgotten city
In the deep trench
In the bottom of the sea
Myths and legends
Withal it appears
With the kingdom that is now
In the bottom of the sea


Bards tell about
A million year old shadow
That lives in a palace
In the city in the sea
They say that shadow
Is the queen itself
But still no proofs
For the bottom of the sea"""
)

    poem_s2 = Poem(
    author = "sayori",
    title = "Бутылочки",
    text = """\
Я снимаю свой скальп, как крышку c коробки печенья.
Там всех моих снов тайное место хранения.
Они как в корзинке котята, забавные кексы, шариков света рой.
Я внутрь залезла поглубже, чтоб сковырнуть один рукой:
На ощупь он тёплый и колючий немного.
Но нельзя время тратить! В бутылку на сохранность его сразу же надо доставить.
А бутылку я ставлю на полку, где все остальные стоят.
Счастливые мысли, счастливые мысли, счастливые мысли в бутылочках в ряд.

Моя коллекция позволяет много друзей заводить.
Каждая бутылочка может любую проблему решить.
Бывает так, что мой друг неважно чувствует себя.
Бутылочка спускается вниз, на помощь приходя.

Ночь за ночью ещё больше снов.
Друг за другом, ещё больше бутыльков.
Всё ниже и ниже мои пальцы опускаются .
Будто в тёмном лесу сквозь чащу пробираются.
Роют и скребут.
Пока шарик не найдут.

Я сдуваю пыль с бутылочных крышек.
Не выглядит так, что срок годности вышел.
Моей пустой полке нужно ещё.
Мои друзья глядят через двери окно.

Наконец всё готово. Я открываю, впуская друзей.
Заходят они торопливо. Хотят мои бутылочки скорей?
Одну за другой лихорадочно достаю я их с полки.
Раздаю всем друзьям, никого не обделив.
Каждую бутылку, всю полку опустошив.
Но каждый раз, из рук их выпуская, о кафель под ногами стукались они.
Счастливые мысли, счастливые мысли, счастливые мысли разлетелись на осколки во все уголки.

Для моих неулыбчивых друзей они предназначались.
Те всё кричат, просят что-то, отчаясь.
Но всё, что я слышу, - эхо, эхо, эхо.
В своей голове."""
    )

    poem_s2_eng = Poem(
    author = "sayori",
    title = "Bottles",
    text = """\
I pop off my scalp like the lid of a cookie jar.
It's the secret place where I keep all my dreams.
Little balls of sunshine, all rubbing together like a bundle of kittens.
I reach inside with my thumb and forefinger and pluck one out.
It's warm and tingly.
But there's no time to waste! I put it in a bottle to keep it safe.
And I put the bottle on the shelf with all of the other bottles.
Happy thoughts, happy thoughts, happy thoughts in bottles, all in a row.

My collection makes me lots of friends.
Each bottle a starlight to make amends.
Sometimes my friend feels a certain way.
Down comes a bottle to save the day.

Night after night, more dreams.
Friend after friend, more bottles.
Deeper and deeper my fingers go.
Like exploring a dark cave, discovering the secrets hiding in the nooks and crannies.
Digging and digging.
Scraping and scraping.

I blow dust off my bottle caps.
It doesn't feel like time elapsed.
My empty shelf could use some more.
My friends look through my locked front door.

Finally, all done. I open up, and in come my friends.
In they come, in such a hurry. Do they want my bottles that much?
I frantically pull them from the shelf, one after the other.
Holding them out to each and every friend.
Each and every bottle.
But every time I let one go, it shatters against the tile between my feet.
Happy thoughts, happy thoughts, happy thoughts in shards, all over the floor.

They were supposed to be for my friends, my friends who aren't smiling.
They're all shouting, pleading. Something.
But all I hear is echo, echo, echo, echo, echo
Inside my head."""
    )

    poem_n2 = Poem(
    author = "natsuki",
    title = "Эми любит пауков",
    text = """\
Вот что я слышала об Эми -
Она любит пауков.
Мерзких, гадких, волосатых!
Не стану с ней водиться из-за её дружков.

У Эми милый певчий голос.
Мою любимую она песню поёт.
Каждый раз, как хор я слышу, моё сердце в ритм бьёт.
Но она любит пауков.
Не подружусь я с ней, мой выбор таков.

Однажды я ногу больно ушибла.
Эми мне помогла до лазарета дойти.
Прикасаться к ней мне было противно.
Она грязна, раз ей по нраву пауки,
Так что дружить мне с ней будет стыдно.

У Эми много друзей,
Она всегда в центре внимания.
О пауках она заводит много речей.
А вдруг пауков полюбит и её компания?
Никогда не быть нам подругами с ней.

Какая разница, что у неё ещё другие увлечения?
Какая разница, что она не говорит о них?
Какая разница, что они все безобидны?

Этому не может быть прощения.
Отвратительным тварям нет оправданий никаких.
Миру будет лучше без пауколюбов, это очевидно.

И я собираюсь всем глаза раскрыть."""
    )

    poem_n2_eng = Poem(
    author = "natsuki",
    title = "Amy Likes Spiders",
    text = """\
You know what I heard about Amy?
Amy likes spiders.
Icky, wriggly, hairy, ugly spiders!
That's why I'm not friends with her.

Amy has a cute singing voice.
I heard her singing my favorite love song.
Every time she sang the chorus, my heart would pound to the rhythm of the words.
But she likes spiders.
That's why I'm not friends with her.

One time, I hurt my leg really bad.
Amy helped me up and took me to the nurse.
I tried not to let her touch me.
She likes spiders, so her hands are probably gross.
That's why I'm not friends with her.

Amy has a lot of friends.
I always see her talking to people.
She probably talks about spiders.
What if her friends start to like spiders too?
That's why I'm not friends with her.

It doesn't matter if she has other hobbies.
It doesn't matter if she keeps it private.
It doesn't matter if it doesn't hurt anyone.

It's gross.
She's gross.
The world is better off without spider lovers.

And I'm gonna tell everyone."""
    )

    poem_y3b = Poem(
    author = "yuri",
    title = "Призрак в тусклом свете. Часть 2",
    text = """\
Пряди моих волос злато отражают, в янтарном свете ниспадающем
Купаясь.
Сине-изумрудный свет мерцает вдалеке.
Одинокая фигура показалась - силуэт, как призрака свечение.
Сердце застучало. Силуэт всё ближе подходил ко мне.
Зонт я распахнула, надеясь, тень - моё убежище.
Но поздно спохватилась я.
Вот он уже стоит под светом фонаря. Я ахнула, зонт уронила.
Мерцает свет. Колотится в груди. Рука его поднялась.

Время замерло, казалось.

Единственный движенья знак - янтарный свет, его рукою отражённый.
Свет мерцает, бьётся сердце в унисон.
Он дразнит меня за то, что отдалась эмоции запретной.
Могли вы знать, что призрак также чувствует тепло?
Я засмеялась, - понять попытки тщетны.
В чём важность осознания того?
Его рука в моей. Мерцанье прекратилось постепенно.
Цвет сердца моего - янтарь, а синий изумруд - его."""
    )

    poem_y3b_eng = Poem(
    author = "yuri",
    title = "Ghost Under the Light pt. 2",
    text = """\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
In the distance, a blue-green light flickers.
A lone figure crosses its path - a silhouette obstructing the eerie glow.
My heart pounds. The silhouette grows. Closer. Closer.
I open my umbrella, casting a shadow to shield me from visibility.
But I am too late.
He steps into the streetlight. I gasp and drop my umbrella.
The light flickers. My heart pounds. He raises his arm.

Time stops.

The only indication of movement is the amber light flickering against his outstretched arm.
The flickering light is in rhythm with the pounding of my heart.
Teasing me for succumbing to this forbidden emotion.
Have you ever heard of a ghost feeling warmth before?
Giving up on understanding, I laugh.
Understanding is overrated.
I touch his hand. The flickering stops.
Ghosts are blue-green. My heart is amber."""
    )

    poem_m2 = Poem(
    author = "monika",
    title = "Спаси меня",
    text = """\
Цвета, они не останавливаются.
Яркие, прекрасные цвета
Мерцают, взрываются, пронзают
Красный, зелёный, синий
Бесконечная
какофония
Бессмысленного
шума

Шум, он не прекращается.
Безумные, грохочущие волны
Пищат, визжат, пронзают
Синус, косинус, тангенс
    Как играть с пластинкой на диджей-вертушке
        Как проигрывать винил на холодной пицце 
Бесконечный
стих
Бессмыслицы
"""
    )

    poem_m2_eng = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't stop.
Bright, beautiful colors
Flashing, expanding, piercing
Red, green, blue
An endless
cacophony
Of meaningless
noise

The noise, it won't stop.
Violent, grating waveforms
Squeaking, screeching, piercing
Sine, cosine, tangent
    Like playing a chalkboard on a turntable
        Like playing a vinyl on a pizza crust
An endless
poem
Of meaningless
    """
    )

    poem_su_eng = Poem(
    author = "sayori",
    title = "My Meadow",
    text = """\

There's a special place that I go to.

Between my feet
The last remaining flower beckons to me.

I twist the stem, freeing it from its clinging roots
Caressing the final joyous moment between my fingers.

But to what ends have I summoned this joy?
For now when I look in every direction
The once-prosperous field before me



Is but a barren wasteland!

    """
)

    poem_su = Poem(
    author = "sayori",
    title = "Мой Луг",
    text = """\

У моих ног, мирно в земле сидящий...

Я вижу последний цветок,

так сладко меня манящий.

Я отрываю стебель, освобождая его от цепких корней...
Тереблю в пальцах последнюю радость своих очей.

Но чего ради лишила я света жизни цветок?
Ведь куда ни глянь – на север, юг, запад или восток...
Передо мной вместо когда-то пышущих жизнью зелёных полей...



Лишь бесплодная пустошь, да серость мёртвых степей!

    """
)

    poem_y2 = Poem(
    author = "yuri",
    title = "Енот",
    text = """\
История эта случилась поздно ночью, когда бутербродами перекусить мне захотелось очень.
Моё внимание привлёк один енот, он за окном шнырял, что видит - подберёт.
Как помню сейчас, свои странные наклонности я тогда заметила в первый раз,
Кусочком хлеба я с енотом поделилась, подсознание моё с последствиями смирилось.
Осознало оно, что, набив живот, ещё не раз ко мне придёт енот.
Пленяющая ножа красота - первым симптомом была.
Хлеба куски - моего любопытства тиски.
Зверёк - соблазна исток.

По мере того как росла луна, всё больше света отражалось от лезвия ножа.
Того же света, что мерцал в моего пушистого друга глазах.
Я режу хлеб, свеж и мягок он. Полосатый зверёк всё сильнее возбуждён.
Или, возможно, то мои эмоции беспокойные, спроецированные на енота довольного.

Енот стал упрям, за мной теперь следует по пятам.
Или как ещё можно сказать, мы в компании друг друга привыкли пребывать.
Аппетит зверька растёт день ото дня, мой хлеб выручает во все времена.
Каждый раз, как ножик берёт моя рука, енот в возбуждении скачет туда-сюда.
Кровь приливает, классический рефлекс Павлова в силу вступает.
Режу хлеб не спеша и снова насыщаю себя."""
    )

    poem_y2_eng = Poem(
    author = "yuri",
    title = "The Raccoon",
    text = """\
It happened in the dead of night while I was slicing bread for a guilty snack.
My attention was caught by the scuttering of a raccoon outside my window.
That was, I believe, the first time I noticed my strange tendencies as an unordinary human.
I gave the raccoon a piece of bread, my subconscious well aware of the consequences.
Well aware that a raccoon that is fed will always come back for more.
The enticing beauty of my cutting knife was the symptom.
The bread, my hungry curiosity.
The raccoon, an urge.

The moon increments its phase and reflects that much more light off of my cutting knife.
The very same light that glistens in the eyes of my raccoon friend.
I slice the bread, fresh and soft. The raccoon becomes excited.
Or perhaps I'm merely projecting my emotions onto the newly-satisfied animal.

The raccoon has taken to following me.
You could say that we've gotten quite used to each other.
The raccoon becomes hungry more and more frequently, so my bread is always handy.
Every time I brandish my cutting knife, the raccoon shows me its excitement.
A rush of blood. Classic Pavlovian conditioning. I slice the bread.
And I feed myself again."""
    )

    poem_peacedets_eng = Poem(
    author = "monika",
    title = "Dig for the Sun",
    text = """\
Off the road\n
I see\n
A young girl\n
I see her\n
Digging her way\n\n
Working harder, going deeper\n
She will walk through Earth innards\n
Just to see the sun\n\n\n

Off the road\n
I talk\n
To young girl\n
She gives a shovel\n
To dig with her\n\n
I don't dare to ask a question\n
Only made a single gesture\n
To dig for the sun\n\n

Off the road\n
we dig\n
Our own way\n
To the land we can\n
See the sun\n\n
After thousand years of midnight\n
The option that I'm given\n
I'm glad to see the sun"""
    )

    poem_peacedets = Poem(
    author = "monika",
    title = "С другой стороны",
    text = """\
Вдоль дороги\n
я вижу\n
девочку одну\n\n
И вижу,\n
как копает она\n
к центру Земли\n\n\n
Копает всё дальше, копает сильнее
Бурит она сквозь почву и магму
Чтоб Солнце увидеть с другой стороны\n\n

У дороги\n
говорю я\n
с девочкой одной\n\n
Она даёт мне\n
лопату\n
чтобы с ней я вместе копала\n\n
Не смею я задавать ей вопросы
О намерениях её и обо всём остальном
Лишь жестом показала\n
копать вместе с ней\n\n

У дороги\n
копаем мы\n
свой собственный путь\n\n
До земли\n
где можем мы\n
Солнце увидеть\n
с другой стороны\n\n\n
После тысячи лет темноты
Она мне наконец предоставила
Возможность солнце увидеть\n\n\n\n\n\n\n\n\n
с другой стороны"""
    )



image paper = "mod_assets/source/images/bg/poem/poem.webp"
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "mod_assets/source/images/bg/poem/poem-glitch1.webp"
image paper_glitch2:
    "mod_assets/source/images/bg/poem/poem-glitch2.webp"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat


transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            if currentpoem.yuri_2:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.yuri_3:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
            else:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
        elif currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        elif currentpoem.author == "natsuki":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
        elif currentpoem.author == "monika":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
        elif currentpoem.author == "lemaman":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "lemaman_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"



style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700





style yuri_text:
    font "mod_assets/source/fonts/poemdreest/y1.ttf"
    size 28
    color "#000"
    outlines []
    textshader None

style yuri_text_2:
    font "mod_assets/source/fonts/poemdreest/y2.ttf"
    size 26
    color "#000"
    outlines []
    textshader None

style yuri_text_3:
    font "mod_assets/source/fonts/poemdreest/y3.ttf"
    size 20
    color "#000"
    outlines []
    justify True
    textshader None

style natsuki_text:
    font "mod_assets/source/fonts/poemdreest/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1
    textshader None

style sayori_text:
    font "mod_assets/source/fonts/poemdreest/s1.ttf"
    size 22
    color "#000"
    outlines []
    textshader None

style monika_text:
    font "mod_assets/source/fonts/poemdreest/m1.ttf"
    size 22
    color "#000"
    outlines []
    textshader None

style lemaman_text:
    font "mod_assets/source/fonts/poemdreest/maki.ttf"
    size 22
    color "#000"
    outlines []
    textshader None
