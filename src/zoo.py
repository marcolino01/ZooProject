class Animal:
    def __init__(self, name: str,
                species: str, 
                age: int, 
                height: float, 
                width: float, 
                preferred_habitat: str,):
        self.name : str = name
        self.species : str = species
        self.age : int = age
        self.height : float = height
        self.width : float = width
        self.preferred_habitat : str = preferred_habitat
        self.health : float = round(100 * (1 / age), 3)
        self.area_animal : float = height * width 
        self.fence : Fence = None

    def area(self):
        return self.height * self.width

    def become_bigger(self, factor : float = 0.02):
        self.height = self.height * factor
        self.width = self.width * factor
        return self.height, self.width
    
    def become_healtier(self, factor: float = 0.01):
        self.health = min(self.health + self.health * factor, 100)

        
    def __str__(self) -> str:
        return f"Animal: (name = {self.name},species = {self.species}, age = {self.age})"
        

    


class Fence:
    def __init__(self, area: float, 
                temperature: float, 
                habitat: str):
        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.animals : list[Animal] = []



    def same_habitat(self, animal: Animal):
        return animal.preferred_habitat == self.habitat
    
    def enough_space(self, animal_area: float):
        return animal_area <= self.area
    
    def update_area(self, new_animal_area: float, old_animal_area: float):
        self.area += old_animal_area
        self.area -= new_animal_area
    
    def add_animal(self, animal: Animal):
        if self.same_habitat(animal) and self.enough_space(animal.area_animal) and animal not in self.animals:
            self.animals.append(animal)
            animal.fence = self
        
    def remove_animal(self, animal: Animal):
        if animal in self.animals:
            self.animals.remove(animal)
            self.area +=  animal.area()
            animal.fence = None


    def __str__(self) -> str:
        return f"Fence(area= {self.area}, temperature={self.temperature}, habitat={self.habitat})"



class ZooKeepers:
    def __init__(self, name: str, 
                 surname: str, 
                 id: str):
        self.name : str = name
        self.surname : str = surname
        self.id : int = id


    def add_animal(self,animal: Animal, fence: Fence):
        fence.add_animal(animal)


    def remove_animal(self, animal: Animal, fence : Fence):
        fence.remove_animal(animal)
    
    
    def feed(self, animal: Animal):
        fence: Fence = animal.fence
        if fence:
            
            new_height, new_widht = animal.become_bigger()
            if fence.enough_space((new_height * new_height) - animal.area()):
               fence.area += animal.area()
               animal.height = new_height
               animal.width = new_widht
               fence.area += animal.area()
               animal.become_healtier()
        
    
    
    def clean(self,fence: Fence):
        occupate_area : float = 0
        
        for animal in fence.animals:
            occupate_area += animal.area()
        self.time: float = occupate_area / fence.area
        
        

        return self.time
        

    def __str__(self) -> str:
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"


class Zoo:
    def __init__(self, zookeepers, fence):
        self.zookepers : list[ZooKeepers] = zookeepers
        self.fence : list[Fence] = fence
        self.animals : list[Animal]
        

    def describe_zoo(self):
        print("Guardians:")
        for guardian in self.zookepers:
            print(guardian.__str__())
        
        print("Fences:")
        for fence in self.fence:
            print(fence.__str__())

        print("Animals:")
        for animal in self.animals:
            print(animal.__str__())

        
    

