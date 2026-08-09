import os
from docx2pdf import convert

def convert_word_to_pdf(input_path, output_path=None):
    """
    Mengonversi file Word (.docx) ke PDF.
    Jika output_path tidak ditentukan, file akan disimpan di folder yang sama dengan nama yang sama.
    """
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' tidak ditemukan.")
        return

    print(f"Mengonversi '{input_path}' ke PDF...")

    # Fungsi convert dari docx2pdf menangani konversi
    convert(input_path, output_path)

    print("Konversi selesai!")

if __name__ == "__main__":
    # Contoh penggunaan
    # Pastikan Anda memiliki file .docx di direktori yang sama
    input_file = "dokumen_contoh.docx"

    if os.path.exists(input_file):
        convert_word_to_pdf(input_file)
    else:
        print(f"Harap sediakan file bernama '{input_file}' untuk pengujian.")
      
