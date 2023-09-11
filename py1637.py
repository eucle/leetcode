def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    widest_area: int = 0
    points.sort(key=lambda x: x[0])
    for i in range(1, len(points)):
        widest_area = max(points[i][0] - points[i - 1][0], widest_area)
    return widest_area
