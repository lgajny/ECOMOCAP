# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 14:10:31 2026

@author: GAJNY
"""

from PIL import Image, ImageDraw

def mm_to_pixels(mm, dpi):
    return int((mm / 25.4) * dpi)

def generate_chessboard_pdf(
    rows,
    cols,
    square_size_mm,
    margin_mm=20,   # 2 cm = 20 mm
    dpi=300,
    output_file="chessboard.pdf"
):
    square_px = mm_to_pixels(square_size_mm, dpi)
    margin_px = mm_to_pixels(margin_mm, dpi)

    board_width = cols * square_px
    board_height = rows * square_px

    width = board_width + 2 * margin_px
    height = board_height + 2 * margin_px

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for row in range(rows):
        for col in range(cols):
            color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)

            x0 = margin_px + col * square_px
            y0 = margin_px + row * square_px
            x1 = x0 + square_px
            y1 = y0 + square_px

            draw.rectangle([x0, y0, x1, y1], fill=color)

    image.save(output_file, "PDF", resolution=dpi)

    print(f"Saved {output_file}")
    print(f"Square size: {square_size_mm} mm")
    print(f"Margin: {margin_mm} mm")
    print(f"DPI: {dpi}")


# Example
generate_chessboard_pdf(rows=14, cols=9, square_size_mm=40, margin_mm=20, dpi=300)
