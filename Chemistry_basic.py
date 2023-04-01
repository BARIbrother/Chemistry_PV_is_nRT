import random
import math
import vpython as vp

vp.scene.userzoom = False
vp.scene.userspin = False

particle_count = 30

vp.box_left = vp.box(pos=vp.vec(-6, 0, 0), size=vp.vec(0.3, 12, 0.3), color=vp.vec(1, 1, 1))
vp.box_right = vp.box(pos=vp.vec(6, 0, 0), size=vp.vec(0.3, 12, 0.3), color=vp.vec(1, 1, 1))
vp.box_bottom = vp.box(pos=vp.vec(0, -6, 0), size=vp.vec(12, 0.3, 0.3), color=vp.vec(1, 1, 1))

vp.box_cylinder = vp.box(pos=vp.vec(0, 6, 0), size=vp.vec(12, 0.3, 0.3), color=vp.vec(1, 0, 0))

particles = []
for a in range(particle_count):
    particles.append(vp.sphere(
        pos=vp.vec(random.uniform(vp.box_left.pos.x, vp.box_right.pos.x), random.uniform(vp.box_bottom.pos.y, vp.box_cylinder.pos.y),
                0), size=vp.vec(0.3, 0.3, 0.3), color=vp.vec(0.3, 0.3, 1)))

speed_x = []
speed_y = []
for a in range(particle_count):
    t = random.uniform(0, 360)
    speed_x.append(math.cos(math.radians(t)) * 0.1)
    speed_y.append(math.sin(math.radians(t)) * 0.1)

collision_count = 0
cc_ago = 0
time_count = 0.01
tc_ago = 0.01

ct = vp.label(pos=vp.vec(-8, 5, 0), size=vp.vec(10, 5, 5), text='collision: ' + str(collision_count))
ct_dt = vp.label(pos=vp.vec(-8, 0, 0), size=vp.vec(10, 5, 5), text='collision per time: \n ' + str(collision_count / time_count))
vt = vp.label(pos=vp.vec(-8, 2.5, 0), size=vp.vec(10, 5, 5),
           text='volume :' + str(round((vp.box_cylinder.pos.y - vp.box_bottom.pos.y) * (vp.box_right.pos.x - vp.box_left.pos.x))))
pv = vp.label(pos=vp.vec(-8, -2.5, 0), size=vp.vec(10, 5, 5), text='P * V =  ' + str(
    round((vp.box_cylinder.pos.y - vp.box_bottom.pos.y) * (vp.box_right.pos.x - vp.box_left.pos.x)) * (
                int(collision_count / time_count * 100) / 100)))

while True:
    vp.rate(100)
    time_count += 0.01

    for a in range(len(particles)):
        particles[a].pos.x += speed_x[a]
        particles[a].pos.y += speed_y[a]
        if speed_x[a] > 0 and particles[a].pos.x >= 6:
            speed_x[a] *= -1
            # collision_count += 1
            ct.text = 'collision: ' + str(collision_count)
        elif speed_x[a] < 0 and particles[a].pos.x <= -6:
            speed_x[a] *= -1
            # collision_count += 1
            ct.text = 'collision: ' + str(collision_count)
        if speed_y[a] > 0 and particles[a].pos.y >= vp.box_cylinder.pos.y:
            speed_y[a] *= -1
            collision_count += 1
            ct.text = 'collision: ' + str(collision_count)
        elif speed_y[a] < 0 and particles[a].pos.y <= -6:
            speed_y[a] *= -1
            # collision_count += 1
            ct.text = 'collision: ' + str(collision_count)

    k = vp.keysdown()
    if 'up' in k:
        vp.box_cylinder.pos.y += 0.1
        collision_count = 0
        time_count = 0.01
    if 'down' in k:
        vp.box_cylinder.pos.y -= 0.1
        collision_count = 0
        time_count = 0.01

    vt.text = 'velocity:' + str(round((vp.box_cylinder.pos.y - vp.box_bottom.pos.y) * (vp.box_right.pos.x - vp.box_left.pos.x)))
    ct_dt.text = 'collision per time: \n ' + str(int(collision_count / time_count * 100) / 100)
    pv.text = 'P * V = ' + str(int((vp.box_cylinder.pos.y - vp.box_bottom.pos.y) * (vp.box_right.pos.x - vp.box_left.pos.x) * int(
        collision_count / time_count * 100) / 100))

