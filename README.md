# Ndejje University Examination Chatbot

## Overview

This is a Rasa-based chatbot designed for Ndejje University to assist students with their examination-related queries. The chatbot provides instant responses to frequently asked questions about examination schedules, results, procedures, and other related topics.

## Features

- **Examination Schedules**: Provides information about upcoming examination dates and times.
- **Results Inquiries**: Answers queries related to exam results release dates and access procedures.
- **Examination Procedures**: Offers guidance on examination rules, required documents, and procedures.
- **General Inquiries**: Responds to general questions about the university's examination processes.

## Installation

To run the chatbot locally, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone git@github.com:Ayikoandrew/small.git
   cd small
2. **Create and Activate a Virtual Environment:**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
4. **Train the Model:**
   ```sh
   rasa train
5. **Run the Chatbot:**
   ```sh
   rasa shell
  **Usage**
To run the chatbot with the Flask template, follow these steps:
1. Start the chatbot
2. Run the Flask App:
   ```sh
   flask --app app run


Contact

For any questions or support, please contact:

    Andrew Ayiko
    Email: andrewayiko40@gmail.com
