class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        for p, s in pairs:
            time = (target-p)/s
            if not stack or time  > stack[-1]:
                stack.append(time)

        return len(stack)