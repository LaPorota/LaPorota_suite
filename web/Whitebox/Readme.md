# Pasos:

#### Pasos de un withebox ordenado.

| orden  | paso | desc |
|-----|-----|------|
| 1 | Code review | Revisión general del código para entender su funcionalidad y generar una shortlist con funciones potencialmente vulnerables |
| 2 | Local testint | Testear/debugear el código localmente para probar los hallazgos e identificar nuevas vulnerabilidades no reconocibles con mera lectura |
| 3 | Proof of Concept | Escribir un exploit para demostrar la explotabilidad del target de manera automática |
| 4 | Patching & remediation | Parchear la vulnerabilidad y todas sus causas |


1) Para lograr esto, hay varios enfoques:
- Buscar funciones que utilicen métodos base del lenguaje que conocemos como inseguros. Ej: En php podríamos buscar exec, system, passthru, etc. Y luego rastrear los llamados a las funciones que las utilizan para poder entender cómo es que el imput del user puede alcanzar a alguna de estas.
- Seleccionar funciones en base a nuestro entendimiento de la aplicación.
- Seleccionar funciones en base al uso de la aplicación: Si estamos probando una app y de pronto encontramos alguna funcionalidad que genere muchos errores, podríamos enfocarnos en esa sección.

#### Cuadro de funciones importantes para code injection

|JavaScript 'NodeJS'	|Python	|PHP	|C/C++	|C#	|Java|
|-----|----|---|---|---|---|
|eval	|eval	|eval	|execlp| |   |		
|Function	|exec	|exec	|execvp	|	|  |
|setInterval |	subprocess.open	|proc_open	|ShellExecute |		| |
|setTimeout	|subprocess.run	|popen	|		
|constructor.constructor	|os.system	|shell_exec |			
|child_process.exec	|os.popen	|passthru	|system	|System.Diagnostics.Process.Start	|Runtime.getRuntime().exec|
|child_process.spawn	| |	system	|popen	 |	
