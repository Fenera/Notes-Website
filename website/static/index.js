function deleteNote(noteId){
    // send a post request to delete-note endpoint
    fetch('/delete-note', {
        method: 'POST', 
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/"; // refresh the page
    });
}