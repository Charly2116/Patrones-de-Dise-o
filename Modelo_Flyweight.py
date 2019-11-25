#Flyweight
'''
Juan Carlos Rangel
25/11/2019
allows the abstraction of reusable parts that
can be shared with other objects,
'''

class Player:
   pass

class level(Player):
   def __init__(self):
      pass
   
   def EXP(self, experience):
      return "Nombre[%s]" % (experience)
#---------------------------------------------------------- 
class Play(Player):
   exp = {} 
   
   def __new__(cls, name, exp_points):
      try:
         id = cls.exp[exp_points]
      except KeyError:
         id = Player.__new__(cls)
         cls.exp[exp_points] = id
      return id
   
   def set_statistics_info(self, codetic_info):
      cg = level()
      self.codetic_info = cg.EXP(codetic_info)
   
   def get_statistics_info(self):
      return (self.codetic_info)
   
#------------------------------------------------------------
def test():
   data = (('a', 1, 'Zoldikcz'), ('a', 2, 'Gremory'), ('b', 1, 'SlayerOne'))
   exp_nivels = []
   for i in data:
      obj = Play(i[0], i[1])
      obj.set_statistics_info(i[2])
      exp_nivels.append(obj)
   
   for i in exp_nivels:
      print ("Statics Level = " + str(id(i)))
      print (i.get_statistics_info())
   print ("Felicidades Eres una leyenda en este Juego")

if __name__ == '__main__':
   test()

