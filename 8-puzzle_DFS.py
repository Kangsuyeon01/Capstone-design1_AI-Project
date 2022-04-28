# 상태를 나타내는 클래스
class State:
  def __init__(self, board, goal, moves=0):
    self.board = board
    self.moves = moves
    self.goal = goal

  # i1과 i2를 교환하여서 새로운 상태를 반환한다.
  def get_new_board(self, i1, i2, moves):
    new_board = self.board[:]
    new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
    return State(new_board, self.goal, moves)

  # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다.
  def expand(self, moves):
    result = []
    i = self.board.index(0)		# 숫자 0(빈칸)의 위치를 찾는다.
    if not i in [0, 1, 2] :		# UP 연산자
      result.append(self.get_new_board(i, i-3, moves))
    if not i in [0, 3, 6] :		# LEFT 연산자
      result.append(self.get_new_board(i, i-1, moves))
    if not i in [2, 5, 8]:		# DOWN 연산자
      result.append(self.get_new_board(i, i+1, moves))
    if not i in [6, 7, 8]:		# RIGHT 연산자
      result.append(self.get_new_board(i, i+3, moves))
    return result

  # 객체를 출력할 때 사용한다.
  def __str__(self):
    return str(self.board[:3]) +"\n"+\
    str(self.board[3:6]) +"\n"+\
    str(self.board[6:]) +"\n"+\
    "------------------"

  def __eq__(self, other):
    return self.board == other.board

# 초기 상태
puzzle = [2, 8, 3,
          1, 6, 4,
          7, 0, 5]

# 목표 상태
goal = [1, 2, 3,
        8, 0, 4,
        7, 6, 5]

# open 리스트
open_stack = [ ]
open_stack.append(State(puzzle, goal))

closed_stack = [ ]
moves = 0

cnt = 0
while len(open_stack) != 0:

    current = open_stack[len(open_stack) - 1]
    cnt += 1
    print("탐색 횟수:",cnt)
    print(current)

    if current.board == goal:
        print('탐색 성공')
        break
    moves = current.moves + 1
    tmp = True
    for state in current.expand(moves): #current에서 move 나올 수 있는 상태공간에 관한 for문
        tmp = True
        if (state not in open_stack) and (state not in closed_stack) : #만약 open_stack과 colsed_stack 안에 없으면
            open_stack.append(state) #open_stack 안에 추가해준다.
            tmp = False
            break

    if tmp == True: #만약 for 문의 if문을 통과하지 못한 상태로 남으면 tmp가 ture 로있을 것이다.
        open_stack.pop() #open_stack을 pop한다. (back tracking)

    closed_stack.append(current) #현재 노드를 방문 처리(closed_stack 에 추가)


else:
    print('탐색 실패')