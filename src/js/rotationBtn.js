const rotationBtn = document.querySelector('.rotation-btn');
getRotationBtn();


function getRotationBtn() {
    let href = window.location.href;
    if (href.includes('/contacts/') || href.includes('/order/')) {
        rotationBtn.style.display = 'none';
    }
}

