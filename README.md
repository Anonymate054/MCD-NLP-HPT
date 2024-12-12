<h1 align="center">
  <br>
  <b>NLP</b>
  <b>By: Luis Enrique Noguera Gil</b>
  <br>
</h1>

<p align="center">
  NLP project</a>.
  <br>
</p>


## Description

### Summary:

YouTube comments are essential for the development and success of a channel, fostering interaction between creators and their audience and strengthening the community around the content. This interaction not only allows viewers to express their opinions and thoughts but also provides valuable feedback for creators to improve and adapt their content to the preferences of their audience (FasterCapital, n.d.).

Additionally, comments serve as social proof, influencing the perception of the quality and credibility of videos. A high number of positive comments can attract more viewers and increase engagement, while the absence of comments or the presence of negative comments can have the opposite effect (FasterCapital, n.d.).

Analyzing comments using Latent Dirichlet Allocation (LDA) allows for the identification of the predominant topics of interest to the audience. This information is invaluable for better understanding viewer expectations and adjusting channel content to meet their interests, promoting greater engagement and strengthening the community around the channel.

### Application to "Historia para Tontos":

"Historia para Tontos" is a channel that narrates historical events in an accessible and entertaining way, covering topics such as international conflicts, historical figures, and ancient cultures. It has a presence on various social media platforms like TikTok, Instagram, Facebook, Spotify, and YouTube.

Its content has two verticals: short videos featuring "Mapita" telling funny historical stories to promote knowledge of Mexican and world history, and a podcast for longer, more digestible historical content.

We spoke with "Mapita" about their social media strategy and some things they would like to implement. One of the most notable comments is the desire to generate more content for their secondary YouTube channel, where the podcast has 26k subscribers, while their TikTok has 7.8 million.

Understanding that short-form, comedic content is more engaging, they would like to know what their podcast subscribers think, in addition to any insights we can extract.

## Technologies Used

- Python 3 ![Python](https://img.shields.io/badge/Python-3.11-blue)

## Project Objective

NLP project

## Analysis Section

Youtube comments

## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate nlp
```

or 

```bash
conda install -c conda-forge mamba
mamba env create -f environment.yml
activate nlp
```

## Modules and default modules

To install the default modules located in the `scripts` directory, use the following command:

```bash
pip install --editable .
```

For more information about the user's modules, refer to `install.md`.

## The resulting directory structure

The directory structure of your new project will look something like this (depending on the settings that you choose):

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── nlp_module         <- User module directory
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-anony-initial-data-exploration`.
│
├── scripts            <- Default modules and scripts for the project
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
```

In order to get more reference of the API look for:

## Enviromental file

Remembar to create `.env` file like this:

```
YT-API-KEY="YOUR_API_KEY"
```

[Developers Google](https://developers.google.com/youtube/v3/docs)

[Python-library](https://google-api-client-libraries.appspot.com/documentation/youtube/v3/python/latest/)