import random
import vpython as  vp
import math

vp.scene.userzoom = False
vp.scene.userspin = False

particle_count = 30

box_left = vp.box(pos=vp.vec(-6, 0, 0), size=vp.vec(0.3, 12, 0.3), color=vp.vec(1, 1, 1))
box_right = vp.box(pos=vp.vec(6, 0, 0), size=vp.vec(0.3, 12, 0.3), color=vp.vec(1, 1, 1))
box_bottom = vp.box(pos=vp.vec(0, -6, 0), size=vp.vec(12, 0.3, 0.3), color=vp.vec(1, 1, 1))

box_cylinder = vp.box(pos=vp.vec(0, 6, 0), size=vp.vec(12, 0.3, 0.3), color=vp.vec(1, 0, 0))

particles = []
for a in range(20):
    particles.append(vp.sphere(
        pos=vp.vec(random.uniform(box_left.pos.x, box_right.pos.x), random.uniform(box_bottom.pos.y, box_cylinder.pos.y),
                0), size=vp.vec(0.3, 0.3, 0.3), color=vp.vec(0.3, 0.3, 1)))

for b in range(10):
    particles.append(vp.sphere(
        pos=vp.vec(random.uniform(box_left.pos.x, box_right.pos.x), random.uniform(box_bottom.pos.y, box_cylinder.pos.y),
                0), size=vp.vec(0.3, 0.3, 0.3), color=vp.vec(1, 0.3, 0.3)))

speed_x = []
speed_y = []
for a in range(particle_count):
    t = random.uniform(0, 360)
    speed_x.append(math.cos(math.radians(t)) * 0.1)
    speed_y.append(math.sin(math.radians(t)) * 0.1)

collision_count_r = 0
collision_count_b = 0
time_count = 0.01
tc_ago = 0.01

rct = vp.label(pos=vp.vec(-8, 5, 0), size=vp.vec(10, 5, 5), text='red collision: ' + str(collision_count_r))
bct = vp.label(pos=vp.vec(8, 5, 0), size=vp.vec(10, 5, 5), text='blue collision: ' + str(collision_count_b))
rct_dt = vp.label(pos=vp.vec(-8, 0, 0), size=vp.vec(10, 5, 5),
               text='red collision per time: \n ' + str(round(collision_count_r / time_count, 2)))
bct_dt = vp.label(pos=vp.vec(8, 0, 0), size=vp.vec(10, 5, 5),
               text='blue collision per time: \n ' + str(round(collision_count_b / time_count, 2)))

vt = vp.label(pos=vp.vec(-8, 2.5, 0), size=vp.vec(10, 5, 5),
           text='volume :' + str(round((box_cylinder.pos.y - box_bottom.pos.y) * (box_right.pos.x - box_left.pos.x))))
rpv = vp.label(pos=vp.vec(-8, -2.5, 0), size=vp.vec(10, 5, 5), text='red P * V =  ' + str(
    round((box_cylinder.pos.y - box_bottom.pos.y) * (box_right.pos.x - box_left.pos.x)) * int(
        collision_count_r / time_count * 100) / 100))
bpv = vp.label(pos=vp.vec(8, -2.5, 0), size=vp.vec(10, 5, 5), text='blue P * V =  ' + str(
    round((box_cylinder.pos.y - box_bottom.pos.y) * (box_right.pos.x - box_left.pos.x)) * int(
        collision_count_b / time_count * 100) / 100))

while True:
    vp.rate(100)
    time_count += 0.01

    for a in range(len(particles)):
        particles[a].pos.x += speed_x[a]
        particles[a].pos.y += speed_y[a]
        if speed_x[a] > 0 and particles[a].pos.x >= 6:
            speed_x[a] *= -1
        elif speed_x[a] < 0 and particles[a].pos.x <= -6:
            speed_x[a] *= -1
        if speed_y[a] > 0 and particles[a].pos.y >= box_cylinder.pos.y:
            speed_y[a] *= -1
            if particles[a].color == vp.vec(1, 0.3, 0.3):
                collision_count_r += 1
                rct.text = 'red collision: ' + str(collision_count_r)
            elif particles[a].color == vp.vec(0.3, 0.3, 1):
                collision_count_b += 1
                bct.text = 'blue collision: ' + str(collision_count_b)
        elif speed_y[a] < 0 and particles[a].pos.y <= -6:
            speed_y[a] *= -1

    k = vp.keysdown()
    if 'up' in k:
        box_cylinder.pos.y += 0.1
        collision_count = 0
        time_count = 0.01
    if 'down' in k:
        box_cylinder.pos.y -= 0.1
        collision_count = 0
        time_count = 0.01

    vt.text = 'velocity:' + str(round((box_cylinder.pos.y - box_bottom.pos.y) * (box_right.pos.x - box_left.pos.x)))
    rct_dt.text = 'red collision per time: \n ' + str(int(collision_count_r / time_count * 100) / 100)
    bct_dt.text = 'blue collision per time: \n ' + str(int(collision_count_b / time_count * 100) / 100)
    rpv.text = 'red P * V = ' + str(
        int((box_cylinder.pos.y - box_bottom.pos.y) * (box_right.pos.x - box_left.pos.x) * int(
            collision_count_r / time_count * 100) / 100))
    bpv.text = 'blue P * V = ' + str(
        int((box_cylinder.pos.y - box_bottom.pos.y) * (box_right.pos.x - box_left.pos.x) * int(
            collision_count_b / time_count * 100) / 100))
