import os
import nltk


def setup_nltk_data():
    # Define the directory to store NLTK data within project
    nltk_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nltk_data')
    os.makedirs(nltk_data_dir, exist_ok=True)

    # Set it manually for the nltk module to find it
    nltk.data.path.append(nltk_data_dir)

    # List of datasets to download
    datasets = [
        'wordnet',
        'omw-1.4',
        'stopwords',
        'punkt',
        'brown',
        'popular',
        'averaged_perceptron_tagger'
    ]

    # Download each dataset with verification
    for dataset in datasets:
        try:
            nltk.download(dataset, download_dir=nltk_data_dir, quiet=True)
            print(f"Successfully downloaded {dataset}")
        except Exception as e:
            print(f"Error downloading {dataset}: {str(e)}")

    print(f"NLTK data downloaded to: {nltk_data_dir}")
