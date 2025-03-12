import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas

def svgs_to_pdf(folder_path, output_pdf='output.pdf'):
    # List and sort SVG files
    svg_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.svg')])
    if not svg_files:
        print("No SVG files found in the folder!")
        return

    # Create a PDF canvas
    c = canvas.Canvas(output_pdf)
    
    # Set page size based on your manifest (533x723 pixels)
    width, height = 533, 723  # Adjust if needed
    
    for svg_file in svg_files:
        svg_path = os.path.join(folder_path, svg_file)
        print(f'Converting {svg_file} to PDF page...')
        
        # Convert SVG to ReportLab drawing
        drawing = svg2rlg(svg_path)
        if drawing:
            # Scale to fit page if necessary (optional)
            drawing.width, drawing.height = width, height
            # Add to PDF
            renderPDF.draw(drawing, c, 0, 0)
            c.showPage()  # New page for each SVG
        else:
            print(f'Failed to process {svg_file}')

    # Save the PDF
    c.save()
    print(f'Merged {len(svg_files)} pages into {output_pdf}')

if __name__ == '__main__':
    folder_path = '/Users/robertopineda/Downloads/korean_book'  # Adjust to your SVG folder
    svgs_to_pdf(folder_path, 'korean_book.pdf')