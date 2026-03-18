import os
from docx2pdf import convert
from pdf2image import convert_from_path

def convert_all_to_jpg_no_watermark():
    # --- YOUR POPPLER PATH ---
    POPPLER_PATH = r"C:\poppler-25.12.0\Library\bin" 
    # -------------------------

    current_dir = os.getcwd()
    
    # Get all .docx files in the current folder (excluding temp Word files starting with ~)
    files = [f for f in os.listdir(current_dir) if f.lower().endswith(".docx") and not f.startswith("~")]

    if not files:
        print("No .docx files found in this folder!")
        return

    for file_name in files:
        # Get filename without extension (e.g., "Meeting_Notes")
        name_only = os.path.splitext(file_name)[0]
        
        # Create folder: "Meeting_Notes_conv"
        output_dir = os.path.join(current_dir, f"{name_only}_conv")
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Step 1: Convert DOCX to a temporary PDF (Watermark-free via MS Word)
        temp_pdf = f"{name_only}_temp.pdf"
        print(f"\n[1/3] Converting to PDF: {file_name}")
        try:
            # Note: This requires MS Word to be installed on your Windows machine
            convert(file_name, temp_pdf)
        except Exception as e:
            print(f"Error converting {file_name}: {e}")
            continue

        # Step 2: Convert PDF pages to JPGs using Poppler
        print(f"[2/3] Rendering pages to high-quality JPG...")
        try:
            images = convert_from_path(temp_pdf, dpi=300, poppler_path=POPPLER_PATH)
            
            # Step 3: Save images with consecutive naming
            print(f"[3/3] Saving images to folder: {name_only}_conv")
            for i, image in enumerate(images):
                # Names: page_1.jpg, page_2.jpg, etc.
                image_filename = f"page_{i + 1}.jpg"
                output_path = os.path.join(output_dir, image_filename)
                image.save(output_path, "JPEG", quality=95)
                print(f"  -> Saved {image_filename}")

        except Exception as e:
            print(f"Error during image generation: {e}")
        
        finally:
            # Clean up the temporary PDF file to keep your folder tidy
            if os.path.exists(temp_pdf):
                os.remove(temp_pdf)

    print("\nAll tasks finished! Check your folders.")

if __name__ == "__main__":
    convert_all_to_jpg_no_watermark()
