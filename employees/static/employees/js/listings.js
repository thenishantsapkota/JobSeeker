const searchBar = document.getElementById('searchBar');
const tableRows = document.getElementsByTagName('tr');

// Add event listener to search bar
searchBar.addEventListener('keyup', () => {
    const searchText = searchBar.value.toLowerCase();

    // Loop through table rows and hide/show based on search text
    for (let i = 1; i < tableRows.length; i++) {
        let rowText = tableRows[i].innerText.toLowerCase();
        if (rowText.includes(searchText)) {
            tableRows[i].style.display = "";
        } else {
            tableRows[i].style.display = "none";
        }
    }
});