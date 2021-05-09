import math
from typing import List


def paralelogramma_kalkulal(a: float, b: float, ma: float, mb: float) -> List:
    kerület = 2 * (a + b)
    terület = a * ma
    if ma == 0:
        terület = b * mb
    if a <= 0 or b <= 0:
        print('Az oldalak hossza nem lehet 0 vagy negatív szám!')
        exit()
    if ma <= 0 and mb <= 0:
        terület = math.nan
        print('===================================================================')
        print('Mindkét magasság értéke nem lehet 0 vagy negatív érték! -> terület számolás sikertelen!')
    return [round(kerület, 3), round(terület, 3)]


print('Paralelogramma kerület-terület számító program')
print('================================================')


def main() -> None:
    print('Csak az egyik magasság kitöltése kötelező, a másikhoz tegyen 0-át!')
    print('===================================================================')
    a = float(input('Kérem az a oldal hosszát cm-ben: '))
    b = float(input('Kérem az b oldal hosszát cm-ben: '))
    ma = float(input('Kérem az a oldalhoz tartozó magasságot cm-ben: '))
    mb = float(input('Kérem az b oldalhoz tartozó magasságot cm-ben: '))
    eredmény = paralelogramma_kalkulal(a, b, ma, mb)
    print('================================')
    print(f'A Paralelogramma kerülete/területe: {eredmény}')


if __name__ == '__main__':
    main()
