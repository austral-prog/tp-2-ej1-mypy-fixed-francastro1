def is_leap_year() -> bool:
    leap: int = int(input("Ingrese un año: "))
    if (leap % 4 == 0 and leap % 100 != 0) or leap % 400 == 0:
        bisiesto: str = "es bisiesto"
        answer: str = f'El año {leap} {bisiesto}'
        print(answer)
        state: bool = True
        return state
    else:
        bisiesto = "no es bisiesto"
        answer = f'El año {leap} {bisiesto}'
        print(answer)
        state = False
        return state
