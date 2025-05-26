# NBA Player Statistic Visualization App

This application provides an interactive dashboard for exploring NBA player statistics from the 2023 season. It is built using the Preswald framework and includes various data visualizations to help users better understand team and player performance.

## Features

- **Team Filter**: Select any NBA team to view only players from that team.
- **Interactive Table**: Displays all player stats for the selected team.
- **Visualization Options**:
  - **Win vs Loss Bar Chart**: Compares total team wins and losses.
  - **PTS vs FGM Scatter Plot**: Displays the relationship between a player's total points and field goals made.

## Dataset

The dataset used in this project is publicly available and can be found here:

**NBA Players Stats (2023 Season)**  
Author: AmirHossein Mirzaie  
Source: [Kaggle Dataset](https://www.kaggle.com/datasets/amirhosseinmirzaie/nba-players-stats2023-season)

This dataset contains:
- Player name, position, team
- Age, games played (GP), points (PTS), field goals made (FGM)
- Win/loss stats (`W`, `L`) and other performance metrics

## Technologies Used

- **Preswald** – for UI components, SQL querying, and dashboard deployment
- **Plotly Express** – for high-quality visual charts
- **Pandas** – for numeric conversions and data prep

## Usage

1. Load the app in your Preswald environment.
2. Use the dropdown to choose an NBA team.
3. Choose a visualization type:
   - View a bar chart comparing total wins vs losses
   - Or see a scatter plot of PTS vs FGM for all players on the team
4. Explore the data table and visuals interactively

## Configuration

Ensure the following block is in your `preswald.toml` file to register the dataset:

```toml
[data.sample_csv]
type = "csv"
path = "data/2023_nba_player_stats.csv"
