// Анимация формы заказа консультации
document.addEventListener('DOMContentLoaded', function() {
    const consultationForm = document.querySelector('.consultation-form');
    
    // Анимация появления формы
    gsap.from(consultationForm, {
        duration: 1,
        x: '100%',
        opacity: 0,
        ease: 'power3.out'
    });

    // Анимация полей формы при фокусе
    const formInputs = consultationForm.querySelectorAll('input, select, textarea');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            gsap.to(this, {
                duration: 0.3,
                scale: 1.05,
                boxShadow: '0 0 10px rgba(0,123,255,0.5)'
            });
        });

        input.addEventListener('blur', function() {
            gsap.to(this, {
                duration: 0.3,
                scale: 1,
                boxShadow: 'none'
            });
        });
    });

    // Анимация кнопки отправки при наведении
    const submitButton = consultationForm.querySelector('button[type="submit"]');
    submitButton.addEventListener('mouseenter', function() {
        gsap.to(this, {
            duration: 0.3,
            backgroundColor: '#0056b3',
            scale: 1.1
        });
    });

    submitButton.addEventListener('mouseleave', function() {
        gsap.to(this, {
            duration: 0.3,
            backgroundColor: '#007bff',
            scale: 1
        });
    });
});

// Анимация ссылок при наведении или нажатии
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('mouseenter', function() {
        gsap.to(this, {
            duration: 0.3,
            color: '#007bff',
            scale: 1.1,
            textShadow: '0 0 5px rgba(0,123,255,0.5)'
        });
    });

    link.addEventListener('mouseleave', function() {
        gsap.to(this, {
            duration: 0.3,
            color: '',
            scale: 1,
            textShadow: 'none'
        });
    });

    link.addEventListener('click', function(e) {
        e.preventDefault();
        const href = this.getAttribute('href');

        gsap.to(this, {
            duration: 0.2,
            scale: 0.9,
            onComplete: function() {
                gsap.to(link, {
                    duration: 0.2,
                    scale: 1,
                    onComplete: function() {
                        window.location.href = href;
                    }
                });
            }
        });
    });
});

// Анимация появления элементов при прокрутке
gsap.registerPlugin(ScrollTrigger);

gsap.utils.toArray('.card, .section').forEach(element => {
    gsap.from(element, {
        duration: 1,
        y: 50,
        opacity: 0,
        ease: 'power3.out',
        scrollTrigger: {
            trigger: element,
            start: 'top 80%',
            end: 'bottom 20%',
            toggleActions: 'play none none reverse'
        }
    });
});