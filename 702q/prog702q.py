from cl702q import *


def main():
    try:
        vehicles: list[Vehicle] = []
        with open("../Langdat/prog702q(1).txt", 'r') as f:
            num = int(f.readline())
            while num != 99:
                name = f.readline()
                tires = f.readline()
                if num == 1:
                    worth = float(f.readline())
                    v = Car(name, tires, worth)
                    vehicles.append(v)
                elif num == 2:
                    miles = int(f.readline())
                    v = Truck(name, tires, miles)
                    vehicles.append(v)
                elif num == 3:
                    fav_word = f.readline().strip()
                    p = Admin(fn, ln, fav_word)
                    people.append(p)
                num = int(f.readline())
            tot = 0.0
            cnt = 0
            tot_stus = 0
            large = ""
            small = "dhgsfkjdhsjfhkdlhgsakhfjhakdhakjhfkjdahgualhglkjfhdgkahekuahfdkjlakuehfkjlhdkuhejfkeheu"
            for person in people:
                if isinstance(person, Student):
                    tot += person.gpa
                    cnt += 1
                elif isinstance(person, Teacher):
                    tot_stus += person.num_stu
                elif isinstance(person, Admin):
                    fw = person.fav_word
                    if len(fw) > len(large):
                        large = fw
                    if len(fw) < len(small):
                        small = fw
            print("Average student GPA:", round(tot/cnt, 2))
            print("Total number of students taught:", tot_stus)
            print("Smallest favorite admin word:", small)
            print("Largest favorite admin word:", large)
    except Exception as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
