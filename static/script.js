// Function to toggle book details (show/hide)
function toggleDetails(bookId) {
    let details = document.getElementById(bookId);
    if (details.style.display === "none") {
        details.style.display = "block"; 
    } else {
        details.style.display = "none"; 
    }
}

// Function to toggle the "More Information" section (show/hide)
function toggleMoreInfo(infoId) {
    let info = document.getElementById(infoId);
    if (info.style.display === "none") {
        info.style.display = "block"; 
    } else {
        info.style.display = "none"; 
    }
}
