init:
        $ a = Character("เรียวตะ อากาเนะ")
        $ r = Character("ยาสุรากิ เรย์")
        $ akarui = Character("อาคารุย มิไร")
        $ h = Character("คิอิโระ ฮิมาวาริ")
        $ g = Character("???")
        #n = navigator
        $ n = Character("")
        $ d = Character("ตุ๊กตา")

image Akane = "Akane2023.png"
image Himawari = "Himawari2023.png"
image Rei = "Rei2023.png"
image Mirai = "Akari Mirai2023.png"
image Ghost1 = "GhostShadow.png"
image Ghost2 = "Ghost.png"
image Ghost_Half = "GhostHalf.png"
image AkaneHalf = "AkaneHalf2023.png"
image HimawariHalf = "HimawariHalf2023.png"
image ReiHalf = "ReiHalf2023.png"
image MiraiHalf = "MiraiHalf2023.png"
#BG
image Building1 = "Building1.png"
image Building2 = "Building2.png"
image bg room = "bg room.jpg"
image GymLine = "GymLine.png"
image GymLine_Red = "GymLine_Red.png"
image StorageroomLine = "StorageroomLine.png"
image bg rooftop = "bg rooftop.jpg"
image bg rooftop_red = "bg rooftop_red.jpg"
#Cutscene
image hallway girl = "Gpj1_1.png"
image hallway flower = "Gpj2_1.png"
image picture_frame ="Gpj3_1.png"
image coffin1 ="Gpj3_2.png"
image coffin2 ="Gpj3_3.png"
image school hallway ="Gpj4_1.png"
image school hallway2 ="Gpj4_2.png"
image school hallway3 ="Gpj4_3.png"
image Mirai_dead ="Gpj5.png"
image Mirai_choked ="Gpj6_1.png"
image Mirai_choked2 ="Gpj6_2.png"
image Mirai_choked3 ="Gpj6_3.png"
image storage room ="Gpj7_1.png"
image white_flower = "Gpj7_2.png"








label start:

#scene 1 นอก รร


#ใช้ show/hide ในการแสดงภาพตัวละคร
    play music "Maestro.mp3"
    play sound "Afternoon_Crickets_Long.mp3"


    scene Building1
    with Dissolve(.5)



    g "นี่ทุกคน เราเข้ามาโรงเรียนตอนนี้มันจะดีหรอ ?"
    show Rei:
        xalign 0.5
        yalign 7.0
    n "ยาสุรากิ เรย์ เอ่ยถามกลุ่มเพื่อนที่กำลังปีนข้ามรั้วโรงเรียนเพื่อที่จะเข้าไปด้านใน"
    hide Rei
    g "ฮึบ ! เราตัดสินใจแล้วนี่ ว่าจะมาตามหามิไรกัน เธอเองก็เห็นด้วยไม่ใช่หรอตอนนั้นน่ะ"
    show Akane:
        xalign 0.75
        yalign 7.0
    n "เรียวตะ อากาเนะ ก้มลงมามองเพื่อนสาวที่ยืนอยู่ฝั่งด้านนอกของโรงเรียน โดยที่เธอนั้นนั่งอยู่บนกำแพงและพร้อมที่จะกระโดดลงไปในฝั่งของโรงเรียน"
    hide Akane
    g "ทั้งสองคนเร็วๆหน่อย เดี๋ยวยามมาจะซวยเอา"
    n "เสียงกึ่งตะโกนจากฝั่งในโรงเรียนเรียกทั้งสองคนอย่างเร่งรีบ"
    show Himawari:
        xalign 0.2
        yalign 7.0
    n "คิอิโระ ฮิมาวาริ เข้ามารออีกฝั่งนานแล้ว เธอนั้นไม่มีอะไรติดตัวกันมาเลย"
    hide Himawari
    show HimawariHalf
    n"ตามหลักความเป็นจริงถ้าลอบเข้าไปไหนสักที่ การพกของมาเยอะแยะเป็นอะไรที่โง่มาก"
    n"และการพกไฟฉายมีสิทธิ์เสี่ยงที่ยามจะเจอพวกเธอโดยง่าย"
    hide HimawariHalf
    n "เรย์ที่ยืนอยู่ด้านนอกยอมเข้ามาด้านในตามเพื่อนๆ เพราะเธอเองก็ยอมรับปากก่อนหน้านี้แล้วว่าจะมาตามหามิไรด้วย เธอจึงต้องยอมรับชะตากรรมครั้งนี้อย่างช่วยไม่ได้"
    stop music fadeout 1.0
    stop sound


    n "ทั้งสี่คนเดินเลาะกำแพงไปเพื่อเข้าไปในตัวอาคารหลักของโรงเรียน จนกระทั่งเข้ามาได้ในที่สุด"





