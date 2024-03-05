from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Dummy datastore
items = ["Item 1", "Item 2"]

@app.get("/", response_class=HTMLResponse)
def get_items(request: Request):
    return templates.TemplateResponse("items.html", {"request": request, "items": items})

@app.post("/add-item")
def add_item(request: Request, item: str = Form(...)):
    items.append(item)
    return templates.TemplateResponse("partials/item.html", {"request": request, "item": item})

