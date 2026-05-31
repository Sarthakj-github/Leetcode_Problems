class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        while asteroids:
            a=asteroids.pop()
            if mass>=a:
                mass+=a
            else:
                return False
        return True
