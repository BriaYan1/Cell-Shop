// Al cargar la página, recuperar el valor del contador del carrito 
document.addEventListener('DOMContentLoaded', function() { 
    var cartCountElement = document.getElementById('cart-count'); 
    if (cartCountElement) { 
        var savedCount = (localStorage.getItem('cartCount')); 
        cartCountElement.innerText = savedCount ? savedCount : 0; // Establecer el contador al valor guardado o a 0 
    } 
}); 
var actualizarBtns = document.getElementsByClassName('update-cart') 
for (i = 0; i < actualizarBtns.length; i++) { 
    actualizarBtns[i].addEventListener('click', function(){ 
        var productId = this.dataset.product 
        var action = this.dataset.action 
        console.log('productId:', productId, 'action:', action) 
        console.log('USER:', user) 
        if(user === 'AnonymousUser'){ 
            console.log('No esta logeado') 
        } 
        else{ 
            updateUserOrder(productId, action) 
        } 
    }) 
} 
function updateUserOrder(productId, action) {
    console.log('Usuario logeado, enviando datos...');
    var url = '/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data);
        // Aquí actualizamos el contador del carrito
        var cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            var currentCount = parseInt(cartCountElement.innerText) || 0; // Obtiene el valor actual del contador
            if (action === 'add') {
                currentCount += 1; // Incrementa el contador
            } else if (action === 'remove') {
                currentCount = Math.max(currentCount - 1, 0); // Decrementa el contador, sin permitir que sea negativo
            }
            cartCountElement.innerText = currentCount; // Actualiza el contador
            localStorage.setItem('cartCount', currentCount); // Guarda el nuevo conteo en localStorage
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}