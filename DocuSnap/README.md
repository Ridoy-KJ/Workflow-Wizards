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
