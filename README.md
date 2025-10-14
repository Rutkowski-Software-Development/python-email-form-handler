# python-email-form-handler

![CI](https://github.com/Rutkowski-Software-Development/python-email-form-handler/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)

Minimal Python script to validate form input, send email via SMTP, and log successes or failures.

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [Logging](#logging)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

## Features

- Reads `--to`, `--subject`, and `--body` from the command line  
- Uses TLS for secure SMTP connections  
- Logs successful sends and errors to `handler.log`  
- Returns exit code `0` on success, `1` on failure  

## Prerequisites

- Python 3.7 or higher  
- Access to an SMTP server (e.g., Gmail, SendGrid)  
- Optional: [`python-dotenv`](https://pypi.org/project/python-dotenv/) for `.env` support  

## Installation

1. Clone the repository  
   ```bash
   git clone git@github.com:Rutkowski-Software-Development/python-email-form-handler.git
   cd python-email-form-handler
   pip install -r requirements.txt