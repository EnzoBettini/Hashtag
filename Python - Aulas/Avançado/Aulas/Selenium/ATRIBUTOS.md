Com certeza! Aqui está um resumo dos localizadores, ações e informações comuns do Selenium em formato de tabela:

---

## Elementos Comuns do Selenium WebDriver

| Categoria         | Tipo/Método              | Descrição                                                                  | Exemplo de Uso (Python)                                                    |
| :---------------- | :----------------------- | :------------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **Localizadores** | `By.ID`                  | Encontra um elemento pelo atributo `id`.                                   | `driver.find_element(By.ID, 'nomeUsuario')`                                |
|                   | `By.NAME`                | Encontra um elemento pelo atributo `name`.                                 | `driver.find_element(By.NAME, 'senha')`                                    |
|                   | `By.CLASS_NAME`          | Encontra um elemento pela classe CSS.                                      | `driver.find_element(By.CLASS_NAME, 'botaoPrimario')`                      |
|                   | `By.TAG_NAME`            | Encontra um elemento pela tag HTML (ex: `div`, `a`).                       | `driver.find_element(By.TAG_NAME, 'h1')`                                   |
|                   | `By.LINK_TEXT`           | Encontra um link pelo texto **exato** visível.                             | `driver.find_element(By.LINK_TEXT, 'Clique aqui')`                         |
|                   | `By.PARTIAL_LINK_TEXT`   | Encontra um link pelo texto **parcial** visível.                           | `driver.find_element(By.PARTIAL_LINK_TEXT, 'Clique')`                      |
|                   | `By.CSS_SELECTOR`        | Encontra elementos usando seletores CSS.                                   | `driver.find_element(By.CSS_SELECTOR, 'input[type="submit"].btn-success')` |
|                   | `By.XPATH`               | Encontra elementos através de um caminho na estrutura XML/HTML.            | `driver.find_element(By.XPATH, '//input[@id="campoEmail"]')`               |
| **Ações**         | `.click()`               | Clica no elemento.                                                         | `elemento.click()`                                                         |
|                   | `.send_keys('texto')`    | Digita texto em campos de entrada.                                         | `campo_texto.send_keys('meu_texto')`                                       |
|                   | `.clear()`               | Limpa o conteúdo de um campo de texto.                                     | `campo_texto.clear()`                                                      |
|                   | `.submit()`              | Envia um formulário.                                                       | `formulario.submit()`                                                      |
| **Informações**   | `.text`                  | Retorna o texto visível de um elemento.                                    | `texto_elemento = elemento.text`                                           |
|                   | `.get_attribute('attr')` | Retorna o valor de um atributo do elemento (ex: `href`, `value`).          | `valor_atributo = elemento.get_attribute('href')`                          |
|                   | `.is_displayed()`        | Verifica se o elemento está visível (`True`/`False`).                      | `visivel = elemento.is_displayed()`                                        |
|                   | `.is_enabled()`          | Verifica se o elemento está habilitado para interação (`True`/`False`).    | `habilitado = elemento.is_enabled()`                                       |
|                   | `.is_selected()`         | Verifica se o elemento (checkbox/radio) está selecionado (`True`/`False`). | `selecionado = elemento.is_selected()`                                     |
|                   | `.tag_name`              | Retorna o nome da tag HTML do elemento.                                    | `tag = elemento.tag_name`                                                  |

---

Espero que esta tabela ajude a visualizar e entender de forma mais clara os principais recursos do Selenium!
