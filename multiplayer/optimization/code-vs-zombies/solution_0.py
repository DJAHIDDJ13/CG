import sys
import math
# Save humans, destroy zombies!

cur_target=-1
change_target=True
savior_id = -1
change_savior = True
# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    humans = {}
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans[str(human_id)] = {'x':human_x, 'y':human_y}

    zombie_count = int(input())
    zombs={}
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombs[str(zombie_id)] = {'x':zombie_x,'y':zombie_y,'nx':zombie_xnext,'ny':zombie_ynext}
    if savior_id == -1:
        cur_score = -1
        cur_id = ''
        for human in humans:
            i=human
            human = humans[human]
            score = -1
            for zombie in zombs:
                zombie = zombs[zombie]
                distance = math.sqrt((human['x'] - zombie['x'])**2 + (human['y'] - zombie['y'])**2)
                if score == -1:
                    score = distance
                else:
                    score = min(score, distance)
            hum_dist = math.sqrt((x-human['x'])**2 + (y - human['y'])**2)
            print(hum_dist,score,file=sys.stderr)
            if (cur_score == -1 or score > cur_score) and hum_dist/1000.0 <= score/400.0:
                cur_score = score
                cur_id = i
        savior_id = cur_id
    if savior_id == '':
        savior_id = list(humans.keys())[0]

    print(x,y,file=sys.stderr)
    print(zombs,file=sys.stderr)
    print(humans,file=sys.stderr)
    print(humans[savior_id]['x'], humans[savior_id]['y'])

        #if change_target:
        #    cur_target = str(zombie_id)
        #zombs[str(zombie_id)] = {'x':zombie_x,'y':zombie_y,'nx':zombie_xnext,'ny':zombie_ynext}
    #if cur_target not in zombs:
    #    change_target = True
    #    cur_target = zombs.keys()[0]
    #print(zombs[cur_target]['nx'], zombs[cur_target]['ny'])


