### INTRO
Hay 3 tipos principales de tecnologías de serialización en .NET:

| tipo  | desc |
|------|------|
|Json | Serializa objetos .NET hacia y desde JSON |
|XML & SOAP | Serializa solamente loas propiedades públicas y campos de un objeto. No preserva fidelidad en los tipos |
|Binary | Guarda el estado completo de un objeto y preserva la fidelidad de tipos. Cuando se deserializa se crea una copia exacta del objeto |


### ObjectDataProvider

- Es una clase que permite crear un objeto que puede usar como una fuente "vinculante"(arbitrario para solucionar problemas puntuales)
- Es parte del Windows Presentation Framework. Un framework de .NET para crear GUIs con XAML(variante de microsonft de XML).

##### Campos principales:

| campo | desc |
|-----|-----|
|ObjectType | Usado para setear el tipo de objeto para crear una instancia del mismo |
|MethodName | Setea el nombre de un método para llamar cuando se crea el objeto |
|MethodParameters | La lista de parámetros para psarle al objeto |

**Usando estos tres campos podemos crear una instancia de un objeto arbitrario, para llamar a un metodo arbitrario con parametros arbitrarios.**

##### Ejemplo:

Podemos crear un objeto que llame de manera arbitraria a la calculadora.

              using System.Windows.Data;
              
              namespace ODPExample
              {
                  internal class Program
                  {
                      static void Main(string[] args)
                      {
                          ObjectDataProvider odp = new ObjectDataProvider();
                          odp.ObjectType = typeof(System.Diagnostics.Process);
                          odp.MethodParameters.Add("C:\\Windows\\System32\\cmd.exe");
                          odp.MethodParameters.Add("/c calc.exe");
                          odp.MethodName = "Start";
                      }
                  }
              }
