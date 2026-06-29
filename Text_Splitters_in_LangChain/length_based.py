from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Path check kar lein ki file isi folder me ho, nahi toh full path 'r' ke sath dein
loader = PyPDFLoader('C:/-Generative-AI-using-LangChain/books/unsupervised_learning.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator="\n" 
)

result = splitter.split_documents(docs)

print(f"Total Chunks: {len(result)}")

if len(result) > 1:
    print("\n--- Chunk 2 Content ---")
    print(result[1].page_content)
