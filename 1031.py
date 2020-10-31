class Myobject() :
    def __init__(self, in_name, in_age) :
        self.name = in_name
        self.age = in_age
    def diff_age (self, other) :
        return self.age - other.age

jane = My.object("jane", 20)
tom = My.object("tom", 30)

print(jane.age-tom.age)
print(jane.age)
jane.add_age(5)

git checkout -b "Issue-#1=fastaqparser"
ll
mkdir src data
ll

git status ##확인하고
git add .
git commit -m "issue #1: Download"
git push origin main