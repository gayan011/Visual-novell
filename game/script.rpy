# кодим код лол..
define k = Character('Катя', color="#c8ffc8")
define gg = Character('[viname]', color="#c8ffc8")
define ks = Character('Ксюша', color="#c8ffc8")
define l = Character('Лиза', color="#c8ffc8")
define z = Character('Женя', color="#c8ffc8")
define v = Character('Ваня', color="#c8ffc8")
define r = Character("Робот-помошник", color="#c8ffc8")

image bg white = "#ffffff"
image room = "images/room_second.png"
image logo = "images/black_logo.png"
image city = "images/eburg_second.png"
image bus = "images/автобус едет 1.png"
image busCom = "images/автобус у компании 1.png"
image holl = "images/холл компании.png"
image koridor1 = "images/Коридор1.png"
image koridor2 = "images/Коридор2.png"
image chillZone = "images/Комната отдыха.png"
image test= "images/test1.png"
image error= "images/error.png"
image q1= "images/question1.png"
image q2= "images/question2.png"
image q3= "images/question3.png"
image q4= "images/question4.png"



image robot1 = "images/карен1.png"
image robot2 = "images/карен2.png"
image robot3 = "images/карен3.png"
image vanya =im.Scale('images/Ваня обычный.png', 700, 1873)
image vanya angry =im.Scale('images/Ваня злой.png', 700, 1873)
image vanya sadly =im.Scale('images/Ваня грустный.png', 700, 1873) 
image vanya Smile =im.Scale('images/Ваня радостный.png', 700, 1873)
image vanya surprised  =im.Scale('images/Ваня удивленный.png', 700, 1873)
image liza =im.Scale('images/Лиза обычная.png', 700, 1873)
image liza Smile =im.Scale('images/Лиза радостная.png', 700, 1873)
image liza angry =im.Scale('images/Лиза сердитая.png', 700, 1873)
image liza surprised =im.Scale('images/Лиза удивленная.png', 700, 1873)
image liza sadly =im.Scale('images/Лиза грустная.png', 700, 1873)
image ksu =im.Scale('images/ксю обычная.png', 700, 1873)
image ksu Smile =im.Scale('images/ксю радостная.png', 700, 1873)
image ksu angry =im.Scale('images/Ксю сердитая.png', 700, 1873)
image ksu surprised =im.Scale('images/Ксю удивленная.png', 700, 1873)
image ksu sadly =im.Scale('images/Ксю грустная.png', 700, 1873)
image zhenya =im.Scale('images/женя обычный.png', 844, 1873)
image zhenya Smile =im.Scale('images/женя радостный.png', 844, 1873)
image zhenya angry = im.Scale('images/женя сердитый.png', 844, 1873)
image zhenya surprised =im.Scale('images/женя удивленный.png', 844, 1873)
image zhenya sadly=im.Scale('images/женя грустный.png', 844, 1873) 
image katy=im.Scale('images/катя обычная.png', 700, 1873)
image katySmile =im.Scale('images/катя радостная.png', 700, 1873)
image robot1=im.Scale('images/карен1.png', 400, 822)
image robot2=im.Scale('images/карен2.png', 400, 822)
image robot3=im.Scale('images/карен3.png', 400, 822)
image robot4=im.Scale('images/карен4.png', 400, 822)
image robot44 = im.Scale('images/карен4.png', 400, 822)
image robot22=im.Scale('images/карен2.png', 400, 822)
image robot5=im.Scale('images/загрузка 1.png', 400, 822)
image robot6 = im.Scale("images/предупреждение 1.png", 400, 822)
image robot7 = im.Scale("images/01.png", 400, 822)
image robot77 = im.Scale("images/01.png", 400, 822)
#music

