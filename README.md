
# Panchayat API

This project is a FastAPI-based web API that provides data about seasons, episodes and casts of the series "Panchayat". The API allows you to fetch all casts, seasons, get specific season details, and retrieve episodes for a given season.


## Run Locally

Clone the project

```bash
  git clone https://github.com/Binodprasadjoshi/panchayat-api.git
```

Go to the project directory

```bash
  cd panchayat-api
```

Start the server

```bash
  uvicorn app:app --reload
```


## API Endpoints
- GET /api/seasons/
    - Retrieves a list of all seasons.

- GET /api/seasons/{season_number}/
    - Retrieves details of a specific season.

- GET /api/seasons/{season_number}/episodes
    - Retrieves a list of all episodes for a specific season.

- GET /api/seasons/{season_number}/episodes/{episode_number}/
    - Retrieves details of a specific episode within a season.

- GET /api/cast
    - Retrieves details of cast of series
