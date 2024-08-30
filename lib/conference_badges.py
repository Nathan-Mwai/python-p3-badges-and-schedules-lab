def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_message = []
    for name in names:
        message = f"Hello, my name is {name}."
        badge_message.append(message)
    return badge_message

def assign_rooms(names):
    assigned =[f"Hello, {name}! You'll be assigned to room {index + 1}!" for index, name in enumerate(names)]
    return assigned


def printer(names):
    [print(badge) for badge in batch_badge_creator(names)]
    [print(room) for room in assign_rooms(names)]
    # return None
printer("John")