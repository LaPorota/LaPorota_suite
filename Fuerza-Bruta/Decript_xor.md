### Hexadecimal

Si tenemos un XOR en hexadecimal y el texto plano con el que fue encriptado podemos conseguir su clave con cyberchef utilizando la receta de hex y la de xort con utf8 en cascada:

    https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':''%7D,'Standard',false)

Agregamos luego en key el texto plano y el hexadecimal en el imput