#scene 2 เข้ามาในอาคาร
    scene bg game2
    show AkaneHalf at right
    show HimawariHalf at left
    with Dissolve(.5)
    a "เอาล่ะ เราจะแยกกันตามหากันคนละที่มันจะได้เร็ว ถ้าใครเจออะไรแล้วให้มารอตรงนี้ถ้าใครเดินหาไม่เจอก็กลับมารอที่นี่ ระวังตัวด้วยมันมืด"
    n "อากาเนะพูดจบเธอได้เดินแยกไปทางโรงยิมเพื่อเริ่มค้นหา คนอื่น ๆ มองหน้ากันก่อนจะแบ่งพื้นที่กัน"
    h "งั้นฉันจะไปชั้น 4-7 เรย์ไปดูบริเวณชั้น1-3 แล้วก็บริเวณด้านล่าง"
    n "ฮิมาวาริถือโอกาสแจกแจงหน้าที่ให้คนที่เหลือ"
    hide AkaneHalf
    hide HimawariHalf
    n "ฮิมาวาริไปชั้น4-7 อากาเนะไปโรงยิมและโรงเก็บของ เรย์ไปชั้น1-3"
    n "เรย์ที่อยู่ตรงนั้นคนเดียวถอนหายใจออกมาและเริ่มตามหาเพื่อนที่หายไปอย่างละเอียดที่สุด"
    r "เฮ้อ…"


# ชั้น 2
    scene bg room
    with Dissolve(.5)
    n "-ชั้น 2-"
    n "เรย์เดินดูแต่ละห้องเรียนของชั้นหนึ่งจนละเอียดแต่ก็ไม่เจอสิ่งมีชีวิตอะไรเลย"

    pause .5

    scene bg game2
    with Dissolve(.5)
    show ReiHalf
    r "นั่นมันห้องสมุดนี่"
    hide ReiHalf
    n "เรย์พูดขึ้นก่อนจะก้าวเท้าเข้าไป มือสองข้างเลื่อนไปเปิดประตูแต่มันกลับโดนล็อกเอาไว้"
    play sound "opendoor8.mp3"
    n "กึก กึก"
    show ReiHalf
    r   "โดนล็อกอยู่แฮะ กุญแจก็น่าจะอยู่กับบรรณารักษ์ห้องสมุด.."
    hide ReiHalf
    n "เมื่อเปิดไม่ได้เรย์จึงตัดใจไปหาที่ชั้น 3"
    n "-ชัั้น 3-"
    n "เมื่อเรย์กำลังจะเดินสำรวจที่ชั้น3 สายตาเธอก็เหลือบไปเห็นเพื่อนผมสั้นของเธอที่ยืนนิ่งค้างอยู่ตรงกลางทางเดิน"

    stop sound
    show hallway girl at truecenter
    with Dissolve(.5)



# ชั้น 3
menu :


    "เดินไปหาเพื่อน" :
        scene bg game2
        with Dissolve(.5)
        show ReiHalf

        r "ฮิมาวาริ ? เป็นอะไรไป"
        hide ReiHalf
        n "ด้วยความเป็นห่วงเรย์ได้เดินเข้าไปหาก่อนจะแตะไหล่จนฮิมาวาริสะดุ้ง"
    "ฮิมาวาริเดินมาหา" :
        scene bg game2
        with Dissolve(.5)
        show ReiHalf
        r "ฮิมาวาริ ฮิมาวาริ!"
        n "เรย์เรียกชื่อเพื่อนเสียงดังขึ้น ฮิมาวาริเดินเข้ามาหาตามเสียงเรียก แต่เสียงเท้าของเธอมันหนักสม่ำเสมอกันจนน่าขนลุก"
        hide ReiHalf
        show HimawariHalf
        h "...."
        n "ฮิมาวาริไม่พูดอะไร หน้าของเธอดูนิ่งเรียบไร้การแสดงอารมณ์ จนเรย์ต้องสะกิดเพื่อนของเธอ"
        hide HimawariHalf

