# Spam Mail Detector with Tkinter GUI

A simple, offline **Spam Mail Detector** application built with **Tkinter** for the GUI and a machine learning model trained on an 83,446-sample email dataset from [Kaggle](https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset). This tool allows users to paste email text and check if it's spam with a single click.

## Features

- **User-Friendly Interface**: Easy-to-use Tkinter GUI for testing.
- **Offline Spam Detection**: Runs entirely locally, so no internet connection is required.
- **Reliable Classification**: Trained on a large dataset, providing accurate and efficient spam detection.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spam-mail-detector.git
   cd spam-mail-detector
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. In the GUI, paste the text you want to check.
3. Click **"Check Spam"** to receive an instant classification.

## Project Structure

- **app.py**: Main file containing the Tkinter application.
- **model/**: Folder containing the pre-trained machine learning model.
- **README.md**: Project description and usage instructions.


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.

---

This tool offers a quick, reliable way to classify messages as spam or not, all within an accessible, local interface.