# Project Setup and Testing Guide

This document provides a comprehensive, step-by-step guide to setting up, running, and testing the project. The instructions below will help ensure that your environment is correctly configured and that all project functionalities are working as expected.

---

## Prerequisites

Before proceeding, make sure you have the following installed and configured on your system:

- **Python**: Download and install the latest version from the [official Python website](https://www.python.org/downloads/).
- **Django**: Install Django using pip if it is not already installed:
  ```bash
  pip install django
  ```

---

## Project Setup

### 1. Download, Install, and Setup Python and Django

Ensure that both Python and Django are installed and properly set up on your machine. Follow the official documentation for detailed installation instructions.

### 2. Launch the Django Shell

Navigate to the project directory in your terminal or command prompt and start the Django shell by running:
```bash
python manage.py shell
```

### 3. Resolve SQLite Errors

If you encounter an SQLite error when launching the Django shell, run the following command to apply all necessary database migrations:
```bash
python manage.py migrate
```
This will update your database schema according to the models defined in the project.

---

## Running Signal Tests

Once your environment is set up and any database issues are resolved, you can test the project's signal functionality. In the Django shell, execute the following commands:

```python
from accuknox_assignment import signals

# Q1: Synchronous execution demonstration
signals.test_sync_signal()

# Q2: Same thread demonstration
signals.test_thread_signal()

# Q3: Transaction behavior demonstration
signals.test_transaction_signal()
```

**Descriptions:**
- **Synchronous Execution**: Demonstrates that the signals are executed synchronously.
- **Same Thread Execution**: Confirms that signals run on the same thread.
- **Transaction Behavior**: Illustrates the behavior of signals within database transactions.

---

## Testing the Class Code

To test the functionality of the class code, run the following command from your terminal or command prompt:
```bash
python accuknox_assignment/rectangle.py
```

### Expected Output

The expected output from running the above command is:

```
{'length': 10}
{'width': 5}
```

This output confirms that the class code is functioning as intended, with the correct attribute values being displayed.

---

## Conclusion

By following these steps, you will have successfully set up the project environment, resolved any initial database issues, and verified the signal and class functionalities. If you encounter any problems or need further assistance, please refer to the project documentation or contact the support team.