label after_menu:
    play sound "heartbeat.mp3"
    show HimawariHalf
    h "!!!!"
    hide HimawariHalf
    show HimawariHalf at left
    show ReiHalf at right
    r "ไม่เป็นอะไรใช่ไหม สีหน้าเธอไม่ค่อยดีเลย"
    hide HimawariHalf
    hide ReiHalf
    n "เรย์ถามด้วยความเป็นห่วง"
    show HimawariHalf
    h "อ้าว เรย์มาได้ไง"
    show HimawariHalf at left
    show ReiHalf at right
    r "ฉันสิต้องถาม นี่มันชั้น 3 นะ เธอต่างหากมาได้ยังไง"
    h "ไม่รู้สิ จู่ๆขามันก็เดินมาเองรู้ตัวอีกทีก็มาอยู่ที่นี่แล้ว"
    hide HimawariHalf
    hide ReiHalf
    n "(ฮิมาวาริกับเรย์อยู่ด้วยกันชั้น 3)"
    show HimawariHalf at left
    show ReiHalf at right
    r "เธอเดินสำรวจชั้น 4-7 เสร็จแล้วหรอ ?"
    h "อื้ม แต่มันมีบางห้องเปิดไม่ได้ฉันเลยลงมา"
    r "ฉันเองก็เหมือนกัน งั้นเราลงไปรอที่ห้องโถงด้านล่างกัน"
    h "อื้ม"
    hide HimawariHalf
    hide ReiHalf
    n "ในระหว่างที่ทั้งสองกำลังเดินลงไปด้านล่างก็พบกับกลีบดอกไม้ที่ร่วงอยู่ตรงขึ้นบันได ดอกไม้กลีบเล็กกลีบน้อยร่างหล่นเป็นทางยาวขึ้นไปชั้นบน"
    play music "Maestro.mp3"
    show hallway flower
    with Dissolve(.5)
    pause #1

    r "ฉันจำได้ว่าตรงนี้มันไม่มีกลีบดอกไม้นี่"
    show hallway flower at truecenter
    with Dissolve(.5)
    show HimawariHalf at left
    show ReiHalf at right
    n "เรย์พูดขึ้นอย่างตกใจ ก่อนหน้านี้เธอมาทางนี้เธอจำไม่ได้เลยสักนิดว่ามีกลีบดอกไม้ร่วงอยู่"
    h "ฉันเองก็ขึ้นลงบันไดแต่ทางด้านซ้ายเลยไม่รู้ว่าบันไดฝั่งนี้มีอะไร"
    n "ฮิมาวาริเองก็ไม่รู้เหมือนกันว่าสิ่งนี้มันมาได้ยังไง"
    h "งั้นเราขึ้นไปดูกันเถอะ"
    hide HimawariHalf
    hide ReiHalf
    n "ฮิมาวาริเดินนำขึ้นไปเพื่อดูในแน่ใจว่ามันคืออะไรกันแน่ เรย์ที่ไม่สามารถปฏิเสธได้จึงเดินตามหลังไป"
    n "ทั้งสองเดินตามกลีบดอกไม้ขึ้นไปยังชั้น 6 กลีบดอกไม้ร่วงตกอยู่หน้าห้องเรียนห้องหนึ่ง"
    show HimawariHalf at left
    show ReiHalf at right
    h "นี่มันห้องเรียนเรานี่"
    n "ฮิมาวาริมีสีหน้าตกใจอย่างเห็นได้ชัด กลีบดอกไม้พาพวกเธอมายังห้องที่พวกเธอนั้นเรียนอยู่ปัจจุบัน"
    scene bg room
    with Dissolve(.5)
    n "ฮิมาวาริกลั้นใจเปิดประตูเข้าไปก็พบกับแท่นบูชาเล็กๆ ที่มีดอกไม้และรูปตั้งอยู่บนโต๊ะๆหนึ่งในห้อง ทั้งสองรู้ได้ในทันทีเลยว่านั่นคือโต๊ะของมิไรที่หายตัวไป"
    h "นั่นมันรูปของมิไรนี่ ใครกันที่ทำแบบนี้"
    show picture_frame at truecenter
    with Dissolve(.5)
    n "ฮิมาวาริทั้งตกใจและรู้สึกโกรธที่มีคนมาเล่นแบบนี้ เธอไม่เชื่อหรอกว่าเพื่อนเธอจะตายแล้ว"
    hide HimawariHalf
    hide ReiHalf

