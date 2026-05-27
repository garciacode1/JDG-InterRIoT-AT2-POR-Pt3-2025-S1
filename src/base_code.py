"""
 Assessment Title: Portfolio Part X
 Cluster:          Intermediate RIoT
 Qualification:    ICT50220 Diploma of Information Technology (Advanced Programming)
 Name:             YOUR NAME
 Student ID:       xxxxxxxxx
 Year/Semester:    20YY/SN

 YOUR SUMMARY OF PORTFOLIO ACTIVITY
 GOES HERE

"""

# Imports
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Global CONSTANTS


## Global Variables

app = FastAPI(title="FastAPI & Jinja2")

BASE_PATH = Path(__file__).parent
print(BASE_PATH)

app.mount("/static",
          StaticFiles(directory="static"),
          name="static")

app.mount("/css",
          StaticFiles(directory="static/css"),
          name="css")
app.mount("/js",
          StaticFiles(directory="static/js"),
          name="js")
app.mount("/images",
          StaticFiles(directory="static/img"),
          name="images")

TEMPLATES = Jinja2Templates(directory="templates")


# Functions/Methods
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return TEMPLATES.TemplateResponse(
        request=request,
        name="pages/home.html"
    )


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return TEMPLATES.TemplateResponse(
        request=request,
        name="pages/about.html"
    )

@app.get("/api/data")
async def api_data(request: Request):
    return { 'name':'Frank Spencer' }

# Main Code
