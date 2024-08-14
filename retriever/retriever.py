class Retriever:
    def __init__(self, vector_store, api_key):
        self.vector_store = vector_store
        self.api_key = api_key
        self.embed_model = None
        self.vector_index = None
        self.retriever = None

    def load_vector_index(self, vector_index_path):
        if os.path.exists(vector_index_path):
            self.vector_index = FAISS.load_local(vector_index_path)
        else:
            raise FileNotFoundError(f"Vector index file not found: {vector_index_path}")

    def create_vector_index(self, documents):
        self.embed_model = OpenAIEmbeddings(api_key=self.api_key, model='text-embedding-3-small')
        self.vector_index = FAISS.from_documents(documents, self.embed_model)
        self.retriever = self.vector_index.as_retriever(search_type="mmr", search_kwargs={"k": 3})

    def save_vector_index(self, vector_index_path):
        self.vector_index.save_local(vector_index_path)

    def get_relevant_documents(self, query):
        result = self.retriever.get_relevant_documents(query)
        return result

    def run(self):
        # 여기에 필요한 코드를 작성하세요.
        # 예를 들어, 벡터 인덱스를 생성하거나 로드하고, 관련 문서를 검색하는 코드를 작성할 수 있습니다.
        pass