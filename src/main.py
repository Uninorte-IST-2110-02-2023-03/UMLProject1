from book import LibroImpreso, LibroDigital, Audiolibro
from company import Editorial
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

    editorial = Editorial('981-56487845-1', 'Editorial Nova', 'Calle 1 # 1 - 1')

    print(libro_1)
    print(libro_2)
    print(libro_3)
    print(editorial)

if __name__ == '__main__':
    main()