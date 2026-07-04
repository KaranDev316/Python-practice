
import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueUpdate, IssueOut, IssueStatus
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["Issues"])

@router.get("", response_model=list[IssueOut])
def get_issues():
    """Get all issues."""
    issues = load_data()
    return issues