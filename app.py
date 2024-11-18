import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build
import requests
from utils import search_web, extract_information

load_dotenv()

def load_google_sheet(sheet_id, range_name, api_key):
    service = build('sheets', 'v4', developerKey=api_key)
    sheet = service.spreadsheets().values().get(spreadsheetId=sheet_id, range=range_name).execute()
    return pd.DataFrame(sheet['values'][1:], columns=sheet['values'][0])

def main():
    st.title("AI Agent for Information Retrieval")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    google_sheet_id = st.text_input("Enter Google Sheet ID")
    range_name = st.text_input("Enter Range Name")
    df = None

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        main_column = st.selectbox("Select the column for entity", df.columns)

    if google_sheet_id and range_name:
        try:
            df = load_google_sheet(google_sheet_id, range_name, os.getenv("GOOGLE_SHEET_API_KEY"))
            st.write(df)
            main_column = st.selectbox("Select the column for entity", df.columns)
        except Exception as e:
            st.error(f"Error loading Google Sheet: {e}")

    prompt = st.text_input("Enter your search query (use {entity} as a placeholder):")

    if st.button("Start Extraction"):
        if prompt and df is not None and main_column:
            results = []
            for entity in df[main_column]:
                query = prompt.format(entity=entity)
                search_results = search_web(query)
                extracted_data = extract_information(query, search_results)
                if extracted_data:
                    results.append(extracted_data)

            results_df = pd.DataFrame(results, columns=["Extracted Data"])
            st.write(results_df)

            csv = results_df.to_csv(index=False)
            st.download_button(label="Download Results", data=csv, file_name="results.csv", mime="text/csv")

if __name__ == "__main__":
    main()
