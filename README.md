# Shrink
A simple URL shortner

This app allows you to shorten long URLs and redirect to the original URL using the shortened version.

## API Endpoints

### 1. Shorten URL

- **Endpoint**: `/shrink/<long_url>`
- **Method**: `POST`
- **Description**: Shortens a given long URL and returns a unique short URL.
- **Input**: 
  - `long_url` (string): The long URL to be shortened. This is passed as a path parameter.
- **Output**: 
  - A JSON object containing the unique short URL.

| HTTP Method | Endpoint               | Path Parameter | Description                       |
|-------------|------------------------|----------------|-----------------------------------|
| `POST`      | `/shrink/<long_url>`   | `long_url`     | Shortens a given long URL         |


### 2. Redirect to Long URL

- **Endpoint**: `/<short_url>`
- **Method**: `GET`
- **Description**: Redirects to the original long URL using the shortened URL.
- **Input**: 
  - `short_url` (string): The short URL to be resolved. This is passed as a path parameter.
- **Output**: 
  - Redirects to the original long URL.

| HTTP Method | Endpoint         | Path Parameter | Description                         |
|-------------|------------------|----------------|-------------------------------------|
| `GET`       | `/<short_url>`   | `short_url`    | Redirects to the original long URL  |
