# 📸 DocuSnap: Batch DOCX to JPG Converter

A privacy-focused, ad-free Python utility to convert Word documents into high-quality, page-by-page JPEG images.

## 🚀 Why DocuSnap?
Most online converters are slow, filled with ads, and pose a privacy risk to your documents. **DocuSnap** runs locally on your machine, handles bulk files, and preserves perfect formatting by leveraging the Microsoft Word rendering engine.

## ✨ Features
- **Zero Watermarks:** Completely clean output.
- **Auto-Organization:** Creates a unique `_conv` folder for every document.
- **Consecutive Naming:** Outputs `page_1.jpg`, `page_2.jpg`, etc.
- **High Resolution:** Default 300 DPI for professional-grade clarity.

## 🛠️ Prerequisites
1. **Microsoft Word:** Installed on Windows.
2. **Poppler:** Download [here](https://github.com) and extract to `C:\poppler-25.12.0\`.

## ⚙️ Installation
```bash
pip install -r requirements.txt



## 🚀 How to Use (Everyday Guide)

1. **Prepare your files**  
   Place the Word documents (`.docx`) you want to convert into the same folder as `docusnap.py`.

2. **Run the script**  
   - Open **PowerShell** or **CMD** in that folder.  
   - Type:  
     ```bash
     python docusnap.py
     ```  
   - Press **Enter**.

3. **Find your images**  
   - If your file was `Report.docx`, a new folder named `Report_conv` will appear.  
   - Inside, you'll find:  
     ```
     page_1.jpg
     page_2.jpg
     ...
     ```

---

## 📝 Important Notes

- **Close Word**: Make sure the document isn’t open in Microsoft Word while the script is running.  
- **Windows only**: This version is optimized for Windows users with Microsoft Word installed.  
- **Quality**: Images are set to **300 DPI** by default for professional clarity.  

---

## 📌 Example Workflow

```bash
# Place Report.docx in the same folder as docusnap.py
python docusnap.py

# Output:
# A folder named Report_conv with page_1.jpg, page_2.jpg, etc.
