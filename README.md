# HR Assistant Application

A web-based application to assist employees with HR-related questions, policies, and procedures.

## Project Structure

```
├── app.py                  # Main application entry point
├── handlers.py             # Event handlers and business logic
├── ui/
│   ├── __init__.py         # Makes ui directory a Python package
│   ├── components.py       # UI components and layout
│   └── theme.py            # Styling, colors, and JavaScript functions
└── README.md               # This documentation
```

## Key Features

- HR policy question and answer system
- Chat history stored in browser localStorage
- Example questions for quick access
- Settings page for administration tasks
- File upload capability for HR policy documents

## Running the Application

To run the application:

```bash
python app.py
```

Or locally with:

```bash
gradio app.py
```

## Interface Preview

The application features a modern interface with:

- Main page with a chat interface and example questions
- Chat history panel that persists between sessions
- Settings page for administrative functions
- Capability cards showing the system's main features

## Technologies Used

- [Gradio](https://www.gradio.app/) - For the web interface
- JavaScript - For local storage and dynamic content
- Python - For backend functionality
