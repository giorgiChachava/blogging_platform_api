import json
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blogs.json")


def _ensure_file_exists():
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump([], f)


def _load_blogs():
    _ensure_file_exists()
    with open(DB_PATH, "r") as f:
        return json.load(f)


def _save_blogs(blogs):
    with open(DB_PATH, "w") as f:
        json.dump(blogs, f, indent=2)

def find_new_id():
    blogs = _load_blogs()
    max_id=0
    for blog in blogs:
        id = int(blog['blog_id'])
        max_id = max(max_id,id)
    return max_id+1

def save_blog(blog_dict):
    blogs = _load_blogs()
    blogs.append(blog_dict)
    _save_blogs(blogs)


def get_all_blogs():
    return _load_blogs()

def delete_blog(blog_id):
    blogs = _load_blogs()
    remaining = [blog for blog in blogs if blog['blog_id'] != blog_id]
    _save_blogs(remaining)


def delete_all_bllogs():
    with open(DB_PATH, "w") as f:
        json.dump([], f)

