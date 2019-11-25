import { stringify } from 'query-string';

const errorValidMail = 'E-mail не валидный.',
    errorValidTel = 'Телефон не валидный.',
    errorCheckbox = 'Дайте разрешение на обработку данных.',
    emailPattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i,
    telPattern = /^[\+|\d][\d\(\)\-\s]{7,50}$/i;

const categorySelectBtn = document.querySelector('.header-nav-select'),
    categorySelect = document.querySelector('.category-select'),
    indexForm = document.querySelector('#head-banner-form'),
    orderForm = document.querySelector('#order-form');

const headerTelBtn = document.querySelector('.header-tel-btn'),
    headerMenuBtn = document.querySelector('.header-menu-btn'),
    closeTelPopupBtn = document.querySelector('.close-tel-popup-btn'),
    closeMenuPopupBtn = document.querySelector('.close-menu-popup-btn'),
    contactsPopup = document.querySelector('.contacts-popup'),
    menuPopup = document.querySelector('.menu-popup');


categorySelectBtn.addEventListener('click', showCategorySelect);

document.addEventListener('click', (e) => {
    if (!e.target.closest('.category-select') && e.target !== categorySelectBtn) {
        categorySelect.classList.remove('category-select-active');
        categorySelectBtn.classList.remove('header-nav-select-active');
    }
});


function showCategorySelect() {
    if (!categorySelect.classList.contains('category-select-active')) {
        categorySelect.classList.add('category-select-active');
        categorySelectBtn.classList.add('header-nav-select-active');
    } else {
        categorySelect.classList.remove('category-select-active');
        categorySelectBtn.classList.remove('header-nav-select-active');
    }
}

headerTelBtn.addEventListener('click', () => {
    document.body.classList.add('body-popup-active');
    contactsPopup.classList.add('popup-active');
});

closeTelPopupBtn.addEventListener('click', () => {
    document.body.classList.remove('body-popup-active');
    contactsPopup.classList.remove('popup-active');
});

headerMenuBtn.addEventListener('click', () => {
    document.body.classList.add('body-popup-active');
    menuPopup.classList.add('popup-active');
});

closeMenuPopupBtn.addEventListener('click', () => {
    document.body.classList.remove('body-popup-active');
    menuPopup.classList.remove('popup-active');
});

document.querySelector('#services-btn').addEventListener('click', () => {
    document.body.classList.remove('body-popup-active');
    menuPopup.classList.remove('popup-active');
});





indexForm && indexForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let form = e.target;
    let item = form.querySelector('[name="item"]').value;
    window.location.href = `/order?${stringify({ item })}`
});


orderForm && orderForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let form = e.target;
    let name = form.querySelector('[name="name"]').value,
        company = form.querySelector('[name="company"]').value,
        tel = form.querySelector('[name="tel"]').value,
        email = form.querySelector('[name="email"]').value,
        item = form.querySelector('[name="item"]').value,
        checkbox = form.querySelector('[name="checkbox"]');
    if (!emailPattern.test(email)) {
        alert(errorValidMail);
    } else if (!telPattern.test(tel)) {
        alert(errorValidTel);
    } else if (!checkbox.checked) {
        alert(errorCheckbox);
    } else {
        let data = { name, company, tel, email, item };
        fetch('/order_form/', {
            method: 'POST',
            credentials: "include",
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify(data)
        })
            .then(() => {
            form.querySelector('[name="name"]').value = '';
            company = form.querySelector('[name="company"]').value = '';
            tel = form.querySelector('[name="tel"]').value = '';
            email = form.querySelector('[name="email"]').value = '';
            item = form.querySelector('[name="item"]').value = '';
            window.location.href = '/success';
            })
            .catch(e => console.log(e))
    }

});













