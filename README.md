# AI Email Classification & Auto-Reply Automation

An AI-powered email automation workflow built with n8n, Google Gemini, PostgreSQL, Gmail, Python, and GitHub.

## Overview

This project automates the processing of incoming emails.

The workflow:

1. Retrieves email data
2. Prepares and parses email content
3. Classifies emails using AI
4. Parses the AI classification result
5. Routes emails by category
6. Generates an appropriate AI reply
7. Sends an automated email response
8. Saves the email record to PostgreSQL

## Workflow Architecture

```text
Manual Trigger
      ↓
Get Email Data
      ↓
Prepare Email Data
      ↓
AI Email Classification
      ↓
Parse AI Result
      ↓
Route by Category
   ↙      ↓       ↓       ↘
Sales  Support  Complaint  General
   └──────┴───────┴────────┘
              ↓
      AI Reply Generation
              ↓
      Send Auto-Reply
              ↓
      Save Email Record
              ↓
           Complete