import random
import constant

def generateStructure(song=None):
    structure = []
    if song != None:
        random.seed(song.hash)
    #there's a large percentage chance that a song starts with an intro.
    if random.randint(1, 6) == 5:
        #we don't start with intro, pick something else
        structure.append(random.choice(constant.pickableparts))
    else:
        structure.append("intro")

    #enter a loop where we have an increasing chance of exiting with each iteration
    odds = [False]*60
    parts = list(constant.pickableparts*4) #copy parts so we can adjust them as we see fit
    #also multiply it by 4 to allow us to dynamically change the odds according to previous random choices, we don't want 11 choruses in a song after-all
    parts.remove("bridge")
    parts.remove("bridge")
    parts.remove("chorus")
    parts.remove("prechorus")
    parts.append("verse")

    while True:
        if (random.choice(odds) and len(structure)>=7) or len(parts) == 0:
            print("Break!")
            print(odds)
            break

        #pick the next element
        nxt = random.choice(parts)
        if nxt in ["chorus", "prechorus"]:
            if random.randint(0, 10) == 5: #low chance that we have a lone chorus/prechorus
                structure.append(nxt)
            else:
                structure += ["prechorus", "chorus"]
            parts.remove("chorus")
            parts.remove("prechorus")
        if nxt in ["verse", "bridge"]:
            structure.append(nxt)
            parts.remove(nxt)
        if nxt == structure[-2]: #if we repeated it, there's a 50% chance that we just skip it
            structure.pop(-1)

        odds += [True]*3

    if random.randint(1, 8) != 5:
        structure.append("outro")
    return structure


print(generateStructure())