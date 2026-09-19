class Solution:

    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # Find the closest point on the rectangle to the circle center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance from center to the closest point
        distX = xCenter - closestX
        distY = yCenter - closestY

        return distX**2 + distY**2 <= radius**2