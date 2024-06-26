class grandfather:
      def fun1(self):
            print('inside grandfather class')
class father(grandfather):
      def fun2(self):
            print('Inside Father class')
class son(father):
      def fun3(self):
            print("inside son class")
s=son()
s.fun1()
s.fun2()
s.fun3()