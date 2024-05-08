# CS 598 EHR Transformer

### BEHRT-based model with embeddings

Instructions to run model:

1) Download `D_ICD_DIAGNOSES.csv.gz` and `diagnoses_icd.csv.gz` from MIMIC-III and keep in a folder called mimic_data. 
2) Run the following to install the required dependencies:
```python3 -m pip install -r requirements.txt`
3) Adjust the variables `diagnoses_file_path`, `map_file_path`, `icd_embedding_txt` accordingly based on the folders where they are stored wherever you are running the model.
4) Run notebook.