menu :
    "หยิบรูปมาดู" :
        $ havedollanswer = "yes"
        n "เรย์หยิบรูปขึ้นมาดูก่อนจะพลิกดูด้านหนัง ปรากฏวันที่ 13/09/XX บนกรอบด้านหลัง"
        show HimawariHalf at left
        show ReiHalf at right
        h "วันที่อะไรน่ะ"
        n "ฮิมาวาริถาม"
        r "ไม่รู้สิ"
        hide HimawariHalf
        hide ReiHalf
    "ไม่หยิบรูป" :
        $ havedollanswer = "no"
        show HimawariHalf at left
        show ReiHalf at right
        r "หืม? ฮิมาวาริดูนี่สิ!"
        n "เรย์ที่กำลังสำรวจมองรอบๆก็ได้พบกับรอยเลือดที่หยดยาวออกทางประตูด้านหลังห้องไป"
        h "ละ เลือดนี่ของใครกัน"
        n "ฮิมาวาริเริ่มสั่นกลัว"
        r "อาจจะเป็นว่ามีใครได้รับบาดเจ็บในช่วงที่โรงเรียนปิดก็ได้"
        hide HimawariHalf
        hide ReiHalf
        n "เรย์จึงเดินตามมันไป รอยเลือดจากที่เป็นหยดๆเปลี่ยนเป็นรอยยาวไปจนถึงประตูดาดฟ้า เรย์พยายามที่จะเปิดมันแต่มันกลับล็อกอยู่"
        play sound "doorlock.mp3"
        n "กึก กึก"
        show HimawariHalf at left
        show ReiHalf at right
        r "“ต้องหากุญแจมาเปิด ฉันว่าน่าจะอยู่ด้านล่าง"
        n "(ฮิมาวาริและเรย์เดินไปชั้นล่าง)"
        hide HimawariHalf
        hide ReiHalf

label after_menu2:

    scene bg game2
    with Dissolve(.5)
    n "-ชั้น 4-"
    stop music fadeout 1.0
    n "ระหว่างที่เดินลงชั้น4จู่ๆหางตาของเรย์ก็เหลือบไปเห็นร่างๆหนึ่งที่ยืนอยู่บนทางเดิน แต่เมื่อหันกลับไปมองก็ไม่พบอะไรมีแต่ทางโล่งๆ"
    show HimawariHalf
    h "มีอะไรรึเปล่า"
    n "ฮิมาวาริหันมาถามเรย์ที่หยุดเดินตามเธอ"
    hide Himawari

menu :
    "ไม่บอกเพื่อน" :
        show HimawariHalf at left
        show ReiHalf at right
        r "ไม่มีอะไร"
        hide HimawariHalf
        n "เรย์ไม่อยากบอกเพื่อนให้รู้สึกกลัวไปมากกว่านี้จึงเลือกที่จะเงียบ "
        hide ReiHalf
    "บอกเพื่อน" :
        show HimawariHalf at left
        show ReiHalf at right
        r "เหมือนฉันเห็นคนยืนอยู่ตรงทางเดิน แต่ตอนนี้ไม่อยู่แล้ว"
        n "เรย์มีสีหน้าซีดลง แม้จะเป็นแค่หางตาแต่เธอมั่นใจว่าเห็นคนยืนอยู่ตรงนั้นจริงๆ"
        h "เธออาจตาฝาดไปเองก็ได้"
        n "ฮิมาวาริพูดปลอบใจทั้งเพื่อนและตัวเองก่อนจะเดินลงไปเพราะมันเริ่มน่าขนลุกขึ้นไปทุกที"
        hide HimawariHalf
        hide ReiHalf

label after_menu3:

    n "ทั้งสองเดินลงมาชั้นล่างแล้วไปห้องเก็บของที่อยู่ใกล้ๆโรงยิมเพื่อไปหาอากาเนะที่แยกออกมาคนเดียว"
    play music "Maestro.mp3"
    n "(ฮิมาวาริและเรย์เดินไปที่ห้องเก็บของ)"

