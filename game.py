print("게임을 시작합니다")
print("테트리스 시작")
print("1. 오른쪽 2. 왼쪽 3. 블럭 바꾸기")
number=input("숫자를 입력하세요 : ")
number = int(number)
if number == 1:
    print("오른쪽")
elif number == 2:
    print("왼쪽")
elif number == 3:
    print("블럭 바꾸기")
else :
    print("숫자를 입력하세요")