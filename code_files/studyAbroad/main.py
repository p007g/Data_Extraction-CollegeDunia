import pandas as pd
import numpy as np
from country import Abroad


countries = ['france', 'malaysia']

for country in countries:
    # make an object------
    data = Abroad(country)

    # access the method-------
    data.city()

    info = {
        "Country":data.university_country,
        "Universities Names":data.university_name, 
        "University Place":data.university_place,
        "Tuition Fees":data.tuition_fees,
        "Living Fees":data.living_fees
        }
    
    df = pd.DataFrame.from_dict(info, orient='index')
    df = df.transpose()
    df.index = np.arange(1, len(df) + 1)


print(df)
# Save to files------
# excel_file = 'Abroad Universities Data.xlsx'
# df.to_excel(excel_file, sheet_name='All Universities')