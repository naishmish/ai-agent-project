# AI Agent for Data Extraction

This project demonstrates an AI agent that reads a dataset (CSV or Google Sheets), performs a web search to retrieve specific information based on user-defined prompts, and displays the results in a dashboard. The user can download the extracted information as a CSV file.

## Features:
1. **Dashboard for File Upload and Google Sheets Connection:**
   - Upload CSV or connect Google Sheets to extract data.
   - Preview uploaded data.

2. **Dynamic Query Input with Prompt Template:**
   - Input custom search prompts for each entity (e.g., "Get the email address of {company}").

3. **Web Search for Information Retrieval:**
   - Perform web searches for each entity using the custom query and gather relevant results.

4. **Use of Groq LLM and HuggingFace for Parsing and Extraction:**
   - Use Groq and HuggingFace API to extract specific information from the search results.

5. **Downloadable Extracted Data:**
   - View and download extracted information in CSV format.

## Setup Instructions:
1. Install dependencies using:
   ```bash
   pip install -r requirements.txt
