# Blogging Platform API

A lightweight REST API for managing blog posts, built with [FastAPI](https://fastapi.tiangolo.com/) and backed by a JSON file.

Sample solution for the [Blogging-platform-api](https://roadmap.sh/projects/blogging-platform-api)
challenge from [roadmap.sh](https://roadmap.sh).

## Features

- Create, read, update blog posts
- Filter posts by category
- JSON file as the data store (no database setup required)
- Automatic API docs (Swagger UI and ReDoc)

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Running the API

Start the development server:

```bash
uvicorn blogging_app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Create a Blog Post

```
POST /posts/
```

**Request body:**

```json
{
  "blog_id": "my-first-post",
  "blog_title": "My First Post",
  "blog_content": "Hello world!",
  "blog_category": "general",
  "tags": ["intro", "hello"]
}
```

**Response:** `201 Created`

Returns an error (`400`) if a post with the given `blog_id` already exists.

### Update a Blog Post

```
PUT /posts/{blog_id}
```

**Request body:**

```json
{
  "blog_title": "Updated Title",
  "blog_content": "Updated content",
  "blog_category": "updates",
  "tags": ["edited"]
}
```

Returns `404` if the post does not exist.

### Get All Blog Posts

```
GET /posts
```

**Query parameters:**

- `category` (optional) — filter posts by category

Returns a list of all posts, or a filtered list of posts matching the given category.

### Get a Single Blog Post

```
GET /posts/{blog_id}
```

Returns `404` if the post does not exist.

## Project Structure

```
blogging_platform_api/
├── blogging_app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app & route handlers
│   └── visuals.py       # Terminal text-animation helpers
├── database/
│   ├── __init__.py
│   ├── db_manager.py    # JSON file CRUD operations
│   └── blogs.json       # Data store
├── LICENSE
└── README.md
```

## Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