#define audio.musfon=
define audio.dislocation="audio/Перемещение.mp3"
define audio.bus="audio/В автобусе.mp3"
define audio.laugh1="audio/Смех1.mp3"
define audio.laugh2="audio/Смех2.mp3"
define audio.busStop="audio/Автобус стоит.mp3"
define audio.shagi="audio/Гиги за шаги.mp3"
define audio.surpr1="audio/Удивление1.mp3"
define audio.surpr2="audio/Удивление2.mp3"
define audio.doorop="audio/door_open.mp3"
define audio.doorcl="audio/door_close.mp3"
define audio.scaryscary="audio/Катастрофа.mp3"
define audio.breakk="audio/Поломка.mp3"
define audio.tecno="audio/Эпичное техно.mp3"
define audio.stuk="audio/Стук по стеклу.mp3"


$ pol=null
$ qwe =null
$ chose1=0
$ score =0

init:
    $ renpy.music.register_channel("channel1", loop=False)
    $ renpy.music.register_channel("channel2", loop=False)
    $ left1= Position(xalign=0.8, yalign=-0.3)
    $ left2= Position(xalign=1.0, yalign=-0.3)
    $ centr11= Position(xalign=0.5, yalign=1.1)
    $ right1= Position(xalign=0.2, yalign=-0.2)
    $ robotright =Position(xalign=0.2, yalign=1.1)
    $ robotleft =Position(xalign=0.8, yalign=1.1)
    
transform move_right1:
    xalign -0.3
    yalign 1.1
    linear 3.0 xalign 0.5
transform move_right2:
    xalign -0.3
    yalign 1.1
    linear 2.0 xalign 0.2
transform move_left1:
    xalign 1.2
    yalign 1.1
    linear 16.0 xalign 0.1
transform move_right3:
    xalign -0.1
    yalign 1.1
    linear 16.0 xalign 1.1
transform move_left2:
    xalign 1.3
    yalign 1.1
    linear 2.0 xalign 0.8
    
label splashscreen:
    

    pause(0.5)
    scene logo
    pause(2)
    scene black with fade
    pause(1)


