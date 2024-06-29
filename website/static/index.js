function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id: noteId })
    }).then(
        (_res) => {window.location.href = "/";});
}