#scene 3 ห้องเก็บของ
    scene black
    with Dissolve(.5)
    n "เมื่อทั้งสองคนเปิดประตูห้องเก็บของออก ก็ได้เห็นบางสิ่งที่ไม่ถูกต้องตั้งตระหง่านอยู่กลางห้องเก็บของ
    "
    n "และสิ่งนั้นก็คือ ตุ๊กตา เก่าๆ โทรมๆ ตัวหนึ่ง ที่มีรูปร่างคล้ายเด็กผู้หญิงตัวเล็ก และเมื่อทั้งสองกำลังก้าวเท้าเข้าไปในห้อง
    ตุ๊กตาตัวนั้นก็เหมือนจะเริ่มมีออร่าบางอย่างออกมา"
    scene storage room at truecenter
    with Dissolve(.5)
    pause #1
    show ReiHalf
    r "ทำไมตุ๊กตาแปลกๆ นี่ถึงมาอยู่ที่นี่ได้ล่ะ?"
    hide ReiHalf
    n "เรย์ถามพร้อมกับรู้สึกสับสนและหวาดกลัวอยู่ลึกๆ"
    d "วันที่เท่าไหร่"
    n "มันถาม"
    show HimawariHalf
    h "วันที่เท่าไหร่อะไร?"
    hide HimawariHalf
    n "ฮิมาวาริเต็มไปด้วยคำถาม ตุ๊กตานั้นเงียบไม่พูดอะไรออกมาอีก"

if havedollanswer == "yes" :
        $ key = "yes"
        show ReiHalf
        r "วันที่ที่อยู่ด้านหลังรูปนั่นรึเปล่า"
        n "เรย์นึกขึ้นได้ว่าที่เธอเดินสำรวจนั้นก็เจอแค่วันที่ที่อยู่บนหลังรูปของมิไรเท่านั้น"
        r "13 กันยายน"
        play sound "Glass_Drop_and_Roll.mp3"
        n "คลิ๊ก"
        n "เสียงเล็กๆดังขึ้นมาจากตุ๊กตามันได้คายบางอย่างออกมา ซึ่งมันเป็นกุญแจที่เขียนว่า’ดาดฟ้า’เอาไว้"
        hide ReiHalf
        jump fire
if havedollanswer == "no" :
        $ key = "no"
        jump fire

label fire :
        stop music fadeout 1.0
        play sound "GirlScreaming.mp3"
        n "และหลังจากตอบคำถามกับตุ๊กตาได้ไม่นาน ก็มีเสียงกรีดร้องดังมาจากทางโรงยิม"
        play music "Paranoia.mp3"
        scene GymLine
        with Dissolve(.5)
        n"เมื่อทั้งสองได้ยินเช่นนั้น จึงวิ่งไปตามเสียงร้องอย่างกระวนกระวายและตื่นตระหนก และเมื่อไปถึงที่โรงยิม ทั้งสองคนกลับเจออากานเนะที่ติดกำลังติดอยู่ในโลงศพ"
        scene coffin1 at top
        with Dissolve(.5)
        pause #1
        show HimawariHalf
        h "อ- อากาเนะจัง!!"
        hide HimawariHalf
        n "ฮิมาวาริตะโกนเรียกอากาเนะด้วยความตกใจอย่างมากที่เห็นเพื่อนของเธอเป็นแบบนั้น"
        show ReiHalf
        r "ไฟ! มีไฟกำลังไหม้!"
        hide ReiHalf
        n "เรย์ตะโกนออกมาด้วยความตกใจ ไฟกำลังไหม้โลงศพอย่างช้าๆ"
        a "ช่วยฉันด้วย!!!! ฮิมาวาริ!เรย์!"
        n "อากาเนะตะโกนข้อความช่วยเหลือพร้อมทุบฝาโลง"
        show HimawariHalf at left
        show ReiHalf at right
        r "เราต้องรีบหาถังดับเพลิง !!"
        n "เรย์พูดด้วยความร้อนรน"
        h "แล้วจะหาที่ไหนล่ะ!?"
        n "ฮิมาวาริถามกลับด้วยความตื่นตระหนก"
        hide HimawariHalf
        hide ReiHalf
menu :
    "หาในโรงยิม" :
        scene GymLine
        with Dissolve(.5)
        show ReiHalf
        r "ในโรงยิมน่าจะมีอยู่นะลองไปหากัน"
        hide ReiHalf
        n "เรย์ควบคุมสติพาฮิมาวาริไปหากันที่โรงยิม"
        show coffin2 at top
        with Dissolve(.5)
        n "แต่พอหาแล้วก็ไม่เจอ ไฟได้เผาไหม้ทั้งโลงศพไปหมดแล้ว "
        show HimawariHalf
        h "กรี๊ด!!! อากาเนะ!!!"
        hide HimawariHalf
        n "ฮิมาวาริกรีดร้องออกมาเมื่อเห็นว่าเพื่อนของตัวเองนั้นได้โดนย่างสดต่อหน้าต่อตาพวกเธอ"
        stop music fadeout 1.0
        play music "The_Last_Time.mp3"
        n "BAD END"
        stop music fadeout 1.0
        jump end_credit

    "หาในห้องเก็บของ" :
        scene StorageroomLine
        with Dissolve(.5)
        show HimawariHalf at left
        show ReiHalf at right
        r "ในห้องโรงเก็บของ! ในนั้นน่าจะมีนะ"
        n " เรย์วิ่งนำหน้าไปที่โรงเก็บของและพวกเธอก็เจอ"
        h "เจอแล้ว!"
        hide HimawariHalf
        hide ReiHalf
        n "ฮิมาวาริเจอสิ่งที่ต้องการ เธอไม่รอช้ารีบนำมันไปดับไปให้เพื่อนที่กำลังโดนไฟเผา"

