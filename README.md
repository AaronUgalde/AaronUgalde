<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg">
  <img alt="Aarón Ugalde. A transit line through ESCOM, the algorithms club, four hackathons and Udemy, with the next stop still open." src="./assets/header-light.svg" width="100%">
</picture>

<p align="center"><samp>
  <a href="https://portafoliohuron.netlify.app/">portfolio</a> ·
  <a href="https://www.linkedin.com/in/ugalde-tellez-aaron-b76567353">linkedin</a> ·
  <a href="mailto:aaronugaldet@gmail.com">aaronugaldet@gmail.com</a>
</samp></p>

Hi, I'm Aarón. I study AI Engineering at IPN–ESCOM in Mexico City, and most of what I build
ends up being the unglamorous middle of a system: the API, the schema, the pipeline that runs
every night, the evaluation that tells you whether the model actually got better.

This summer I interned on the Skills & Learning data science team at **Udemy**. I worked on
deduplicating a ~17,000-node skills taxonomy (bi-encoder retrieval, a fine-tuned cross-encoder,
Louvain clustering, then an LLM pass to merge and re-parent), built a two-judge LLM evaluation
with golden sets that showed a 16% precision gain over the old mapping, and moved the batch job
into Airflow so it runs over 85,000+ learning activities without anyone babysitting it.

Outside of that I compete in ICPC and teach at ESCOM's algorithms club and its AI club, GAIA.
I'm open to relocating.

### Things I've built

**[MetroAR-CDMX](https://github.com/AaronUgalde/MetroAR-CDMX)** · Kotlin, Jetpack Compose<br>
Point your phone around and see which way to walk to the nearest Metro, Metrobús or train
station in Mexico City. I wrote the AR math myself (Haversine bearings, projection with the
camera's real field of view, sensor smoothing that doesn't spin at 359° → 0°) and a pipeline
that turns the city's GTFS feed into an offline dataset of 1,000 stations across 36 lines.

<p>
  <img src="https://raw.githubusercontent.com/AaronUgalde/MetroAR-CDMX/main/docs/screenshots/ar-view.jpg" width="150" alt="MetroAR camera view with station markers">
  <img src="https://raw.githubusercontent.com/AaronUgalde/MetroAR-CDMX/main/docs/screenshots/navigation.jpg" width="150" alt="MetroAR walking navigation">
  <img src="https://raw.githubusercontent.com/AaronUgalde/MetroAR-CDMX/main/docs/screenshots/map.jpg" width="150" alt="MetroAR offline map">
</p>

**[reactor-http](https://github.com/AaronUgalde/reactor-http)** · C<br>
An HTTP/1.1 server in ~1,700 lines of C with no dependencies. Reactor pattern, one epoll/kqueue
loop per core, `sendfile` for static files. Holds 10,000 concurrent connections on my laptop and
passes its test suite under ASan/UBSan. The most fun bug was kqueue handing me a read and a
write event for the same connection in one batch, right after I'd freed it.

**[cv-tailor-mcp](https://github.com/AaronUgalde/cv-tailor-mcp)** · Python · [PyPI](https://pypi.org/project/cv-tailor-mcp/)<br>
An MCP server that lets Claude Code or Cursor tailor a one-page LaTeX CV to a job posting.
It tries three spacing profiles until the PDF fits one page and turns `pdflatex` noise into
diagnostics an agent can act on. I wrote it because I was tired of doing that by hand.

**[credit-risk-modeling](https://github.com/AaronUgalde/credit-risk-modeling)** · Python, FastAPI<br>
Credit default model over 32k loan applications, taken past the notebook: custom scikit-learn
transformers, model selection by stratified CV (random forest, AUC 0.934), SHAP explanations per
request, and a FastAPI service with batch scoring.

**[hotel-perros](https://github.com/AaronUgalde/hotel-perros)** · TypeScript, PostgreSQL<br>
Management system for a dog hotel. 35-table schema, 100+ REST endpoints in a layered Express
backend, JWT auth with roles, and a React front end with a reservation calendar.

**[finetuning_t5_flant5_mt5_en2picto](https://github.com/AaronUgalde/finetuning_t5_flant5_mt5_en2picto)** + **[pictograms-annotator](https://github.com/AaronUgalde/pictograms-annotator)** · Python<br>
Translating sentences into ARASAAC pictograms for augmentative communication. I fine-tuned
T5, FLAN-T5 and mT5 for English → pictograms, then built a web app so a whole class can annotate
more training data.

**[esp32-cam-pet-bowl](https://github.com/AaronUgalde/esp32-cam-pet-bowl)** · C++, Python<br>
A patrol robot that checks on a pet's food bowl. ESP32 + Arduino over UART, a CNN on
ESP32-CAM frames, and a Telegram alert when something's off.

**[RAG-temarios](https://github.com/AaronUgalde/RAG-temarios)** · Python<br>
Ask questions about ESCOM's syllabi in plain Spanish. FAISS, MiniLM embeddings, Streamlit.

**[Competitive_Programming](https://github.com/AaronUgalde/Competitive_Programming)** · C++<br>
600+ accepted solutions from Codeforces, AtCoder and CSES, plus the template and stress tester
I bring to contests.

### Lately

<!-- recent:start -->
- [pictograms-annotator](https://github.com/AaronUgalde/pictograms-annotator) <sub>Python · today</sub>
- [MetroAR-CDMX](https://github.com/AaronUgalde/MetroAR-CDMX) <sub>Kotlin · today</sub>
- [Proyecto-Paralelo](https://github.com/AaronUgalde/Proyecto-Paralelo) <sub>TeX · 4 days ago</sub>
- [reactor-http](https://github.com/AaronUgalde/reactor-http) <sub>C · 16 days ago</sub>
- [picto_xp3](https://github.com/AaronUgalde/picto_xp3) <sub>Python · 19 days ago</sub>
<!-- recent:end -->

<sub>The list above is updated by <a href="./.github/workflows/update-readme.yml">a small workflow</a> in this repo.</sub>

<details>
<summary><sub>Tools I reach for</sub></summary>
<br>

Python, C++, TypeScript, SQL, Kotlin. FastAPI, Express, Next.js, React. PostgreSQL and PostGIS,
Docker, Airflow, Databricks, AWS SageMaker. PyTorch, Hugging Face, sentence-transformers,
scikit-learn, SHAP, FAISS, NetworkX.

</details>
