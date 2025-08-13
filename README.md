# Unstructured_text_cleaning

# Capabilities 
This script is a powerful tool designed to extract, clean, and structure text from various document types. Its main capabilities are:

**Multi-Format File Processing**: It can read and extract raw text from four different file formats: PDF (.pdf), Microsoft Word (.docx), Plain Text (.txt), and HTML (.html).

**Intelligent Content Cleaning**: The script automatically detects whether the input content is HTML or plain text.

For HTML, it intelligently strips away common "boilerplate" like navigation bars, headers, footers, scripts, and styles to isolate the main content.

For all text, it removes a customizable list of noise keywords, extra whitespace, and non-essential characters.

**Language Filtering**: It processes the cleaned text to identify and keep only the chunks that are written in English.

**Meaningful Chunking**: It uses a Recursive Character Splitting method to break down the final text into well-sized, semantically relevant chunks, which is ideal for feeding into language models or for analysis.

**File Output**: After processing, it saves the clean, chunked text into a new file named [original_filename]_output.txt for easy access.

# Core Logic Engine 
The script operates through a clear, step-by-step pipeline:

**File Input & Text Extraction**: The process starts in the main() function, which prompts for a file path. The extract_text_from_file() function is then called to identify the file's extension and use the appropriate library (pdfplumber for PDF, python-docx for Word) to read the document and convert its entire content into a single block of raw text.

**Unified Cleaning**(clean_content): This is the central "engine" of the script. All the raw text is passed to this single, smart function.

**Pipeline Detection**: The function first performs a quick check on the text to see if it contains common HTML tags (like <div> or <html>).

**HTML Path**: If tags are found, it uses the BeautifulSoup library to parse the text, surgically remove the unwanted HTML elements (like <nav> and <script>), and extract the core content.

**Plain Text Path**: If no tags are found, it skips the HTML parsing entirely and uses the raw text directly. This is the path taken for PDF, DOCX, and TXT files.

**Recursive Splitting**: Once a clean block of text is obtained (from either path), it's passed to the recursive_character_split() function. This function intelligently breaks the text into smaller chunks of a consistent size, trying to make the splits at natural boundaries like paragraphs or sentences.

Final Filtering & Output: Each of these chunks goes through a final filtering process (_filter_and_clean_chunks()) to remove noise words and ensure it's in English. The resulting clean chunks are then printed to the console and saved to the output file.

