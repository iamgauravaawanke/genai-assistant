from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunks_split(docs):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0
    )
    
    texts = text_splitter.split_text(docs)
    return texts

    
    


