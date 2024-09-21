// Function to handle image conversion
async function convertImage() {
  const imageFile = document.getElementById("imageFile").files[0];
  if (!imageFile) {
    alert("Please select an image file to upload.");
    return;
  }

  const formData = new FormData();
  formData.append("file", imageFile);

  try {
    const response = await fetch("http://127.0.0.1:8000/ocr-image/", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data = await response.json();
    displayResult(data.text);
  } catch (error) {
    console.error("Error during image conversion:", error);
    alert("Failed to convert image. Check the console for details.");
  }
}

// Function to handle PDF conversion
async function convertPdf() {
  const pdfFile = document.getElementById("pdfFile").files[0];
  if (!pdfFile) {
    alert("Please select a PDF file to upload.");
    return;
  }

  const formData = new FormData();
  formData.append("file", pdfFile);

  try {
    const response = await fetch("http://127.0.0.1:8000/ocr-pdf/", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Error: ${response.statusText}`);
    }

    const data = await response.json();
    displayResult(data.text);
  } catch (error) {
    console.error("Error during PDF conversion:", error);
    alert("Failed to convert PDF. Check the console for details.");
  }
}

// Function to display the result in JSON format
function displayResult(text) {
  const resultDiv = document.getElementById("result");
  const jsonResult = document.getElementById("jsonResult");

  jsonResult.textContent = JSON.stringify({ text: text }, null, 2);
  resultDiv.style.display = "block";
}
