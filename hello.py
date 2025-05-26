from preswald import connect, query, table, text, selectbox, plotly, sidebar
import plotly.express as px
import plotly.graph_objects as go

connect()
sidebar()
text("# NBA Team Statistics- 2023 Season")

# --- UTILITY FUNCTIONS ---

def get_team_list():
    team_sql = "SELECT DISTINCT Team FROM sample_csv WHERE Team IS NOT NULL"
    teams_df = query(team_sql, "sample_csv")
    return sorted(teams_df["Team"].dropna().tolist())

def get_team_data(team):
    sql = f"SELECT * FROM sample_csv WHERE Team = '{team}'"
    return query(sql, "sample_csv")

def show_win_loss_bar(df, team):
    if "W" in df.columns and "L" in df.columns:
        wins = df["W"].astype(float).sum()
        losses = df["L"].astype(float).sum()

        fig = go.Figure([
            go.Bar(name="Wins", x=["Record"], y=[wins], marker_color="green"),
            go.Bar(name="Losses", x=["Record"], y=[losses], marker_color="red")
        ])
        fig.update_layout(title=f"Win vs Loss for {team}", barmode="group")
        plotly(fig)
    else:
        text("Columns 'W' and 'L' not found.")

def show_pts_vs_fgm_scatter(df, team):
    import pandas as pd
    import plotly.express as px
    from preswald import plotly, text

    if "PTS" not in df.columns or "FGM" not in df.columns:
        text("Columns 'PTS' or 'FGM' not found.")
        return

    df_cleaned = df.copy()
    df_cleaned["PTS"] = pd.to_numeric(df_cleaned["PTS"], errors="coerce")
    df_cleaned["FGM"] = pd.to_numeric(df_cleaned["FGM"], errors="coerce")
    df_cleaned = df_cleaned.dropna(subset=["PTS", "FGM"])

    if df_cleaned.empty:
        text("No valid data to plot.")
        return

    fig = px.scatter(
        df_cleaned,
        x="FGM",
        y="PTS",
        hover_data=["PName"] if "PName" in df_cleaned.columns else None,
        title=f"{team}: PTS vs FGM",
        labels={"FGM": "Field Goals Made", "PTS": "Points"}
    )
    fig.update_layout(
        xaxis_type="linear",
        xaxis_tickangle=0
    )
    plotly(fig)

# --- UI LOGIC ---

team_list = get_team_list()
selected_team = selectbox("Select a team:", team_list)
viz_option = selectbox("Select a visualization:", ["Win vs Loss", "PTS vs FGM"])

team_df = get_team_data(selected_team)
table(team_df, title=f"Players from {selected_team}")

if viz_option == "Win vs Loss":
    show_win_loss_bar(team_df, selected_team)
elif viz_option == "PTS vs FGM":
    show_pts_vs_fgm_scatter(team_df, selected_team)