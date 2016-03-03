import pyglet

hook = 'Sound'


def exiter(dt):
    pyglet.app.exit()


def run_command(command):
    command[0] = command[0].replace(' ', '')
    if command == ['alert']:
        sound = pyglet.resource.media('media/alert.mp3')
        sound.play()

        pyglet.clock.schedule_once(exiter, sound.duration)

        pyglet.app.run()
