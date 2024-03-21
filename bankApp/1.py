
# Parent class : User => Ota (Super) klass
class User():
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
    
    def show_details(self):    
        """ Foydalanuvchi ma'lumotlarini ko'rsatuvhci funksiya """
        print("Shaxsiy ma'lumotlar:")
        info = f"Name : {self.name}\nSurname : {self.surname}\nAge : {self.age}\nGender : {self.gender}"   
        return info
    

# user1 = User('Nazar',"Ne'matov",20,"Male")   # user1 obyektini yaratdik   
# print(user1.show_details())

# Child class : Voris class
class Bank(User):
    def __init__(self, name, surname, age, gender):
        super().__init__(name, surname, age, gender)
        self.balance = 0
    # deposit - bankka qo'yilgan pul miqdori.              amount - miqdor (yig'indi) - biz qo'yadigan summa 
    def deposit(self, amount):
        """ Bankka qo'yilgan pul miqdori """ 
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Hisob balansi yangilandi :  $", self.balance)

# user1 = Bank('Nazar',"Ne'matov",20,"Male")   # user1 obyektini yaratdik   
# print(user1.deposit(100)) # bankka dastlab 100$  qo'yildi.     
# print(user1.deposit(400))  # bankka yana 400$ qo'yildi , endi jami summa => amount = 400 , balance = 500
# print(user1.deposit(500))


# withdraw - bank hisob raqamidan pul olmoq
    def withdraw(self, amount):
        """ Bankdagi hisob raqamdan pul yechib olish """
        self.amount = amount
        if (self.amount > self.balance):
            print("Hisobingizda mablag' yetarli emas, Hisobingizdagi mavjud balance : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Hisob balansi yangilandi :  $", self.balance)
            
# user1 = Bank('Nazar',"Ne'matov",20,"Male")   # user1 obyektini yaratdik   
# print(user1.deposit(10))
# print(user1.withdraw(500))

    def view_balance(self):
        """Joriy Balansni ko'rsatish """
        self.show_details()
        print("Hisob balansi yangilandi :  $", self.balance)

# user1 = Bank('Nazar',"Ne'matov",20,"Male")   # user1 obyektini yaratdik   
# print(user1.deposit(1000))
# print(user1.withdraw(100))
# print(user1.show_details())
# print(user1.view_balance())