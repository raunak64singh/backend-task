# HROne Backend Intern Task

This FastAPI backend supports creating products, listing them, placing orders, and retrieving user-specific orders. MongoDB Atlas is used for persistence.

## Endpoints

- `POST /products`
- `GET /products?name=shoe&size=large&limit=5&offset=0`
- `POST /orders`
- `GET /orders/{user_id}?limit=5&offset=0`

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Make sure to set `.env` variables for MongoDB Atlas connection.