label start:
    #call scene2

    
    scene black
    
    "Что ж, это вы… В первую очередь, мы зададим вам вопрос, на который вы должны дать однозначный ответ."
    "В чём смысл вашей жизни?."
    "Шутка!"
    "Конечно мы не собираемся задавать вам подобные вопросы, когда вы пришли сюда явно не за тем, чтобы отвечать у доски ;)"
    
    menu:
        "Выберите пол главного героя:"
        
        "Мужской":
            $ pol="Мужской"
        "Женский":
            $ pol="Женский"
    
    "Вам будет предоставлена возможность выбора имени, наиболее подходящего вам, потому что создание точной копии вас у нас бы заняло целую жизнь!"
    
    $ viname = renpy.input("Итак, введите имя:")
      
    "(Звук телефонного уведомления)"
    
    "*С вашего счёта списали все средства*"
    
    "Ахахахаха, теперь вы – банкрот!"
    "Вот до чего дошли современные технологии: лишь определив ваши примерные характеристики мы уже смогли вас взломать!"
    "Ладно, чтобы не испортить вам весь настрой, давайте договоримся: если вы пройдёте эту игру, мы вам вернём эти средства обратно (честное хакерское), ну, а если нет, что ж, вы получите конфетку :)"
    
    "Теперь, когда выбор сделан, давайте переместимся в другой мир…"
    
    play sound dislocation volume 0.2
    scene bg white 
    
    "Глава 0.1: Предисловие."
    pause (3)
    scene black
    gg "…Сколько времени я уже сплю?"

    pause (0.5)
    play music bus volume 0.05
    scene bus
    "(открывает глаза, виду игрока открывается окно автобуса, за окном вдалеке видно здание компании Docool)"
    gg "Видимо не очень много."
    gg "- Ого, мы уже совсем скоро приедем! Интересно, чем же мы будем заниматься?"
    show liza at left1
    l "-О, а что если будет так: \n Сначала всё хорошо – нас тепло встретят, а потом внезапно начнётся хакерская атака и нам разрешат посмотреть, как работают специалисты!"
    gg "- Ха-ха-ха, Лиза, ты как обычно в своём репертуаре! Это напомнило мне 1 сентября, когда мы только поступили."
    gg "Ты тогда была такой же впечатлённой и не затыкалась ни на секунду."
    show liza Smile at left1
    l "- Да что вы говорите, а кто-то в первый же день чуть не заблудился в коридорах института."
    gg "- Ладно, 1:1."
    show liza at left1
    gg "- Да, тогда всё было таким неизведанным и непривычным"
    gg "- Особенно первые дни учёбы: пары вместо уроков, а они ещё и длятся полтора часа"
    gg "- Так много теории на лекциях, сложновато было слушать, а потом еще и на практике все отрабатывать..."
    show liza Smile at left1
    l "-Даа, это уж точно. А ещё из-за того, что пары находились в разных корпусах университета, приходилось бегать из одного в другое и успевать найти нужный кабинет"
    gg "-Пфф, да уж, думаю, я это не забуду до 60 лет."
    show liza at left1
    l "-А почему только до 60? У тебя потом что, память пропадёт?"
    gg "- А в 60 лет я на пенсию... \n Вот еще помнить тяжесть студенческих дней."
    show liza Smile at left1
    if pol == "Женский":
        l "- Хорошо, многопочтенная подруга, можно я тогда к вам присоединюсь лет через 40?"
    else:
        l "- Хорошо, многопочтенный друг, можно я тогда к вам присоединюсь лет через 40?"
    $ renpy.sound.play("Смех1.mp3", channel="channel1")
    $ renpy.sound.play("Смех2.mp3", channel="channel2")
    gg "Хорошо, что мы познакомились, думаю, мы и вправду будем дружить ещё до старости."
    scene busCom
    $ renpy.sound.play("Автобус стоит.mp3", channel="channel1", fadein=4)
    $ renpy.sound.play("Гиги за шаги.mp3", channel="channel2", fadein=1)
    "(Вид из окна размыт. Автобус снижает скорость"
    pause (3)
    $ renpy.music.stop("channel1")
    $ renpy.music.stop("channel2")
    "Глава 1.1: Прибытие студентов."
    scene holl with Fade(2.0, 0.0, 2.0)
    show liza at left2
    l "-Ого, здесь всё выглядит так современно и круто!"
    gg "-Да, производит хорошее первое впечатление."
    show robot2 at move_right1
    play sound surpr2
    pause(3)
    show zhenya surprised at right1
    z "- Карен приехала, берегитесь, где-то рядом Планктон!"
    show liza Smile at left2
    gg "- Похоже кто-то пересмотрел Губки Боба"
    hide liza
    hide zhenya
    r "-Доброе утро, студенты"
    r "-Рад вас видеть в нашей компании «Docool» на учебном мероприятии! Или, как обычно говорят, на практике."
    r "Сегодня вы увидите устройство нашей IT-компании, а также сможете решить несколько задач и попробовать себя в роли специалистов по информационной безопасности."
    show robot22 at move_right2
    r "-Так как вас довольно много, разделитесь на 2 равные группы. Мы с другим роботом-помощником  объясним, что делать дальше."
    call menu1 from _call_menu1
    if chose1==1:
        call scene1 from _call_scene1
    elif chose1==2:
        call scene2 from _call_scene2




