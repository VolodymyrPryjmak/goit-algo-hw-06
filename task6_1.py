from collections import UserDict
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(self, field, new_field = ""):
        try:
            if func.__name__ == "add_phone":
               return func(self, field)
            elif func.__name__ == "edit_phone":    
               return func(self, field, new_field)

        except ValueError:
            print(f" Неправильний формат номеру телефону  {field} {new_field} {func.__name__}")
            return 
    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self,name):
        super().__init__(name)

class Phone(Field):
    def __init__(self,phone):
        super().__init__(phone)
        self.is_valid = self.is_valid()

    def is_valid(self):
        if (len(self.value) != 10) or (self.value.isdigit() == False):
           return False
        else:
            return True 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    @input_error
    def add_phone(self, phone):
        if Phone(phone).is_valid == True:
           self.phones.append(Phone(phone))
        else:
            raise ValueError()

    def remove_phone(self, phone):
        for el in self.phones: 
            if str(el) == phone:
               self.phones.remove(el) 

    def find_phone(self, phone):
        for el in self.phones:
            if str(el) == phone:
               return el  
        return None    
    
    @input_error
    def edit_phone(self, phone, new_phone):
        try:
            old_phone = Record.find_phone(self,phone) 
            if  Phone(new_phone).is_valid == True:
                self.phones[self.phones.index(old_phone)] = new_phone
            else:
                raise ValueError()
        except:
            raise ValueError() 
        
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record): 
        self.data[record.name.value] = record

    def find(self, record_name):
        for el in self.data:
            if record_name == el:
               el_phone = self.data.get(el)
               return el_phone
        return None

    def delete(self, record):          
        for el in self.data:
            if record == el:
               self.data.pop(el)
               return 
        return  

    def __str__(self):
        st = ""
        for x in self.data:
            x_phone = self.data.get(x)
            st += str(x) + " phones: "
            for p in x_phone.phones:
                st += f" {p}"
            st += "\n"
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
    print(f"{john.name}:  {found_phone}")  # Виведення: John: 5555555555

    john.remove_phone("7777777777")
# Видалення запису Jane
    book.delete("Jane")
    print(book)
