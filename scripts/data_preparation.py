#!/usr/bin/env python3
"""
Script de preparação de dados: converte PDFs em imagens.

Este script:
1. Lê todos os PDFs de uma pasta de entrada
2. Converte cada PDF em imagens (uma por página)
3. Cria uma pasta para cada PDF com nome normalizado
4. Salva as imagens na pasta correspondente
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List

try:
    from pdf2image import convert_from_path
except ImportError:
    print("ERRO: pdf2image não está instalado.")
    print("Instale com: pip install pdf2image")
    print("No macOS, também é necessário: brew install poppler")
    sys.exit(1)


def normalize_filename(filename: str) -> str:
    """
    Normaliza o nome do arquivo removendo espaços e caracteres especiais.
    
    Args:
        filename: Nome do arquivo original
        
    Returns:
        Nome normalizado com espaços substituídos por underscores
    """
    # Remove extensão
    name = Path(filename).stem
    
    # Substitui espaços por underscores
    name = name.replace(" ", "_")
    
    # Remove caracteres especiais, mantendo apenas letras, números, underscores e hífens
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    
    # Remove underscores múltiplos
    name = re.sub(r'_+', '_', name)
    
    # Remove underscores no início e fim
    name = name.strip('_')
    
    return name


def convert_pdf_to_images(
    pdf_path: Path,
    output_dir: Path,
    dpi: int = 200,
    fmt: str = "jpg"
) -> List[Path]:
    """
    Converte um PDF em imagens (uma por página).
    
    Args:
        pdf_path: Caminho para o arquivo PDF
        output_dir: Diretório onde salvar as imagens
        dpi: Resolução das imagens (padrão: 200)
        fmt: Formato das imagens ('jpg' ou 'png', padrão: 'jpg')
        
    Returns:
        Lista de caminhos das imagens criadas
    """
    print(f"  Convertendo {pdf_path.name}...")
    
    try:
        # Converte PDF em imagens
        images = convert_from_path(
            pdf_path,
            dpi=dpi,
            fmt=fmt,
            output_folder=None,  # Retorna objetos PIL Image
            thread_count=4  # Paraleliza conversão
        )
        
        # Cria diretório de saída se não existir
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Salva cada página como imagem
        image_paths = []
        for i, image in enumerate(images, start=1):
            image_filename = f"{output_dir.name}_page-{i:04d}.{fmt}"
            image_path = output_dir / image_filename
            image.save(image_path, fmt.upper())
            image_paths.append(image_path)
        
        print(f"  ✓ {len(image_paths)} páginas convertidas")
        return image_paths
        
    except Exception as e:
        print(f"  ✗ Erro ao converter {pdf_path.name}: {e}")
        return []


def process_pdfs(
    input_dir: Path,
    output_base_dir: Path,
    dpi: int = 200,
    fmt: str = "jpg"
) -> dict:
    """
    Processa todos os PDFs de um diretório.
    
    Args:
        input_dir: Diretório contendo os PDFs
        output_base_dir: Diretório base onde criar as pastas de saída
        dpi: Resolução das imagens
        fmt: Formato das imagens
        
    Returns:
        Dicionário com estatísticas do processamento
    """
    # Encontra todos os PDFs
    pdf_files = list(input_dir.glob("*.pdf"))
    
    if not pdf_files:
        print(f"Nenhum PDF encontrado em {input_dir}")
        return {
            "total_pdfs": 0,
            "successful": 0,
            "failed": 0,
            "total_pages": 0
        }
    
    print(f"\nEncontrados {len(pdf_files)} arquivo(s) PDF\n")
    
    # Cria diretório base de saída se não existir
    output_base_dir.mkdir(parents=True, exist_ok=True)
    
    stats = {
        "total_pdfs": len(pdf_files),
        "successful": 0,
        "failed": 0,
        "total_pages": 0
    }
    
    # Processa cada PDF
    for pdf_path in pdf_files:
        # Normaliza nome do arquivo
        normalized_name = normalize_filename(pdf_path.name)
        
        # Cria diretório de saída para este PDF
        pdf_output_dir = output_base_dir / normalized_name
        
        print(f"Processando: {pdf_path.name}")
        print(f"  Pasta de saída: {pdf_output_dir.name}")
        
        # Converte PDF em imagens
        image_paths = convert_pdf_to_images(
            pdf_path,
            pdf_output_dir,
            dpi=dpi,
            fmt=fmt
        )
        
        if image_paths:
            stats["successful"] += 1
            stats["total_pages"] += len(image_paths)
        else:
            stats["failed"] += 1
        
        print()
    
    return stats


def main():
    """Função principal do script."""
    parser = argparse.ArgumentParser(
        description="Converte PDFs em imagens para preparação de dados"
    )
    parser.add_argument(
        "--input-dir",
        type=str,
        default="data/pdfs",
        help="Diretório contendo os PDFs (padrão: data/pdfs)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="data/images",
        help="Diretório base para salvar as imagens (padrão: data/images)"
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=200,
        help="Resolução das imagens em DPI (padrão: 200)"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["jpg", "png"],
        default="jpg",
        help="Formato das imagens: jpg ou png (padrão: jpg)"
    )
    
    args = parser.parse_args()
    
    # Converte strings em Path objects
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    
    # Valida diretório de entrada
    if not input_dir.exists():
        print(f"ERRO: Diretório de entrada não existe: {input_dir}")
        print(f"Crie o diretório e adicione PDFs nele.")
        sys.exit(1)
    
    if not input_dir.is_dir():
        print(f"ERRO: Caminho não é um diretório: {input_dir}")
        sys.exit(1)
    
    # Processa PDFs
    print("=" * 60)
    print("PREPARAÇÃO DE DADOS: PDF → Imagens")
    print("=" * 60)
    print(f"Diretório de entrada: {input_dir.absolute()}")
    print(f"Diretório de saída: {output_dir.absolute()}")
    print(f"DPI: {args.dpi}")
    print(f"Formato: {args.format.upper()}")
    print("=" * 60)
    
    stats = process_pdfs(
        input_dir,
        output_dir,
        dpi=args.dpi,
        fmt=args.format
    )
    
    # Exibe estatísticas finais
    print("=" * 60)
    print("RESUMO DO PROCESSAMENTO")
    print("=" * 60)
    print(f"Total de PDFs: {stats['total_pdfs']}")
    print(f"Convertidos com sucesso: {stats['successful']}")
    print(f"Falhas: {stats['failed']}")
    print(f"Total de páginas processadas: {stats['total_pages']}")
    print("=" * 60)
    
    if stats["failed"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()