label scene1:
    #налево
    r "-Теперь, пройдёмте за мной."
    hide robot2
    scene koridor2 with Fade(2.0, 0.0, 2.0)
    show zhenya at left2
    z "-Интересно, а робот может слышать нас?"
    hide zhenya
    show robot2 at move_left1
    r "-Конечно, я умею принимать голосовые запросы и отвечать на них. Можете задавать мне вопросы про интересующие вас темы."
    
    play music shagi volume 0.5
    show liza at left2
    l "-Когда был изобретён первый компьютер?"
    hide liza
    r "-В 1941 году."
    show liza at left2
    l "-А когда наступит конец света?"
    hide liza
    r "В моей базе данных нет ответа нет на этот вопрос, но на него есть ответ в сети Интернет. Я дам ссылку на сайт с ответом на Ваш вопрос, но предупрежу, что источник может быть недостоверным"
    show liza at left2    
    l "-Да, до сих пор удивляюсь, как же я смогла определиться с выбором профессии. Тогда это казалось чем-то непонятным. Но вот я здесь, уже уверена в том, куда я иду."
    hide liza
    gg "-Да, выбор был не из простых: тесты на профориентацию, всякие обзоры на профессии. У меня глаза часто уставали от бесконечных пролистываний страниц сайтов с видами профессий "
    gg "-Хорошо, что этот период остался позади."
    r "-Итак, теперь я подробно расскажу, чем мы займёмся. Для начала, вы пройдёте тест на знание IT-сферы в целом в качестве подготовки к будущим действиям."
    r "Затем, мы отправимся на экскурсию по этажам компании, после чего вы попробуете решить несколько обычных для специалиста по информационной безопасности задач."
    show vanya at left1
    v "- А насколько сложными могут быть задачи?"
    hide vanya
    r "-Ваших знаний будет достаточно, чтобы решить пару задач, так что можете не беспокоиться."
    show zhenya Smile at right1
    z "-Вань, ты чего, уже готовишься сдаться? Мы же даже не начали."
    hide zhenya
    show vanya Smile at right1
    v "-Я рассчитываю наиболее хорошую стратегию для решения задач заранее, мне так просто шах не поставить, ха-ха!"
    hide vanya
    show zhenya Smile at right1
    z "-Да уж, тебя так просто не сломить."
    scene black with Fade(2.0, 0.0, 2.0)
    stop music
    play sound doorop
    pause(2)
    play sound doorcl
    scene chillZone with Fade(2.0, 0.0, 2.0)
    show robot44 at centr11
    r "- Для прохождения теста вам понадобятся ваши телефоны."
    r " С помощью QR-кода на моём экране перейдите на сайт, созданный компанией для проведения опросов и различной активности, и начните прохождение теста, нажав кнопку «Начать»."
    call menu2 from _call_menu2
    
    "Глава 2: «Хакерская» атака."
    show zhenya surprised at right1
    z "-Чё за?"
    hide zhenya
    gg "-Похоже, сайт накрылся из-за большого количества запросов."
    scene chillZone
    show robot5 at centr11
    r "-Боюсь, Вы не правы. В настоящий момент происходит проникновение злоумышленников в продукты компании."
    show liza at left1
    l "-Хакерская атака что ли?"
    hide liza   
    r "-Да. К сожалению, нам придётся прервать прохождение практики."
    show vanya at left2
    v "-И что нам теперь делать?"
    hide vanya
    show liza at left1
    l "-Такой же вопрос. Мы же не собираемся просто стоять здесь?"
    hide robot5
    show robot6 at centr11
    r "-Мне понадобится ваша помощь, я связался с другим роботом-помощником и мы пришли к единому решению: необходимо связаться с кем-нибудь из сотрудников компании. "
    r "Сегодня выходной день – суббота, поэтому все работают удалённо, кроме нас – роботов"
    r "А для связи с работником необходимо иметь доступ к его рабочему месту. Давайте воссоединимся с вашими одногруппниками в холле 1-го этажа."
    scene koridor1
    play music shagi
    show robot5 at move_right3
    gg "- Я не совсем понимаю, а где найти это рабочее место и как понять, что это то, что нам надо?"
    r "-В данном случае нам лучше всего сразу связаться со специалистами отдела безопасности, который находится на 6-м этаже здания. "
    r "Хотя, мы можем связаться и с сотрудниками технического отдела, он расположен на 2-м этаже"
    r "Так будет быстрее и скорость нам сейчас важна, а доступ к рабочему месту будет обеспечен мной или другим роботом-помощником."
    gg "-Лиза, ты похоже накаркала, когда мы в автобусе ехали."
    show liza Smile at right1
    l "-Ну, я всё равно не выспалась, значит, в следующий раз."
    hide liza
    show zhenya at left1
    z "-Лиза, ты что, гадалка?"
    hide zhenya
    show liza Smile at left2
    l "-Да, сейчас я загадаю, когда тебе прилетит щелбан."
    hide liza
    show zhenya at left2
    z "-Ой, не надо пж."
    stop music
    scene holl with Fade(2.0, 0.0, 2.0)
    show robot2 at move_right2
    show robot22 at move_left2
    pause(2)
    hide robot2
    hide robot22
    show robot7 at robotright
    show robot77 at robotleft
    play music breakk volume 0.3
    show zhenya angry at right1
    z "-Сегодня всё решило сломаться?"
    hide zhenya
    show liza sadly at left1
    l "-Тише ты, тут посочувствовать надо – у них просто сегодня очень много событий происходит, вот и стресс начался. "
    hide liza
    stop music 
    play music tecno volume 0.3
    r "-Студенты, вы не сможете выбраться из этого здания: я взломал всю включённую технику, поэтому вы будете вынуждены наблюдать за тем, как всё здесь поглотит хаос. Да начнётся игра на выживание!"
    play sound stuk
    z "-Входные двери действительно закрыты!"

    gg "- Значит, остальные двери должны быть открыты. Давайте пойдём на 2-й этаж, робот говорил, что там получится связаться со специалистами."
    show vanya at right1
    v "-А если компьютер тоже взломан?"
    hide vanya
    show ksu at left2
    ks "-Если он выключен, то хакер не может его взломать. А сотрудники всегда выключают компы, когда уходят с работы."
    hide ksu
    show liza at left1
    l "-Отлично, надо поспешить. Чем быстрее мы с этим закончим, тем лучше."
    scene 
    return
    
    
    

