#!/usr/bin/env python3
"""
Extract all pages from a PDF file into individual page images for processing.
Designed for the Orthodox Catechism project to convert the raw PDF into processable images.
"""
from __future__ import annotations
import argparse
import io
import os
import sys
from pathlib import Path
from typing import Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF is required. Install with: pip install PyMuPDF")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


def extract_pdf_pages(
    pdf_path: str,
    output_dir: str,
    image_format: str = "png",
    dpi: int = 300,
    verbose: bool = True
) -> bool:
    """
    Extract all pages from a PDF file into individual images.
    
    Args:
        pdf_path: Path to the input PDF file
        output_dir: Directory to save the extracted page images
        image_format: Output image format ('png' or 'jpeg')
        dpi: Resolution for the extracted images (default: 300 DPI for OCR)
        verbose: Whether to print progress information
        
    Returns:
        bool: True if extraction was successful, False otherwise
    """
    try:
        # Validate input file
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file not found: {pdf_path}")
            return False
        
        # Create output directory
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Open the PDF
        if verbose:
            print(f"Opening PDF: {pdf_path}")
        
        pdf_document = fitz.open(pdf_path)
        total_pages = len(pdf_document)
        
        if verbose:
            print(f"Found {total_pages} pages in the PDF")
            print(f"Extracting pages at {dpi} DPI to {output_dir}/")
        
        # Extract each page
        successful_extractions = 0
        
        for page_num in range(total_pages):
            try:
                # Get the page
                page = pdf_document[page_num]
                
                # Create a matrix for the desired DPI
                # fitz uses 72 DPI by default, so we scale accordingly
                zoom = dpi / 72.0
                matrix = fitz.Matrix(zoom, zoom)
                
                # Render page to pixmap
                pixmap = page.get_pixmap(matrix=matrix)
                
                # Generate output filename
                page_filename = f"page_{page_num + 1:03d}.{image_format.lower()}"
                output_path = os.path.join(output_dir, page_filename)
                
                # Save the image
                if image_format.lower() == "png":
                    pixmap.save(output_path)
                else:
                    # For JPEG, we need to convert via PIL to handle transparency
                    img_data = pixmap.tobytes("ppm")
                    img = Image.open(io.BytesIO(img_data))
                    if image_format.lower() == "jpeg":
                        # Convert RGBA to RGB for JPEG
                        if img.mode == "RGBA":
                            img = img.convert("RGB")
                    img.save(output_path, format=image_format.upper())
                
                successful_extractions += 1
                
                if verbose:
                    print(f"  Extracted page {page_num + 1}/{total_pages}: {page_filename}")
                
            except Exception as e:
                print(f"Error extracting page {page_num + 1}: {e}")
                continue
        
        # Close the PDF
        pdf_document.close()
        
        if verbose:
            print(f"\nExtraction complete!")
            print(f"Successfully extracted {successful_extractions}/{total_pages} pages")
            print(f"Images saved to: {output_dir}")
        
        return successful_extractions > 0
        
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return False


def main() -> None:
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(
        description="Extract PDF pages into individual images for processing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract all pages from the raw PDF (default behavior)
  python extract_pdf_pages.py
  
  # Specify custom input and output
  python extract_pdf_pages.py --input custom.pdf --output my_pages/
  
  # Extract as JPEG with lower resolution
  python extract_pdf_pages.py --format jpeg --dpi 150
  
  # Quiet mode (minimal output)
  python extract_pdf_pages.py --quiet
        """
    )
    
    parser.add_argument(
        "-i", "--input",
        default="../original/orthodox-catechism-raw.pdf",
        help="Path to input PDF file (default: ../original/orthodox-catechism-raw.pdf)"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="../pages",
        help="Output directory for extracted images (default: ../pages)"
    )
    
    parser.add_argument(
        "-f", "--format",
        choices=["png", "jpeg", "jpg"],
        default="png",
        help="Output image format (default: png)"
    )
    
    parser.add_argument(
        "-d", "--dpi",
        type=int,
        default=300,
        help="Resolution in DPI for extracted images (default: 300)"
    )
    
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress progress output"
    )
    
    args = parser.parse_args()
    
    # Normalize format
    image_format = "jpeg" if args.format == "jpg" else args.format
    
    # Convert relative paths to absolute paths based on script location
    script_dir = Path(__file__).parent
    input_path = Path(script_dir) / args.input
    output_path = Path(script_dir) / args.output
    
    # Validate DPI
    if args.dpi < 72 or args.dpi > 600:
        print("Warning: DPI should typically be between 72 and 600")
    
    if not args.quiet:
        print("Orthodox Catechism PDF Page Extractor")
        print("=" * 40)
        print(f"Input PDF: {input_path}")
        print(f"Output directory: {output_path}")
        print(f"Image format: {image_format.upper()}")
        print(f"Resolution: {args.dpi} DPI")
        print()
    
    # Extract the pages
    success = extract_pdf_pages(
        str(input_path),
        str(output_path),
        image_format,
        args.dpi,
        not args.quiet
    )
    
    if success:
        if not args.quiet:
            print("\n✓ PDF page extraction completed successfully!")
        sys.exit(0)
    else:
        print("\n✗ PDF page extraction failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
