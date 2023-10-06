from collections import UserDict
import re

class PhoneTooShort(ValueError):
    pass

class PhoneIncludesNotOnlyNumbers(ValueError):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
    

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) != 10:
            raise  PhoneTooShort("Phone number should be 10 digits long.")
        if len(re.findall('\d', self.value)) != 10:
            raise PhoneIncludesNotOnlyNumbers("Phone number should only include digits.")
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
         list_of_phones = [el.value for el in self.phones]
         if phone in list_of_phones:
            index_of_phone_to_remove = list_of_phones.index(phone)
            self.phones.pop(index_of_phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        list_of_phones = [el.value for el in self.phones]
        self.phones[list_of_phones.index(old_phone)] = Phone(new_phone)
    
    def find_phone(self, phone_to_find):
        list_of_phones = [el.value for el in self.phones]
        if phone_to_find in list_of_phones:
            return self.phones[list_of_phones.index(phone_to_find)]


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name_value):
        if name_value in self.data:
            found_record = self.data[name_value]
            return found_record
        return None
    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
