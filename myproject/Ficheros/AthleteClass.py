from datetime import datetime


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



