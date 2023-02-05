#!/usr/bin/env python
# coding: utf-8

# ACA/IPONWEB OOP EXAM Babajanyan Esfira

# In[3]:


#Task 1
#Creating Error class for the age- limiting it to 18-100
class InvalidAgeException(Exception):
    def __init__(self, value, message):
        self._value = value
        self._message = message
        super().__init__(f"{message}: f{value}")


class Patient():
    def __init__(self, name, surname, age, gender):
        if not (18 <= age <= 100):
            raise InvalidAgeException(age, "Patient must be more than 18 and less than 100 years old")
        
        self._name = name
        self._surname = surname
        self._age = age
        self._gender = gender
        
    def __repr__(self):
        return f"{self._name} {self._surname} - {self._gender}, {self._age} years old."
    
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self,val):
        self._name = val
    
    @name.deleter
    def name(self):
        del self._name
        
    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, val):
        self._surname = val
    
    @surname.deleter
    def surname(self):
        del self._surname
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, val):
        self._age = val
    
    @age.deleter
    def age(self):
        del self._age
        
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, val):
        return self._val
    
    @gender.deleter
    def gender(self):
        del self._gender
        
    def __ne__(self, other):
        if (self._name == other._) and  (self._surname == other._surname) and (self._age == other._age):
            return False
        else:
            return True


# In[9]:


patient1 = Patient("Esfira", "Babajanyan", 20, "F")
print(patient1)


# In[7]:


patient2 = Patient("Bob", "Johnson", 10, "M")
print(patient2)


# In[12]:


patient1.age = 21
print(patient1)


# In[13]:


from datetime import timedelta


# In[29]:


class ExceededNumOfPatientsException(Exception):
    def __init__(self, value, message):
        self._value = value
        self._message = message
        super().__init__(f"{message}: f{value}")

class Doctor():
    def __init__(self, name, surname, schedule):
        self._name = name
        self._surname = surname
        self._schedule = schedule #dict with {datetime:Patient}
        
    
    def __repr__(self):
        return f"Doctor {self._name} {self._surname} schedule {self._schedule}."
    
    
    def num_of_patients(self):
        count == 0
        for i in self._schedule.values():
            count += 1
        if count > 16:
            raise ExceededNumOfPatientsException(count, "Number of patients must be less than 16.")
    
    def is_free(self, datetime):
        if datetime in self._schedule.keys():
            print("This timeslot is busy")
            return False
        else:
            print("This timeslot is available")
            return True
            
    def is_registered(self, patient):
        if patient in self._schedule.values():
            print("Patient is already registered")
            return False
        else:
            print("Patient can be registered")
            return True
    
    #has-a relationship with patient
    def register_patient(self,patient,datetime):
        if self.is_free(datetime) and self.is_registered(patient):
            print("Patient is registered")
            self._schedule[datetime] = self._schedule[patient]
        
        


# In[17]:


#Task 2
class QuantityException(Exception):
    def __init__(self, value, message):
        self._value = value
        self._message = message
        super().__init__(f"{message}: f{value}")


class Product():
    def __init__(self, price, ID, quantity):
        self.price = price
        self.ID = ID
        self.quantity = quantity
        
    def __repr__(self):
        return f"Product {self.ID} has price of {self.price} and is available in {self.quantity}"
    
    def buy(self,count):
        if count > self.quantity:
            raise QuantityException(count, "The product is not available in that quantity")
        else:
            self.count -= quantity
            
    


# In[18]:


class Inventory():
    def __init__(self,products):
        self.products = products
    
    def __repr__(self):
        return f"The list of products in inventory - {self.products}"
    
    def get_by_id(self,num): 
        for i in self.products: #since porducts cotnaint product type objects and those have ID member
            if num == i.ID:     #we can implement ID on our product list memebers
                return i
    
    def sum_of_products(self, product):
        num = 0
        for i in self.products:
            num += i.quantity
        return num
    
         


# In[19]:


#Task 3
class Passenger():
    def __init__(self, name, city, rooms):
        self._name = name
        self._city = city
        self._rooms = rooms
        
    def __repr__(self):
        return f"{self._name} flies to {self._city} and booked {self._rooms}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, val):
        self._city = val
        
    @proerty
    def rooms(self):
        return self._rooms
    
    @rooms.setter
    def rooms(self, val):
        self._rooms = val


# In[22]:


class Hotel():
    def __init__(self, city, rooms):
        self._city = city
        self._rooms = rooms #dict {room type: count of free rooms}
        
    def __repr__(self):
        return f"City - {self._city}, available rooms - {self._rooms}"

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, val):
        self._city = val
    
    def free_rooms_list(self, room_type):
        return self._rooms.get(room_type)

    
    def reserve_rooms(self, room_type, count):
        if self._rooms[room_type] !=0 and self._rooms[room_type] <= count:
            self._rooms[room_type] -= count
        else:
            print("Not enough rooms available, decrease demanded count.")
            
    


# In[ ]:




