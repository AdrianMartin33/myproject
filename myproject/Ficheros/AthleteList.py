from datetime import datetime


class AthleteList(list):
    def __init__(self, name: str, dob: datetime = None, times: list = []) -> None:
        self.name = name
        self.dob = dob
        list.__init__([])
        self.extend(times)

    def fast3times(self) -> None:
        ordenados = self.times
        ordenados.sort()
        if len(ordenados) <= 3:
            return ordenados
        else:
            return ordenados[0:3]


juan = AthleteList("Juan Español", datetime.today(), ['26', '23', '14'])
juan.append("2:12")
juan.extend(['3', "35", '12:6'])
print(juan)