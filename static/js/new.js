document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.carousel-image');
    const indicators = document.querySelectorAll('.cylinder');
    let currentIndex = 0;

    function updateCarousel(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
            indicators[i].classList.toggle('active', i === index);
        });
        currentIndex = index;
    }

    window.prevSlide = function () {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        updateCarousel(currentIndex);
    }

    window.nextSlide = function () {
        currentIndex = (currentIndex + 1) % slides.length;
        updateCarousel(currentIndex);
    }

    // Add click event to indicators
    indicators.forEach((indicator, i) => {
        indicator.addEventListener('click', () => {
            updateCarousel(i);
        });
    });
});