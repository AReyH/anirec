# Anirec

This repo is a project to work on an anime recommendation system that uses both [Collaborative Filtering](https://developers.google.com/machine-learning/recommendation/collaborative/basics) and [Content-Based Filtering](https://developers.google.com/machine-learning/recommendation/content-based/basics) to suggest shows tailored to users' tastes. The project scrapes user ratings from [MyAnimeList](https://myanimelist.net/) and uses that data to generate personalized recommendations.

---

## Features

- **User Data Scraping**: Collects anime ratings from MyAnimeList users using BeautifulSoup.
- **Recommendation Engines**:
  - **Collaborative Filtering**: Suggests anime based on similarities between users' preferences.
  - **Content-Based Filtering**: Suggests anime based on anime features and the user's rating history.
- **Comparison of Methods**: Both recommendation strategies are implemented, with performance comparison planned to select the best approach.

---

## Getting Started

### Requirements

- Python 3.11+
- Packages:
    ```bash
    conda env create -f environment.yml
    ```

*(BeautifulSoup4, requests, etc.)*

### Usage

1. **Scrape User Data**
   Run the scraping script to collect anime ratings:

   ```bash
   python ./scripts/scraper.py
   ```
2. **Train Recommendation Models**
   Train the collaborative and content-based models (NOT YET IMPLEMENTED):

   ```bash
   python train_models.py
   ```
3. **Generate Recommendations**
   Get anime recommendations for a specific user(NOT YET IMPLEMENTED):

   ```bash
   python recommend.py --user USERNAME
   ```

---

## Project Structure

```
anirec/
│
├── data/               # Scraped data
├── scripts/                # Source code
│   ├── scraper.py
│   ├── train_models.py
│   ├── recommend.py
│   └── utils.py
├── requirements.txt
└── README.md
```

---

## Future Work

* Compare the performance of Collaborative Filtering vs Content-Based Filtering.
* Deploy the system as a web app for easier user interaction.
* Expand the dataset to include more users and additional anime features (genres, themes, studios, etc.).

---

## Notes

* Make sure to comply with MyAnimeList's [Terms of Service](https://myanimelist.net/about.php) when scraping data.
* This project is intended for **educational purposes ONLY**.

---

## License

MIT License © 2026 Arturo Rey