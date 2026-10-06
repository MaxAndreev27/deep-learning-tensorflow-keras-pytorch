# Contributing

Thank you for helping improve this chapter-based learning project. Contributions can include notebook corrections, clearer explanations, reproducible examples, and improvements to setup instructions.

## Before Opening an Issue

Search existing issues first. For substantial changes, open an issue to discuss the proposed approach before investing in implementation.

## Chapter Structure

- Keep chapter material in a numbered root directory such as `01_introduction_nn_dl/`, `02_dl_with_tensorflow/`, or `03_dl_with_keras/`.
- Keep chapter-specific dependencies in that chapter's `requirements.txt` and its Python version in `.python-version`.
- Create the virtual environment inside the chapter directory. Do not commit `.venv/` or generated model files (`*.keras`, `*.weights.h5`).
- Save Keras models in the native `.keras` format (use `.weights.h5` for weights only) instead of legacy `.h5`.
- Prefer focused notebooks with explanatory Markdown and runnable code cells.
- Use relative paths so notebooks work from the repository after cloning.

## Notebook Contributions

- Run the cells affected by your changes using the chapter's documented environment.
- Check that outputs, plots, and printed results match the notebook's explanation.
- Keep random seeds fixed in examples where reproducibility matters.
- Avoid committing credentials, personal data, unrelated generated files, or local environment folders.
- Explain whether reported metrics are training, validation, or test results.

## Copyright and Attribution

Write original explanations and implementations. Do not submit scans, substantial copied text, or unlicensed code, datasets, figures, or other material from the reference book or third parties. Cite references and respect their licenses.

## Pull Requests

- Keep each pull request focused and describe the learning goal or bug addressed.
- List the affected chapter and notebooks.
- Include the commands or notebook cells you ran and summarize the result.
- Update documentation when setup, behavior, or chapter contents change.
- Complete the checklist in the pull request template.
