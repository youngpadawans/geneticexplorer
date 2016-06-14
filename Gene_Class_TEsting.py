__author__ = 'theep_000'
class Gene:

    __ingredient = ""
    score_dict = {"tomato sauce" : 7,"pesto" : 5,"mozzarella" : 5,"alfredo sauce" : 10, "pasta shells" : 7,"chile sauce" : 5, "pasta bowties" : 5, "parmesan" : 10,"meatballs" : 8,"pasta tubes" : 10,"shredded chicken" : 10,"basil" : 7, "spinach" : 10,"chives" : 2,"shrimp" : 2,"mushroom" : 2,"macaroni" : 5,"feta cheese" : 2,"noodles" : 7,"sausage" : 7,"olives": 0}

    def __init__(self, ingredient):

        self.__ingredient = ingredient
