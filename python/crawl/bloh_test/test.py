import pandas as pd
df=pd.DataFrame({
    "rank":["1","2","3"],
    "title":["The Shawshank Redemption","The Godfather","The Godfather: Part II"],
    "rating_star":["5","5","5"],
    "rating_num":["9.6","9.2","9.0"],
    "comments":["222222","222222","222222"]
})
df.to_excel('output.xlsx',index=False)