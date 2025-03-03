from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def init(self,name):
        super().__init__(name)


class Phone(Field):
    def init(self,phone):
        super().__init__(phone)

    def valid(self,phone):
        if len(phone) == 10:
           return phone.isdigit() 
        return False 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if Phone.valid(self, phone) == True: 
           self.phones.append(phone) 
        else:
           print(f"Некоректний номер телефону: {phone} ")
         
    def remove_phone(self, phone):
        for el in self.phones: 
            if el == phone:
               self.phones.remove(el) 

    def edit_phone(self, phone, new_phone):
        if Phone.valid(self, new_phone) == True: 
            for el in self.phones:
                if el == phone:
                   self.phones[self.phones.index(el)] = new_phone
                   return
        else:       
            print(f"Некоректний новий номер телефону: {new_phone} ")
            return
    
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"

    def find_phone(self, phone):
        for el in self.phones: 
            if el == phone:
               return el  
        return None    

class AddressBook(UserDict):

    def add_record(self, name ): 
        self.data[name] = name
        
    def find(self, name):
        for el in self:
            if name.strip() == str(el.name).strip():
               return el
        return None

    def delete(self, name):          
        for el in self:
            if name.strip() == str(el.name).strip():
               self.pop(el)
               return 
        return  
    
    def __str__(self):
        st = ""
        for x in self:
            st = st + str(x) + "\n"
        return  st
    
if __name__ == "__main__":    
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("7777777777")
# Додавання запису John до адресної 
    book.add_record(john_record)
# Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")

    book.add_record(jane_record)

# Виведення всіх записів у книзі
    print(book)

    john = book.find("John")
    john_record.edit_phone("1234567890", "1112223333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    john.remove_phone("7777777777")
# Видалення запису Jane
    book.delete("Jane")
    print(book)
