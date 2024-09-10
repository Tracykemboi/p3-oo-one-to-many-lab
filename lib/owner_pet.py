class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__ (self,name,pet_type,owner=None):
        self.name=name
        self.pet_type=pet_type
        self.owner=owner
        Pet.all.append(self)
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,value):
        if value not in self.PET_TYPES:
            raise ValueError(f'{value} is not in the PET_TYPES')
        self._pet_type = value


class Owner:
    def __init__ (self,name):
        self.name=name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner==self]
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner=self
        else:
            raise ValueError(f'{pet} is not a Pet')
    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet:pet.name)

