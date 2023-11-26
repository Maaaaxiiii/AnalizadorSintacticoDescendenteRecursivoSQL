# AnalizadorSintacticoDescendenteRecursivoSQL


__Este es el repositorio de:__


- Muñoz Tapia Alan Arath

- Reyes López Maximiliano

- Santos Alan Eduardo

__Gramática Utilizada:__
1. Q -> __select__ D __from__ T
2. D -> __distinct__ P | P
3. P -> * | A
4. A -> A~2~ A~1~
5. A~1~ -> __,__ A | Ɛ
6.  A~2~ -> __id__  A~3~
7.  A~3~ -> __.__ __id__ | Ɛ
8. T -> T~2~ T~1~
9. T~1~ -> __,__ T | Ɛ
10. T~2~ -> __id__ T~3~ 
11. T~3~ -> __id__ | Ɛ

__Analizar un archivo de texto__

- Para ejecutar `python3 main.py nombre_archivo.txt`

__Analizar texto directamente desde la terminal__

- Para ejecutar `python3 main.py`, ahora solo hay que usar la terminal para introducir las cadenas que se desean analizar. Para salir hay que usar la combinación `ctrl + C`