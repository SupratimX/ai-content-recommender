// Wait for the HTML page to be fully loaded before running any code
document.addEventListener('DOMContentLoaded', () => {

    // Get the HTML elements we need to work with
    const form = document.getElementById('book-form');
    const resultsDiv = document.getElementById('results');
    const submitButton = document.getElementById('submit-button');

    // Add an event listener for when the form is submitted
    form.addEventListener('submit', async (event) => {
        // Prevent the form from doing its default "submit" action
        // (which would just reload the page)
        event.preventDefault();

        // 1. Get the values from the form inputs
        const branch = document.getElementById('branch').value;
        const semester = document.getElementById('semester').value;
        const subject = document.getElementById('subject').value;

        // Show a loading message and disable the button
        resultsDiv.innerHTML = '<p>Searching for books...</p>';
        submitButton.disabled = true;
        submitButton.innerText = 'Searching...';

        try {
            // 2. Send the data to our Python backend (app.py)
            const response = await fetch('/get_books', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                // Convert the JavaScript data into a JSON string
                body: JSON.stringify({
                    branch: branch,
                    semester: semester,
                    subject: subject
                }),
            });

            // 3. Get the JSON response back from the server
            const data = await response.json();

            if (!response.ok) {
                const errorMessage = data && data.error ? data.error : 'Server returned an error.';
                resultsDiv.innerHTML = `<p class="error">${errorMessage}</p>`;
                return;
            }

            // 4. Display the results
            displayBooks(data);

        } catch (error) {
            // If something goes wrong (e.g., network error)
            console.error('Error fetching books:', error);
            resultsDiv.innerHTML = '<p>An error occurred connecting to the server. Please check the console and try again.</p>';
        } finally {
            // Re-enable the button when we're done
            submitButton.disabled = false;
            submitButton.innerText = 'Find Books';
        }
    });

    // This function takes the list of books and turns it into HTML
    function displayBooks(books) {
        // If the list is empty or not an array, show a "not found" message
        if (!Array.isArray(books) || books.length === 0) {
            resultsDiv.innerHTML = '<p>No books found for this combination. Try checking your spelling.</p>';
            return;
        }

        // If we found books, create an HTML card for each one
        let html = '';
        books.forEach(book => {
            html += `
                <div class="book-card">
                    <h3>${book.title}</h3>
                    <p><strong>Author:</strong> ${book.author}</p>
                    <p class="book-description">${book.description}</p>
                    <div class="book-links">
                        <a href="${book.buy_link}" target="_blank" class="buy-link">Buy Now</a>
                        <a href="${book.free_link}" target="_blank" class="free-link">Find Free Version</a>
                    </div>
                </div>
            `;
        });

        // Put the newly created HTML into the results div
        resultsDiv.innerHTML = html;
    }
});

