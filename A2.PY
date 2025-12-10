class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)


class emp(person):
    def __init__(self, name, age, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, age)

obj=emp("Rahul", 23, 25000, "intern")
obj.display()
print(obj.salary)
print(obj.post)

        


        
        
