from random import randint

sten_saks_papir = ["sten", "saks", "papir"]

while True:
    spil = input("Sten, Saks eller papir?")
    sten_saks_papir = ["sten", "saks", "papir"]
    randum = sten_saks_papir[randint(0, 2)]
    print(randum)

    if spil == "sten":
        if randum == "sten":
            print('Det blev lige')
        elif randum == "papir":
            print('Jeg Vandt!!')
        elif randum == "saks":
            print("Øv, Du Vandt!!")
    elif spil == "papir":
        if randum == "papir":
            print('Det blev lige')
        elif randum == "saks":
            print('Jeg Vandt!!')
        elif randum == "sten":
            print("Øv, Du Vandt!!")
    elif spil == "saks":
        if randum == "saks":
            print('Det blev lige')
        elif randum == "sten":
            print('Jeg Vandt!!')
        elif randum == "papir":
            print("Øv, Du Vandt!!")
    else:
        print("Skriv sten, skaks eller papir:")
