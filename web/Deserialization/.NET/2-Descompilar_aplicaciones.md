### Intro

- .NET está escrito en C#
- Las aplicaciones son compliadas en **intermediate code**(Microsoft Intermediate Lenguage [MSIL]).
- Salvo que se encuentre ofuscado, descompilarlo es fácil y resuelve en un código muy similar al original.

### Herramientas

#### Jet Brains dotPeek (windows-only)

##### Descarga:
    https://www.jetbrains.com/decompiler/

##### Desco

Simplemente cargamos el archivo desde file > open.

Haciendole click derecho a la carpeta general creada en el assembly explorer > export project podemos generar una copia para luego analizarla por separado con otras herramientas.


#### ILSpy (cross-platform)

##### Descarga

    https://github.com/icsharpcode/ILSpy/releases

##### Desco

Funciona igual que dotPeek (pero en algunos casos el código es más parecido al original)


