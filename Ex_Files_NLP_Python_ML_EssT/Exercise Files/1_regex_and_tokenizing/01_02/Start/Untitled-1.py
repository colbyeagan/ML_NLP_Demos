
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
    trackList = list()
    while left < right and top < bottom:

        # goes across top
        for i in range(left, right):
            print("ACROSS TOP")
            print(matrix[top][i])
            trackList.append(matrix[top][i])
        top += 1

        # goes across right
        for i in range(top, bottom):
            print("ACROSS RIGHT")
            print(matrix[i][right-1])
            trackList.append(matrix[i][right-1])
        right -= 1
        
        if not (left < right and top < bottom): 
           break

        # goes across bottom
        for i in range(right-1, left-1, -1):
            print("ACROSS BOTTOM")
            print(matrix[bottom-1][i])
            trackList.append(matrix[bottom-1][i])
        bottom -= 1

        # goes across left
        for i in range(bottom, top-1, -1):
            print("ACROSS LEFT")
            print(matrix[i][left])
            trackList.append(matrix[i][left])
        left += 1
    return(trackList)
        
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(f"EXPECTED: {[1,2,3,6,9,8,7,4,5]}")