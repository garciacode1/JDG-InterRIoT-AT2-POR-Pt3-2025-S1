"""
 Assessment Title: Portfolio Part 3
 Cluster:          Intermediate RIoT
 Qualification:    ICT50220 Diploma of Information Technology (Advanced Programming)
 Name:             Juan Garcia
 Student ID:       20114823
 Year/Semester:    2026/S1

 YOUR SUMMARY OF PORTFOLIO ACTIVITY
 GOES HERE

"""

# Imports
import casbin
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi_authz import CasbinMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import basic_auth

# Global CONSTANTS


## Global Variables

api = FastAPI(title="JDG-InterIOT-AT2-POR-Pt3-2025-S1")

enforcer = casbin.Enforcer(
    "api/rbac_model.conf",
    "api/rbac_policy.csv",
)

backend = basic_auth.BasicAuth()

api.add_middleware(CasbinMiddleware, enforcer=enforcer)
api.add_middleware(AuthenticationMiddleware, backend=backend)


BASE_PATH = Path(__file__).parent
print(BASE_PATH)

api.mount("/static",
          StaticFiles(directory="static"),
          name="static")

api.mount("/css",
          StaticFiles(directory="static/css"),
          name="css")
api.mount("/js",
          StaticFiles(directory="static/js"),
          name="js")
api.mount("/images",
          StaticFiles(directory="static/img"),
          name="images")

TEMPLATES = Jinja2Templates(directory="templates")


# Functions/Methods
@api.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return TEMPLATES.TemplateResponse(
        request=request,
        name="pages/home.html"
    )
@api.get("/api")
async def api_index():
    return {"success": True, "message": "Welcome", "data": [{"greeting": "Hello, world."}]}

@api.get("/api/ds1/res1")
async def api_ds1_res1():
    return "Resource 1 has been accessed"


@api.get("/api/ds2/res2")
async def api_ds2_res2():
    return "Resource 2 has been accessed"
@api.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return TEMPLATES.TemplateResponse(
        request=request,
        name="pages/about.html"
    )

@api.get("/api/data")
async def api_data(request: Request):
    return { 'name':'Frank Spencer' }

# Main Code
