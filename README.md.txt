# Local Waste Reporter

Local Waste Reporter is a lightweight Flask web application that allows users to report waste issues in their area. Users can submit a description, address, and optionally upload an image. The submitted reports are stored with a timestamp and displayed in a styled list on the same page.

## 🔧 Features

- Submit waste-related issues with a short description and address
- Optional image upload for visual documentation
- View a list of all submitted reports with timestamps
- Clean and responsive green/orange UI
- Built with Flask, HTML, CSS, and JavaScript 

## 📁 Project Structure
local-waste-reporter/
│
├── app.py # Flask backend
├── /templates/
│ └── index.html # Main HTML page
├── /static/
│ ├── styles.css # CSS styling
│ └── script.js # JavaScript
## 🚀 How to Run the Project

Follow these steps to run the project on your local machine:

 1. Clone the Repository

```bash
git clone https://github.com/Tamannayadav141/localWasteReporter.git
cd localWasteReporter

2. Set Up a Virtual Environment (Optional)
   python -m venv venv
      Then activate it:

      On Windows: venv\Scripts\activate
      On Mac/Linux:source venv/bin/activate
3. Install Dependencies
   pip install Flask

4.Run the Flask App
  python app.py




## 💡 Future Enhancements

- Add geolocation/map view
- Export reports as PDF or Excel
- Admin dashboard to manage and resolve reports

