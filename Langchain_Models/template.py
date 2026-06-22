import os

# ==========================
# Folder Structure
# ==========================

folders = [
    "1.LLMs",
    "2.ChatModels",
    "3.EmbeddingModels"
]

# ==========================
# Files Structure
# ==========================

files = [
    # 1.LLMs
    "1.LLMs/1_llm_demo.py",

    # 2.ChatModels
    "2.ChatModels/1_chatmodel_openai.py",
    "2.ChatModels/2_chatmodel_anthropic.py",
    "2.ChatModels/3_chatmodel_google.py",
    "2.ChatModels/4_chatmodel_hf_api.py",
    "2.ChatModels/5_chatmodel_hf_local.py",

    # 3.EmbeddingModels
    "3.EmbeddingModels/1_embedding_openai_query.py",
    "3.EmbeddingModels/2_embedding_openai_docs.py",
    "3.EmbeddingModels/3_embedding_hf_local.py",
    "3.EmbeddingModels/4_document_similarity.py",

    # Root Files
    ".gitignore",
    "requirements.txt",
    "test.py"
]

# ==========================
# Create Folders
# ==========================

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# ==========================
# Create Files
# ==========================

for file in files:
    with open(file, "w") as f:
        pass

print("✅ Project structure created successfully!")