label scene2:
    #направо
    r "-Следуйте  за мной."
    scene koridor2
    play music shagi volume 0.5
    show robot2 at move_right3
    r "-Если у вас появятся вопросы, то можете задать их."
    show zhenya at left2
    z "-Скажите, а чем эта практика отличается от той, которую могут провести в самом институте?"
    hide zhenya
    r "-К сожалению, я не знаю, как проходят практики у Вас в институте, поэтому не могу сравнить эти 2 практики."
    r "-Однако я уверенно могу сказать, что на нашем предприятии Вы получите очень полезный опыт работы."
    show liza at left1
    l "-(шёпотом) Когда мы уже столкнёмся с хакерами?"
    hide liza
    show ksu at right1
    ks "-Не думаю, что на первой практике это сразу же произойдёт."
    hide ksu
    gg "-Конечно, сначала нужна завязка, потом развитие, а потом в момент кульминации мы увидим хакеров."
    show zhenya Smile at left2
    z "-А может всё будет как в эпичной манге?"
    hide zhenya
    show liza surprised at right1
    l "-Етижи пассатижи, мы так можем написать целый роман, подобный «Войне и миру». "
    hide liza
    r "-Итак, теперь я подробно расскажу, чем мы займёмся. Для начала, вы пройдёте тест на знание IT-сферы в целом в качестве подготовки к будущим действиям."
    r "-Затем, мы отправимся на экскурсию по этажам компании, после чего вы попробуете решить несколько обычных для специалиста по информационной безопасности задач."
    gg "-Звучит интересно, а какие это могут быть задачи? "
    r "-Я не могу Вам сказать, это упростит решение задач."
    show liza Smile at right1
    l "Что [viname], хочешь считерить? "
    hide liza
    gg "-Пфф, я и без подсказок справлюсь."
    scene black with Fade(2.0, 0.0, 2.0)
    stop music
    play sound doorop
    pause(2)
    play sound doorcl
    scene chillZone with Fade(2.0, 0.0, 2.0)
    show robot44 at centr11
    r "- Для прохождения теста вам понадобятся ваши телефоны."
    r " С помощью QR-кода на моём экране перейдите на сайт, созданный компанией для проведения опросов и различной активности, и начните прохождение теста, нажав кнопку «Начать»."
    call menu2 from _call_menu2_1
    "Глава 2: «Хакерская» атака."
    show zhenya at right1
    z "-Неужто сайт не выдержал одновременного захода 15 человек?"
    hide zhenya
    scene chillZone
    show robot5 at centr11
    r "-Боюсь, Вы не правы. В настоящий момент происходит проникновение злоумышленников в продукты компании."
    r "К сожалению, нам придётся прервать прохождение практики."
    show ksu surprised at left1
    ks "-Ладно, беру свои слова об атаке хакеров назад"
    hide ksu
    hide robot5
    show robot6 at centr11
    r "-Нет, но мне понадобится ваша помощь, я связался с другим роботом-помощником и мы пришли к единому решению: необходимо связаться с кем-нибудь из сотрудников компании. "
    r "Сегодня выходной день – суббота, поэтому все работают удалённо, кроме нас – роботов"
    r "А для связи с работником необходимо иметь доступ к его рабочему месту. Давайте воссоединимся с вашими одногруппниками в холле 1-го этажа."
    scene koridor2
    play music shagi
    show robot5 at move_left1
    gg "-А почему вы – роботы не можете сами связаться с работниками?"
    r "-Потому что всегда есть риск того, что мы можем в неисправном состоянии сделать что-то неправильно."
    r "Поэтому, согласно протоколу, необходимо, чтобы с человеком связался другой человек, не робот."
    show liza at left1 
    l "-И куда нам надо идти, с кем конкретно связаться?"
    r "-В данном случае нам лучше всего сразу связаться со специалистами отдела безопасности, который находится на 6-м этаже здания."
    r " Хотя, мы можем связаться и с сотрудниками технического отдела, он расположен на 2-м этаже."
    r " Так будет быстрее и скорость нам сейчас важна, а доступ к рабочему месту будет обеспечен мной или другим роботом-помощником."
    stop music
    scene holl with Fade(2.0, 0.0, 2.0)
    
    
    
    
    return

    
    








