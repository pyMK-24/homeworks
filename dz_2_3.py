class Computer: 
    def __init__(self,cpu,memory): 
        self.__cpu = cpu 
        self.__memory = memory 
         
    def get_cpu(self): 
        return self.__cpu 
     
    def set_cpu(self,value): 
        self.__cpu = value 
     
    def get_memory(self): 
        return self.__memory 
     
    def set_memory(self,value): 
        self.__memory = value 
         
    def make_computations(self): 
        plus = self.__cpu + self.__memory 
        minus = self.__cpu - self.__memory 
        multiply = self.__cpu * self.__memory 
        if self.__memory != 0: 
            divide = self.__cpu / self.__memory 
        else: 
            divide = "на ноль делить нельзя" 
        return plus,minus,multiply,divide 
     
    def __lt__(self, other): 
        return self.__memory < other.__memory 
 
    def __gt__(self, other): 
        return self.__memory > other.__memory 
 
    def __eq__(self, other): 
        return self.__memory == other.__memory 
 
    def __ne__(self, other): 
        return self.__memory != other.__memory 
 
    def __le__(self, other): 
        return self.__memory <= other.__memory 
 
    def __ge__(self, other): 
        return self.__memory >= other.__memory 
     
     
    def __str__(self): 
        return f"Computer: cpu = {self.__cpu}, memory = {self.__memory}" 
        
class Phone: 
    def __init__(self,sim_cards_list): 
        self.__sim_cards_list = sim_cards_list 
     
    def get_sim_cards_list(self): 
        return self.__sim_cards_list 
     
    def set_sim_cards_list(self,value): 
        self.__sim_cards_list = value 
     
    def call(self,sim_card_number,call_to_number): 
        try: 
            operator = self.__sim_cards_list[sim_card_number -1] 
            print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number} - {operator}') 
        except IndexError: 
            print(f'Некорректный ввод.Доступные номера от 1 до {len(self.__sim_cards_list)}.') 
             
    def __str__(self): 
        return f"sim cards = {self.__sim_cards_list}" 
 
class SmartPhone(Computer,Phone): 
    def __init__(self, cpu, memory,sim_cards_list): 
        Computer.__init__(self,cpu,memory) 
        Phone.__init__(self,sim_cards_list) 
         
    def use_gps(self,location): 
        print(f'Через 150 метров будет {location}') 
         
    def __str__(self): 
        return f"{Computer.__str__(self)}, SIM cards = {self.get_sim_cards_list()}"
        
computer_1 = Computer(8,4) 
computer_2 = Computer(24,6)
print(computer_1) 
computations = computer_1.make_computations() 
print(f'Computations: {computations}')
print(f"computer_1 has less memory than computer_2: {computer_1 < computer_2}")
print(f"Computer_1 has more memory than computer_2: {computer_1 > computer_2}")
print(f"Computer_1 and computer_2 have the same memory: {computer_1 == computer_2}")
print(f"computer memory _1 is not equal to computer memory _2: {computer_1 != computer_2}")
print(f"computer_1 has less or equal memory than computer_2: {computer_1 <= computer_2}")
print(f"computer_1 has more or equal memory than computer_2: {computer_1 >= computer_2}")

phone_1 = Phone(["MegaCom","Beeline","o!"])
phone_2 = Phone(["MegaCom","Beeline","o!"])
phone_1.call(1,"+996700800900")
phone_2.call(2,"+996500700800")

smartphone = SmartPhone(4,16,["MegaCom"])
smartphone.use_gps("park Gorky")
smartphone.call(1,"996111222333")
print(smartphone)
