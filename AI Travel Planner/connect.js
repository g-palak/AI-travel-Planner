document.getElementById('userInputForm').addEventListener('submit', async (event) => {
  // Prevent the page from reloading
  event.preventDefault(); 
  
  // Gather the form data
  const formData = new FormData(event.target);
  const data = Object.fromEntries(formData.entries());

  try {
    // Send data to your FastAPI endpoint
    const response = await fetch('http://127.0.0.1:8000/trip-plan', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data) // Convert JS object to JSON string
    });

    const result = await response.json();
    document.getElementById('responseMessage').innerText = result.message;
    
  } catch (error) {
    console.error('Error:', error);
    document.getElementById('responseMessage').innerText = 'Submission failed.';
  }
});
