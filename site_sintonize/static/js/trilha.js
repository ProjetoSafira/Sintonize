
(function() {
    /**
     * Adiciona animação de aparição suave aos elementos selecionados.
     * @param {string} selector - Seletor CSS dos elementos a animar.
     * @param {Object} options - Opções do IntersectionObserver.
     */
    function animarAparicao(selector, options) {
        const elementos = document.querySelectorAll(selector);
        if (!elementos.length) return;

        const observer = new IntersectionObserver((entries, observerInstance) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observerInstance.unobserve(entry.target); // Para animar só uma vez
                }
            });
        }, options);

        elementos.forEach(el => observer.observe(el));
    }

    document.addEventListener("DOMContentLoaded", function() {
        // Animação dos blocos de sintomas
        animarAparicao('.sintoma-bloco', { threshold: 0.9 });

        // Animação da seção de diagnóstico
        animarAparicao('.diagnostico-section', { threshold: 0.2 });
    });
})();



