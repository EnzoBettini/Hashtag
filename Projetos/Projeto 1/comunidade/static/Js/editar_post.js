document.addEventListener('click', function (e) {
    // abrir
    const openBtn = e.target.closest('.icone-editar-post');
    if (openBtn) {
        const id = openBtn.getAttribute('data-modal-target');
        const modal = document.getElementById(id);
        if (modal) {
            modal.classList.add('is-open');
            document.body.style.overflow = 'hidden'; // bloqueia scroll do fundo
        }
    }

    // fechar (botão fechar)
    if (e.target.classList.contains('close-modal')) {
        const modal = e.target.closest('.modal-container-enzo');
        closeModal(modal);
    }

    // fechar (clicando fora, no overlay)
    if (e.target.classList.contains('modal-container-enzo')) {
        closeModal(e.target);
    }
});

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        const openModal = document.querySelector('.modal-container-enzo.is-open');
        if (openModal) closeModal(openModal);
    }
});

function closeModal(modalEl) {
    if (!modalEl) return;
    modalEl.classList.remove('is-open');
    // libera scroll se não houver outro modal aberto
    if (!document.querySelector('.modal-container-enzo.is-open')) {
        document.body.style.overflow = '';
    }
}
