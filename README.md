# Quiz API

## A simple API for random quiz questions

Made by [takos22](https://github.com/takos22) and [Banik](https://github.com/Banik1103)

## Table of Contents

- [Usage](#usage)
- [Getting Started](#getting_started)

## Usage <a name = "usage"></a>

There are 2 subdomains:

- `/question` - returns a random question.

  `/question/<category_id>` - returns a random question from a specified category. List of categories [here](#categories).

    ```json
    {
      "id": "1",
      "question": "Question?",
      "choices": ["Answer 1", "Answer 2", "Answer 3"]
    }
    ```

- `/answer/<question_id>` - returns the answer to a given question.

  ```json
  {
    "id": "1",
    "answer": "Answer 2"
  }
  ```

### Categories <a name = "categories"></a>

Here's the list of available categories along with their IDs:

1. Tech
2. Science
3. Sports

## Getting Started <a name = "getting_started"></a>

To run this project locally for development and testing purposes, follow these steps.

### Modules

Install the required modules for the API through `pip`.

```bash
pip install -r requirements.txt
```

### Running the API

Add the `FLASK_APP` enviroment variable.

- In cmd:

  ```bash
  set FLASK_APP=run.py
  ```

- In other terminals:

  ```bash
  export FLASK_APP=run.py
  ```

Make the database migrations.

```bash
flask db upgrade
```

Then run the flask API.

```bash
flask run
```

Then you can make requests to it! You can use the example in [example.py](example.py).
