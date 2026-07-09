// Change this to your FastAPI server URL if running the frontend separately
const API_BASE = 'http://127.0.0.1:8001/api/v1/notes';

const notesList = document.getElementById('notes-list');
const emptyState = document.getElementById('empty-state');
const modalOverlay = document.getElementById('modal-overlay');
const modalTitle = document.getElementById('modal-title');
const noteForm = document.getElementById('note-form');
const noteIdInput = document.getElementById('note-id');
const titleInput = document.getElementById('note-title-input');
const bodyInput = document.getElementById('note-body-input');

let isEditing = false;

/* ============================================
   API Helpers
   ============================================ */
async function apiGet(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function apiPost(url, payload) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function apiPut(url, payload) {
  const res = await fetch(url, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function apiDelete(url) {
  const res = await fetch(url, { method: 'DELETE' });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
}

/* ============================================
   Render
   ============================================ */
function renderNotes(notes) {
  notesList.innerHTML = '';

  if (!notes || notes.length === 0) {
    emptyState.classList.remove('hidden');
    return;
  }

  emptyState.classList.add('hidden');

  notes.forEach((note) => {
    const li = document.createElement('li');
    li.className = 'note-card';
    li.innerHTML = `
      <h3 class="note-card-title">${escapeHtml(note.title)}</h3>
      <p class="note-card-body">${escapeHtml(note.body)}</p>
      <div class="note-card-actions">
        <button class="btn btn-edit" data-action="edit" data-id="${note.id}" type="button">Edit</button>
        <button class="btn btn-danger" data-action="delete" data-id="${note.id}" type="button">Delete</button>
      </div>
    `;
    notesList.appendChild(li);
  });
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

/* ============================================
   Data
   ============================================ */
async function loadNotes() {
  try {
    const notes = await apiGet(API_BASE);
    renderNotes(notes);
  } catch (err) {
    showError('Failed to load notes. Make sure the API server is running.');
  }
}

async function saveNote() {
  const id = noteIdInput.value;
  const title = titleInput.value.trim();
  const body = bodyInput.value.trim();

  if (!title || !body) return;

  try {
    if (isEditing && id) {
      await apiPut(`${API_BASE}/${id}`, { title, body });
    } else {
      await apiPost(API_BASE, { title, body });
    }
    closeModal();
    await loadNotes();
  } catch (err) {
    showError('Failed to save note.');
  }
}

async function deleteNote(id) {
  if (!confirm('Are you sure you want to delete this note?')) return;
  try {
    await apiDelete(`${API_BASE}/${id}`);
    await loadNotes();
  } catch (err) {
    showError('Failed to delete note.');
  }
}

/* ============================================
   Modal
   ============================================ */
function openCreateModal() {
  isEditing = false;
  noteIdInput.value = '';
  titleInput.value = '';
  bodyInput.value = '';
  modalTitle.textContent = 'Create Note';
  modalOverlay.classList.remove('hidden');
  titleInput.focus();
}

function openEditModal(note) {
  isEditing = true;
  noteIdInput.value = note.id;
  titleInput.value = note.title;
  bodyInput.value = note.body;
  modalTitle.textContent = 'Edit Note';
  modalOverlay.classList.remove('hidden');
  titleInput.focus();
}

function closeModal() {
  modalOverlay.classList.add('hidden');
}

function showError(message) {
  alert(message);
}

/* ============================================
   Event Listeners
   ============================================ */
document.getElementById('btn-open-create').addEventListener('click', openCreateModal);
document.getElementById('btn-close-modal').addEventListener('click', closeModal);
document.getElementById('btn-cancel').addEventListener('click', closeModal);

noteForm.addEventListener('submit', (e) => {
  e.preventDefault();
  saveNote();
});

notesList.addEventListener('click', async (e) => {
  const btn = e.target.closest('button[data-action]');
  if (!btn) return;

  const action = btn.dataset.action;
  const id = btn.dataset.id;

  if (action === 'delete') {
    await deleteNote(id);
  } else if (action === 'edit') {
    try {
      const note = await apiGet(`${API_BASE}/${id}`);
      openEditModal(note);
    } catch (err) {
      showError('Failed to load note for editing.');
    }
  }
});

modalOverlay.addEventListener('click', (e) => {
  if (e.target === modalOverlay) closeModal();
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && !modalOverlay.classList.contains('hidden')) {
    closeModal();
  }
});

/* ============================================
   Init
   ============================================ */
loadNotes();
