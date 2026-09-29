# Deep Learning with TensorFlow, Keras and PyTorch

An independent, chapter-by-chapter collection of Jupyter notebooks and hands-on examples for studying deep learning with Python.

This project follows the topics in _Глубокое обучение с TensorFlow, Keras и PyTorch_ (D. A. Movchan, ed., 2025). It is an independent study companion, not an official repository of the book or its publisher. Explanations and implementations here are prepared for this repository; the book remains the work of its authors and publisher.

## Chapters

| Chapter                                                                          | Topics                                                                               |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [01 - Introduction to Neural Networks and Deep Learning](01_introduction_nn_dl/) | Perceptron, multilayer perceptron, XOR, gradient descent, Momentum, RMSprop and Adam |

Chapters are organized as numbered directories in the repository root (`01_...`, `02_...`). Each chapter may include its own notebooks and `requirements.txt`.

## Getting Started

The current chapter environment uses Python `3.13.13`.

```bash
python -m venv .venv
```

Activate the environment, then install the chapter dependencies:

```bash
# Linux or macOS
source .venv/bin/activate
python -m pip install -r 01_introduction_nn_dl/requirements.txt
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r 01_introduction_nn_dl\requirements.txt
```

Open a chapter notebook in VS Code and select `.venv` as its Python kernel. Later chapters may use different dependencies; install the requirements listed in the chapter you are running.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for chapter structure, notebook checks, and pull request guidance. Please keep examples original and do not commit scans, substantial copied passages, or other material from the book without permission.

## Project Standards

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Contributing Guide](CONTRIBUTING.md)

## License

No license has been selected yet. Until one is added, the repository's code and materials are not granted an open-source license. The book and any third-party materials remain subject to their respective rights and licenses.
