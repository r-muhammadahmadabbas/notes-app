# 📝 NotesApp - Capture Your Thoughts

A modern, responsive note-taking application built with **FastAPI** and **MongoDB**. It features a clean UI designed with Bootstrap 5, allowing users to create, store, and prioritize their thoughts.

## 🚀 Features

- **FastAPI Backend**: High-performance API using Python.
- **MongoDB Storage**: NoSQL database for flexible data persistence.
- **Server-Side Rendering**: Uses **Jinja2** templates to serve dynamic HTML.
- **Modern UI**: Styled with Bootstrap 5, featuring glassmorphism effects and a masonry layout for notes.
- **Priority Handling**: Ability to mark notes as "Important" with visual badges.

## 📂 Project Structure

```text
📦 project1
 ┣ 📂 config
 ┃ ┗ 📜 db.py          # Database connection
 ┣ 📂 models
 ┃ ┗ 📜 note.py        # Pydantic data models
 ┣ 📂 routes
 ┃ ┗ 📜 note.py        # API endpoints and logic
 ┣ 📂 schemas
 ┃ ┗ 📜 note.py        # Data serializers
 ┣ 📂 static           # CSS/JS assets
 ┣ 📂 templates
 ┃ ┗ 📜 index.html     # Frontend interface
 ┗ 📜 index.py         # Application entry point