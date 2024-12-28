from pdf_processor import extract_text_from_pdf, get_pdf_metadata

def test_pdf_extraction():
    # Path to the PDF file in test-case directory
    pdf_path = "test_cases/example.pdf"

    try:
        # Extract text
        print("Extracting text from PDF...")
        text = extract_text_from_pdf(pdf_path)
        print("\nExtracted Text:")
        print("-" * 50)
        print(text)
        print("-" * 50)
        
        # Get metadata
        print("\nExtracting metadata...")
        metadata = get_pdf_metadata(pdf_path)
        print("\nMetadata:")
        print("-" * 50)
        for key, value in metadata.items():
            print(f"{key}: {value}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_pdf_extraction() 