label menu2:
    scene test
    menu:
        "Начать":
            pass
    scene q1
    menu:
        "Что такое IT (Информационные технологии)?"
        "Использование компьютерных систем или устройств для передачи информации":
            "Правильно"
        "Технологии, применяемые на роботах":
            "Неправильно"
        "Технологии, применяемые на людях":
            "Неправильно"
    scene q2
    menu:
        "Кто может использовать IT-технологии?"
        "Практически любой человек (переход к следующему вопросу)":
            "Правильно"
        "Люди, достигшие 18-ти летия":
            "Неправильно"
        "Продвинутые IT-специалисты":
            "Неправильно"
    scene q3
    menu:
        "Выберите преимущества работы в IT-сфере:"
        "Карьерный рост и развитие, записывать код в тетрадь":
            "Неправильно"
        "Записывать код в тетрадь, высокая заработная плата (если специалист уже состоявшийся)":
            "Неправильно"
            
        "Возможность удалённой работы, карьерный рост и развитие, высокая заработная плата (если специалист уже состоявшийся)":
            "Правильно"
        "Высокая конкуренция, сидячая работа":
            "Неправильно"
        "Высокая заработная плата (если специалист уже состоявшийся), сидячая работа":
            "Неправильно"
    scene q4
    menu:        
        "Какие направления есть в IT-сфере?"
        "Бизнес":
            pass
        "Общепит":
            pass
        "Торговля":
            pass
        "Образование":
            pass
        "Технологии":
            pass
        "Медицина":
            pass
        "Искусство и развлечения":
            pass
    scene error
    play music scaryscary
    return

label menu1:
    menu:
        gg "Хмм... Я пойду с..."
        "Пойти налево (группа с Лизой, Женей и Ваней)":
            $ chose1=1
        "Пойти направо (группа с Лизой, Ксюшей и Ваней)":
            $ chose1=2
        "Я человек прямолинейный":
            r "вы не можете пройти сквозь стену"
            call menu1 from _call_menu1_1

    