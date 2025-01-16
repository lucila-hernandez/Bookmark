function toggleDetails(bookId) {
    let details = document.getElementById(bookId);
    if (details.style.display === "none") {
        details.style.display = "block"; 
    } else {
        details.style.display = "none"; 
    }
}
