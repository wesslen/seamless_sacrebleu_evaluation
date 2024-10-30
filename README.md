# Machine Translation Evaluation Pipeline

A Python-based pipeline for evaluating machine translations using the Seamless M4T V2 model and sacreBLEU metrics.

## Overview

This repository contains tools for:
- Batch translation using Meta's [Seamless M4T V2 model](https://huggingface.co/facebook/seamless-m4t-v2-large)
- Translation quality evaluation using [sacreBLEU metrics](https://github.com/mjpost/sacrebleu)
- Support for multiple reference translations
- GPU acceleration support

## Repository Structure

```
.
├── notebooks/
│   └── translation_evaluation.ipynb    # Main evaluation notebook
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.8+
- PyTorch
- Transformers
- sacreBLEU
- tqdm
- GPU with 26.6+ GB VRAM (used Colab A100)

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/wesslen/seamless_sacrebleu_evaluation.git
cd mt-evaluation-pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Open the notebook in Google Colab or Jupyter:
   - Navigate to `notebooks/translation_evaluation.ipynb`
   - If using Colab, ensure you have enabled GPU runtime (A100)

## Usage

The notebook provides a complete pipeline for:

1. Loading and preparing source texts
2. Performing batch translation
3. Computing BLEU scores using sacreBLEU

Example usage in the notebook:

```python
# Initialize the evaluator
evaluator = TranslationEvaluator()

# Prepare your texts
source_texts = [
    "Hello, my dog is cute",
    "The weather is nice today"
]

references = [
    ["Bonjour, mon chien est mignon"],
    ["Le temps est beau aujourd'hui"]
]

# Translate and evaluate
translations = evaluator.translate_batch(
    texts=source_texts,
    src_lang="eng",
    tgt_lang="fra"
)

bleu_score = evaluator.evaluate_translations(
    hypotheses=translations,
    references=references
)
```

## Features

- **Batch Processing**: Efficiently handles multiple translations in batches
- **GPU Support**: Automatic GPU detection and utilization when available
- **Multiple References**: Support for multiple reference translations per source text
- **BLEU Scoring**: Industry-standard BLEU score calculation using sacreBLEU
- **Progress Tracking**: Real-time progress bars for batch translation

## Model Information

The pipeline uses Facebook's Seamless M4T V2 model:
- Model Card: [facebook/seamless-m4t-v2-large](https://huggingface.co/facebook/seamless-m4t-v2-large)
- Size: ~2.5GB
- Capabilities: Multilingual text-to-text translation

## Notes

- First-time model download may take several minutes (~2.5GB)
- GPU is recommended for faster translation
- The model supports multiple language pairs (check model card for full list)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this pipeline in your research, please cite:

```bibtex
@misc{seamless_m4t_2023,
  title={Seamless M4T: Massively Multilingual & Multimodal Machine Translation},
  author={Meta AI},
  year={2023},
  publisher={Meta AI}
}

@inproceedings{post-2018-call,
  title = "A Call for Clarity in Reporting {BLEU} Scores",
  author = "Post, Matt",
  booktitle = "Proceedings of the Third Conference on Machine Translation: Research Papers",
  year = "2018",
  publisher = "Association for Computational Linguistics",
  url = "https://www.aclweb.org/anthology/W18-6319",
}
```
