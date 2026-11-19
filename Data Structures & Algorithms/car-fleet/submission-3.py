class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 9miles 3 miles/hr 1hr=3miles -> 3 hrs
        # 6miles 2 miles/hr 1hr=2miles -> 3 hrs

        # 6miles 2miles/hr 1hr=2miles -> 3 hrs
        # 9miles 2miles/hr 1hr=2miles -> 2.5 hr
        # 10miles 1miles/hr 1hr=1mile -> 10 hrs
        # 3miles 1mikes/hr 1hr=1miles -> 3hrs

        # dict={times:[]}

        # if same time go to that array and atlast return how many times exists return the value

        # we need to sort the pos,speed because if a car1 is at position near to the target and going slowly and car2 is behind the car1 is going much speeder than car2 then car2 will catch car1 at some position so both will come under the same car fleet.
        # so if car1 which ahead of car2 if car2 time taken is less than or equal to time taken by car1 then both will be same fleet else not.

        d=defaultdict(list)
        max_time=0
        for pos, sp in sorted(zip(position, speed), reverse=True):
            time_taken = (target - pos) / sp
            if time_taken > max_time:
                max_time = time_taken
            d[max_time].append(pos)
        
        return len(d.keys())

            



