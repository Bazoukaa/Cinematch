
# CineMatch - Your Personal Movie Matchmaker 🎥

Welcome to **CineMatch**, a personalized movie recommendation system that helps you find the perfect movie based on your favorite genres and era preferences. Powered by IMDb data, CineMatch allows users to explore a variety of genres and choose movies from different time periods, providing top-rated suggestions along the way!

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Data Source](#data-source)
- [License](#license)

## Features
- **Interactive Interface**: Simple prompts to select your favorite movie genres and era (before or after 2000).
- **Top 10 Movies**: Option to view top 10 movies by vote average within your selected genres.
- **Detailed Movie Information**: Provides detailed movie information such as title, overview, cast, director, release date, and more.
- **Customizable Options**: Filter movies by genre and era, and choose to see additional movie details on demand.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/cinematch.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd cinematch
   ```

3. **Install the required Python packages**:
   Make sure you have Python installed. You can install the necessary dependencies using:
   ```bash
   pip install pandas
   ```

4. **Download the IMDb dataset**:
   The system uses an IMDb dataset in CSV format. You can download the IMDb data from [IMDb datasets](https://www.imdb.com/interfaces/) and place it in the appropriate folder.
   Ensure that the file path in the script points to the location of the CSV file.

## Usage

1. **Run the CineMatch system**:
   ```bash
   python cinematch.py
   ```

2. **Follow the prompts**:
   - Enter your name.
   - Choose your preferred genres from the available list.
   - Select whether you'd like movies from the "old" era (before 2000) or the "new" era (from 2000 onwards).
   - Optionally, you can view the top 10 movies sorted by vote average.

3. **Explore movie recommendations**:
   - Choose a movie from the generated list, and view detailed information such as overview, cast, director, runtime, and more.

## Requirements
- Python 3.x
- pandas library

## Data Source
This project uses IMDb data, which can be obtained from the official IMDb datasets [here](https://www.imdb.com/interfaces/). The script assumes the dataset is in CSV format with fields such as:
- `genres`
- `release_year`
- `vote_average`
- `original_title`
- `overview`
- `cast`
- `director`
- `release_date`
- `runtime`
- `budget`
- `revenue`
- `popularity`
- `vote_count`
- `keywords`
- `homepage`
