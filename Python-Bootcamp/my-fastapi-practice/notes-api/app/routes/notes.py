import uuid
from fastapi import APIRouter, HTTPException, status
from ..schemas.note import NoteCreate, NoteUpdate,NoteResponse
from ..storage.note_storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["Issues"])

@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_issue(payload: NoteCreate):
    """
    Create new issue
    The issue is persisted to data/issues.json
    """
    issues = load_data()

    issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.body,

    }

    issues.append(issue)
    save_data(issues)

    return issue