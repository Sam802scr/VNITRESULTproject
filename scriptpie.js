function getAnalysis() {
    const selectedCourse = document.getElementById('options').value;
    fetch(`/resultbackend/grade-distribution/?course=${encodeURIComponent(selectedCourse)}`)
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('pieChart').getContext('2d');
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: Object.keys(data),
                    datasets: [{
                        data: Object.values(data),
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#ff9900', '#66ff66', '#ccffcc', '#ff6666'],
                    }]
                },
                options: {
                    responsive: true
                }
            });
        });
}