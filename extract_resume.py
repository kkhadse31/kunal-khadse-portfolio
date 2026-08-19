from pypdf import PdfReader

pdf_path = r'C:\Users\kunalkhadse\OneDrive - Microsoft\Documents\New folder\Kunal_Khadse_CV.pdf'
reader = PdfReader(pdf_path)
print('TOTAL_PAGES', len(reader.pages))
text_parts = []
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ''
    text_parts.append(f'--- PAGE {i} ---\n{text}')
full_text = '\n'.join(text_parts)
print(full_text[:40000])
