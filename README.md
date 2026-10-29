# Bianca Morandi — prévia de website

Demonstração independente desenvolvida por Alan Rodrigues. Inclui a versão com fonte Manrope, biblioteca interativa, galeria de vídeos e Radar Criminal com notícias oficiais do STJ.

## Publicar no GitHub Pages

1. Extraia este ZIP.
2. Crie um repositório no GitHub com a branch `main`.
3. Envie o conteúdo extraído, mantendo `index.html`, `assets`, `scripts` e `.github` na raiz. Não envie apenas o ZIP.
4. Em **Settings → Pages → Build and deployment → Source**, selecione **GitHub Actions**.
5. Na aba **Actions**, abra **Publicar site e atualizar notícias** e clique em **Run workflow**. Caso necessário, habilite Actions para o repositório.
6. Aguarde o fluxo concluir. O endereço aparece em **Settings → Pages**.

**A pasta `.github` precisa ser enviada.** Ela pode ficar oculta no explorador. O GitHub Desktop ou o Git permitem enviar a estrutura completa. Pelo navegador, confira se o arquivo `.github/workflows/pages.yml` aparece no repositório; se não aparecer, crie-o com **Add file → Create new file** e copie o conteúdo fornecido.

Se a branch tiver outro nome, ajuste `branches: [main]` no workflow.

## Notícias automáticas

O workflow consulta o RSS oficial do STJ a cada hora e publica uma nova versão com até 12 títulos da área criminal. O site mostra até seis resultados por filtro, com data, fonte e link original, sem comentários da advogada.

O agendamento depende do GitHub Actions e pode sofrer atrasos. Se o RSS estiver indisponível, o site mantém a seleção incluída no pacote e mostra a data dessa seleção. O agendamento de repositórios públicos pode ser desativado pelo GitHub após longos períodos sem atividade; reative na aba Actions quando necessário.

Não é necessário configurar chave, senha ou serviço pago de notícias. A disponibilidade do Pages e os limites de Actions dependem do plano e das configurações da conta. Este pacote não configura cobrança ou contratação.

**Importante:** publicar somente pela opção `Deploy from a branch` exibirá a seleção incluída no ZIP, mas não executará o fluxo de atualização automática fornecido aqui.

## Editar

- `index.html`: textos, visual e interações.
- `assets/`: fotos, capas dos Reels e fontes locais.
- `scripts/update_news.py`: consulta e filtragem do RSS.
- `.github/workflows/pages.yml`: publicação e agendamento.

Os vídeos abrem os Reels originais no Instagram; não há arquivos de vídeo hospedados neste pacote. Não inclui painel administrativo, formulário com recebimento de dados ou agenda de consultas.

Para conferir localmente, execute `python -m http.server 8000` na pasta e abra `http://localhost:8000`. Isso também permite carregar o arquivo JSON das notícias. Abrir por duplo clique pode impedir a leitura do JSON por restrições do navegador.

## Antes de usar como site oficial

A advogada deve validar os textos, a identificação profissional e sua inscrição na OAB. As imagens e os vídeos são do perfil @biancamorandi.advogada. As notícias pertencem ao STJ e são acessadas na fonte original.

O site está identificado como demonstração independente. Nenhuma credencial ou configuração privada da hospedagem da prévia está incluída.
