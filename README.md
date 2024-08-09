# Music Genre Classification (Not just a regular classification but Classifying within tracks)
## Overview
The "Music Genre Classification" project developed at Drexel University leverages advanced machine learning techniques to classify music by genre. Utilizing Python libraries like librosa for audio processing and XGBoost for classification, this model classifies individual portions of music tracks, improving accuracy in multi-genre identification.

## Motivation / Basic Idea
### Basic Idea :
Have you ever noticed that a single track might start off a certain way but end up completely different towards the end.
- Example : Listen to "Free Bird - Lynard Skynard". The first 1:50 seconds sound entirely different from the last ending 1:50 seconds.


With the increasing complexity of musical compositions and their classifications, this project seeks to address the challenges in traditional genre classification by breaking down tracks into segments. This approach benefits music professionals, streaming platforms, and enhances personalized music discovery and recommendations.

## Features
- Detailed Audio Analysis: Converts audio files into Mel Spectrograms for detailed analysis.
- Harmony-Percussion Segregation: Uses librosa to distinguish between harmonic and percussive elements of a track.
- Advanced Classification: Employs XGBoost to classify music segments into multiple genres, based on harmony, tempo, and instrumental elements.
- Dataset: Trained on the GTZAN dataset, which includes 100 files across 10 different genres.
  
## Model Workflow
1. Preprocessing: Converts audio tracks into wave plots and subsequently into spectrograms.
2. Feature Extraction: Implements Mel scale conversions to enhance the analysis quality.
3. Genre Classification: Classifies each music segment into one or more genres based on its distinct features.
   
## Results
The model achieves a nuanced classification of music, identifying multiple genres within single tracks and providing insights into the complexity of musical compositions. It effectively handles diverse musical attributes from a segmental perspective, offering a comprehensive genre classification.

## Contributions
Contributions to enhance the model's accuracy or extend its functionality are welcome. Please fork the repository, make your changes, and submit a pull request.

