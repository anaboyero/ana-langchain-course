
from dotenv import load_dotenv
load_dotenv()
import os 
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
'''from langchain.agents import create_agent
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
'''

def main():
    print("Hello from langchain-ana!")
    print(os.environ["MY_TEST_API_KEY"])
    information="""
José Luis de Castro Zahera (Santiago de Compostela, 23 de mayo de 1966), más conocido como Luis Zahera, es un actor español, ganador de dos premios Goya al mejor actor de reparto por sus interpretaciones en El reino (2018) y As bestas (2022). Distinguido por la Medalla de Oro al Mérito en las Bellas Artes 2023. [1]​

Biografía: Saltó a la fama en Galicia por su papel de Petróleo en la serie de la TVG, Mareas vivas. Previamente, hizo su debut en el cine con la película Divinas palabras (1987), de José Luis García Sánchez. En sus primeros años, también tuvo participaciones destacadas en otros programas locales como Luar o Land Rober.[2]​

Su primer papel importante en una ficción nacional le llegó con Sin tetas no hay paraíso (2008) en su primera y segunda temporada, donde interpretó a uno de los antagonistas Ramón Vega.[3]​ En esos años participó en películas como Celda 211 (2009), La playa de los ahogados (2015), A cambio de nada (2015) o Que Dios nos perdone (2016).

Con su interpretación de Cabrera en El reino (2018) del director Rodrigo Sorogoyen obtuvo su primer galardón en los premios Goya como mejor interpretación masculina de reparto.[4]​ Ese mismo año protagonizó la serie Vivir sin permiso en Telecinco como Antonio Yáñez Ferreiro en la que se mantuvo en sus dos temporadas.[5]​

Sus siguientes incursiones en el cine fueron con las cintas Mientras dure la guerra (2019), de Alejandro Amenábar, donde interpretó a Atilano Coco; Loco por ella (2021) de Dani de la Orden donde hace de un paciente de un psiquiátrico con esquizofrenia llamado Saúl; y en la película original de Netflix Xtremo (2021). En 2022 comenzó a interpretar a Ezequiel Fandiño en Entrevías, en la que se mantuvo durante sus cuatro temporadas con un personaje principal.[6]​

En 2022 obtuvo diversos reconocimientos y elogios gracias a su papel de Xan Anta en As bestas, tales como premiaciones en los Fotogramas de Plata, en las Medallas del Círculo de Escritores Cinematográficos, en la Unión de Actores y Actrices, en los Premios Feroz y por segunda vez en los Premios Goya, en todos los casos como mejor actor de reparto. Por todos estos trabajos, recibió la Medalla de Oro al Mérito en las Bellas Artes en 2023.[7]​

Ha tenido también un papel destacado en la miniserie de Disney+ La última a finales de 2022, así como en las películas Infiesto (2023) de Netflix, Awareness (2023), una película de acción de Amazon Prime Video o en las cinematográficas Pájaros (2024) de Pau Durà, El correo de Daniel Calparsoro y la serie de Netflix Animal (2025), donde interpreta a un veterinario rural de Galicia llamado Antón, que ha supuesto su primera papel protagonista en una serie.

""" 

    summary_template = """

    Given the information {information} about a person, i want you to create:

    1. A short summary of no more than 50 words.
    2. A list of 5 relevant tags that describe the person.
    3. An interesting fact about the person.
    """

    summary_prompt_template = PromptTemplate(input_variables=[information], template=summary_template)
    
    #llm = ChatOllama(model="gpt-oss:latest", temperature=0)
    llm = ChatOpenAI()

    chain = summary_prompt_template | llm 

    response = chain.invoke(input={"information":information})

    print(response.content)



if __name__ == "__main__":
    main()