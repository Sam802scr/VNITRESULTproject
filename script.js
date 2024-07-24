document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    const selectedBranch = document.getElementById('options').value;
    let pdfUrl = '';

    // Map the selected branch to the corresponding PDF URL
    const pdfUrls = {
        cse: 'https://raw.githubusercontent.com/Sam802scr/vnitresults/main/Computer%20Science%20%26%20Engineering.pdf',
        ece: 'http://yourdomain.com/pdfs/ece.pdf',
        eee: 'https://raw.githubusercontent.com/Sam802scr/vnitresults/main/Electrical%20Engineering.pdf',
        mech: 'http://yourdomain.com/pdfs/mech.pdf',
        civil: 'http://yourdomain.com/pdfs/civil.pdf',
        chem: 'http://yourdomain.com/pdfs/chem.pdf',
        meta: 'http://yourdomain.com/pdfs/meta.pdf',
        min: 'http://yourdomain.com/pdfs/min.pdf'
    };

    // Get the URL for the selected branch
    pdfUrl = pdfUrls[selectedBranch];

    if (pdfUrl) {
        // Create a temporary anchor element and trigger the download
        const tempLink = document.createElement('a');
        tempLink.href = pdfUrl;
        tempLink.download = pdfUrl.split('/').pop(); // Extract the file name from the URL
        document.body.appendChild(tempLink); // Append the link to the body
        tempLink.click(); // Simulate a click on the link
        document.body.removeChild(tempLink); // Remove the link from the document
    } else {
        alert('Please select a valid branch.');
    }
});