label after_menu4:
    if key == "no" :
        scene GymLine
        with Dissolve(.5)
        show ReiHalf
        r "เราจะไปไหนกันดีล่ะ ที่นี่มันอันตราย"
        n "เรย์ที่มีสติเยอะที่สุดในกลุ่มพูดเตือนเพื่อนๆ ทั้งหมดพยักหน้าแล้วออกไปจากที่นี่"
        hide ReiHalf
        n "เมื่อเดินออกมาจากโรงยิมทั้งสามก็ต้องชะงักเมื่อเจอร่างสีซีดของเด็กสาวที่ยืนก้มหน้าก้มตาดักทางพวกเธออยู่ เรย์จำเธอได้ดีเธอคือคนคนเดียวกับเมื่อตอนนั้น"

        scene school hallway2 at truecenter
        with Dissolve(.5)
        pause #1
        show AkaneHalf
        a "ธะ เธอที่ขังฉันไว้ในโลงนี่!?"
        hide AkaneHalf
        n "อากาเนะมีสีหน้าตกใจอย่างเห็นได้ชัด เพื่อนๆที่เหลือที่ได้ยินดังนั้นก็ตกใจ"
        scene school hallway3 at truecenter
        with Dissolve(.5)

        g "ใช่ ฉันเอง แปลกใจจังที่ยังไม่ตาย"
        n "ผีตนนั้นยิ้มแสดงความสงสัยออกมาด้วยคำพูด"
        g "หึหึ แต่ยังไงพวกแกก็ต้องตายอยู่ที่นี่!"

        scene black

        n "BAD END"
        jump end_credit
    if key == "yes" :
        scene GymLine_Red
        with Dissolve(.5)
        show ReiHalf
        r "เรารีบออกไปจากที่นี่กันเถอะ! ฉันได้กุญแจดาดฟ้ามาแล้ว"
        hide ReiHalf
        n "เรย์และฮิวามาริช่วยเพื่อนเธอออกมาและวิ่งกลับไปยังตัวอาคารเพื่อไปที่ดาดฟ้า"
        jump redsky

