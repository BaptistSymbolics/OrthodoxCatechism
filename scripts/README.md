# Orthodox Catechism Scripts

This directory contains utility scripts for processing the Orthodox Catechism project.

## extract_pdf_pages.py

A Python script that extracts all pages from the raw PDF file into individual page images for further processing.

### Features

- **High-quality extraction**: 300 DPI by default (suitable for OCR processing)
- **Flexible output formats**: PNG (default) or JPEG
- **Configurable resolution**: Adjustable DPI settings
- **Progress tracking**: Real-time extraction progress
- **Error handling**: Graceful handling of corrupted pages
- **Automatic directory creation**: Creates output directory if needed

### Requirements

Install the required dependencies:

```bash
pip install -r ../requirements.txt
```

Required packages:
- `PyMuPDF>=1.23.0` - For PDF processing
- `Pillow>=9.0.0` - For image handling

### Usage

#### Basic Usage

Extract all pages from the raw PDF to the `pages/` directory:

```bash
cd scripts/
python extract_pdf_pages.py
```

This will:
- Process `../original/orthodox-catechism-raw.pdf`
- Create individual PNG files in `../pages/`
- Use 300 DPI resolution
- Show progress information

#### Advanced Usage

```bash
# Custom input and output paths
python extract_pdf_pages.py --input /path/to/custom.pdf --output /path/to/output/

# Different image format and resolution
python extract_pdf_pages.py --format jpeg --dpi 150

# Quiet mode (minimal output)
python extract_pdf_pages.py --quiet

# High resolution for detailed processing
python extract_pdf_pages.py --dpi 600
```

#### Command Line Options

- `-i, --input`: Input PDF file path (default: `../original/orthodox-catechism-raw.pdf`)
- `-o, --output`: Output directory for images (default: `../pages`)
- `-f, --format`: Image format - `png`, `jpeg`, or `jpg` (default: `png`)
- `-d, --dpi`: Resolution in DPI (default: `300`)
- `-q, --quiet`: Suppress progress output
- `-h, --help`: Show help message

### Output

The script creates numbered image files:
- `page_001.png` - First page
- `page_002.png` - Second page
- `page_003.png` - Third page
- ... and so on

### Example Output

```
Orthodox Catechism PDF Page Extractor
========================================
Input PDF: /path/to/orthodox-catechism-raw.pdf
Output directory: /path/to/pages
Image format: PNG
Resolution: 300 DPI

Opening PDF: /path/to/orthodox-catechism-raw.pdf
Found 99 pages in the PDF
Extracting pages at 300 DPI to /path/to/pages/
  Extracted page 1/99: page_001.png
  Extracted page 2/99: page_002.png
  ...
  Extracted page 99/99: page_099.png

Extraction complete!
Successfully extracted 99/99 pages
Images saved to: /path/to/pages

✓ PDF page extraction completed successfully!
```

### File Information

For the Orthodox Catechism raw PDF:
- **Total pages**: 99
- **Image dimensions**: ~1864 x 3190 pixels (at 300 DPI)
- **File format**: PNG (8-bit RGB)
- **Total output size**: ~401MB for all pages
- **Average file size**: ~4MB per page

### Integration with Project Workflow

This script is designed to work seamlessly with the existing Orthodox Catechism project:

1. **Input**: Uses the `original/orthodox-catechism-raw.pdf` file
2. **Output**: Creates a `pages/` directory with individual page images
3. **Processing**: Images can be used for OCR, manual review, or other processing tasks
4. **Quality**: 300 DPI resolution provides excellent quality for text recognition

### Troubleshooting

#### Common Issues

1. **Missing dependencies**: Install with `pip install -r ../requirements.txt`
2. **Permission errors**: Ensure write access to the output directory
3. **Memory issues**: For very large PDFs, consider using lower DPI settings
4. **Corrupted pages**: The script will skip corrupted pages and continue

#### Error Messages

- `Error: PDF file not found`: Check the input file path
- `Error: PyMuPDF is required`: Install PyMuPDF with `pip install PyMuPDF`
- `Error: Pillow is required`: Install Pillow with `pip install Pillow`

### Performance Notes

- **Processing time**: ~2-3 minutes for 99 pages on modern hardware
- **Memory usage**: Moderate (processes one page at a time)
- **Disk space**: ~4MB per page at 300 DPI
- **CPU usage**: Moderate during processing

## Other Scripts

### toml_to_latex.py

Converts TOML catechism files to LaTeX format for PDF generation. See the main project documentation for usage details.
