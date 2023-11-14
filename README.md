# X-ray Image Effect Project

This project applies an X-ray effect to images using Python and the Python Imaging Library (PIL). It is a useful tool for creating datasets with characteristics of x-ray images.

---

## Environment Setup

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setting Up a Virtual Environment

1. **Create a Virtual Environment**:

In your terminal, navigate to your project directory and run:

```bash
python -m venv .venv
```

This will create a virtual environment named `.venv` in your project directory.

2. **Activate the Virtual Environment**:
- On Windows, run:
  ```
  .\venv\Scripts\activate
  ```
- On Linux or macOS, run:
  ```
  source venv/bin/activate
  ```

### Installing Dependencies

With the virtual environment activated, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

## Project Configuration

1. **Application Settings**:

Configure the input and output paths in the `src/config.py` file. For example:
```python
APP_PATH_INPUT_IMAGES = 'path/to/input/images/directory'
APP_PATH_OUTPUT_IMAGES = 'path/to/output/images/directory'
```

---

## Usage

To use the application, ensure the virtual environment is activated. In the root directory of the project, run:

```bash
python main.py
```

This will process all images in the specified input directory and save the X-ray effect images to the output directory.

---

## Additional Notes

- Ensure the input directory contains images in supported formats (`.png`, `.jpg`, `.jpeg`, `.webp`).
- The script will create the output directory if it does not exist.

---

## License

This project is open-sourced and available to everyone under the [MIT License](LICENSE).
