# Caso 1 🧾 - Automatizando posts a partir do Obsidian

Certa noite me veio um pensamento:  
**"E se eu quiser criar um blog com meus textos do Obsidian?"**

Como o Obsidian salva tudo em arquivos `.md`, pensei em usar o [Astro](https://astro.build/) pra montar esse blog, já que ele suporta Markdown direto como post.

Mas aí bateu a dúvida:  
**Como saber a data em que cada texto foi criado?**

Foi aí que criei esse script pra me ajudar 🥸

---

## 🔧 O que o script faz:

1. Pega o nome do arquivo e remove a extensão `.md`
2. Faz um backup do arquivo original
3. Pega a data de criação do arquivo (pelo sistema)
4. Gera um novo nome combinando a data com o nome original
5. Copia o arquivo para uma pasta chamada `posts/`

---

## 💡 Exemplo:

Se você tiver um arquivo:

`caso-1/Arquivo_de_Teste.md`

Ele vai gerar:

`caso-1/backup/Arquivo_de_Teste.md`

`caso-1/posts/2025-05-29-Arquivo_de_Teste.md`

<strong>PS</strong>:. Eu deveria realizar mais commits 😥