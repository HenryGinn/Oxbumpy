from oxbumpy import load_data, read_json, get_df, display


data = read_json("eights_2024.json")
divs = read_json("eights_2024_divs.json")
df = get_df(data, "Eights 2024")
display_obj = display(df, divs)
