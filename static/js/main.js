document.addEventListener('DOMContentLoaded', function() {
    const consultationToggle = document.getElementById('consultationToggle');
    const consultationForm = document.getElementById('consultationForm');

    if (consultationToggle && consultationForm) {
        consultationToggle.addEventListener('click', function() {
            consultationForm.classList.toggle('active');
        });
        // Обновление страницы при возвращении на нее
        window.addEventListener('pageshow', function(event) {
            if (event.persisted) {
                window.location.reload();
            }
        });
    }

    // Закрытие формы при клике вне её
    document.addEventListener('click', function(event) {
        if (!consultationForm.contains(event.target) && event.target !== consultationToggle) {
            consultationForm.classList.remove('active');
        }
    });

    // Обработка мобильного меню
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
    }
});