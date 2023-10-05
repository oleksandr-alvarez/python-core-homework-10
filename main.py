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
            raise PhoneTooShort
        if len(re.findall('\d', self.value)) != 10:
            raise PhoneIncludesNotOnlyNumbers
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone).value)
    
    def remove_phone(self, phone):
        self.phones.remove(Phone(phone).value)

    def edit_phone(self, old_phone, new_phone):
        self.phones[self.phones.index(old_phone)] = new_phone
    
    def find_phone(self, phone_to_find):
        if phone_to_find in self.phones:
            return phone_to_find


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name_value):
        if name_value in self.data:
            found_record = self.data[name_value]
            return found_record
        else:
            return None
    
    def delete(self, name):
        self.data.pop(name)
