class Solution:
    def trap(self, height) -> int:
        last_pillars = [(0,0,0)]
        water = 0
        pos = 0
        for h in height:
            if h == 0:
                pos += 1
                continue
            i = 0
            low = 0
            high = len(last_pillars)
            i = (high - low)//2
            while i > -1:
                if h == last_pillars[i][1]:
                    break
                if h > last_pillars[i][2] and h < last_pillars[i][1]:
                    break
                if h > last_pillars[i][1]:
                    high = i
                if h <= last_pillars[i][2]:
                    low = i
                i = low + (high - low)//2
                if i == 0:
                    break
            new_pillars = last_pillars[:i]
            while i < len(last_pillars):
                pillar_pos, h_max, h_min = last_pillars[i]
                if h >= h_max:
                    for i in range(i, len(last_pillars)):
                        pillar_pos, h_max, h_min = last_pillars[i]
                        water += (pos - pillar_pos - 1) * (h_max - h_min)
                    new_pillars.append((pos, h, 0))
                    break
                elif h < h_max and h > h_min:
                    water += (pos - pillar_pos - 1) * (h - h_min)
                    old_pillar_pos = pillar_pos
                    old_h_max = h_max
                    for i in range(i+1, len(last_pillars)):
                        pillar_pos, h_max, h_min = last_pillars[i]
                        water += (pos - pillar_pos - 1) * (h_max - h_min)
                    new_pillars.append((old_pillar_pos, old_h_max, h))
                    new_pillars.append((pos, h, 0))
                    break
                elif h < h_min:
                    if i == len(last_pillars) - 1:
                        water += (pos - pillar_pos - 1) * (h)
                        new_pillars.append((old_pillar_pos, h_min, h))
                        new_pillars.append((pos, h, 0))                
                new_pillars.append((pillar_pos, h_max, h_min))
                i += 1
            last_pillars = new_pillars
                
            pos += 1
        return water
