# Pasta de PDFs

Coloque aqui os arquivos PDF que deseja converter em imagens.

O script `data-preparation` irá:
1. Ler todos os PDFs desta pasta
2. Converter cada página em uma imagem
3. Criar uma pasta para cada PDF em `../images/` com o nome normalizado do arquivo

## Exemplo

Se você colocar um arquivo chamado `TERMO CONVENIO 169-2022.pdf` aqui, o script criará:
- `../images/TERMO_CONVENIO_169-2022/TERMO_CONVENIO_169-2022_page-0001.jpg`
- `../images/TERMO_CONVENIO_169-2022/TERMO_CONVENIO_169-2022_page-0002.jpg`
- etc.

## Uso

```bash
# Coloque seus PDFs nesta pasta
cp /caminho/para/seu/arquivo.pdf data/pdfs/

# Execute o script
make data-preparation
```

