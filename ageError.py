# create your own exceptionn class 'ageError' that is raised when age is less than
# 18 and check whether the person can vote or not 
class ageError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
age=int(input('enter your age'))
try:
    if age<18:
        raise ageError('not elligble for vote')
    else:
        print("Congratulations! you can vote")
except ageError as ae:
    print(ae)