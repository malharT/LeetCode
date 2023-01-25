from collections import deque 
class Solution:
    def merge(self, a, b, key=None):
        if len(a) == 0 or len(b) == 0:
            return a + b
        result = []
        i = 0
        j = 0
        while len(a) > i and len(b) > j:
            if key(a[i]) < key(b[j]):
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        result += a[i:]
        result += b[j:]
        return result

    def mergeSort(self, a):
        l = len(a)
        if len(a) < 2:
            return a
        s = l//2
        a_1 = a[:s]
        a_2 = a[s:]
        a_1 = self.mergeSort(a_1)
        a_2 = self.mergeSort(a_2)
        a = self.merge(a_1, a_2, key=lambda i:self.position[i])
        return a

    def isFleet(self, fleet_pos, fleet_speed, car_pos, car_speed, target):
        if car_speed>fleet_speed:
            catchup_time = (fleet_pos-car_pos)/float(car_speed-fleet_speed)
        else:
            if fleet_pos == car_pos and car_speed == fleet_speed:
                return True
            else:
                return False
        fleet_time = (target-fleet_pos)/float(fleet_speed)
        if catchup_time <= fleet_time:
            return True
        else:
            return False

    def carFleet(self, target: int, position: List[int], speed: List[int], key=None) -> int:
        self.position = position
        sorted_indices = self.mergeSort(list(range(len(position))))
        # sorted_indices = sorted(list(range(len(position))), key=lambda i: position[i])
        new_position = []
        new_speed = []
        for i in sorted_indices:
            new_position.append(position[i])
            new_speed.append(speed[i])
        fleets = 1
        fleet = new_position.pop(), new_speed.pop()
        while len(new_position) > 0:
            car_pos = new_position.pop()
            car_speed = new_speed.pop()
            if self.isFleet(fleet[0], fleet[1], car_pos, car_speed, target):
                continue
            else:
                fleet = car_pos, car_speed
                fleets += 1
        return fleets