import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeepers, Fence, Animal

class TestZoo(TestCase):

    def setUp(self) -> None:       #creazione istanze per effettuare il test
        
        #self.zoo1 : Zoo = Zoo()
        self.zookeeper_1 : ZooKeepers = ZooKeepers("Gianni", "Rossi",1)
        self.fence1 : Fence = Fence(area=100, temperature=25.0, habitat="savana")
        self.animal1 : Animal = Animal(name="Pluto",species="Canide",age=5, height=3.0 ,width=1.0, preferred_habitat="savana")

    def test_animal_dimension(self):

        self.zookeeper_1.add_animal(self.animal1, self.fence1)
        result: int = len(self.fence1.animals)
        message : str = f"Error: the function add_animal should not add self.animal into self.fence"

        self.assertEqual(result, 1, message)

    def test_remove_animal(self):

        self.zookeeper_1.remove_animal(self.animal1, self.fence1)
        result : int = len(self.fence1.animals)
        message : str = f"Error: the function remove_animal should not remove self.animal into self.fence"

        self.assertEqual(result, 0, message)
                

if __name__ == "__main__":

    unittest.main()

    jjjjjjjjj