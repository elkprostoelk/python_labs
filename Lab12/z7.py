BOTTOM, TOP, LEFT, RIGHT = (4, -1, -1, 17)
START_X, START_Y = (0, 0)
matrix = []
mazeMap = open('map.txt')
row_ind = 0
for row in mazeMap:
  column_index = 0
  matrix.append([])
  for column in row:
    if (column == 'S'):
        start_x = row_ind;
        start_y = column_index
        matrix[row_ind].append({ 'Visited': True, 'canVisit': False, 'destin': False })
    elif (column == 'F'):
        matrix[row_ind].append({ 'canVisit': True, 'Visited': False, 'destin': True })
    elif (column == ' '):
      matrix[row_ind].append({ 'canVisit': True, 'Visited': False, 'destin': False })
    else:
      matrix[row_ind].append({ 'canVisit': False, 'Visited': False, 'destin': False })
    column_index += 1
  row_ind += 1

def move(coordin_x = START_X, coordin_y = START_Y, path_len = 1):
  next_x = coordin_x + 1
  next_y = coordin_y + 1

  if next_x < RIGHT and next_x > LEFT and matrix[coordin_y][next_x]['canVisit']:
    if matrix[coordin_y][next_x]['destin']:
      return path_len
    else:
      shortest_path = move(next_x, coordin_y, path_len + 1)
      if (shortest_path != False):
        return shortest_path
  if next_y > TOP and next_y < BOTTOM and matrix[next_y][next_x]['canVisit']:
    if matrix[next_y][coordin_x]['destin']:
      return path_len
    else:
      shortest_path = move(coordin_x, next_y, path_len + 1)
      if (shortest_path != False):
        return shortest_path
  else:
    return False

print(move())