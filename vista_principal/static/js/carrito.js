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

// carrito.js

document.addEventListener('DOMContentLoaded', function() {
    // Selecciona todos los botones de agregar al carrito
    const updateCartButtons = document.querySelectorAll('.update-cart');
    
    // Añade un evento a cada botón
    updateCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.dataset.product;
            const action = this.dataset.action;
            
            // Realiza la solicitud AJAX
            fetch('/update_item/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    'productId': productId,
                    'action': action
                })
            })
            .then(response => response.json())
            .then(data => {
                // Actualiza el número de productos en el carrito
                document.querySelector('.count').textContent = data.total_productos;
            });
        });
    });
});

