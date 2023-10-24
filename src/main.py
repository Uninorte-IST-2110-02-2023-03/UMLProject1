from book import LibroImpreso, LibroDigital, Audiolibro
from core import Megaferia
from company import Editorial
from person import Autor, Gerente, Narrador

def main() -> None:
    megaferia = Megaferia()

    autor_1 = Autor('Autor 1', 847965457)
    autor_2 = Autor('Autor 2', 847965458)
    autor_3 = Autor('Autor 3', 847965459)

    gerente_1 = Gerente('Gerente 1', 987944945)
    gerente_2 = Gerente('Gerente 2', 886486457)

    narrador_1 = Narrador('Narrador 1', 1589874678)

    editorial_1 = Editorial('981-56487845-1', 'Editorial Nova 1', 'Calle 1 # 1 - 1', gerente_1)
    editorial_2 = Editorial('981-56487845-2', 'Editorial Nova 2', 'Calle 2 # 2 - 2', gerente_2)

    megaferia.add_stand(50000.0)
    megaferia.add_stand(100000.0)
    megaferia.add_stand(75000.0)

    editorial_1.add_stand(megaferia.get_stand(0))
    editorial_1.add_stand(megaferia.get_stand(1))

    editorial_2.add_stand(megaferia.get_stand(0))
    editorial_2.add_stand(megaferia.get_stand(2))

    libro_1 = LibroImpreso(
        titulo = 'Cien años de soledad',
        isbn = '848559455',
        genero = 'Novela',
        formato = 'Tapa dura',
        valor = 85000.0,
        editorial = editorial_1,
        paginas = 496,
        num_ejemplares = 5
    )

    libro_2 = LibroDigital(
        titulo = 'El aliento de los dioses',
        isbn = '5848485984',
        genero = 'Novela',
        formato = 'pdf',
        valor = 60000.0,
        editorial = editorial_2,
        has_hipervinculo = True
    )

    libro_3 = Audiolibro(
        titulo = 'Harry Potter',
        isbn = '1896455814',
        genero = 'Novela',
        formato = 'mp4',
        valor = 50000.0,
        editorial = editorial_1,
        duracion = 330,
        narrador = narrador_1
    )

    autor_1.add_libro(libro_1)
    autor_1.add_libro(libro_3)
    autor_2.add_libro(libro_1)
    autor_2.add_libro(libro_2)
    autor_3.add_libro(libro_1)
    autor_3.add_libro(libro_2)


if __name__ == '__main__':
    main()