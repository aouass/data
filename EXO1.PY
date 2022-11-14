import math
f=lambda x:x/(x**2+1)
g=lambda x:math.atan(x)

h=lambda x:(f(x)-g(x))**2
L=lambda N:[n for n in range(-N,N +1)]

R= lambda N : sum([h(x) for x in L(N)])
#print(R(6))




class T:
    def __f(self,x):
        return x/(x**2+1)
    def __g(self,x):
        return math.atan(x)
    def __h(self,x):
        return (self.__f(x)-self.__g(x))**2
    def __L(self,N):
        return ([n for n in range(-N,N+1)])
    def _getvaleur(self,N):
        return(sum([self.__h(x) for x in self.__L(N)]))

r=T()
print(r._getvaleur(6))