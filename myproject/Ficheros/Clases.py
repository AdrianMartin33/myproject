from datetime import datetime


class Count:
    pass


a = Count()
b = Count()


class Count:
    def increase(self):
        self.val += 1

    val = 0


c = Count()
c.increase()
c.increase()
print(c.val)


class Count:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        s = 'Counter ' + str(self.val) + ', ' + str(self.incr)
        return s  # Cuando saque el objeto por pantalla me sacará esto


d = Count(100, 10)
print(d.val)
print(d.incr)
d.increase()
print(d)


class Athlete:
    def __init__(self, name: str, dob: datetime = None, times: list = []) -> None:
        self.name = name
        self.dob = dob
        self.times = times

    def fast3times(self) -> None:
        ordenados = self.times
        ordenados.sort()
        if len(ordenados) <= 3:
            return ordenados
        else:
            return ordenados[0:3]

    def add_one_time(self, a_time):
        self.times.append(a_time)

    def add_times(self, list_times):
        self.times.extend(list_times)


ana = Athlete('Ana', datetime.today(), ['26', '23', '14'])
print(ana.times)
print(ana.fast3times())
javi = Athlete('Javi')
print(javi.dob)