label redsky :
    play music "Paranoia.mp3"
    scene Building2 at top
    with Dissolve(.5)
    n "ทั้งสามหนีตายออกมาท้องฟ้ากลายเป็นสีแดงน่ากลัว ทั้งสามวิ่งขึ้นไปบนดาดฟ้าเมื่อได้กุญแจมาแล้ว
    เมื่อไขกุญแจได้แล้วเปิดประตูออกไปก็ร่างของเพื่อนที่หายไปและวงพิธีกรรมแปลกๆ"
    stop music fadeout 1.0
    play music "Descendants.mp3"
    scene bg rooftop_red
    pause #1
    show AkaneHalf
    scene Mirai_dead at top
    with Dissolve(.5)
    pause #1
    a "มิไร!!!"
    n "อากาเนะตะโกนเรียกชื่อเพื่อนของเธอที่หายตัวไป"
    hide AkaneHalf
    hide MiraiHalf
    scene bg rooftop_red

    show HimawariHalf
    h "เธอใช่ไหมที่จับเพื่อนของเรามา ได้โปรดปล่อยเพื่อนเราไปเถอะ"
    n "ฮิมาวาริขอร้อง"
    hide HimawariHalf
    show Ghost1:
        xalign 0.5
        yalign 0.1
    g "พวกแกอย่ามายุ่ง ยัยนี่จะต้องไปกับฉัน!!!"
    n "ผีตนนี้ตะคอกใส่ทั้้งสามคน"
    hide Ghost1
    show AkaneHalf
    a "ทำไมล่ะ ทำไมเธอต้องทำแบบนี้ด้วย มิไรไปทำอะไรให้เธอ"
    n "อากาเนะถาม"
    hide AkaneHalf
    show Ghost_Half:
        xalign 0.5
        yalign 0.1
    g "เพราะเธอคือตัวตายตัวแทนของฉันยังไงล่ะ"
    hide Ghost2
    n "ผีตนนั้นแสยะยิ้มออกมา"
    stop music fadeout 1.0
    show ReiHalf
    hide Ghost_Half
    r "คุณ… คือคนที่ตายไปเมื่อ 5 ปีก่อนใช่ไหมล่ะคะ..."
    hide ReiHalf
    n "เรย์พูดขึ้นท่ามกลางความกดดัน"
    show Ghost_Half at right
    show ReiHalf at left
    g "......."
    n "ผีตนนั้นชะงักไป ซึ่งเรย์พูดถูก"
    r "คุณตายเพราะว่าคุณโดนคนในห้องเรียนกลั่นแกล้งจนคุณทนไม่ไหวแล้วฆ่าตัวตายใช่ไหมล่ะคะ"
    n "เรย์ยังคงพูดต่อ ทั้งคนทั้งผีหันมามองเธอเป็นตาเดียว"
    g "แกรู้ได้ยังไง"
    n "ผีตนนั้นถามด้วยความโกรธ"
    r "ฉันไปอ่านเจอมาจากหนังสือพิมพ์ในห้องสมุดเมื่อหลายวันก่อน ทำไมคุณถึงต้องทำกับเธอด้วย มิไรเธอไม่รู้เรื่องอะไรปล่อยเธอไปเถอะ"
    hide Ghost_Half
    hide ReiHalf
    n "เรย์ขอร้องอีกแรง"

menu :
    "เล่าความจริง" :
        play music "PainfulMemories.mp3"
        show ReiHalf
        r "ความจริงแล้ว...ทุกคนในที่นี้ก็ไม่ต่างกันหรอกนะ ทุกคนที่อยู่ในที่แห่งนี้... ตอนนี้... ต่างก็เคยโดนกลั่นแกล้งมาเหมือนกันทั้งนั้น"
        hide ReiHalf
        n "เรย์เล่าความจริงของเธอและเพื่อนๆ ให้ผีตนนั้นฟัง"
        show HimawariHalf at right
        show AkaneHalf at left
        h ".......อ - อือ... ใช่แล้วล่ะ"
        n "ฮิมาวาริพูดพร้อมทั้งทำหน้าเศร้าโศก พลางกลั้นน้ำตาที่กำลังเริ่มพรั่งพรูออกมา"
        a "ทำไม… เธอถึงต้องมาพูดเรื่องแบบนี้เอาตอนนี้ด้วยล่ะ...."
        n "อากาเนะเบือนหน้าหนี ทำสีหน้าตกใจและวิตกกังวลกับสิ่งที่เรย์พูดออกมา"
        hide HimawariHalf
        hide AkaneHalf
        show ReiHalf at right
        show Ghost_Half at left
        r "พวกเราเข้าใจความรู้สึกของเธอนะ ที่ต้องโดดเดี่ยวมาตลอด... แต่การที่เธอทำแบบนี้ มันก็ไม่ต่างอะไรกับสิ่งที่ที่พวกนั้นเคยแกล้งเธอเลยนะ"
        n "เรย์พูด"
        scene Mirai_choked at truecenter
        with Dissolve(.5)
        g "........ก็ได้........"
        stop music fadeout 1.0
        hide ReiHalf
        hide Ghost_Half
        n "หลังจากที่ผีตนนั้นได้ฟังคำพูดของเรย์ และหยุดคิดอยู่ชั่วครู่หนึ่ง เธอก็ตระหนักได้ว่าสิ่งที่ทำอยู่ตอนนี้มันไม่ได้ต่างจากสิ่งที่เธอถูกกระทำมาเลย"
        n "เธอจึงตัดสินใจที่จะปล่อยมิไรไป เพราะเธอไม่อยากให้คนอื่นต้องมาเจอความเจ็บปวดแบบเดียวกับเธอ"
        jump true_end

    "พยายามขอร้อง" :
        show ReiHalf
        r "ฉันขอร้องล่ะ ช่วยปล่อยมิไรไปด้วยเถอะนะ แล้วพวกเราจะไม่มายุ่งกับเธออีก"
        hide ReiHalf
        n "เรย์พูดเสียงอ่อนน้ำตาเธอไหลลงมาเพื่อขอความเห็นใจ"
        scene Mirai_choked at truecenter
        with Dissolve(.5)
        g "......"
        scene Mirai_choked2 at truecenter
        with Dissolve(.5)
        n "ผีนิ่งเงียบไปก่อนที่มันจะแสยะยิ้ม"
        r "ย - อย่านะขอร้องล่ะ อย่าฆ่ามิไรเลยนะได้โปรดเถอะ ปล่อยเธอไปเถอะนะ"
        n "เรย์ขอร้องผีตนนั้นอย่างอ้อนวอน"
        g "หึ! ขอร้องยังไงยัยนี่ก็ต้องตายอยู่ดี! รวมถึงพวกแกด้วย!"
        hide Ghost_Half
        hide ReiHalf
        n "เมื่อพูดจบ ผีตนนั้นก็หักคอมิไรต่อหน้าเรย์และเพื่อนของเธอ"
        scene Mirai_choked3 at truecenter
        with Dissolve(.5)
        h "กรี๊ดดดดดด!!!  ไม่นะ!!!!"

        n "ฮิมาวาริกรีดร้องสุดขีด เพราะสิ่งที่เธอกำลังเห็นอยู่คือเพื่อนที่ถูกฆ่าตายต่อหน้าต่อตาของเธอ"

        a "ไม่… ไม่จริง นี่มันไม่ใช่เรื่องจริง!! ใช่แล้ว ที่เราเห็นอยู่ตอนนี้มันเป็นแค่ความฝันสินะ ฮะฮะ..."

        n "อากาเนะ ที่ได้เห็นเพื่อนตัวเองถูกฆ่าตายต่อหน้า ก็กำลังหลอกตัวเองว่าสิ่งที่เกิดขึ้นนั้นไม่ใช่เรื่องจริงด้วยสีหน้าที่ไม่ต่างอะไรกับคนที่เสียสติไปแล้ว"
        n "เสียงกรีดร้องแสนเจ็บปวดดังไปทั่วโรงเรียน พร้อมกับเสียงหัวเราะสะใจของผีตนนั้น"
        play music "The_Last_Time.mp3"
        n "BAD END"
        stop music fadeout 1.0
        jump end_credit


