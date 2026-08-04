from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from database.db_manager import _ensure_file_exists, _load_blogs, _save_blogs, get_all_blogs, save_blog, delete_all_bllogs, delete_blog

class blog_details(BaseModel):
    blog_id : str
    blog_title : str
    blog_content : str
    blog_category : str
    tags : list[str]
    
class update_blog(BaseModel):
    blog_title : str
    blog_category : str
    blog_content : str
    tags : list[str]



app = FastAPI()


@app.post("/posts/", status_code = 201)
async def add_blog(blog : blog_details):
    blogs = _load_blogs()
    blog_id = blog.blog_id
    for blogg in blogs:
        if blog_id == blogg['blog_id']:
            raise HTTPException(status_code=400, detail=f"blog with id = {blog_id} already exists")

    save_blog(blog.model_dump())
    return f"blog added. id = {blog_id}"
    
@app.put("/posts/{blog_id}")
async def updated_blog(blog_id: str, new_blog: update_blog):
    blogs = _load_blogs()
    check = True
    for blog in blogs:
        if blog['blog_id'] == blog_id:
            check = False
    if check:
        raise HTTPException(status_code=404, detail=f"blog with id = {blog_id} doesnt exist")  
    
    delete_blog(blog_id)
    blog = {
        'blog_id': blog_id,
        'blog_title': new_blog.blog_title,
        'blog_category': new_blog.blog_category,
        'blog_content': new_blog.blog_content,
        'tags': new_blog.tags,
    }
    save_blog(blog)
    return f"blog updated. id = {blog_id}"
    

@app.get("/posts")
async def read_blogs(category: Optional[str]=None):
    blogs = _load_blogs()
    if category==None:
        return blogs
    blog_output = []
    for blog in blogs:
        if blog['blog_category']==category:
            blog_output.append(blog)
    return blog_output

@app.get("/posts/{blog_id}")
async def read_blog(blog_id : str):    
    blogs = _load_blogs()
    for blog in blogs:
        if blog['blog_id'] == blog_id:
            return blog
    raise HTTPException(status_code=404, detail=f"blog with id = {blog_id} doesnt exist")
        

def main():
    print()    









#if __name__=="__main__":
    #main()