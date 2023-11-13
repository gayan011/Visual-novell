# Игра начинается здесь:
define s = Character('Сильвия', color="#c8ffc8")
define m = Character('Джон', color="#ffffff")


image meadow = "images/fon.png"
image gg = "images/gg_main_second.png"
image room = "images/room_second.png"
image logo = "images/logo_final.jpg"
image city = "images/eburg_second.png"
label splashscreen:
    

    pause(0.5)
    scene logo
    pause(2)
    scene black with fade
    pause(1)
    
label start:
    
    scene black
    "..."
    "bing bing bing!!!"
    m "Очередное утро, а не поспать бы мне еще..."
    m "Первой парой основы безопаснисти компьютерных систем. \n Странно это противоречит безопасности моего будильника..."    

    scene room

    m "Сегодня ожидается великий день."

    m "Не опоздать бы на пары."
    
    show gg
    
    m "Пора покорять этот мир."
    
    scene city

    m "Какой же красивый город ранним утром"
    
    scene meadow

    m "Эмм... Такое ощущение что я единственный кто приехал так рано."

    show gg
        
    m "Привет"

    "Молчание."