label true_end :
    scene black
    with Dissolve(.5)

    scene bg rooftop
    with Dissolve(.5)
    play music "PainfulMemories.mp3"
    n "หลังจากที่ผีตนนั้นไปสู่สุขติแล้ว ท้องฟ้าได้กลับมาเป็นสีดำยามราตรีเช่นเดิม และแสงจันทร์สีเลือดกลับมาเป็นสีฟ้าอีกครั้ง"
    show AkaneHalf at right
    show ReiHalf at left
    a "มันจบแล้วสินะ"
    n "อากาเนะถามเพื่อนๆของเธอ"
    hide AkaneHalf
    hide ReiHalf
    r "ใช่ มันจบแล้วล่ะ"
    n "เรย์ยิ้ม และหลังจากนั้นทั้งสามช่วยกันพยุงร่างของมิไรลงไปด้านล่างและพาเธอกลับบ้านอีกครั้ง"

    scene black
    with Dissolve(.5)
    pause #1
    scene white_flower at top
    with Dissolve(.5)
    n "-เช้าวันต่อมา-"
    n "ทั้งสี่คนเดินไปยังห้องเก็บของเพื่อไปหาโต๊ะเรียนที่เธอคนนั้นเคยใช้เพื่อฆ่าตัวเอง ก่อนจะนำดอกไม้ไปวางเอาไว้เพื่อระลึกถึงเธอ"
    stop music fadeout 1.0
    n " TRUE END"
    jump end_credit


label end_credit :
    scene black
    with Dissolve(.5)
    centered " Haunted School - Game Project\n
    พงศ์ภูชิษ เศวตเศรนี 2013210238\n
พรชนก พิริยะรังสรรค์ 2013210477\n
กันทรากร ลิขิตสุวณิชย์ 2013210352\n
แพรวา อเนกนิธิพันธ์ 2013211293\n
นดล ปัทมอนุพงศ์ 2013210824\n
ชนวัฒน์ รัตนวิบูลย์สม 2013212184\n
ภัทรพงศ์ ศักดิ์เวคิน 2013210592\n
ชนาธิป บันเทิงสุข 2013211442"
    return


    # This ends the game.

return
