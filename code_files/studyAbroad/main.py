import pandas as pd
import numpy as np
from country import Abroad


countries = ['canada', 'australia', 'germany', 'hong-kong', 'ireland', 'malaysia', 'netherlands', 
             'new-zealand', 'singapore', 'sweden', 'uk', 'usa', 'france', 'italy', 'uae']

for country in countries:
    # make an object------
    data = Abroad(country)

    # access the method-------
    data.city()

    info = {
        "Country":data.university_country,
        "Universities Names":data.university_name, 
        "University Place":data.university_place
        }

    df = pd.DataFrame(info)
    df.index = np.arange(1, len(df) + 1)


# Save to Excel file------
print(df)
df.to_excel('Abroad Universities Data.xlsx', sheet_name='All Universities')