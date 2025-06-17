from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=100,
    separators=["\n\n", "\n"],
)

markdown_path = "output_test/income_tax.md"
text_path = "output_test/income_tax.txt"
# loader = UnstructuredMarkdownLoader(markdown_path)

# document_list = loader.load_and_split(text_splitter)

loader = TextLoader(text_path)

document_list = loader.load_and_split(text_splitter)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma.from_documents(
    documents=document_list,
    embedding=embeddings,
    collection_name="income_tax_collection",
    persist_directory="income_tax_collection",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})
