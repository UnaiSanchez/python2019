from random import seed, choice
def asdf(input):
    seed(input)
    choices= u"1234567890ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz<>,.-´ç`+'¡º;:_¨Ç^¿*?¿!·$%&/()\|@#~€¬[]{}áéíóúÁÉÍÓÚ😀😇😜😒😭🤬👾😺💙💥🦶👅👦🧔🧑‍🦰👩‍🦱👩‍🦲🧑‍🦲🙍‍♀️🙎‍♂️🧏‍♂️🤦🧑‍🎓👨‍🏫🧑‍🌾👨‍🔧🧑‍✈️👨‍🚀🧑‍🚒🕵️‍♂️💂🤴🧚‍♂️🧛🧞‍♂️🧞‍♀️🧍‍♀️🧎‍♂️👨‍🦯🧑‍🦼👩‍🦽👯‍♀️🧗🏌️‍♂️🚵‍♂️🧘👨‍❤️‍💋‍👨👨‍👩‍👧🧄🧇🧀🍔🍛🍜🦐🍫🥄🌍🌎🗾🧭🏔🏗🏘🏬🏯🗽🌁🚕🛵🛹🚁🕧🕝🌑🌠⛈🌬🎈🎑🏀🥅♟🧥🩲⛑💍📯🎺🖨📼🗞💼🗂📅✂⛏🔗💉🩹🚽🧽🗿⚠🚯🔞🔃🔝♋♌♎⛎🔂⏩⏪⚕⚜✔➕➖➗〽✴6️⃣9️⃣🔠🅱🈂"
    hashed = ""
    for _in range(64):
        hashed += choice(choices)
    return(hashed)
asdf("perritos")