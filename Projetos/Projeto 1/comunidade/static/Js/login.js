var botaoCriarConta = document.getElementById("botao_submit_criar_conta")
var botaoAceitarTermos = document.getElementById("aceitar-termos")

botaoAceitarTermos.addEventListener('change', (event) => {
    if (event.target.checked) {
        botaoCriarConta.classList.remove('disabled')
    } else {
        botaoCriarConta.classList.add('disabled')
    }
})
