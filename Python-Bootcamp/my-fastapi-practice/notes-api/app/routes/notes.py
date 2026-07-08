import uuid
from fastapi import APIRouter, HTTPException, status
from app.storage.note_storage import load_data, save_data
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
router = APIRouter(prefix="/api/v1/notes", tags=["Issues"])

@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate):
    """
    Create new note
    The issue is persisted to data/issues.json
    """

    notes = load_data()
    note = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.body,

    }

    notes.append(note)
    save_data(notes)

    return notes

@router.get("/{note_id}", response_model=NoteResponse, status_code=status.HTTP_200_OK)
def get_note(note_id: str):
    """Get a single note by ID."""
    notes = load_data()
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Note not found"
    )

@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: str, payload: NoteUpdate):
    """Update an existing note by ID."""
    notes = load_data()

    for note in notes:
        if note["id"] == note_id:
            if payload.title is not None:
                note["title"] = payload.title
            if payload.body is not None:
                note["body"] = payload.body

            save_data(notes)
            return note

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Note not found"
    )