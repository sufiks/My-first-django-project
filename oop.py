class Person():
    def __init__(self,sex,spouse):
        self.sex = sex
        self.spouse = spouse

    def bride(self,s_spouse):
        if (self.sex == 'male' or self.sex == 'female') and (s_spouse.sex == 'female' or s_spouse.sex == 'male') and self.spouse == 'no' and s_spouse.spouse == 'no':
            self.spouse='yes'
            s_spouse.spouse = 'yes'
            print('Свадьбе быть!')


        else:
            print(f'пидорам и лезбухам тут не место!')



    def divorce(self,b_spouse):
        if b_spouse.spouse == 'no' or self.spouse == 'no':
            print(f'Вы не можете быть разведены')
        else:
            print('Счастливой жизни!')

Misha=Person('male','no')
Masha=Person('female','no')
Grisha=Person('male','no')
Misha.bride(Masha)
Grisha.bride(Masha)