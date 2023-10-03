from book import LibroImpreso, LibroDigital, Audiolibro
from core import Megaferia
from person import Autor

def main() -> None:
    #nombre = input('Digite el nombre del autor: ')
    #cedula = int(input('Digite el cedula del autor: '))
    
    #autor = Autor(nombre, cedula)

    #print(autor)

    libro_1 = LibroImpreso(
        titulo = 'Cien años de soledad',
        isbn = '848559455',
        genero = 'Novela',
        formato = 'Tapa dura',
        valor = 85000.0,
        paginas = 496,
        num_ejemplares = 5
    )

    libro_2 = LibroDigital(
        titulo = 'El aliento de los dioses',
        isbn = '5848485984',
        genero = 'Novela',
        formato = 'pdf',
        valor = 60000.0,
        has_hipervinculo = True
    )

    libro_3 = Audiolibro(
        titulo = 'Harry Potter',
        isbn = '1896455814',
        genero = 'Novela',
        formato = 'mp4',
        valor = 50000.0,
        duracion = 330
    )

    megaferia = Megaferia()

    print(libro_1)
    print(libro_2)
    print(libro_3)
    print(megaferia)

    megaferia.add_stand(50000.0)
    megaferia.add_stand(100000.0)
    megaferia.add_stand(75000.0)

    print(megaferia)

if __name__ == '__main__':
    main()