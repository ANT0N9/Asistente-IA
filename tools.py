from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M%S")
    formatted_text = f"--- Research Output ---\nTimestamp {timestamp}\n\n{data}\n\n"
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
        
    return f"Datos guardados en {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Guarda la información investigada en un archivo de texto para referencia futura. Toma una cadena de texto como entrada y devuelve una confirmación de guardado.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Busqueda en la web para obtener información actualizada sobre un tema específico.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)