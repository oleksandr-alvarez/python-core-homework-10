from collections import UserDict

class PhoneTooShortError(ValueError):
    pass

class PhoneIncludesNotOnlyNumbersError(ValueError):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) != 10:
            raise  PhoneTooShortError("Phone number should be 10 digits long.")
        if not self.value.isdigit():
            raise PhoneIncludesNotOnlyNumbersError("Phone number should only include digits.")
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone_to_remove):
         search_for_phone = list(filter(lambda phone: phone.value == phone_to_remove, self.phones))
         if search_for_phone:
             self.phones.remove(search_for_phone[0])
         

    def edit_phone(self, old_phone, new_phone):
        search_for_phone = list(filter(lambda phone: phone.value == old_phone, self.phones))
        if search_for_phone:
            search_for_phone[0].value = new_phone
        else:
            raise ValueError
    
    def find_phone(self, phone_to_find):
        search_for_phone = list(filter(lambda phone: phone.value == phone_to_find, self.phones))
        if search_for_phone:
            return search_for_phone[0]
 
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name_value):
        return self.data.get(name_value)
    
    def delete(self, name):
        self.data.pop(name, 'Name not present')
