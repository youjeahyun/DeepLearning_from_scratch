## 파이썬 인터프리터는 '대화 모드'식 프로그래밍임
## 내가 가끔 까먹는 거만 문법 정리

print(3 ** 2) ## **는 거듭 제곱을 의미 (3 ** 2는 3의 2제곱)

# 리스트 및 슬라이스 기법
a = [1, 2, 3, 4, 5]
print(a[0:2]) # 0번째 원소부터 순차적으로 2개 원소 얻기 3까지 출력되는것이아니라 1,2 만
print(a[1:]) # 1번째 원소부터 모두 얻기
print(a[:3]) # 처음부터 3개 원소 얻기
print(a[:-1]) # 처음부터 마지막 원소의 1개 앞까지 얻기
print(a[:-2]) # 처음부터 마지막 원소의 2개 앞까지 얻기

#파이썬에서 리스트는 터언어로말하면 배열 딕셔너리는 객체 혹은 맵
me = { # 딕셔너리 저장
    'first': 'John',
}
print (me['first']) # 딕셔너리 조회

#클래스 정의
class testClass:
    def __init__(self, name):
        self.name = name #받은 인자를 초기화

    def hello(self, age):
        print('hello my name is ' + self.name + " my age is " + str(age)) # init 초기화에서 name을 갖고와서 출력 하고 age는 메서드호출시 받았던 값을 출력

m = testClass('John') # name 인자로 John을 전달하면서 인스턴스 생성
m.hello(20) #인스턴스에서 hello 메서드를 호출함 호출할때 hello 메서드의 인자로 20을 같이 보낸다.
# 클래스 생성시 self는 명시적으로 적어줌, 클래스안에 함수들은 메서드라고 지칭함.

