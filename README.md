# 📊 FMCG AI Analytics Assistant

An AI-powered business analytics assistant that allows users to ask natural-language questions about FMCG sales and promotion data.

The system uses a local Large Language Model (Llama 3.2) to understand business questions and converts them into structured analytical queries. The actual business calculations are performed deterministically using Python and Pandas to ensure reliable and verifiable results.

---

## 🎯 Problem Statement

Business users often have sales data but may not have the technical skills required to write SQL queries or Python code.

This project provides a natural-language interface where users can ask questions such as:

- Did promotions improve sales in the South region?
- Did last month's campaign improve sales?
- Which region had the highest sales?
- Which product category performed best?

The system converts these questions into structured queries and performs reliable data analysis.

---

## 🚀 Key Features

- 🤖 Natural-language business question answering
- 🧠 Local LLM integration using Llama 3.2
- 📊 FMCG sales and promotion analytics
- 🗺️ Region-based filtering
- 📅 Time-period filtering
- 📈 Promotion uplift calculation
- 🛡️ Query validation and guardrails
- ⚡ FastAPI REST API
- 📊 Streamlit interactive dashboard
- 📉 KPI cards and data visualizations
- 🔍 Deterministic Python-based calculations

---

## 🏗️ System Architecture

```text
                    User
                      │
                      ▼
          ┌─────────────────────┐
          │  Streamlit Dashboard │
          └──────────┬──────────┘
                     │
                     ▼
             ┌───────────────┐
             │   FastAPI API  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   Llama 3.2    │
             │  Query Parser  │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   Guardrails   │
             │ Query Validation│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ Analytics Engine│
             │    Pandas      │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ Verified Business│
             │     Answer      │
             └───────────────┘