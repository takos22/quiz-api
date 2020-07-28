# Quiz API

## A simple API for random quiz questions

Made by [takos22](https://github.com/takos22) and [Banik](https://github.com/Banik1103)

## Table of Contents

- [Usage](#usage)
- [Getting Started](#getting_started)

## Usage <a name = "usage"></a>

There are 2 subdomains:

- `/question` - returns a random question on the format:

    ```json
    {
      "id": 1,
      "question": "Question?",
      "choices": ["Answer 1", "Answer 2", "Answer 3"]
    }
    ```

- `/answer/<id>` - returns the answer to a given question

  ```json
  {
    "id": 1,
    "answer": "Answer 2"
  }
  ```

## Getting Started <a name = "getting_started"></a>

To run this project locally for development and testing purposes, follow these steps.

### Modules

Install the required modules for the API through `pip`.

```bash
pip install -r requirements.txt
```

### Running the API

Add the `FLASK_APP` enviroment variable

- In cmd:

  ```bash
  set FLASK_APP=run.py
  ```

- In other terminals:

  ```bash
  export FLASK_APP=run.py
  ```

Then run the flask api

```bash
flask run
```

Then you can make requests to it! You can use the example in [test.py](test.py)