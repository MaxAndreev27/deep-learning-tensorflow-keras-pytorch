# Deep Learning with TensorFlow, Keras and PyTorch

An independent, chapter-by-chapter collection of Jupyter notebooks and hands-on examples for studying deep learning with Python.

This project follows the topics in _Глубокое обучение с TensorFlow, Keras и PyTorch_ (D. A. Movchan, ed., 2025). It is an independent study companion, not an official repository of the book or its publisher. Explanations and implementations here are prepared for this repository; the book remains the work of its authors and publisher.

## Chapters

| Chapter | Notebook | Topics |
| ------- | -------- | ------ |
| [01 - Introduction to Neural Networks and Deep Learning](01_introduction_nn_dl/) | [perceptron_nn_dl.ipynb](01_introduction_nn_dl/perceptron_nn_dl.ipynb) | Perceptron, multilayer perceptron, XOR, gradient descent, Momentum, RMSprop, Adam, overfitting, underfitting, L1/L2 regularization, dropout, early stopping, and loss functions (MSE, binary/categorical cross-entropy, hinge, and custom Keras losses) |
| [02 - Deep Learning with TensorFlow](02_dl_with_tensorflow/) | [tensorflow_examples.ipynb](02_dl_with_tensorflow/tensorflow_examples.ipynb) | Tensors and tensor operations, `tf.data` pipelines, simple networks on MNIST, learning rate scheduling, early stopping, dropout, KerasTuner, transfer learning and fine-tuning with MobileNetV2, KerasCV YOLOv8 object detection, text embeddings, and saving/loading models and checkpoints |
| [03 - Deep Learning with Keras](03_dl_with_keras/) | [keras_examples.ipynb](03_dl_with_keras/keras_examples.ipynb) | Sequential and Functional APIs, compiling, training and evaluating models, multi-output models, shared layers, combining Sequential and Functional models, `ModelCheckpoint`, and `EarlyStopping` |
| [04 - Deep Learning with PyTorch](04_dl_with_pytorch/) | [pytorch_examples.ipynb](04_dl_with_pytorch/pytorch_examples.ipynb) | Tensors and autograd, a simple computational graph, feedforward networks, training on MNIST, loading a pre-trained ResNet-18 for image classification, feature extraction, fine-tuning the last layers, training on CIFAR-10, and evaluating a fine-tuned model |

Chapters are organized as numbered directories in the repository root (`01_...`, `02_...`, `03_...`, `04_...`). Each chapter has its own notebook, `requirements.txt`, and `.python-version`. Chapters 02 and 04 also use an `images/` directory.

Generated artifacts (`.venv/`, `data/`, `*.keras`, `*.weights.h5`, `*.pth`, and tuner output) are created locally when you run the notebooks and are excluded from version control. Chapter 04 downloads the MNIST and CIFAR-10 datasets into `04_dl_with_pytorch/data/` and saves trained PyTorch weights (`*.pth`) next to the notebook.

## Getting Started

Each chapter pins its own dependencies and uses Python `3.13.13` (see the chapter's `.python-version`). Create a separate virtual environment inside the chapter you want to run, for example `03_dl_with_keras`:

```bash
cd 03_dl_with_keras
python -m venv .venv
```

Activate the environment, then install the chapter dependencies:

```bash
# Linux or macOS
source .venv/bin/activate
python -m pip install -r requirements.txt
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Open the chapter notebook in VS Code and select the chapter's `.venv` as its Python kernel. Chapter 02 needs additional packages (such as KerasTuner and KerasCV), so always install the requirements of the chapter you are running.

Chapter 04 pins CPU builds of PyTorch (`torch==...+cpu`, `torchvision==...+cpu`), which are not hosted on PyPI. Install them with the PyTorch CPU package index:

```bash
python -m pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for chapter structure, notebook checks, and pull request guidance. Please keep examples original and do not commit scans, substantial copied passages, or other material from the book without permission.

## Project Standards

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Contributing Guide](CONTRIBUTING.md)

## License

No license has been selected yet. Until one is added, the repository's code and materials are not granted an open-source license. The book and any third-party materials remain subject to their respective rights and licenses.
