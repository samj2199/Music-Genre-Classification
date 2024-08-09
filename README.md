# Music Composition Similarity Detection
## Project Overview
This project introduces a novel Machine Learning (ML) model designed to quantify the similarity between musical compositions (musical aspect only), aiding composers and producers in assessing the originality of their work. Developed at Drexel University as part of Pattern Recognition course, this system leverages advanced audio processing techniques and machine learning algorithms to identify and measure similarities across a vast database of songs.

## Abstract
In the realm of music composition, the line between inspiration and infringement can often blur, leading to legal and ethical complexities. This paper introduces a novel Machine Learning (ML) model aimed at quantifying the similarity between a subject song and a vast database of musical compositions. The model employs a robust feature extraction mechanism, leveraging Mel Frequency Cepstral Coefficients (MFCCs) and other distinctive audio features. By comparing these features, the model curates a refined list of compositions bearing the closest resemblance to the input track, enabling composers to assess the originality of their work. We utilize the 'Librosa' and 'OpenSmile' libraries for feature extraction from audio signals, which are transformed into Mel Spectrograms via Fourier and Constant Q transforms. The model's efficacy is demonstrated through a range of machine learning algorithms, including K-Nearest Neighbors (KNN), Siamese Networks, Convolutional Neural Networks (CNN), and XGBOOST, with a focus on datasets tailored to similarity detection in beat patterns, lyrics, melodies, and harmony.

## Trials
- ### 1st Approach :
  The initial phase of our project was devoted to the comparative analysis of two distinct musical pieces: 'Sail' by Awolnation, a well-known track in the music industry, and 'One and Only', an original composition inspired by the former. Our goal was to establish a systematic framework for detecting similarities between these two pieces using various audio signal processing techniques and similarity measures.
  
- ### 2nd Approach :
  To enhance the scope of our music similarity detection project, we curated a dataset of 16 songs with perceived similar characteristics, designated as the training set, and 3 distinct songs for testing. The objective was to refine our model's ability to discern nuanced similarities within a larger and more diverse corpus of music.
  
- ### 3rd Approach :
  Our initial dataset comprised a diverse collection of songs spanning a variety of genres and styles. We employed the Librosa and OpenSmile libraries to extract an extensive set of features, including Mel Frequency Cepstral Coefficients (MFCCs), spectral contrast, and chroma features. These features were chosen for their established ability to capture the distinct aspects of musical signatures.

## Features
Feature Extraction: Utilizes Mel Frequency Cepstral Coefficients (MFCCs) and other audio features extracted via Librosa and OpenSmile libraries.
Algorithmic Analysis: Employs machine learning algorithms such as K-Nearest Neighbors (KNN), Convolutional Neural Networks (CNNs), Siamese Networks, and XGBOOST to analyze and compare features.
Comprehensive Database: Compares features against a curated dataset tailored for similarity detection in aspects such as beat patterns, lyrics, melodies, and harmony.

## Motivation
In the digital era, distinguishing between inspiration and infringement in music composition has become increasingly complex. This project aims to provide composers with a tool to ensure their creations are distinct, helping to navigate and potentially safeguard against copyright challenges.

## Model Workflow
Input Acquisition: Receives a musical track as input.
Feature Extraction: Extracts salient features focusing on Notes pattern, Chord Progression, beat patterns, melodic lines, Use of silence and Space (harmonic structures),tempo and Timbre analysis.
Similarity Assessment: Compares these features against a database, refining a list of similar songs through successive comparisons to offer a granularity in similarity scores.
Results
The model demonstrates high accuracy in detecting similarity:

Evaluated using a variety of metrics across different musical features.
Provides a detailed similarity score that helps in understanding the closeness between different musical pieces.

## References
- Kim, Y.E., Whitman, B. (2002). Singer Identification in Popular Music Recordings Using Voice Coding Features.
- Martin, K.D. (1999). Sound-source recognition: a theory and computational model.
