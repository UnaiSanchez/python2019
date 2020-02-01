def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()

def person_does_something(name,something):
    def func(text):
        return name + 'does' + something(text)

nico_shout = person_does_something("nico",shout)
nico_wispers =person_does_something("nico",whisper)
print(nico_shout("hola"))

