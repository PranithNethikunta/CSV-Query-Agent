# Project **DASH-(Data Access Solution Hub)**

## Problem Statement
**DASH (Data Access Solution Hub)** is an AI-powered assistant designed for **grocery managers and non-technical users** who need quick access to business data but lack SQL or programming skills.

In most retail and grocery operations,suppose sales data is scattered in Excel sheets making it hard for non-technical teams to access insights without involving analysts or Excel experts.

**DASH solves this** by enabling users to ask **natural language questions** and receive instant **answers and reports**, all powered by AI and connected to multiple data sources in real time.

# DataFrame Query Agent

This project lets you ask natural language questions about your CSV file and get instant answers by automatically converting your questions into executable pandas code using a Groq LLM.

## Features
- Load any CSV dataset
- Automatically extract and understand dataset schema
- Translate natural language questions into pandas queries
- Execute queries securely and return results
- CLI interface to interact with your data
- Built-in logging and error handling

## How It Works
1. Loads your CSV file path from `.env`
2. Extracts schema (columns, types, sample data)
3. Uses Groq LLM to convert your question into pandas code
4. Runs the code on the DataFrame and returns the output

## Setup Instructions

1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
