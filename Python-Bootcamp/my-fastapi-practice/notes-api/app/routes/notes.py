from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix="/api/v1/issues", tags=["Issues"])