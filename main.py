import os
import docx
import pdfplumber
from cleaner import clean_content

def extract_text_from_file(file_path: str) -> str:
    """Detects the file type and extracts raw text content."""
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()
    text = ""
    print(f"📄 Reading file with extension: {file_extension}")

    if file_extension == '.pdf':
        with pdfplumber.open(file_path) as pdf:
            all_pages_text = [page.extract_text() for page in pdf.pages if page.extract_text()]
            text = "\n".join(all_pages_text)
    
    elif file_extension == '.docx':
        doc = docx.Document(file_path)
        all_paras_text = [para.text for para in doc.paragraphs if para.text]
        text = "\n".join(all_paras_text)
        
    elif file_extension in ['.txt', '.html']:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
    else:
        print(f"❌ Error: Unsupported file type '{file_extension}'.")
        print("This tool currently supports .pdf, .docx, .txt, and .html files.")

    return text

def main():
    """Main function to handle file input, processing, and output."""
    file_path = input("Enter the path to your file (.pdf, .docx, .html, or .txt): ")

    if not os.path.exists(file_path):
        print(f"❌ Error: The file '{file_path}' was not found.")
        return

    try:
        raw_content = extract_text_from_file(file_path)
        
        if not raw_content.strip():
            print("Could not extract any text, or the file is empty.")
            return
            
        # --- MODIFIED: A single call to the unified cleaning function ---
        final_chunks = clean_content(raw_content)
        
        print("\n✅ Successfully cleaned text. Here are the English-only chunks:")
        print("---")
        
        if final_chunks:
            for i, chunk in enumerate(final_chunks, 1):
                print(f"Chunk {i}: {chunk}")

            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_filename = f"{base_name}_output.txt"

            with open(output_filename, 'w', encoding='utf-8') as f_out:
                for chunk in final_chunks:
                    f_out.write(f"{chunk}\n\n")
            
            print("\n---")
            print(f"💾 Output successfully saved to: {output_filename}")
            
        else:
            print("No valid English content was found after processing.")

    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")

if __name__ == "__main__":
    main()
