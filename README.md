<h1>Python - Juego Apuestas Consola</h1>
<br>
<p>Se solicita a ud crear un juego de azar, el funcionamiento del juego se basa en que el usuario ingrese una apuesta <code>(que puede ser <code>X1</code>, <code>X3</code>, <code>X5</code> ó <code>X7</code>, no hay más opciones)</code>, en cada apuesta se le descontará de su saldo <code>$100</code> por el multiplicador, es decir, si el usuario apostó <code>X3</code> se descuenta de su saldo <code>$300</code>, luego el programa debe generar <code>9</code> números al azar y mostrarlos en pantalla como sigue:</p>
<br>
<br>
<center><img src="https://imgur.com/fXLPeZQ.png" alt=""></center>
<br><br>
<p>El jugador gana en caso de que aparezcan <code>3</code> números consecutivos iguales, pero la disposición y el premio de esos números consecutivos depende de la apuesta, tal como se observa en la siguiente figura: </p>
<br><br>
<center><img src="https://imgur.com/CQfB2Z1.png" alt=""></center>
<br><br>
<p>El jugador no puede realizar la apuesta si no tiene el dinero suficiente, en caso de que intente realizar una jugada sin dinero suficiente se le debe mostrar un mensaje de advertencia.</p>
<br>
<p>En cada intento se debe mostrar al usuario un menú como el siguiente: </p>
<br><br>
<center><img src="https://imgur.com/WXGtjbr.png" alt=""></center>
<br><br>
<p>Se le solicita a ud implementar dos funciones, una función llamada <code>imprimirMenu()</code> la cual debe imprimir el menú mostrado arriba, solicitar el ingreso de la opción y retornar la opción ingresada por el usuario. La segunda función se debe llamar jugar y debe recibir como argumento la apuesta del usuario e implementar la lógica descrita del juego, esta función debe devolver el premio de la jugada. Además considere que en cada jugada se debe mostrar el saldo del usuario.</p>


