def son():

    print("Son function started")

    print("Son function ended")


def father():

    print("Father function started")

    son()

    print("Father function ended")


father()